# GitHub 领域日报 · 2026-10-18

生成时间：2026-10-18 07:34（北京时间）。数据拉取开始于 2026-10-18 07:30:38（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-18（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-11 及之后有推送、总 star > 3。轮换页 `page = (当年第 291 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) 用一次前向做分类、打分和是否判断，并按请求选检查点；近 30 天新建，总 star 33269。
2. [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) 在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，要确认时可以就地批准；近 30 天新建，总 star 5442。
3. [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) 让代理把难问题答成一页能直接读的 HTML；近 30 天新建，总 star 3609。

## A. 今日热度

Trending 页面解析到 13 条。页面不带 topics，因此只按仓库名和强特征描述归类。没有仓库的名称或强特征描述命中领域关键词。

本日无命中领域的热门仓库。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：2992
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：1006
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：402
- [andrisgauracs/wifi-sensing-kit](https://github.com/andrisgauracs/wifi-sensing-kit)
  - 说明：用三块约 10 美元的 ESP32-S3，靠 WiFi 信号判断人在做什么，训练时用摄像头当老师。
  - 领域：嵌入式 Embedded
  - 总 star：171
- [cyber-murmel/esp-sdr-zephyr](https://github.com/cyber-murmel/esp-sdr-zephyr)
  - 说明：在 Zephyr 上做 ESP32 的 2.4 GHz 软件无线电，用实时系统来收这一频段的信号。
  - 领域：嵌入式 Embedded
  - 总 star：140

### AI

- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
  - 说明：用一次前向完成文本上的分类、打分和是否判断，并按请求挑选检查点，覆盖描述中的 100 多种语言。
  - 领域：AI
  - 总 star：33269
- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：5442
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：3609
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：2992。

### 功率器件 Power Devices

- [tPkl/OpenRdson](https://github.com/tPkl/OpenRdson)
  - 说明：用开源网格和有限元做场效应管版图的寄生参数提取，用来替代 Synopsys / SFT 的 R3D。
  - 领域：功率器件 Power Devices
  - 总 star：6

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [cocel-postech/genz-lio](https://github.com/cocel-postech/genz-lio)
  - 说明：激光雷达加 IMU 的里程计，针对室内外和退化场景把位姿估稳；仓库标明发表于 IEEE T-FR 2026。
  - 领域：自动控制 Control
  - 总 star：111
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：38
- [uzh-rpg/why_does_deep_learning_improve_visual_slam](https://github.com/uzh-rpg/why_does_deep_learning_improve_visual_slam)
  - 说明：在 ORB-SLAM3 里用 DROID-SLAM 学到的光流和不确定度做二维数据关联，替换 ORB 描述子匹配，用来看深度学习改的是视觉 SLAM 的哪一段。仓库描述为空，这句话来自 README 开头。
  - 领域：自动控制 Control
  - 总 star：22

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 4。

### 嵌入式 Embedded

- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：用 ESP32 读 Wi-Fi 信道状态来判断有没有人在动，不必再装专用红外或雷达；带 C++ SDK，也能接到 ESPHome 和 Matter。
  - 领域：嵌入式 Embedded
  - 总 star：9629
- [platformio/platformio-core](https://github.com/platformio/platformio-core)
  - 说明：给 Arduino、ESP32、STM32、Zephyr、RISC-V 这些板子共用一套编译、烧录和调试入口，不用为每块芯片另搭工具链。
  - 领域：嵌入式 Embedded
  - 总 star：9534
- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的官方固件，让 ESP32、STM32、nRF52 靠 LoRa 组离网网格，没有蜂窝和互联网也能传消息。
  - 领域：嵌入式 Embedded
  - 总 star：8439
- [crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)
  - 说明：跑在 ESP32 墨水屏上的开源电子书固件，用来在便宜的墨水屏硬件上读 EPUB。
  - 领域：嵌入式 Embedded
  - 总 star：8391
- [FastLED/FastLED](https://github.com/FastLED/FastLED)
  - 说明：在 Arduino 和 ESP32 上驱动 WS2812、APA102 这类可寻址彩灯，把时序和动画交给库。
  - 领域：嵌入式 Embedded
  - 总 star：7508

### AI

- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
  - 说明：把编程代理每次会话里做过的事压成可检索的记忆，下次开会话时再注回去，避免换一个会话就失忆。
  - 领域：AI
  - 总 star：101410
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
  - 说明：让代理用一条命令行去读 Twitter、Reddit、YouTube、GitHub、B 站和小红书，不必为每个网站另买 API。
  - 领域：AI
  - 总 star：98724
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
  - 说明：给编程代理补上审美，用参考图和浏览器检查来做页面，少交一版千篇一律的界面。
  - 领域：AI
  - 总 star：98437
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：高吞吐、省显存的大模型推理服务，用来把 LLM 部署出去。
  - 领域：AI
  - 总 star：94006
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：把网页爬成适合大模型阅读的 Markdown，给代理和检索提供干净正文。
  - 领域：AI
  - 总 star：85722
- [pypose/pypose](https://github.com/pypose/pypose) — 见下方「自动控制 Control」完整条目。话题含 pytorch，此处不展开。领域：AI。总 star：1615。

### 功率器件 Power Devices

本页无符合领域的常青仓库。规则命中的 `Oire/sic` 是简易图片转换器（Simple Image Converter），`SIC-GT-26-27/Contenido_Colabs_SIC` 是同步课用的 Colab，都与碳化硅器件无关，不进正文。

### 电力电子电源 Power Supply

- [fl4p/batmon-ha](https://github.com/fl4p/batmon-ha)
  - 说明：Home Assistant 插件，经蓝牙读取 JK、JBD、Daly、ANT、SOK 等电池管理系统的数据，用来看电芯状态。
  - 领域：电力电子电源 Power Supply
  - 总 star：525

### 自动控制 Control

- [pypose/pypose](https://github.com/pypose/pypose)
  - 说明：在流形上做可微机器人学，把李群、卡尔曼滤波和 SLAM 放进能反传的库里，用来把几何估计和网络训练接在一起。
  - 领域：自动控制 Control
  - 总 star：1615
- [amap-cvlab/ABot-Recon](https://github.com/amap-cvlab/ABot-Recon)
  - 说明：只靠视频流做长轨迹的三维重建，重点是把局部上下文留住，避免轨迹一长就漂。
  - 领域：自动控制 Control
  - 总 star：1383
- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用 MuJoCo 搭肌肉骨骼模型的控制任务，包成 Gym 环境，用来训练肌肉驱动的动作。
  - 领域：自动控制 Control
  - 总 star：1258

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

`uzh-rpg/why_does_deep_learning_improve_visual_slam` 的搜索结果和仓库接口描述都为空。正文那一句来自该仓库 README 的第一段，star 数仍以搜索接口为准（22）。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 13 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），括号内为总 star、stars today：`anthropics/claude-plugins-official`（41701，1383）、`MadsLorentzen/ai-job-search`（50323，1397；名称和描述里的 AI 是弱词）、`affaan-m/ECC`（282465，1145）、`HKUDS/CLI-Anything`（54039，580）、`K-Dense-AI/scientific-agent-skills`（52223，879；名称和描述里的 AI 是弱词）、`akitaonrails/ai-memory`（9902，208；名称里的 AI 是弱词）、`android/skills`（8408，368；描述为空）、`stablyai/orca`（95365，829）、`anthropics/claude-code`（151708，168）、`debpalash/VoiceStudio`（73265，2135）、`anomalyco/opencode`（215255，576）、`ruvnet/ruflo`（76044，406；描述里的 RAG 是弱词，未计入）、`xerj-org/xerj`（7766，1102；描述里的 RAG 是弱词，未计入）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-18 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-18 stars:>2`。`total_count=402`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文。`onehumanbeing/esp32-iphone-agent` 同时话题含 `llm`，完整条目在本节，AI 一节一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-18 stars:>2`。`total_count=2140`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 7。正文保留 `NandhaKishorM/laya`（33269）、`Louis-CFM/coucou`（5442）、`QingYunA/answer-me-with-html`（3609）。另有 1 条跨领域一行：`esp32-iphone-agent` 来自嵌入式检索。
  - 未命中：`zai-org/ZCode`（总 star 7909）、`mizorewww/laya-mlx`（6956；描述里的 PyTorch 出现在否定句里，且 `pytorch` 不是强特征描述词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-18 stars:>2`。`total_count=5`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 6）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 4）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（18）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`SiCo`、`Sichuan` 按词边界都不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-18 stars:>2`。`total_count=77`，返回 5，规则保留 0。剩余配额 5。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（166）、`KawaiiBunga/MKVDCU-Recomp`（40）、`ningbainb/Dcode`（37）、`meztinos515/Acrobat-Pro-DC`（35）、`lamb2k/re4dc`（31）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-18 stars:>2`。`total_count=50`，返回 5，规则保留 4，未命中 1。剩余配额 9。正文保留 `cocel-postech/genz-lio`（111）、`TrentIndeed/kinetiqgym`（38）、`uzh-rpg/why_does_deep_learning_improve_visual_slam`（22）。
  - `sd88me/mpc-vst-plugins`（总 star 120）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，与模型预测控制无关，正文不收。
  - `xwtk/hmg_nemesis`（69）：名称和 topics 未命中。

### C. 领域常青（`pushed:>=2026-10-11 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-11 stars:>3`。`total_count=1155`，返回 5，规则保留 5，清单类排除 0。剩余配额 8。这 5 条都写入正文。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-11 stars:>3`。`total_count=8463`，返回 5，规则保留 5，未命中 0，排除清单 0。剩余配额 9。正文保留 `thedotmack/claude-mem`（101410，topic `ai-agents`）、`Panniantong/Agent-Reach`（98724，topic `llm-tools` 按词边界命中 `llm`）、`Leonxlnx/taste-skill`（98437，topic `ai-agents`）、`vllm-project/vllm`（94006）、`unclecode/crawl4ai`（85722）。另有一行 `pypose/pypose`，来自自动控制检索，话题含 `pytorch`。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-11 stars:>3`。`total_count=20`，返回 5，规则保留 2，未命中 3。剩余配额 6。规则保留的 2 条人工剔除后，本页正文为空。
  - `Oire/sic`（总 star 4）：仓库名是 `sic`，描述是 Simple Image Converter，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 4）：同步课 Colab，与碳化硅器件无关，正文不收。这条也出现在本日功率器件新项目检索里。
  - 名称和 topics 未命中：`rvandewater/SICdb_MEDS`（6；萨尔茨堡重症监护数据库，`SICdb` 按词边界不等于 `sic`）、`PanosMagic32/sick-fansubs`（4）、`tbermen/SiCoPR`（4；`SiCo` 按词边界不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-11 stars:>3`。`total_count=356`，返回 5，规则保留 1，未命中 4。剩余配额 4。正文完整条目为 `fl4p/batmon-ha`（525，topic `bms`）。
  - 名称和 topics 未命中电力电子：`ciribob/DCS-SimpleRadioStandalone`（558）、`AAFOptimus/AAFFamilyDCHAudio`（557）、`hashicorp/consul-replicate`（525）、`dcm4che/dcm4chee-arc-light`（506）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-11 stars:>3`。`total_count=212`，返回 5，规则保留 4，清单类排除 1。剩余配额 8。正文保留 `pypose/pypose`（1615）、`amap-cvlab/ABot-Recon`（1383）、`MyoHub/myosuite`（1258）。`pypose/pypose` 同时话题含 `pytorch`，AI 一节一行带过。
  - 清单排除：`Awesome-Image-Registration-Organization/awesome-image-registration`（总 star 1550，脚本按 awesome 排除，话题含 `slam`）。
  - `Vincentqyw/cv-arxiv-daily`（总 star 1506）：话题含 `slam`，内容是用 GitHub Actions 每日更新计算机视觉论文，属论文清单，正文不收。
