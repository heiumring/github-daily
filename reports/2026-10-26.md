# GitHub 领域日报 · 2026-10-26

生成时间：2026-10-26 07:35（北京时间）。数据拉取开始于 2026-10-26 07:30:44（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-26（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-19 及之后有推送、总 star > 3。轮换页 `page = (当年第 299 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) 用多个大模型代理搭一套金融交易框架；今日热度里唯一命中，总 star 114560，24 小时新增 star 636。
2. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，眼睛走 AirPlay，手走 USB HID；近 30 天新建，总 star 3877。
3. [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library) 给永磁同步电机做磁场定向控制，位置环、速度环、电流环以及 PID、LADRC 都在库里，面向 MCU 上的伺服；领域常青，总 star 1108，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 11 条。页面不带 topics，因此只按仓库名和强特征描述归类。规则命中 1 条，清单类排除 0 条。按 24 小时新增 star 降序。

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
  - 说明：多个大模型代理组成一套金融交易框架，用来把交易决策交给这组代理。
  - 领域：AI
  - 总 star：114560
  - 24 小时新增 star：636

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：3877
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：1117
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：441
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验台收成一个网页，能看实时引脚、跑交互模拟、读 esp-labs 固件和实验记录，界面有 11 种语言。
  - 领域：嵌入式 Embedded
  - 总 star：282
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：254

### AI

- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor、Gemini CLI、Antigravity 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：6447
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：4425
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：3877。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：2781
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：254。

### 功率器件 Power Devices

- [tPkl/OpenRdson](https://github.com/tPkl/OpenRdson)
  - 说明：用开源网格和有限元做场效应管版图的寄生参数提取，用来替代 Synopsys / SFT 的 R3D。
  - 领域：功率器件 Power Devices
  - 总 star：6

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：89
- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室把 2026 年 RoboMaster 超级对抗赛哨兵的定位开源出来，用 Livox MID360 做激光雷达与 IMU 里程计，并带重定位，跑在 ROS 2 上。
  - 领域：自动控制 Control
  - 总 star：80

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 4。

### 嵌入式 Embedded

- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：用 ESP32 读 Wi-Fi 信道状态信息来判断有没有人在动，带 C++ SDK，以及 ESPHome、原生固件和 Matter 几种接法，用来做不靠摄像头的运动检测。
  - 领域：嵌入式 Embedded
  - 总 star：9685
- [crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)
  - 说明：开源墨水屏电子书固件，跑在 ESP32 上，用来读 EPUB。
  - 领域：嵌入式 Embedded
  - 总 star：8517
- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的官方固件，在没有蜂窝网时用 LoRa 做网状通信，板级覆盖 ESP32、STM32，也支持 nRF52 和 RP2040。
  - 领域：嵌入式 Embedded
  - 总 star：8476
- [FastLED/FastLED](https://github.com/FastLED/FastLED)
  - 说明：在 Arduino 上做彩色 LED 动画的库，也覆盖 ESP32 和 Teensy，用来驱动 WS2812、APA102 这类可寻址灯珠。
  - 领域：嵌入式 Embedded
  - 总 star：7516
- [BruceDevices/firmware](https://github.com/BruceDevices/firmware)
  - 说明：面向 Cardputer、M5Stack、LilyGO 等板卡的 ESP32 固件，话题含射频、NFC 和 offsec，用来在这些板上跑一套现成的硬件工具固件。
  - 领域：嵌入式 Embedded
  - 总 star：7082
- [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library) — 见下方「自动控制 Control」完整条目。话题含 embedded 与 mcu，此处不展开。领域：嵌入式 Embedded。总 star：1108。
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：706。

### AI

- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：高吞吐、省内存的大模型推理引擎，用来把 LLM 做成可调用的服务。
  - 领域：AI
  - 总 star：95485
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：开源网页爬虫，把网站收成适合大模型阅读的 Markdown，给 LLM 和代理提供干净文本，可以自己部署。
  - 领域：AI
  - 总 star：86260
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)
  - 说明：多智能体框架，用来部署一组会协作的自主代理，并接到 Claude Code、Codex、Hermes 等编程助手。
  - 领域：AI
  - 总 star：79275
- [unslothai/unsloth](https://github.com/unslothai/unsloth)
  - 说明：在本地跑和训练大模型与扩散模型的界面，支持 GGUF 和 MLX，描述里还列出 Qwen3.8、DeepSeek-V4.1、MiniMax-H3、Gemma 4、FLUX。
  - 领域：AI
  - 总 star：78560
- [stereolabs/zed-sdk](https://github.com/stereolabs/zed-sdk) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：1246。

### 功率器件 Power Devices

本页剔除撞名后没有功率器件仓库。

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：把阳光电源 SH*RT、SHx.RS、SH*K、SxT 这几族逆变器接到 Home Assistant，经 Modbus 读运行数据。
  - 领域：电力电子电源 Power Supply
  - 总 star：706
- [fl4p/batmon-ha](https://github.com/fl4p/batmon-ha)
  - 说明：Home Assistant 插件，经蓝牙连接 JK、JBD、Daly、ANT、SOK、Supervolt 等电池管理系统，用来在家里读电池数据。
  - 领域：电力电子电源 Power Supply
  - 总 star：528

### 自动控制 Control

- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用 MuJoCo 模拟肌肉骨骼模型，并包成 OpenAI Gym 任务，用来试验运动控制算法怎么驱动这些肌肉模型。
  - 领域：自动控制 Control
  - 总 star：1265
- [stereolabs/zed-sdk](https://github.com/stereolabs/zed-sdk)
  - 说明：Stereolabs ZED 相机的空间感知开发包，用来做双目深度、定位建图和机器人环境感知。
  - 领域：自动控制 Control
  - 总 star：1246
- [SJTU-ViSYS/M2DGR](https://github.com/SJTU-ViSYS/M2DGR)
  - 说明：地面机器人的多模态、多场景数据集，发表于 RA-L 2021 与 ICRA 2022，给 SLAM 研究提供可对照的数据。
  - 领域：自动控制 Control
  - 总 star：1219
- [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library)
  - 说明：给有传感器或无传感器的永磁同步电机做磁场定向控制，含基于 SVPWM 的位置环、速度环和电流环，并带可配置的 PID 和 LADRC，用来在 MCU 上做伺服。
  - 领域：自动控制 Control
  - 总 star：1108

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 11 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`TauricResearch/TradingAgents`（总 star 114560，stars today 636）。描述含强特征词 LLM，归入 AI。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`cloudflare/security-audit-skill`（46808，2874；coding-agent 不是强特征词）、`debpalash/VoiceStudio`（86734，1588）、`Nutlope/hallmark`（33681，1359；描述里的 AI 是弱词）、`pbakaus/impeccable`（87641，1113；描述里的 AI 是弱词）、`makecindy/cindy`（4819，677；描述里的 AI Agent 是弱词）、`pollen-robotics/microduck`（11605，657；双足小鸭机器人，名称和描述都没有领域词）、`Renhuai123/ziwei-doushu`（7525，255）、`coollabsio/coolify`（64333，192）、`AgriciDaniel/claude-seo`（20817，179；描述里的 WebMCP、`llms.txt` 按词边界不等于 llm，也不是强特征词）、`JetBrains/thinkrail`（1653，52）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-26 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-26 stars:>2`。`total_count=390`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文。`onehumanbeing/esp32-iphone-agent`（3877）和 `raullenchai/esp32-thinks`（254）同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`agharsallah/esp-labs-web`（282）话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单或 awesome 合集，正文保留。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-26 stars:>2`。`total_count=2382`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 8。正文保留 `Louis-CFM/coucou`（6447）、`QingYunA/answer-me-with-html`（4425）、`Leonxlnx/earshot`（2781）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`kaankiziltug/logo-design-skill`（总 star 4574；描述里的 AI agents 是弱词）、`openfilm/openfilm`（总 star 2824；描述里的 AI video agent 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-26 stars:>2`。`total_count=5`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 5）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（23）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`SiCo`、`Sichuan` 按词边界都不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-26 stars:>2`。`total_count=77`，返回 5，规则保留 0。剩余配额 8。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（190）、`CompaLarios18/MH4UltimateDC`（56）、`Lida-V/3DCharaMakeSkills-Lida`（49）、`lamb2k/re4dc`（37）、`two-delta/DCOCO`（36；描述为空）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-26 stars:>2`。`total_count=54`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `TrentIndeed/kinetiqgym`（89）、`mozihe/z-localization`（80）。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 42）。话题含 `ros2` 与 `slam`，描述写明是机器人开发自学课程地图和面试型测验，属课程清单，不进正文。
  - 名称和 topics 未命中：`xwtk/hmg_nemesis`（190）、`lbgos/rift-s-linux`（31；描述里的 SLAM 不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-19 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-19 stars:>3`。`total_count=1155`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。这 5 条都写入正文。`Sguan-ZhouQing/SguanFOC_Library` 不在这 5 条里，来自自动控制检索；话题含 `embedded` 与 `mcu`，要解决的是永磁同步电机的磁场定向控制，完整条目在自动控制，本节一行带过。`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant` 不在这 5 条里，来自电力电子检索；话题含 `modbus`，本节一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-19 stars:>3`。`total_count=8851`，返回 5，规则保留 4，未命中 1，清单类排除 0。剩余配额 8。正文保留 `vllm-project/vllm`（95485，话题含 `llm`、`pytorch`、`transformer`）、`unclecode/crawl4ai`（86260，话题含 `llm` 与 `ai-agents`）、`ruvnet/ruflo`（79275，话题含 `ai-agents`）、`unslothai/unsloth`（78560，话题含 `llm`；`stable-diffusion` 按词边界计入 `diffusion`）。`stereolabs/zed-sdk` 不在这 5 条里，来自自动控制检索，话题含 `computer-vision`，本节一行带过。
  - 未命中：`lobehub/lobehub`（总 star 83490）。描述里的 AI team 是弱词，名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-19 stars:>3`。`total_count=24`，返回 5，规则保留 2，清单类排除 1，未命中 2。剩余配额 8。`page=4`、`per_page=5`，本页返回满 5 条。规则保留的 2 条都是撞名，正文不收。本页没有功率器件完整条目，也没有可跨领域一行带过的功率器件仓库。
  - `miha42-github/company_dns`（10）：话题含 `sic`，描述是 EDGAR 公司数据与 SEC 行业分类 SIC 查询，与碳化硅器件无关，正文不收。
  - `Oire/sic`（5）：名称是 SIC，描述为 Simple Image Converter，是图片转换器，正文不收。
  - 清单类排除：`satnamrsm/https-github.com-sickn33-antigravity-awesome-skills`（总 star 8）。名称含 awesome，且名称和 topics 都没有功率器件关键词。
  - 名称按词边界不等于 `sic`：`reekta92/sicth`（7）、`dfirs1car1o/sicario-spec`（5）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-19 stars:>3`。`total_count=386`，返回 5，规则保留 2，未命中 3。剩余配额 9。正文完整条目为 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（706，topic `inverter`）和 `fl4p/batmon-ha`（528，topic `bms`）。阳光电源那条同时话题含 `modbus`，嵌入式一节一行带过。
  - 名称和 topics 未命中电力电子：`hackthedev/dcts-shipping`（642）、`hashicorp/consul-replicate`（525）、`dcm4che/dcm4chee-arc-light`（506）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-19 stars:>3`。`total_count=223`，返回 5，规则保留 5，清单类排除 0。剩余配额 7。正文保留 `MyoHub/myosuite`（1265）、`stereolabs/zed-sdk`（1246）、`SJTU-ViSYS/M2DGR`（1219）、`Sguan-ZhouQing/SguanFOC_Library`（1108）。`zed-sdk` 同时话题含 `computer-vision`，完整条目在本节，AI 一节一行带过。`SguanFOC_Library` 同时话题含 `embedded` 与 `mcu`，完整条目在本节，嵌入式一节一行带过。
  - 清单类剔除：`Vincentqyw/cv-arxiv-daily`（总 star 1506）。话题含 `slam`，描述是用 GitHub Actions 每天更新计算机视觉论文，属每日论文清单，不进正文。脚本的清单规则没有命中这条描述，此处人工剔除。
