# GitHub 领域日报 · 2026-11-01

生成时间：2026-11-01 07:31（北京时间）。数据拉取开始于 2026-11-01 07:31:40（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-02（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-25 及之后有推送、总 star > 3。轮换页 `page = (当年第 305 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [wangzan101/Mika](https://github.com/wangzan101/Mika) 把私人助理装进安卓手机：说一句话，它在一块后台屏上打开 App、点按和打字，自己的屏幕还能继续用；创建于 2026-10-29，总 star 2687，没有 24 小时新增数据。
2. [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) 让代理把难问题收成一页能直接读的 HTML，用来替代一长串聊天记录；近 30 天新建，总 star 4966，没有 24 小时新增数据。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，眼睛走 AirPlay，手走 USB HID，不用 Mac、开发者账号或越狱；近 30 天新建，总 star 4160，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 14 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。嵌入式、AI、功率器件、电力电子电源、自动控制在这 14 条里都没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4160
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验台收成一个网页，能看实时引脚、跑交互模拟、读 esp-labs 固件和实验记录，界面有 11 种语言。
  - 领域：嵌入式 Embedded
  - 总 star：610
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：456
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：260
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在 Waveshare 1.75C 圆屏 ESP32 上做语音终端，接 Grok，屏幕有会眨眼的眼睛、字幕和朗读，仓库同时放固件和后端。
  - 领域：嵌入式 Embedded
  - 总 star：240

### AI

- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：4966
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4160。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：3380
- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块单独的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。
  - 领域：AI
  - 总 star：2687
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：260。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 驱动直流泵的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：8。

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室开源了 2026 年 RoboMaster 超级对抗赛哨兵的定位。README 写明这是 ROS 2 激光惯性定位栈，能做里程计、点云建图、先验地图定位、回环和重定位，也可接 UWB；示例传感器是 Livox Mid-360。
  - 领域：自动控制 Control
  - 总 star：113
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机和绳轮在软件里设定；网站、组装预览和带价格的零件表已经公开，CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：103
- [prohurtz/BSB-SLAM](https://github.com/prohurtz/BSB-SLAM)
  - 说明：给 Bigscreen Beyond 头显加一只 Xvisio XR50 SLAM 摄像头和 SteamVR 驱动，这样定位不必再靠灯塔基站。
  - 领域：自动控制 Control
  - 总 star：36
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用递归非均匀 B 样条做多传感器里程计，同一套 ROS 2 框架覆盖激光惯性、激光视觉惯性和带腿运动学的组合，并可选用全局样条修正。
  - 领域：自动控制 Control
  - 总 star：35
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino、超声波和一台泵做水位闭环，通断、P 和 PI 都有；市电泵走固态继电器，直流泵用 MOSFET 做 PWM，并带溢出、干转和传感器丢失保护。
  - 领域：自动控制 Control
  - 总 star：8

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：用 ESP32 经 Wi-Fi 控制 WS2812B 等数字灯带。
  - 领域：嵌入式 Embedded
  - 总 star：18949
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：面向单片机、WebAssembly 和命令行的 Go 编译器，基于 LLVM，话题含 ESP32 与 STM32。
  - 领域：嵌入式 Embedded
  - 总 star：17873
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：ESP32 系列芯片的 Arduino 核心，让 Arduino 的写法跑在乐鑫芯片上。
  - 领域：嵌入式 Embedded
  - 总 star：17647
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：给 RepRap 3D 打印机用的固件，8 位和 32 位微控制器都能跑，话题含 ESP32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：17646
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：Zephyr 项目的主仓库，面向多种硬件架构的可扩展实时操作系统。
  - 领域：嵌入式 Embedded
  - 总 star：16969
- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd)
  - 说明：给 Flipper Zero 和 ESP32 做的特斯拉 CAN 工具，能看电池管理系统仪表并抓取总线数据。设备本身是 CAN/ESP32，所以完整条目放在嵌入式；电力电子只因 BMS 仪表一行带过。
  - 领域：嵌入式 Embedded
  - 总 star：1193

### AI

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图在本地编排和运行扩散模型，同时提供界面、API 和后端。话题 `stable-diffusion` 按词边界计入 diffusion。
  - 领域：AI
  - 总 star：144356
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：让 AI 代理操作浏览器的 Python 库，另外提供隐匿浏览器和托管的代理 API。
  - 领域：AI
  - 总 star：119676
- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：可扩展的编程代理外壳，自带统一的 LLM 接口、代理循环、终端界面和命令行。搜索话题为空，靠描述里的 LLM 计入。
  - 领域：AI
  - 总 star：119184

### 功率器件 Power Devices

本页无符合领域的常青仓库。返回的 5 条里，没有碳化硅、IGBT、MOSFET 或功率电子话题。名称里的 SICK、sicp、SICAP、Phy-SIC，以及描述里的 `[sic]`，都不是功率器件。

### 电力电子电源 Power Supply

- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS 仪表，此处不展开。领域：电力电子电源 Power Supply。总 star：1193。
- [stuartpittaway/diyBMSv4](https://github.com/stuartpittaway/diyBMSv4)
  - 说明：锂离子电池包的自制电池管理系统，这个仓库放的是硬件设计。
  - 领域：电力电子电源 Power Supply
  - 总 star：1143
- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：用 ESPHome 经串口或蓝牙监测并控制极空电池管理系统。话题 `jikong-bms` 按词边界计入 bms。
  - 领域：电力电子电源 Power Supply
  - 总 star：1043

### 自动控制 Control

- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：可单独运行的 SLAM 库和程序，话题覆盖定位与建图，并能接到 ROS 2。
  - 领域：自动控制 Control
  - 总 star：4071
- [RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)
  - 说明：用图做非线性最小二乘的 C++ 框架，现成支持多种 SLAM 和光束法平差。
  - 领域：自动控制 Control
  - 总 star：3478
- [luigifreda/pyslam](https://github.com/luigifreda/pyslam)
  - 说明：Python/C++ 视觉 SLAM，单目、双目和 RGB-D 都能跑，并带闭环、体重建、深度预测和语义分割。
  - 领域：自动控制 Control
  - 总 star：3435

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`ASIG-X/RESPLE2`、`prohurtz/BSB-SLAM`、`wangzan101/Mika`、`earendil-works/pi`、`stuartpittaway/diyBMSv4`、`YuxuanSnow/Phy-SIC`、`mozihe/z-localization`、`hypery11/flipper-tesla-fsd`、`introlab/rtabmap`、`RainerKuemmerle/g2o`、`syssi/esphome-jk-bms`、`w2rc/gogettr`、`Samarth030312/arduino-water-level-control-lab`、`TrentIndeed/kinetiqgym`。这 14 次是核心接口，不计入上面 11 次搜索配额。`rtabmap` 的 README 与搜索描述同为一句库和独立程序，定位、建图和 ROS 2 来自搜索话题。`esphome-jk-bms` 与水位实验的说明没有超出搜索描述。`diyBMSv4` 的 README 写明最新控制器是 ESP32 并支持 CAN 与 RS485，搜索话题没有 `esp32`，不跨到嵌入式。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 14 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`thedotmack/claude-mem`（107807，1723；描述里的 AI 是弱词）、`pbakaus/impeccable`（98230，1339；描述里的 AI 是弱词）、`milind-soni/OpenMausBot`（9569，1304）、`pingdotgg/t3code`（35443，1148；描述为空）、`Orkas-AI/Orkas`（6109，1118；描述里的 AI team 是弱词）、`Renhuai123/ziwei-doushu`（12244，1093）、`HKUDS/DeepTutor`（52768，1035）、`lightpanda-io/browser`（39210，929；描述里的 AI 是弱词）、`mattpocock/skills`（308334，882）、`Donchitos/Claude-Code-Game-Studios`（31129，724；描述是 “49 AI agents”，空格写法不等于 `ai-agents`）、`obra/superpowers`（310037，663；描述里的 agentic 是弱词）、`vorssaint/vorssaint-utils`（31874，499）、`bregman-arie/devops-exercises`（85954，341；描述是 DevOps 面试题合集，没有领域词，脚本清单规则匹配的是 interview guide，这条未标成清单）、`THU-MAIC/OpenMAIC`（42168，115；描述里的 multi-agent 不等于 `ai-agents`）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-02 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-02 stars:>2`。`total_count=434`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4160）、`agharsallah/esp-labs-web`（610）、`Adolanium/hermes-gadget-sdk`（456）、`raullenchai/esp32-thinks`（260）、`Liu-zhongxian/zongzhu-bot`（240）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单或 awesome 合集，正文保留。`hermes-gadget-sdk` 话题没有 `llm`，不跨到 AI。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-02 stars:>2`。`total_count=2501`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 8。正文保留 `QingYunA/answer-me-with-html`（4966）、`Leonxlnx/earshot`（3380）、`wangzan101/Mika`（2687）。另有 2 条跨领域一行：`esp32-iphone-agent`（4160）、`esp32-thinks`（260），来自嵌入式检索。这两条话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`openfilm/openfilm`（总 star 3910；描述里的 AI video agent 是弱词）、`CopilotKit/OpenDuet`（总 star 1730；描述里的 AI agent 是弱词）。名称和 topics 都没有领域关键词。`openfilm` 夹在 `answer-me-with-html` 与 `earshot` 之间，所以本页按总 star 不是连续的 3 个命中仓库。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-02 stars:>2`。`total_count=4`，返回 4，规则保留 2，未命中 2。剩余配额 8。本查询只有 4 条满足条件，所以不足 5 条。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 8）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`aswin-code513/First-Sick-First-Served`（3）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`First-Sick` 与 `Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-02 stars:>2`。`total_count=66`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称、话题和描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`4DCodeBench/4DCodeBench`（200）、`CompaLarios18/MH4UltimateDC`（81）、`two-delta/DCOCO`（56；描述为空）、`Lida-V/3DCharaMakeSkills-Lida`（54）、`meztinos515/Acrobat-Pro-DC`（36；描述是 PDF 工具）。检索词 `dc-dc` 在搜索侧会撞上仓库名或 README 里的 DC。名称里能看到 DC 的是 `MH4UltimateDC`、`DCOCO`、`Acrobat-Pro-DC`。`4DCodeBench` 与 `3DCharaMakeSkills-Lida` 的名称和描述里没有这些词，命中点不在接口返回的名称、话题和描述中。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-02 stars:>2`。`total_count=67`，返回 5，规则保留 5，未命中 0。剩余配额 9。正文保留 `mozihe/z-localization`（113）、`TrentIndeed/kinetiqgym`（103）、`prohurtz/BSB-SLAM`（36）、`ASIG-X/RESPLE2`（35）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（8），因为水位控制比 MOSFET 开关更贴近本领域。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 83）。话题含 `ros2` 与 `slam`，描述写明是机器人开发自学课程地图和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。

### C. 领域常青（`pushed:>=2026-10-25 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-25 stars:>3`。`total_count=1214`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。正文完整条目 5 条来自本查询：`wled/WLED`（18949）、`tinygo-org/tinygo`（17873）、`espressif/arduino-esp32`（17647）、`MarlinFirmware/Marlin`（17646）、`zephyrproject-rtos/zephyr`（16969）。`hypery11/flipper-tesla-fsd`（1193）来自电力电子检索，话题含 `can-bus`、描述含 `esp32`，设备本身更贴近嵌入式，完整条目写在本节。`Marlin` 是 3D 打印机固件，不是公开课清单。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-25 stars:>3`。`total_count=8878`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `Comfy-Org/ComfyUI`（144356；话题 `pytorch` 与 `stable-diffusion`）、`browser-use/browser-use`（119676；话题 `llm` 与 `ai-agents`）、`earendil-works/pi`（119184；描述含 LLM，话题为空）。
  - 未命中：`langflow-ai/langflow`（总 star 156203；描述里的 AI-powered agents 是弱词）、`addyosmani/agent-skills`（总 star 112247；描述里的 AI coding agents 是弱词）。名称和 topics 都没有领域关键词。`langflow` 排在本页最前，`agent-skills` 排在 `pi` 之后，所以本页按总 star 不是连续的 3 个命中仓库。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-25 stars:>3`。`total_count=26`，返回 5，规则保留 2，未命中 2。剩余配额 7。`page=2`、`per_page=5`，本页返回满 5 条。规则保留的 2 条经人工剔除后，正文写「本页无符合领域的常青仓库」。
  - `SICKAG/sick_scan_xd`（总 star 178）：SICK 激光雷达和雷达驱动，名称不等于 `sic`。话题含 `ros2`，但不在自动控制常青前 5，不跨节。
  - `hexlet-volunteers/hexlet-sicp`（总 star 114）：SICP 教材学习进度服务，`sicp` 不等于 `sic`。
  - `w2rc/gogettr`（总 star 96）：描述和 README 里的 `[sic]` 是「原文如此」，不是碳化硅。正文不收。
  - `sicap-pro/SICAP.ai`（总 star 95）：公共采购检索，名称 `SICAP` 不等于 `sic`。
  - `YuxuanSnow/Phy-SIC`（总 star 63）：单张图片上的人体与场景接触估计，README 写明是 SIGGRAPH Asia 2025 的图形学工作，不是碳化硅器件。正文不收。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-25 stars:>3`。`total_count=403`，返回 5，规则保留 3，未命中 1。剩余配额 9。正文完整条目为 `stuartpittaway/diyBMSv4`（1143）、`syssi/esphome-jk-bms`（1043）。`hypery11/flipper-tesla-fsd`（1193）描述含 BMS，完整条目在嵌入式，本节一行。`dcm2niix`（1210）排在本页最前但未命中，所以本页按总 star 不是连续的电力电子仓库。
  - 名称和 topics 未命中：`rordenlab/dcm2niix`（1210；名称里的 DC 不等于 `dc-dc`）。
  - `wlcrs/huawei_solar`（940）描述是 Huawei Solar inverters，复数按词边界不等于 `inverter`，话题含 `modbus`，因此归入嵌入式而不是电力电子。它不在嵌入式常青前 5，不跨节。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-25 stars:>3`。`total_count=222`，返回 5，规则保留 3，未命中 1，清单类排除 1。剩余配额 9。正文保留 `introlab/rtabmap`（4071）、`RainerKuemmerle/g2o`（3478）、`luigifreda/pyslam`（3435）。`vedderb/bldc`（3548）夹在 `rtabmap` 与 `g2o` 之间，所以本页按总 star 不是连续的 3 个命中仓库。
  - 名称和 topics 未命中：`vedderb/bldc`（总 star 3548）。描述是 “The VESC motor control firmware”，`motor control` 是空格写法，不等于 `motor-control`；名称 `bldc` 不在控制关键词表，正文不收。
  - 清单类剔除：`jslee02/awesome-robotics-libraries`（总 star 3099）。名称含 awesome，话题含 `slam`，脚本已标成清单，正文不收。
