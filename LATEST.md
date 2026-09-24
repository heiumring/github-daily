# GitHub 领域日报 · 2026-09-25

生成时间：2026-09-25 07:45（北京时间）。数据拉取开始于 2026-09-25 07:42:55（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-08-26（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-09-18 及之后有推送、总 star > 3。轮换页 `page = (当年第 268 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [leejet/stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) 用纯 C/C++ 做扩散模型推理，是今日 Trending 里唯一命中领域关键词的仓库，24 小时新增 star 69。
2. [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) 用一次前向做分类、打分和是否判断，而不是逐字生成；近 30 天新建，总 star 22990。
3. [ruvnet/RuView](https://github.com/ruvnet/RuView) 用普通 WiFi 信号做空间感知和有人检测，不靠摄像头；领域常青页第一名，总 star 94934。

## A. 今日热度

Trending 页面解析到 14 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。嵌入式、功率器件、电力电子电源、自动控制在这 14 条里没有命中。

### AI

- [leejet/stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp)
  - 说明：把 Stable Diffusion、Flux 一类扩散模型的推理做成纯 C/C++，这样不用带 Python 运行时，也能在更紧的环境里跑图。
  - 领域：AI
  - 总 star：7237
  - 24 小时新增 star：69

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agamrossen/VolAnti](https://github.com/agamrossen/VolAnti)
  - 说明：用麦克风阵列听螺旋桨的声音来发现无人机，不靠无线电，光纤图传、自己不发射信号的 FPV 也能被听到。
  - 领域：嵌入式 Embedded
  - 总 star：385
- [MaxGramser/homeassistant_espscreen](https://github.com/MaxGramser/homeassistant_espscreen)
  - 说明：把便宜的 ESP32 触摸屏做成 Home Assistant 面板，用拖拽编辑界面，不用手写 YAML，也不用自己刷固件。
  - 领域：嵌入式 Embedded
  - 总 star：320
- [Frankweb33/flybrain-robot-bridge](https://github.com/Frankweb33/flybrain-robot-bridge)
  - 说明：把果蝇神经回路的思路接到相机和电机上，用光流和 IMU 把看见的画面变成机器人动作；现在仍是实验桥接，不是完整飞控。
  - 领域：嵌入式 Embedded
  - 总 star：219
- [KyThuatUAV/ESP32_FC](https://github.com/KyThuatUAV/ESP32_FC)
  - 说明：仓库说明是越南语，内容是基于 ESP32 研究和开发无人机飞控，没有更细的英文功能描述。
  - 领域：嵌入式 Embedded
  - 总 star：171
- [skizzophrenic/SquachWatch-CYD](https://github.com/skizzophrenic/SquachWatch-CYD)
  - 说明：给廉价黄板写的固件，用来发现 AirTag、Flock 摄像头、追踪器这类身边的监视设备。
  - 领域：嵌入式 Embedded
  - 总 star：142

### AI

- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
  - 说明：很多地方只要分类、打分或是否判断，却还在用自回归模型逐字生成。它一次前向给出这类决定，并按请求挑选检查点。
  - 领域：AI
  - 总 star：22990
- [Nanako0129/sepia](https://github.com/Nanako0129/sepia)
  - 说明：给兼容 Agent Skills 的编程助手用的去 AI 味写作技能，按小说或正式文体改句子，而不是再包一层聊天窗口。
  - 领域：AI
  - 总 star：2834
- [Frankweb33/flybrain-robot-bridge](https://github.com/Frankweb33/flybrain-robot-bridge) — 见上方「嵌入式 Embedded」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：219。

### 功率器件 Power Devices

本日无新项目。

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [amap-cvlab/ABot-Recon](https://github.com/amap-cvlab/ABot-Recon)
  - 说明：只吃视频流做长时程在线三维重建，不必先准备激光雷达或深度相机。
  - 领域：自动控制 Control
  - 总 star：1020
- [reality-opened/openreality](https://github.com/reality-opened/openreality)
  - 说明：把手机视频变成可以交给编程助手查询的三维场景，仓库里同时放了查询工具和 VGGT-SLAM。
  - 领域：自动控制 Control
  - 总 star：102
- [Hbelief1998/Functional-SLAM-CoRL_2026](https://github.com/Hbelief1998/Functional-SLAM-CoRL_2026)
  - 说明：建图时不只记几何，还在线维护场景里物体能做什么的功能图；仓库标明已被 CoRL 2026 接收。
  - 领域：自动控制 Control
  - 总 star：49

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 1。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：用普通 WiFi 信号做实时空间感知、生命体征和有人检测，现场不用装摄像头。
  - 领域：嵌入式 Embedded
  - 总 star：94934
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：用来写游戏的轻量 C 库，话题同时标了嵌入式和 ESP32，同一套图形代码可以往板上带。
  - 领域：嵌入式 Embedded
  - 总 star：34857
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：跑在 ESP32 上的聊天机器人，通过 MCP 接外部工具，让小设备也能当对话终端。
  - 领域：嵌入式 Embedded
  - 总 star：30191
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：给 ESP8266 和 ESP32 设备用的替代固件，用网页配置，经 MQTT 或 HTTP 在本地做家居自动化。
  - 领域：嵌入式 Embedded
  - 总 star：24773
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：从小 MCU 到带 3D 的处理器都能用的嵌入式图形界面库，用来在设备上自己画界面。
  - 领域：嵌入式 Embedded
  - 总 star：24746
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：11155。

### AI

- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：用同一套接口加载文本、视觉、语音和多模态模型，做训练或推理，不用为每种模型重写加载代码。
  - 领域：AI
  - 总 star：166616
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：在一个工作区里搭智能体流程和检索流水线，可以云上或自托管，避免每个应用都重写模型接入。
  - 领域：AI
  - 总 star：157118

### 功率器件 Power Devices

- [medwatt/gmid](https://github.com/medwatt/gmid)
  - 说明：用 gm/Id 查找表和设计曲线，给模拟电路里的 MOSFET 做多工艺角自动选尺寸，少靠手工反复调管子。
  - 领域：功率器件 Power Devices
  - 总 star：158

### 电力电子电源 Power Supply

按收紧规则过滤后，本页没有可列入的仓库。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：机器人算法的 Python 示例和讲义，用来读定位、建图、SLAM 和路径规划，不是直接刷进飞控的固件。
  - 领域：自动控制 Control
  - 总 star：30583
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：穿越机开源飞控固件，把陀螺仪、电机和遥控收成可调的飞控。
  - 领域：自动控制 Control
  - 总 star：11577
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：开源扫地机器人，用 ESP32 加上 ROS 2 和激光 SLAM 做清扫导航。
  - 领域：自动控制 Control
  - 总 star：11155
- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：同时做定位和建图的 SLAM 库，带独立程序，能接到 ROS 2，用来解决机器人在未知环境里一边走一边建图的问题。
  - 领域：自动控制 Control
  - 总 star：4010

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用已有 `scripts/fetch_github_daily.py`，本次未改脚本。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 14 条，规则命中 1 条（`leejet/stable-diffusion.cpp`，仓库名含 diffusion，总 star 7237，stars today 69），清单类排除 0 条。
- 说明：页面有 stars today，没有 topics。描述里的 agent、llm 等弱词未计入。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-08-26 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-08-26 stars:>2`。`total_count=318`，返回 5，规则保留 5，排除清单 0。剩余配额 9。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-08-26 stars:>2`。`total_count=2224`，返回 5，规则保留 2，未命中 3，排除清单 0。剩余配额 8。未命中：`zai-org/ZCode`（总 star 6707）、`mizorewww/laya-mlx`（6214）、`ZJU-REAL/Easel`（1322）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-08-26 stars:>2`。`total_count=3`，返回 3，名称命中 sic 的 2 条经审阅为撞名，正文不收；另 1 条名称和 topics 都未命中。剩余配额 9。
  - `overclocked-shushil/SIC--Hackathon`（总 star 3）：名称含 SIC，无描述，不能确认是碳化硅器件。
  - `Team4-Project2-Sic/Network-Intrusion_Project2_SIC`（总 star 3）：名称含 SIC，无描述，仓库名是网络入侵检测。
  - `MadestSamurai/bd2-sichuan`（总 star 6）：搜索撞到文本，名称和 topics 未命中。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-08-26 stars:>2`。`total_count=57`，返回 5，没有一条 topics 或仓库名命中电源关键词。剩余配额 9。
  - `kadenball/qwen38-27b-rtx3060-dcfr`（总 star 28）：只命中 topic `llm`，是本地大模型补丁，不在本次 AI 查询前 5，正文不单列。
  - `ara-mkr/Wonder-Pill`（128）、`lezviebloody6143/Acrobat-DC-Pro`（43）、`ningbainb/Dcode`（26）：名称和 topics 未命中。
  - `SAM0-0/ATHER-OBD-READER`（33）：描述写到电动车 BMS 和 CAN，但 topics 与仓库名未命中；`bms` 不在强特征词表。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-08-26 stars:>2`。`total_count=32`，返回 5，规则保留 3，其余不进控制节。剩余配额 9。
  - `Frankweb33/flybrain-robot-bridge`（219）：本查询返回，但未命中控制关键词；已写入嵌入式，并在 AI 一行带过。
  - `Gerrylgr/TrailBlazer_Community`（48）：描述含 SLAM 与 ROS 2，topics 和仓库名未命中。

### C. 领域常青（`pushed:>=2026-09-18 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-09-18 stars:>3`。`total_count=945`，返回 5，规则保留 5，排除清单 0。剩余配额 9。`makerspet/oomwoo` 不在这 5 条里，因话题同时含 esp32 与 ros2/slam，在本节用一行带到自动控制的完整条目。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-09-18 stars:>3`。`total_count=7466`，返回 5，规则保留 2，清单类排除 1，未命中 2。剩余配额 7。
  - 排除清单：`Shubhamsaboo/awesome-llm-apps`（总 star 139663），awesome 合集。
  - 未命中：`langflow-ai/langflow`（155221）、`msitarzewski/agency-agents`（154516）。名称和 topics 没有 llm / pytorch / transformer / diffusion / ai-agents。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-09-18 stars:>3`。`total_count=19`，返回 5，正文保留 1（`medwatt/gmid`，总 star 158）。剩余配额 9。
  - `microsoft/Sico`（268）：查询返回，topics 和名称未命中功率器件词；topic 含 `llm`，描述是企业数字员工平台，不在本次 AI 查询前 5，正文不单列。
  - 名称和 topics 未命中：`SickChill/sickchill`（2445）、`source-academy/sicp`（1020）、`siconos/siconos`（187）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-09-18 stars:>3`。`total_count=299`，返回 5，没有一条 topics 或仓库名命中电源关键词。剩余配额 9。
  - `tbnobody/OpenDTU`（2191）：描述写明与 Hoymiles/TSUN/Solenso 逆变器通信，topics 含 esp32，但没有电源关键词；`inverter` 不在强特征词表。它也不在嵌入式查询的前 5 里，正文不单列。
  - `dalathegreat/Battery-Emulator`（2927）：描述涉及电池包和光伏逆变器，topics 与仓库名未命中电源关键词。
  - `mjbots/moteus`（1301）：描述是无刷电机控制器，topics 与仓库名未命中本次电源关键词。
  - 未命中：`NVIDIA/dcgm-exporter`（1882）、`dcm4che/dcm4che`（1458）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-09-18 stars:>3`。`total_count=156`，返回 5，正文保留 4。剩余配额 8。
  - `Aleksoid1978/MPC-BE`（4504）：仓库名命中 `mpc`，实为 Windows 音视频播放器，不是模型预测控制，正文不收。
