#!/usr/bin/env python3
"""抓取 GitHub 领域日报所需的原始数据。

只使用 Python 标准库。不得在本文件中写入账号、密码或密钥。
可选读取环境变量 GITHUB_TOKEN 或 GH_TOKEN 作为请求头，变量不存在时匿名访问。

请求纪律：
- A 为 Trending 页面（since=daily），不调用 OSS Insight。
- B 每领域 1 次：created:>=运行日往前 30 天，stars:>2，按总 star 降序，per_page=5。
- C 每领域 1 次：pushed:>=运行日往前 7 天，stars:>3，按总 star 降序，per_page=5，
  page = (运行日当年第几天 mod 4) + 1。
- 日期只用绝对日期。单查询 OR 不超过 5 个。
- 全部串行，相邻请求间隔 7 秒。HTTP 403/429 时等待 30 秒再重试一次。
- 运行日按北京时间（UTC+8）的日历日期。

用法：
  python3 scripts/fetch_github_daily.py /tmp/github_daily.json
标准输出打印数据源摘要；完整 JSON 写入给定路径。不传路径则 JSON 打到标准输出。
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from html import unescape
from html.parser import HTMLParser

BEIJING = timezone(timedelta(hours=8))
USER_AGENT = "github-daily-fetch/1.0"
INTERVAL_SEC = 7
RETRY_WAIT_SEC = 30
SEARCH_URL = "https://api.github.com/search/repositories"
TRENDING_URL = "https://github.com/trending?since=daily"

# 检索用关键词组：每组最多 5 项（OR 不超过 5 个）。
# GitHub 仓库搜索对多个 topic: 做 OR 会返回 total_count=0（不报 422）。
# 因此每组只保留 1 个 topic:，其余用同一关键词表里的仓库名/文本关键词。
# 功率器件不用裸 gan：会撞上生成对抗网络（GAN），把氮化镓结果挤出前 5。
SEARCH_TERMS = {
    "embedded": [
        "topic:embedded",
        "esp32",
        "stm32",
        "zephyr",
        "freertos",
    ],
    "ai": [
        "topic:llm",
        "pytorch",
        "transformer",
        "diffusion",
        "ai-agents",
    ],
    "power_devices": [
        "topic:power-electronics",
        "igbt",
        "sic",
        "mosfet",
        "wide-bandgap",
    ],
    "power_supply": [
        "topic:mppt",
        "bms",
        "inverter",
        "dc-dc",
        "llc",
    ],
    "control": [
        "topic:ros2",
        "slam",
        "motor-control",
        "flight-controller",
        "mpc",
    ],
}

# 归类关键词：topics 或仓库名命中即计入。描述仅强特征词才计入。
CLASS_KEYWORDS = {
    "embedded": [
        "embedded",
        "rtos",
        "esp32",
        "stm32",
        "zephyr",
        "fpga",
        "freertos",
        "firmware",
        "bare-metal",
        "risc-v",
        "cortex-m",
        "mcu",
        "modbus",
        "can-bus",
        "dsp",
        "verilog",
        "vhdl",
        "yosys",
        "verilator",
        "cocotb",
        "zynq",
    ],
    "ai": [
        "llm",
        "ai-agents",
        "computer-vision",
        "pytorch",
        "transformer",
        "diffusion",
        "reinforcement-learning",
    ],
    "power_devices": [
        "power-electronics",
        "sic",
        "gan",
        "igbt",
        "mosfet",
        "wide-bandgap",
        "spice",
        "device-modeling",
    ],
    "power_supply": [
        "power-electronics",
        "mppt",
        "bms",
        "inverter",
        "dc-dc",
        "buck",
        "boost",
        "llc",
        "pfc",
        "motor-drive",
        "power-supply",
        "microgrid",
        "pll",
    ],
    "control": [
        "control-systems",
        "ros2",
        "slam",
        "pid",
        "mpc",
        "kalman-filter",
        "foc",
        "motor-control",
        "flight-controller",
    ],
}

DOMAIN_LABELS = {
    "embedded": "嵌入式 Embedded",
    "ai": "AI",
    "power_devices": "功率器件 Power Devices",
    "power_supply": "电力电子电源 Power Supply",
    "control": "自动控制 Control",
}

STRONG_DESC_WORDS = {
    "power-electronics",
    "igbt",
    "sic",
    "mppt",
    "bldc",
    "foc",
    "zephyr",
    "freertos",
    "rtos",
    "risc-v",
    "stm32",
    "esp32",
    "verilog",
    "vhdl",
    "llc",
    "pfc",
}

# 强特征词落到领域。共享词两边都记，贴近度由更具体的命中决定。
STRONG_WORD_DOMAINS = {
    "power-electronics": ["power_devices", "power_supply"],
    "igbt": ["power_devices"],
    "sic": ["power_devices"],
    "mppt": ["power_supply"],
    "bldc": ["control", "embedded"],
    "foc": ["control"],
    "zephyr": ["embedded"],
    "freertos": ["embedded"],
    "rtos": ["embedded"],
    "risc-v": ["embedded"],
    "stm32": ["embedded"],
    "esp32": ["embedded"],
    "verilog": ["embedded"],
    "vhdl": ["embedded"],
    "llc": ["power_supply"],
    "pfc": ["power_supply"],
}


def beijing_now() -> datetime:
    return datetime.now(BEIJING)


def keyword_hit(text: str, keyword: str) -> bool:
    if not text:
        return False
    hay = text.lower().replace("_", "-")
    needle = keyword.lower().replace("_", "-")
    return (
        re.search(
            rf"(?<![a-z0-9]){re.escape(needle)}(?![a-z0-9])",
            hay,
        )
        is not None
    )


def is_list_repo(name: str, description: str) -> bool:
    """排除公开课清单、面试指南、awesome 合集。"""
    repo = name.split("/")[-1]
    folded = repo.lower().replace("_", "-")
    desc = (description or "").lower()
    if re.search(r"(^|-)awesome($|-)", folded):
        return True
    if "javaguide" in folded.replace("-", ""):
        return True
    if re.search(
        r"(interview-guide|video-courses|course-list|cheatsheet|learning-path)",
        folded,
    ):
        return True
    if re.search(
        r"(curated list|awesome list|a list of|interview guide|公开课|面试指南|资源清单)",
        desc,
    ):
        return True
    return False


def drop_ambiguous_matches(
    matches: dict[str, list[str]],
    name: str,
    topics: list[str],
    description: str,
) -> dict[str, list[str]]:
    """gan 同时是氮化镓和生成对抗网络。仅 gan 命中且上下文是神经网络时，不归入功率器件。"""
    reasons = matches.get("power_devices") or []
    if not reasons:
        return matches
    if any(item.split(":")[-1] != "gan" for item in reasons):
        return matches
    blob = " ".join([name, description or "", " ".join(topics or [])]).lower()
    ml_markers = (
        "adversarial",
        "generative",
        "deep-learning",
        "pytorch",
        "stylegan",
        "cyclegan",
        "gans",
        "neural",
    )
    if any(marker in blob for marker in ml_markers):
        matches = dict(matches)
        matches.pop("power_devices", None)
    return matches


def classify(name: str, topics: list[str], description: str) -> dict[str, list[str]]:
    reasons: dict[str, list[str]] = {key: [] for key in CLASS_KEYWORDS}
    repo_name = name.split("/")[-1]
    topic_text = " ".join(topics or [])
    for domain, words in CLASS_KEYWORDS.items():
        for word in words:
            if any(keyword_hit(topic, word) for topic in topics or []):
                reasons[domain].append(f"topic:{word}")
            elif keyword_hit(repo_name, word):
                reasons[domain].append(f"name:{word}")
    desc_hits = [word for word in STRONG_DESC_WORDS if keyword_hit(description or "", word)]
    for word in desc_hits:
        for domain in STRONG_WORD_DOMAINS.get(word, []):
            mark = f"desc:{word}"
            if mark not in reasons[domain]:
                reasons[domain].append(mark)
    matched = {domain: hits for domain, hits in reasons.items() if hits}
    return drop_ambiguous_matches(matched, name, topics, description)


class TrendingArticleParser(HTMLParser):
    """解析单个 trending article 片段。"""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self.paragraphs: list[str] = []
        self.repo_href = ""
        self.language = ""
        self._in_h2 = False
        self._in_h2_anchor = False
        self._h2_href = ""
        self._in_p = False
        self._p_buf: list[str] = []
        self._anchor_depth = 0
        self._anchor_href = ""
        self._anchor_buf: list[str] = []
        self._in_lang = False
        self._lang_buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {key: value or "" for key, value in attrs}
        if tag == "h2":
            self._in_h2 = True
        elif tag == "a":
            self._anchor_depth += 1
            if self._anchor_depth == 1:
                self._anchor_href = attr.get("href", "")
                self._anchor_buf = []
            if self._in_h2 and not self.repo_href:
                self._in_h2_anchor = True
                self._h2_href = attr.get("href", "")
        elif tag == "p" and not self._in_p:
            self._in_p = True
            self._p_buf = []
        elif tag == "span" and attr.get("itemprop") == "programmingLanguage":
            self._in_lang = True
            self._lang_buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "h2":
            self._in_h2 = False
            if self._in_h2_anchor and self._h2_href:
                self.repo_href = self._h2_href
            self._in_h2_anchor = False
        elif tag == "a" and self._anchor_depth:
            self._anchor_depth -= 1
            if self._anchor_depth == 0:
                text = re.sub(r"\s+", " ", "".join(self._anchor_buf)).strip()
                self.links.append((self._anchor_href, text))
                self._anchor_buf = []
        elif tag == "p" and self._in_p:
            text = re.sub(r"\s+", " ", "".join(self._p_buf)).strip()
            if text:
                self.paragraphs.append(text)
            self._in_p = False
            self._p_buf = []
        elif tag == "span" and self._in_lang:
            self.language = re.sub(r"\s+", " ", "".join(self._lang_buf)).strip()
            self._in_lang = False
            self._lang_buf = []

    def handle_data(self, data: str) -> None:
        if self._in_p:
            self._p_buf.append(data)
        if self._anchor_depth:
            self._anchor_buf.append(data)
        if self._in_lang:
            self._lang_buf.append(data)


def parse_int(text: str) -> int | None:
    match = re.search(r"([\d,]+)", text or "")
    if not match:
        return None
    return int(match.group(1).replace(",", ""))


def parse_trending(html_text: str) -> list[dict]:
    # 不先对整页 unescape：属性里的 &quot; 解开后会截断标签。
    # 文本节点由 HTMLParser(convert_charrefs=True) 解码，描述再 unescape 一次兜底。
    repos: list[dict] = []
    parts = html_text.split('<article class="Box-row">')
    for part in parts[1:]:
        fragment = part.split("</article>", 1)[0]
        parser = TrendingArticleParser()
        parser.feed(fragment)
        parser.close()
        href = parser.repo_href
        if not re.fullmatch(r"/[^/]+/[^/]+", href or ""):
            continue
        if href.startswith("/sponsors/"):
            continue
        full_name = href[1:]
        stars_today = None
        today_match = re.search(r"([\d,]+)\s+stars today", fragment)
        if today_match:
            stars_today = int(today_match.group(1).replace(",", ""))
        stars = None
        for href, text in parser.links:
            if href.endswith("/stargazers"):
                stars = parse_int(text)
                break
        description = unescape(parser.paragraphs[0]) if parser.paragraphs else ""
        repos.append(
            {
                "full_name": full_name,
                "url": f"https://github.com/{full_name}",
                "description": description,
                "stars": stars,
                "stars_today": stars_today,
                "topics": [],
                "language": parser.language,
                "topics_available": False,
            }
        )
    return repos


def auth_headers() -> dict[str, str]:
    import os

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


class FetchState:
    def __init__(self) -> None:
        self.calls = 0

    def pause_before(self) -> None:
        if self.calls > 0:
            time.sleep(INTERVAL_SEC)
        self.calls += 1


def http_get(url: str, headers: dict[str, str]) -> tuple[int, str, dict[str, str]]:
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.status, body, {k.lower(): v for k, v in response.headers.items()}
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        hdrs = {k.lower(): v for k, v in error.headers.items()} if error.headers else {}
        return error.code, body, hdrs


def http_get_with_retry(url: str, headers: dict[str, str], state: FetchState) -> dict:
    state.pause_before()
    status, body, hdrs = http_get(url, headers)
    retried = False
    if status in {403, 429}:
        time.sleep(RETRY_WAIT_SEC)
        retried = True
        status, body, hdrs = http_get(url, headers)
    return {
        "http_status": status,
        "body": body,
        "headers": hdrs,
        "retried_after_rate_limit": retried,
        "rate_limit_remaining": hdrs.get("x-ratelimit-remaining"),
    }


def error_message(status: int, body: str) -> str:
    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        payload = None
    if isinstance(payload, dict):
        message = payload.get("message") or ""
        errors = payload.get("errors")
        if errors:
            return f"HTTP {status}: {message}; errors={errors}"
        if message:
            return f"HTTP {status}: {message}"
    snippet = re.sub(r"\s+", " ", body)[:240]
    return f"HTTP {status}: {snippet}"


def build_search_url(terms: list[str], qualifier: str, page: int) -> tuple[str, str]:
    if len(terms) > 5:
        raise ValueError("单查询 OR 不得超过 5 个")
    or_expr = " OR ".join(terms)
    query = f"({or_expr}) {qualifier}"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": "5",
        "page": str(page),
    }
    return query, SEARCH_URL + "?" + urllib.parse.urlencode(params)


def simplify_repo(item: dict) -> dict:
    full_name = item.get("full_name") or ""
    topics = item.get("topics") or []
    description = item.get("description") or ""
    return {
        "full_name": full_name,
        "url": item.get("html_url") or f"https://github.com/{full_name}",
        "description": description,
        "stars": item.get("stargazers_count"),
        "stars_today": None,
        "topics": topics,
        "language": item.get("language") or "",
        "created_at": item.get("created_at"),
        "pushed_at": item.get("pushed_at"),
        "topics_available": True,
        "matches": classify(full_name, topics, description),
        "excluded_list": is_list_repo(full_name, description),
    }


def annotate_trending(repos: list[dict]) -> list[dict]:
    annotated = []
    for repo in repos:
        item = dict(repo)
        item["matches"] = classify(
            item["full_name"],
            item.get("topics") or [],
            item.get("description") or "",
        )
        item["excluded_list"] = is_list_repo(
            item["full_name"], item.get("description") or ""
        )
        annotated.append(item)
    return annotated


def kept_repos(repos: list[dict], domain: str | None = None) -> list[dict]:
    """只保留命中当前领域的仓库。其它领域的命中留在 matches 里，供跨领域一行带过。"""
    kept = []
    for repo in repos:
        if repo.get("excluded_list"):
            continue
        matches = repo.get("matches") or {}
        if domain is not None:
            if domain not in matches:
                continue
        elif not matches:
            continue
        kept.append(repo)
    return kept


def fetch_all() -> dict:
    now = beijing_now()
    run_date = now.date()
    created_since = run_date - timedelta(days=30)
    pushed_since = run_date - timedelta(days=7)
    day_of_year = run_date.timetuple().tm_yday
    page = (day_of_year % 4) + 1
    headers = auth_headers()
    state = FetchState()
    sources: list[dict] = []

    trending_result = http_get_with_retry(TRENDING_URL, headers, state)
    trending_repos: list[dict] = []
    trending_source = {
        "section": "A",
        "domain": None,
        "kind": "trending_daily",
        "url": TRENDING_URL,
        "query": None,
        "ok": False,
        "http_status": trending_result["http_status"],
        "returned": 0,
        "kept": 0,
        "excluded_list": 0,
        "retried_after_rate_limit": trending_result["retried_after_rate_limit"],
        "rate_limit_remaining": trending_result["rate_limit_remaining"],
        "error": None,
        "note": "页面 stars today 即 24 小时新增 star。页面不提供 topics，A 块只按仓库名与强特征描述归类。",
    }
    if trending_result["http_status"] == 200:
        trending_repos = annotate_trending(parse_trending(trending_result["body"]))
        matched = [
            repo
            for repo in trending_repos
            if repo.get("matches") and not repo.get("excluded_list")
        ]
        excluded = sum(1 for repo in trending_repos if repo.get("excluded_list"))
        trending_source["ok"] = True
        trending_source["returned"] = len(trending_repos)
        trending_source["kept"] = len(matched)
        trending_source["excluded_list"] = excluded
    else:
        trending_source["error"] = error_message(
            trending_result["http_status"], trending_result["body"]
        )
    sources.append(trending_source)

    domains_out: dict[str, dict] = {}
    for domain, terms in SEARCH_TERMS.items():
        new_query, new_url = build_search_url(
            terms,
            f"created:>={created_since.isoformat()} stars:>2",
            page=1,
        )
        new_source, new_repos = run_search(
            section="B",
            domain=domain,
            query=new_query,
            url=new_url,
            headers=headers,
            state=state,
        )
        sources.append(new_source)

        ever_query, ever_url = build_search_url(
            terms,
            f"pushed:>={pushed_since.isoformat()} stars:>3",
            page=page,
        )
        ever_source, ever_repos = run_search(
            section="C",
            domain=domain,
            query=ever_query,
            url=ever_url,
            headers=headers,
            state=state,
        )
        sources.append(ever_source)
        domains_out[domain] = {
            "label": DOMAIN_LABELS[domain],
            "new": new_repos,
            "evergreen": ever_repos,
        }

    matched_trending = [
        repo
        for repo in trending_repos
        if repo.get("matches") and not repo.get("excluded_list")
    ]
    matched_trending.sort(
        key=lambda repo: (
            repo["stars_today"] is not None,
            repo["stars_today"] or 0,
        ),
        reverse=True,
    )

    return {
        "generated_at_beijing": now.strftime("%Y-%m-%d %H:%M:%S"),
        "run_date": run_date.isoformat(),
        "day_of_year": day_of_year,
        "evergreen_page": page,
        "created_since": created_since.isoformat(),
        "pushed_since": pushed_since.isoformat(),
        "request_count": state.calls,
        "sources": sources,
        "trending_all": trending_repos,
        "trending_matched": matched_trending,
        "domains": domains_out,
    }


def run_search(
    section: str,
    domain: str,
    query: str,
    url: str,
    headers: dict[str, str],
    state: FetchState,
) -> tuple[dict, list[dict]]:
    result = http_get_with_retry(url, headers, state)
    source = {
        "section": section,
        "domain": domain,
        "label": DOMAIN_LABELS[domain],
        "kind": "search",
        "url": url,
        "query": query,
        "ok": False,
        "http_status": result["http_status"],
        "returned": 0,
        "kept": 0,
        "excluded_list": 0,
        "unmatched": 0,
        "total_count": None,
        "incomplete_results": None,
        "retried_after_rate_limit": result["retried_after_rate_limit"],
        "rate_limit_remaining": result["rate_limit_remaining"],
        "error": None,
    }
    repos: list[dict] = []
    if result["http_status"] != 200:
        source["error"] = error_message(result["http_status"], result["body"])
        return source, repos
    try:
        payload = json.loads(result["body"])
    except json.JSONDecodeError as exc:
        source["error"] = f"HTTP 200 但 JSON 解析失败: {exc}"
        return source, repos
    items = payload.get("items") or []
    repos = [simplify_repo(item) for item in items]
    source["ok"] = True
    source["returned"] = len(repos)
    source["total_count"] = payload.get("total_count")
    source["incomplete_results"] = payload.get("incomplete_results")
    source["excluded_list"] = sum(1 for repo in repos if repo.get("excluded_list"))
    source["unmatched"] = sum(
        1
        for repo in repos
        if not repo.get("matches") and not repo.get("excluded_list")
    )
    kept = kept_repos(repos, domain)
    source["kept"] = len(kept)
    source["dropped"] = [
        {
            "full_name": repo["full_name"],
            "stars": repo["stars"],
            "excluded_list": repo.get("excluded_list"),
            "matches": repo.get("matches") or {},
            "description": repo.get("description") or "",
        }
        for repo in repos
        if repo not in kept
    ]
    return source, kept


def main() -> int:
    data = fetch_all()
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.write("\n")
    else:
        sys.stdout.write(text)
        sys.stdout.write("\n")
    print(
        f"run_date={data['run_date']} page={data['evergreen_page']} "
        f"requests={data['request_count']}",
        file=sys.stderr,
    )
    for source in data["sources"]:
        flag = "OK" if source["ok"] else "FAIL"
        print(
            f"[{flag}] {source['section']} {source.get('domain') or '-'} "
            f"status={source['http_status']} returned={source['returned']} "
            f"kept={source['kept']} error={source['error']}",
            file=sys.stderr,
        )
    return 0 if all(source["ok"] for source in data["sources"]) else 1


if __name__ == "__main__":
    sys.exit(main())
