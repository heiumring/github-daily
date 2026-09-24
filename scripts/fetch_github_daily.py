#!/usr/bin/env python3
"""抓取 GitHub 领域日报的原始数据。

只使用 Python 标准库（urllib）。不读取、不写入任何账号或密钥。
标准输出为 JSON：各数据源成败、归类后的仓库。报告正文由调用方据此撰写。

GitHub Search 的实际约束（脚本按此发请求，并在 sources 里写明）：
- 不接受 pushed:>7d，日期必须是 ISO 8601，因此改用 pushed:>=（北京时间今日减 7 天）
- 一条查询最多 5 个 OR，因此每个领域只拿 6 个代表性关键词去检索
- 未认证检索限流约 10 次/分钟，故检索串行、间隔 2 秒，总次数不超过 5
归类仍使用完整关键词表，不限于检索用的那 6 个。
"""

from __future__ import annotations

import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

BJ = timezone(timedelta(hours=8))
USER_AGENT = "github-daily-report/1.0"
OSS_URL = (
    "https://api.ossinsight.io/v1/trends/repos/"
    "?period=past_24_hours&language=All"
)
TRENDING_URL = "https://github.com/trending?since=daily"
SEARCH_URL = "https://api.github.com/search/repositories"

# 完整关键词表。匹配时小写，连字符与空格等价。
KEYWORDS = {
    "embedded": [
        "embedded-systems",
        "rtos",
        "stm32",
        "esp32",
        "zephyr",
        "freertos",
        "firmware",
        "bare-metal",
        "risc-v",
        "cortex-m",
        "mcu",
        "modbus",
        "can-bus",
        "dsp",
        "fpga",
        "verilog",
        "vhdl",
        "hdl",
        "yosys",
        "verilator",
        "cocotb",
        "zynq",
        "softcore",
    ],
    "ai": [
        "llm",
        "ai-agents",
        "rag",
        "mcp",
        "pytorch",
        "transformer",
        "diffusion",
        "computer-vision",
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
        "inverter",
        "dc-dc",
        "buck",
        "boost",
        "llc",
        "pfc",
        "mppt",
        "bms",
        "motor-drive",
        "power-supply",
        "microgrid",
        "pll",
    ],
    "control": [
        "control-systems",
        "pid",
        "mpc",
        "kalman-filter",
        "foc",
        "motor-control",
        "ros2",
        "slam",
        "flight-controller",
    ],
}

# 每域最多 6 个词（5 个 OR）。避开过短、会把检索结果淹没掉的词：
# gan 会命中生成对抗网络，boost/buck/pid 等过泛。这些词仍参与归类。
SEARCH_TERMS = {
    "embedded": [
        "embedded-systems",
        "freertos",
        "stm32",
        "esp32",
        "zephyr",
        "fpga",
    ],
    "ai": [
        "llm",
        "ai-agents",
        "rag",
        "mcp",
        "pytorch",
        "transformer",
    ],
    "power_devices": [
        "power-electronics",
        "igbt",
        "mosfet",
        "wide-bandgap",
        "device-modeling",
        "sic",
    ],
    "power_supply": [
        "inverter",
        "dc-dc",
        "power-supply",
        "motor-drive",
        "microgrid",
        "mppt",
    ],
    "control": [
        "control-systems",
        "motor-control",
        "flight-controller",
        "ros2",
        "kalman-filter",
        "slam",
    ],
}

DOMAIN_ORDER = [
    "embedded",
    "ai",
    "power_devices",
    "power_supply",
    "control",
]


def http_get(url: str, headers: dict[str, str], timeout: int = 30):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read()


def normalize(text: str) -> str:
    return text.lower().replace("-", " ").replace("_", " ")


def keyword_in(text: str, keyword: str) -> bool:
    hay = normalize(text)
    needle = normalize(keyword)
    if not needle:
        return False
    pattern = r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])"
    return re.search(pattern, hay) is not None


def classify(name: str, description: str, topics: list[str]) -> dict[str, list[str]]:
    parts = [name, description or ""]
    parts.extend(topics or [])
    hits: dict[str, list[str]] = {}
    for domain in DOMAIN_ORDER:
        matched = []
        for kw in KEYWORDS[domain]:
            if any(keyword_in(part, kw) for part in parts if part):
                matched.append(kw)
        if matched:
            hits[domain] = matched
    return hits


def parse_int(value) -> int | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return int(value)
    text = str(value).strip().replace(",", "")
    if not text:
        return None
    try:
        return int(float(text))
    except ValueError:
        return None


def blank_repo(full_name: str) -> dict:
    owner, _, name = full_name.partition("/")
    return {
        "full_name": full_name,
        "name": name or full_name,
        "owner": owner,
        "description": "",
        "topics": [],
        "stars": None,
        "stars_24h": None,
        "sources": [],
    }


def merge_repo(bucket: dict[str, dict], incoming: dict) -> None:
    key = incoming["full_name"].lower()
    current = bucket.get(key)
    if current is None:
        bucket[key] = incoming
        return
    if incoming.get("stars_24h") is not None:
        current["stars_24h"] = incoming["stars_24h"]
    if incoming.get("stars") is not None and (
        current.get("stars") is None or incoming["stars"] > current["stars"]
    ):
        current["stars"] = incoming["stars"]
    if len(incoming.get("description") or "") > len(current.get("description") or ""):
        current["description"] = incoming["description"]
    topics = set(current.get("topics") or [])
    topics.update(incoming.get("topics") or [])
    current["topics"] = sorted(topics)
    for src in incoming.get("sources") or []:
        if src not in current["sources"]:
            current["sources"].append(src)


def fetch_ossinsight() -> tuple[dict, list[dict]]:
    status = {
        "ok": False,
        "url": OSS_URL,
        "http_status": None,
        "count": 0,
        "reason": None,
    }
    repos: list[dict] = []
    try:
        code, body = http_get(
            OSS_URL,
            {"User-Agent": USER_AGENT, "Accept": "application/json"},
        )
    except urllib.error.URLError as exc:
        status["reason"] = f"网络错误：{exc.reason}"
        return status, repos

    status["http_status"] = code
    try:
        payload = json.loads(body.decode("utf-8", errors="replace"))
    except json.JSONDecodeError:
        status["reason"] = f"HTTP {code}，响应不是 JSON"
        return status, repos

    if code != 200:
        message = payload.get("message") if isinstance(payload, dict) else None
        status["reason"] = f"HTTP {code}" + (f"：{message}" if message else "")
        return status, repos

    rows = []
    if isinstance(payload, dict):
        data = payload.get("data") or {}
        if isinstance(data, dict):
            rows = data.get("rows") or []
    if not isinstance(rows, list):
        rows = []

    quality = payload.get("data_quality") if isinstance(payload, dict) else None
    if not rows:
        if isinstance(quality, dict) and quality.get("status") not in (None, "ok", "available"):
            reason = quality.get("reason") or quality.get("status")
            since = quality.get("unavailable_since")
            extra = f"（自 {since} 起不可用）" if since else ""
            status["reason"] = f"接口返回空列表。{reason}{extra}"
        else:
            status["reason"] = "接口返回空的 data.rows"
        return status, repos

    status["ok"] = True
    status["reason"] = None
    for row in rows[:100]:
        if not isinstance(row, dict):
            continue
        full_name = row.get("repo_name") or row.get("full_name") or row.get("repo")
        if not full_name or "/" not in str(full_name):
            continue
        repo = blank_repo(str(full_name))
        repo["description"] = (row.get("description") or "") or ""
        topics = row.get("topics") or row.get("repo_topics") or []
        if isinstance(topics, str):
            topics = [part for part in re.split(r"[, ]+", topics) if part]
        repo["topics"] = [str(t) for t in topics]
        # OSS Insight 的 stars 是时间窗内新增，不是累计 star。
        repo["stars_24h"] = parse_int(row.get("stars"))
        repo["stars"] = parse_int(
            row.get("total_stars")
            or row.get("stargazers_count")
            or row.get("star_count")
        )
        repo["sources"] = ["ossinsight"]
        repos.append(repo)
    status["count"] = len(repos)
    if not repos:
        status["ok"] = False
        status["reason"] = "data.rows 有记录，但没有可识别的 repo_name"
    return status, repos


def fetch_trending() -> tuple[dict, list[dict]]:
    status = {
        "ok": False,
        "url": TRENDING_URL,
        "http_status": None,
        "count": 0,
        "reason": None,
    }
    repos: list[dict] = []
    try:
        code, body = http_get(
            TRENDING_URL,
            {"User-Agent": USER_AGENT, "Accept": "text/html"},
        )
    except urllib.error.URLError as exc:
        status["reason"] = f"网络错误：{exc.reason}"
        return status, repos

    status["http_status"] = code
    if code != 200:
        status["reason"] = f"HTTP {code}"
        return status, repos

    page = body.decode("utf-8", errors="replace")
    articles = re.findall(r"<article\b.*?</article>", page, flags=re.S | re.I)
    for article in articles:
        name_match = re.search(
            r'<h2[^>]*>.*?<a[^>]*href="/([^"/]+)/([^"/]+)"',
            article,
            flags=re.S,
        )
        if not name_match:
            continue
        full_name = f"{name_match.group(1)}/{name_match.group(2)}"
        repo = blank_repo(full_name)
        desc_match = re.search(
            r'<p class="col-9 color-fg-muted[^"]*">(.*?)</p>',
            article,
            flags=re.S,
        )
        if desc_match:
            text = re.sub(r"<[^>]+>", " ", desc_match.group(1))
            repo["description"] = re.sub(r"\s+", " ", html.unescape(text)).strip()
        today_match = re.search(r"([0-9][0-9,]*)\s+stars?\s+today", article)
        if today_match:
            repo["stars_24h"] = parse_int(today_match.group(1))
        star_link = re.search(
            r'href="/[^"]+/stargazers"[^>]*>(.*?)</a>',
            article,
            flags=re.S,
        )
        if star_link:
            star_text = re.sub(r"<[^>]+>", " ", star_link.group(1))
            num = re.search(r"([0-9][0-9,]*)", star_text)
            if num:
                repo["stars"] = parse_int(num.group(1))
        repo["sources"] = ["github_trending"]
        repos.append(repo)

    status["count"] = len(repos)
    if repos:
        status["ok"] = True
    else:
        status["reason"] = "页面已返回，但没有解析出带仓库名的 trending 条目"
    return status, repos


def search_term(keyword: str) -> str:
    if "-" in keyword or " " in keyword:
        return '"' + keyword + '"'
    return keyword


def fetch_searches(pushed_since: str) -> tuple[dict, list[dict]]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    status = {
        "ok": False,
        "request_count": 0,
        "interval_seconds": 2,
        "note": (
            "GitHub Search 拒绝字面量 pushed:>7d（需要 ISO 8601 日期），"
            "且一条查询最多 5 个 OR。因此每个领域用 6 个代表性关键词，"
            f"限定 pushed:>={pushed_since} stars:>3，按 stars 降序取 10 条。"
            "检索串行执行，每次间隔 2 秒。"
        ),
        "domains": {},
    }
    repos: list[dict] = []
    for index, domain in enumerate(DOMAIN_ORDER):
        if index:
            time.sleep(2)
        terms = " OR ".join(search_term(kw) for kw in SEARCH_TERMS[domain])
        query = f"{terms} pushed:>={pushed_since} stars:>3"
        url = SEARCH_URL + "?" + urllib.parse.urlencode(
            {
                "q": query,
                "sort": "stars",
                "order": "desc",
                "per_page": "10",
            }
        )
        domain_status = {
            "ok": False,
            "query": query,
            "http_status": None,
            "total_count": None,
            "returned": 0,
            "reason": None,
        }
        status["request_count"] += 1
        try:
            code, body = http_get(url, headers)
        except urllib.error.URLError as exc:
            domain_status["reason"] = f"网络错误：{exc.reason}"
            status["domains"][domain] = domain_status
            continue

        domain_status["http_status"] = code
        try:
            payload = json.loads(body.decode("utf-8", errors="replace"))
        except json.JSONDecodeError:
            domain_status["reason"] = f"HTTP {code}，响应不是 JSON"
            status["domains"][domain] = domain_status
            continue

        if code != 200 or not isinstance(payload, dict) or "items" not in payload:
            message = payload.get("message") if isinstance(payload, dict) else None
            errors = payload.get("errors") if isinstance(payload, dict) else None
            detail = message or "请求失败"
            if errors:
                detail = f"{detail}；{json.dumps(errors, ensure_ascii=False)}"
            domain_status["reason"] = f"HTTP {code}：{detail}"
            status["domains"][domain] = domain_status
            continue

        items = payload.get("items") or []
        domain_status["ok"] = True
        domain_status["total_count"] = payload.get("total_count")
        domain_status["returned"] = len(items)
        status["domains"][domain] = domain_status
        for item in items:
            full_name = item.get("full_name")
            if not full_name:
                continue
            repo = blank_repo(full_name)
            repo["description"] = item.get("description") or ""
            topics = item.get("topics") or []
            repo["topics"] = [str(t) for t in topics]
            repo["stars"] = parse_int(item.get("stargazers_count"))
            repo["sources"] = [f"github_search:{domain}"]
            repos.append(repo)

    status["ok"] = all(item.get("ok") for item in status["domains"].values()) and bool(
        status["domains"]
    )
    if not status["ok"]:
        failed = [
            name
            for name, item in status["domains"].items()
            if not item.get("ok")
        ]
        status["reason"] = "部分或全部领域检索失败：" + "、".join(failed)
    return status, repos


def build() -> dict:
    now = datetime.now(BJ)
    pushed_since = (now.date() - timedelta(days=7)).isoformat()
    window_start = now - timedelta(hours=24)
    bucket: dict[str, dict] = {}

    oss_status, oss_repos = fetch_ossinsight()
    for repo in oss_repos:
        merge_repo(bucket, repo)

    trending_status = {
        "ok": None,
        "skipped": False,
        "url": TRENDING_URL,
        "reason": None,
        "count": 0,
    }
    if not oss_status["ok"]:
        trending_status, trending_repos = fetch_trending()
        for repo in trending_repos:
            merge_repo(bucket, repo)
    else:
        trending_status["skipped"] = True
        trending_status["reason"] = "OSS Insight 已成功，按规则未再抓取 GitHub Trending 兜底页"

    search_status, search_repos = fetch_searches(pushed_since)
    for repo in search_repos:
        merge_repo(bucket, repo)

    classified = []
    for repo in bucket.values():
        hits = classify(repo["name"], repo["description"], repo["topics"])
        if not hits:
            continue
        repo["domains"] = list(hits.keys())
        repo["matched_keywords"] = hits
        repo["url"] = f"https://github.com/{repo['full_name']}"
        classified.append(repo)

    classified.sort(
        key=lambda item: (item["stars_24h"] or 0, item["stars"] or 0),
        reverse=True,
    )

    by_domain = {domain: [] for domain in DOMAIN_ORDER}
    for repo in classified:
        for domain in repo["domains"]:
            by_domain[domain].append(repo["full_name"])

    return {
        "generated_at_bj": now.isoformat(timespec="seconds"),
        "report_date": now.date().isoformat(),
        "window": {
            "intended": "过去 24 小时",
            "start_bj": window_start.isoformat(timespec="seconds"),
            "end_bj": now.isoformat(timespec="seconds"),
            "search_pushed_since": pushed_since,
        },
        "sources": {
            "ossinsight": oss_status,
            "github_trending": trending_status,
            "github_search": search_status,
        },
        "domain_counts": {domain: len(names) for domain, names in by_domain.items()},
        "repos": classified,
    }


def main() -> None:
    report = build()
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
