# GitHub 领域日报 · 2026-10-28

生成时间：2026-10-28 07:35（北京时间）。数据拉取开始于 2026-10-28 07:30:38（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-28（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-21 及之后有推送、总 star > 3。轮换页 `page = (当年第 301 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，眼睛走 AirPlay，手走 USB HID，不必用 Mac，也不必越狱；近 30 天新建，总 star 4013。
2. [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) 用节点图搭扩散模型的界面和本地推理后端；本页常青轮换才排到它，总 star 143558，没有 24 小时新增数据。
3. [stuartpittaway/diyBMSv4](https://github.com/stuartpittaway/diyBMSv4) 给锂离子电池包做的自制电池管理系统，仓库放的是硬件设计；领域常青，总 star 1141，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 11 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。嵌入式、AI、功率器件、电力电子电源、自动控制在这 11 条里都没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4013
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：1157
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验台收成一个网页，能看实时引脚、跑交互模拟、读 esp-labs 固件和实验记录，界面有 11 种语言。
  - 领域：嵌入式 Embedded
  - 总 star：504
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：449
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：258

### AI

- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：4544
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4013。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：3048
- [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu)
  - 说明：把 AI 写出来的日语改成读起来自然的日语，作为给编程代理用的推敲技能，而不是另做一套翻译器。
  - 领域：AI
  - 总 star：2603
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：258。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 驱动直流泵的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：8。

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室把 2026 年 RoboMaster 超级对抗赛哨兵的定位开源出来，用 Livox MID360 做激光雷达与 IMU 里程计，并带重定位，跑在 ROS 2 上。
  - 领域：自动控制 Control
  - 总 star：97
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：95
- [prohurtz/BSB-SLAM](https://github.com/prohurtz/BSB-SLAM)
  - 说明：给 Bigscreen Beyond 头显加自身定位：用一颗 Xvisio XR50 SLAM 相机跟踪，Lighthouse 基站可以收起来，并带 SteamVR 驱动和桌面设置程序。
  - 领域：自动控制 Control
  - 总 star：31
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino 做水箱水位控制实验：超声波测水位，市电泵走固态继电器，直流泵走 MOSFET，带通断、P 和 PI，以及按水箱和泵参数来的 MATLAB 应用和 Simulink。
  - 领域：自动控制 Control
  - 总 star：8

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 2。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：用 ESP32 经 WiFi 控制 WS2812B 等数字 RGB 灯，用来改灯带颜色和效果，而不必自己写无线灯控固件。
  - 领域：嵌入式 Embedded
  - 总 star：18927
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：把 Go 编译到单片机、WebAssembly 和命令行小工具上，话题覆盖 ESP32 与 STM32，用来在小设备上跑 Go。
  - 领域：嵌入式 Embedded
  - 总 star：17852
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：给 RepRap 3D 打印机用的固件，8 位和 32 位微控制器都能跑，话题含 ESP32 与 firmware；很多成品打印机出厂就带它。
  - 领域：嵌入式 Embedded
  - 总 star：17640
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：ESP32 系列的 Arduino 核心，用来在 Arduino 环境里写 ESP32 程序。
  - 领域：嵌入式 Embedded
  - 总 star：17632
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：可扩展的实时操作系统，面向多种硬件架构，话题含 RTOS、MCU 与 embedded，用来在单片机上跑多线程而不必自写调度器。
  - 领域：嵌入式 Embedded
  - 总 star：16925

### AI

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图搭扩散模型的界面、API 和后端，在本地跑推理，不必为每个模型另写一套调用代码。
  - 领域：AI
  - 总 star：143558
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：开源 Python 库，让 AI 代理操作浏览器，并提供云端隐身浏览器和托管代理接口。
  - 领域：AI
  - 总 star：119312
- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：一套 AI 代理工具包，把统一的大模型接口、代理循环、终端界面和编程代理命令行放在一起。
  - 领域：AI
  - 总 star：118285
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：把 Gemini 放进终端的开源代理，用来在命令行里直接调用，而不必再包一层桌面客户端。
  - 领域：AI
  - 总 star：108581

### 功率器件 Power Devices

本页无符合领域的常青仓库。返回的 5 条里，`w2rc/gogettr` 描述中的 `[sic]` 是“原文如此”，不是碳化硅；`epilys/sic` 是按标签组织的链接聚合。其余名称按词边界都不等于 `sic`（`sicp-racket`、`hexlet-sicp`、`SiCo`），没有功率器件话题。

### 电力电子电源 Power Supply

- [stuartpittaway/diyBMSv4](https://github.com/stuartpittaway/diyBMSv4)
  - 说明：给锂离子电池包做的自制电池管理系统，本仓库放的是 KiCad 硬件。README 写明控制器板用 ESP32；搜索接口的话题没有 `esp32`，因此不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：1141
- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：用 ESPHome 经串口或蓝牙监测并控制极空电池管理系统（JK-BMS），用来看电芯并下发控制。
  - 领域：电力电子电源 Power Supply
  - 总 star：1041

### 自动控制 Control

- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：RTAB-Map 的库和可单独运行的程序，用来做同步定位与建图；话题覆盖 ROS 2、定位、建图和扫描。
  - 领域：自动控制 Control
  - 总 star：4061
- [RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)
  - 说明：通用图优化框架，话题含 SLAM，用来把位姿和约束收成图再求解，而不必自写优化器。
  - 领域：自动控制 Control
  - 总 star：3477
- [luigifreda/pyslam](https://github.com/luigifreda/pyslam)
  - 说明：用 Python/C++ 做视觉 SLAM，支持单目、双目和 RGB-D，并带闭环、体积重建、深度预测和语义分割，用来从相机序列里同时得到轨迹和场景。
  - 领域：自动控制 Control
  - 总 star：3434

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

`prohurtz/BSB-SLAM` 与 `stuartpittaway/diyBMSv4` 的搜索描述过短，说明里关于 XR50、SteamVR、KiCad 硬件和 ESP32 控制器的句子来自 README 正文，star 仍用搜索接口。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 11 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`Nutlope/hallmark`（38928，2859；描述里的 AI 是弱词）、`HKUDS/DeepTutor`（45800，1587）、`pbakaus/impeccable`（90460，1458；描述里的 AI 是弱词）、`makecindy/cindy`（7434，1446；描述里的 AI Agent 是弱词）、`elayadesign/ai-design-skills`（9246，1395；描述为空，名称里的 ai 是弱词）、`JetBrains/thinkrail`（3948，1211）、`affaan-m/ECC`（290848，1183）、`gitroomhq/postiz-app`（39330，953；描述里的 agentic 是弱词）、`togg53192-cmd/jailbreaks`（5462，890；描述是 “LIST OF ALL MY JAILBREAKS”，没有领域词，脚本的清单规则也未命中）、`nightly-labs/openbot`（2381，794；描述里的 AI teammates 是弱词）、`obra/superpowers`（306399，608；描述里的 agentic 是弱词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-28 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-28 stars:>2`。`total_count=427`，返回 5，规则保留 5，排除清单 0。剩余配额 6。这 5 条都写入正文。`onehumanbeing/esp32-iphone-agent`（4013）和 `raullenchai/esp32-thinks`（258）同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`agharsallah/esp-labs-web`（504）话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单或 awesome 合集，正文保留。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-28 stars:>2`。`total_count=2423`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `QingYunA/answer-me-with-html`（4544）、`Leonxlnx/earshot`（3048）、`nanaism/yomiyasu`（2603）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`openfilm/openfilm`（总 star 3186；描述里的 AI video agent 是弱词）、`oil-oil/oil-ui`（总 star 2415；描述里的 AI agents 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-28 stars:>2`。`total_count=4`，返回 4，规则保留 2，未命中 2。剩余配额 8。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 8）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（25）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`SiCo`、`Sichuan` 按词边界都不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-28 stars:>2`。`total_count=78`，返回 5，规则保留 0。剩余配额 7。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（192）、`CompaLarios18/MH4UltimateDC`（70）、`two-delta/DCOCO`（55；描述为空）、`Lida-V/3DCharaMakeSkills-Lida`（53）、`lamb2k/re4dc`（39）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-28 stars:>2`。`total_count=56`，返回 5，规则保留 4，未命中 1。剩余配额 5。正文保留 `mozihe/z-localization`（97）、`TrentIndeed/kinetiqgym`（95）、`prohurtz/BSB-SLAM`（31）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（8），因为水位控制比 MOSFET 开关更贴近本领域。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 67）。话题含 `ros2` 与 `slam`，描述写明是机器人开发自学课程地图和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。
  - 名称和 topics 未命中：`lbgos/rift-s-linux`（32；描述里的 SLAM 不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-21 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-21 stars:>3`。`total_count=1199`，返回 5，规则保留 5，清单类排除 0。剩余配额 7。这 5 条都写入正文：`wled/WLED`（18927）、`tinygo-org/tinygo`（17852）、`MarlinFirmware/Marlin`（17640）、`espressif/arduino-esp32`（17632）、`zephyrproject-rtos/zephyr`（16925）。本页没有第二领域命中。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-21 stars:>3`。`total_count=8788`，返回 5，规则保留 4，排除清单 1。剩余配额 9。正文保留 `Comfy-Org/ComfyUI`（143558；话题 `pytorch`，`stable-diffusion` 按词边界计入 `diffusion`）、`browser-use/browser-use`（119312；话题 `llm` 与 `ai-agents`）、`earendil-works/pi`（118285；话题为空，描述含强特征词 LLM）、`google-gemini/gemini-cli`（108581；话题 `ai-agents`，描述里的 AI agent 本身是弱词）。
  - 清单类剔除：`Shubhamsaboo/awesome-llm-apps`（总 star 143243）。名称命中 `llm`，仓库是 AI Agents 合集，不进正文。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-21 stars:>3`。`total_count=24`，返回 5，规则保留 2，未命中 3。剩余配额 5。`page=2`、`per_page=5`，本页返回满 5 条。规则保留的 2 条都是撞名，本页正文为空。
  - `w2rc/gogettr`（总 star 96）：描述 “non-bias [sic] social network” 里的 `[sic]` 是“原文如此”，GETTR 的公开 API 客户端，与碳化硅器件无关，正文不收。
  - `epilys/sic`（总 star 27）：仓库名命中 `sic`，实为按标签组织的链接聚合，正文不收。
  - 名称按词边界不等于 `sic`，也没有功率器件话题：`hexlet-boilerplates/sicp-racket`（136；描述为空）、`hexlet-volunteers/hexlet-sicp`（114；SICP 读书进度服务）、`opencad-abu/SiCo`（25）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-21 stars:>3`。`total_count=386`，返回 5，规则保留 2，未归入电力电子 3。剩余配额 6。正文保留 `stuartpittaway/diyBMSv4`（1141；话题 `bms`）、`syssi/esphome-jk-bms`（1041；话题 `bms`，描述含 `bms`）。
  - `pnoker/iot-dc3`（总 star 1268）：未归入电力电子。话题含 `modbus` 与 `ai-agents`，但不是本页嵌入式或 AI 检索的前 5，不跨节。
  - 名称和 topics 未命中：`rordenlab/dcm2niix`（1209）、`NVIDIA/DCGM`（809）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-21 stars:>3`。`total_count=240`，返回 5，规则保留 3，未命中 1，清单类排除 1。剩余配额 4。正文保留 `introlab/rtabmap`（4061）、`RainerKuemmerle/g2o`（3477）、`luigifreda/pyslam`（3434）。
  - `vedderb/bldc`（总 star 3538）：描述是 “motor control”（空格），名称 `bldc` 不在控制关键词表，正文不收。
  - 清单类剔除：`jslee02/awesome-robotics-libraries`（总 star 3096）。话题含 `slam`，仓库是机器人库合集，不进正文。
