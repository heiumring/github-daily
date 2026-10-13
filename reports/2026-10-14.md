# GitHub 领域日报 · 2026-10-14

生成时间：2026-10-14 07:34（北京时间）。数据拉取开始于 2026-10-14 07:31:06（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-14（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-07 及之后有推送、总 star > 3。轮换页 `page = (当年第 287 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [lyogavin/airllm](https://github.com/lyogavin/airllm) 是今日 Trending 里唯一命中领域关键词的仓库，24 小时新增 star 1004，总 star 38298，要在单张 4GB 显卡上跑超大语言模型推理。
2. [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) 用一次前向做分类、打分和是否判断，而不是逐字生成；近 30 天新建，总 star 32768。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真机 iPhone；近 30 天新建，总 star 1495。

## A. 今日热度

Trending 页面解析到 9 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。嵌入式、功率器件、电力电子电源、自动控制在这 9 条里没有命中。

### AI

- [lyogavin/airllm](https://github.com/lyogavin/airllm)
  - 说明：按仓库描述，在单张 4GB 显卡上做 AirLLM 2.8T 的大语言模型推理，用来在小显存机器上跑本来装不下的模型。
  - 领域：AI
  - 总 star：38298
  - 24 小时新增 star：1004

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：1495
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：882
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：381
- [Frankweb33/flybrain-robot-bridge](https://github.com/Frankweb33/flybrain-robot-bridge)
  - 说明：把果蝇神经回路的思路接到相机和电机上，用光流和 IMU 把看见的画面变成机器人动作；仓库写明现在仍是实验桥接。
  - 领域：嵌入式 Embedded
  - 总 star：227
- [andrisgauracs/wifi-sensing-kit](https://github.com/andrisgauracs/wifi-sensing-kit)
  - 说明：用三块约 10 美元的 ESP32-S3，靠 WiFi 信号判断人在做什么，训练时用摄像头当老师。
  - 领域：嵌入式 Embedded
  - 总 star：132

### AI

- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
  - 说明：用一次前向完成文本上的分类、打分和是否判断，并按请求挑选检查点，覆盖描述中的 100 多种语言。
  - 领域：AI
  - 总 star：32768
- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：5115
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：1495。
- [Frankweb33/flybrain-robot-bridge](https://github.com/Frankweb33/flybrain-robot-bridge) — 见上方「嵌入式 Embedded」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：227。

### 功率器件 Power Devices

- [tPkl/OpenRdson](https://github.com/tPkl/OpenRdson)
  - 说明：开源的场效应管版图寄生参数提取，用网格和有限元去对标 Synopsys / SFT 的 R3D，给模拟版图做提取。
  - 领域：功率器件 Power Devices
  - 总 star：6

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [cocel-postech/genz-lio](https://github.com/cocel-postech/genz-lio)
  - 说明：激光雷达加 IMU 的里程计，针对室内外和退化场景把位姿估稳；仓库标明发表于 IEEE T-FR 2026。
  - 领域：自动控制 Control
  - 总 star：80
- [HengyiWang/amb3r-slam](https://github.com/HengyiWang/amb3r-slam)
  - 说明：面向公里级范围的 SLAM，用分层后端处理很长的轨迹，而不是只在室内小地图里定位。
  - 领域：自动控制 Control
  - 总 star：74

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 4。

### 嵌入式 Embedded

- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：用 ESP32 采集 Wi-Fi 信道状态做动作感知，并带 C++ SDK、ESPHome 和 Matter 前端，把人体活动检测接进智能家居。
  - 领域：嵌入式 Embedded
  - 总 star：9582
- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的官方固件，在 ESP32、STM32、nRF52 等芯片上做离网 LoRa 网格通信。
  - 领域：嵌入式 Embedded
  - 总 star：8420
- [crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)
  - 说明：开源墨水屏电子书固件，跑在 ESP32 上，用来读 EPUB。
  - 领域：嵌入式 Embedded
  - 总 star：8337
- [FastLED/FastLED](https://github.com/FastLED/FastLED)
  - 说明：给 Arduino、ESP32 等板上的可寻址彩色灯珠做动画库，把不同灯珠协议收成一套接口。
  - 领域：嵌入式 Embedded
  - 总 star：7508

### AI

- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
  - 说明：给智能体一条命令行去读和搜索推特、Reddit、YouTube、GitHub、B 站和小红书，不用按网站分别接付费 API。
  - 领域：AI
  - 总 star：96983
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
  - 说明：给编程助手一套设计技能，用美术方向、参考图和浏览器检查来做页面，让生成结果离开千篇一律的模板。
  - 领域：AI
  - 总 star：95586
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：做高吞吐、省内存的大模型推理和在线服务，用来把模型稳定地对外提供。
  - 领域：AI
  - 总 star：93733
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：把任意网站抓成适合大模型阅读的 Markdown，给智能体提供网页内容，可以自己部署，也可以走它的云服务。
  - 领域：AI
  - 总 star：85461
- [pypose/pypose](https://github.com/pypose/pypose) — 见下方「自动控制 Control」完整条目。话题含 pytorch，此处不展开。领域：AI。总 star：1614。

### 功率器件 Power Devices

本页没有可列入正文的功率器件仓库。

### 电力电子电源 Power Supply

- [fl4p/batmon-ha](https://github.com/fl4p/batmon-ha)
  - 说明：给 Home Assistant 加一个蓝牙接入，把 JK、JBD、Daly、ANT、SOK、Supervolt 等电池管理系统的数据收进来，不必为每个牌子单独做网关。
  - 领域：电力电子电源 Power Supply
  - 总 star：523

### 自动控制 Control

- [google-deepmind/mujoco_mpc](https://github.com/google-deepmind/mujoco_mpc)
  - 说明：在 MuJoCo 里用模型预测控制实时合成动作，用来在仿真中直接算出下一步该怎么动。
  - 领域：自动控制 Control
  - 总 star：1744
- [pypose/pypose](https://github.com/pypose/pypose)
  - 说明：在流形上做可微分的机器人算法，把位姿、SLAM 和卡尔曼滤波收成能跟着学习一起反传的库。
  - 领域：自动控制 Control
  - 总 star：1614
- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用 MuJoCo 搭一组肌肉骨骼模型的控制任务，并包成 Gym 环境，用来研究肌肉驱动下的运动控制。
  - 领域：自动控制 Control
  - 总 star：1253

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 9 条，规则命中 1 条（`lyogavin/airllm`，描述中的 `LLM` 命中强特征词 `llm`；仓库名 `airllm` 不能按词边界拆出 `llm`。总 star 38298，stars today 1004），清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词）：`morluto/rea`（总 star 205861，stars today 54706）、`storytold/artcraft`（25553，4078）、`debpalash/VoiceStudio`（63152，2277）、`bilawalsidhu/gods-eye-view`（55313，1961）、`cathrynlavery/diagram-design`（54040，1813）、`xtool-org/xtool`（9296，1182）、`mksglu/context-mode`（28195，978；描述里的 AI、MCP 是弱词，未计入）、`vercel-labs/skills`（34467，187）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-14 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-14 stars:>2`。`total_count=379`，返回 5，规则保留 5，排除清单 0。剩余配额 9。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-14 stars:>2`。`total_count=2033`，返回 5，规则保留 2，未命中 3，排除清单 0。剩余配额 9。正文另有 2 条来自嵌入式检索的跨领域一行（`esp32-iphone-agent`、`flybrain-robot-bridge`）。
  - 未命中：`zai-org/ZCode`（总 star 7772）、`mizorewww/laya-mlx`（6916；描述里的 PyTorch 出现在否定句里，且 `pytorch` 不是强特征描述词）、`mhtsec/ARTEX`（3870）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-14 stars:>2`。`total_count=5`，返回 5，规则保留 2，未命中 3。剩余配额 8。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 6）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（16）、`MadestSamurai/bd2-sichuan`（12）、`MicroFarmerVoyage/hellraiser-revival-motion-sickness-tool`（8）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-14 stars:>2`。`total_count=72`，返回 5，规则保留 0。剩余配额 7。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（141）、`ningbainb/Dcode`（37）、`meztinos515/Acrobat-Pro-DC`（35）、`KawaiiBunga/MKVDCU-Recomp`（35）、`lamb2k/re4dc`（26）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-14 stars:>2`。`total_count=50`，返回 5，规则保留 3，未命中控制关键词 2。剩余配额 9。正文保留 2 条。
  - `sd88me/mpc-vst-plugins`（总 star 115）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，与模型预测控制无关，正文不收。
  - `Frankweb33/flybrain-robot-bridge`（227）：本查询返回，但未命中控制关键词；已写入嵌入式，并在 AI 一行带过。描述里的 “motor control” 是两个词，不等于 `motor-control`。
  - `xwtk/hmg_nemesis`（59）：名称和 topics 未命中。

### C. 领域常青（`pushed:>=2026-10-07 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-07 stars:>3`。`total_count=1124`，返回 5，规则保留 4，清单类排除 1。剩余配额 9。
  - 排除清单：`nhivp/Awesome-Embedded`（总 star 9212），awesome 合集。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-07 stars:>3`。`total_count=8243`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 9。`Panniantong/Agent-Reach` 的话题是 `llm-tools`，按词边界命中 `llm`。`pypose/pypose` 不在这 5 条里，因话题含 `pytorch`，本节一行带过，完整条目在自动控制。
  - 未命中：`lobehub/lobehub`（总 star 83209）。名称和 topics 没有 llm / pytorch / transformer / diffusion / ai-agents。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-07 stars:>3`。`total_count=23`，返回 5，规则保留 1，清单类排除 1，未命中 3。剩余配额 8。本页没有可展开的功率器件条目。
  - `miha42-github/company_dns`（总 star 10）：话题和描述里的 `sic` 是 EDGAR / 美国上市公司的行业分类代码（Standard Industrial Classification），与碳化硅器件无关，正文不收。
  - 排除清单：`satnamrsm/https-github.com-sickn33-antigravity-awesome-skills`（总 star 8），名称含 awesome；同时 `sickn33` 按词边界不等于 `sic`，规则上也没有领域命中。
  - 名称和 topics 未命中：`CAPS-DGU/UmJoonSIC`（9；`UmJoonSIC` 按词边界不等于 `sic`）、`MicroFarmerVoyage/hellraiser-revival-motion-sickness-tool`（8）、`SICKAG/SICK-App-Designer-Docs`（8）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-07 stars:>3`。`total_count=361`，返回 5，规则保留 1，未命中 4。剩余配额 9。正文保留 `fl4p/batmon-ha`（总 star 523，topic `bms`）。
  - 名称和 topics 未命中：`hackthedev/dcts-shipping`（645）、`ciribob/DCS-SimpleRadioStandalone`（558）、`hashicorp/consul-replicate`（525）、`dcm4che/dcm4chee-arc-light`（505）。检索词 `dc-dc` 在搜索侧撞上了名称或描述里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-07 stars:>3`。`total_count=222`，返回 5，规则保留 4，未命中 1。剩余配额 6。正文保留 3 条。`google-deepmind/mujoco_mpc` 的话题含 `mpc` 与 `motor-control`，是模型预测控制，不是音序器撞名。`pypose/pypose` 同时话题含 `pytorch`，完整条目在本节，AI 一节一行带过。
  - 排除清单：`Vincentqyw/cv-arxiv-daily`（总 star 1506）。话题含 `slam`，仓库是用 GitHub Actions 每日更新的计算机视觉论文清单，属于清单类，正文不收。
  - 未命中：`nvidia-isaac/cuVSLAM`（1862）。描述写到 SLAM，但 `slam` 不是强特征描述词；仓库名 `cuVSLAM` 按词边界不能拆出 `slam`。
