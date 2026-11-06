# GitHub 领域日报 · 2026-11-07

生成时间：2026-11-07 07:38（北京时间）。数据拉取开始于 2026-11-07 07:33:08（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-08（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-31 及之后有推送、总 star > 3。轮换页 `page = (当年第 311 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) 给智能体查企业数据加一层语义本体：指标在哪、定义是否一致、查询是否符合认证口径，并把出处一起返回，避免答得快但数字是错的；描述含 LLM，总 star 8965，24 小时新增 star 2005。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 7385，没有 24 小时新增数据。
3. [meshtastic/firmware](https://github.com/meshtastic/firmware) 是 Meshtastic 的官方固件，用 LoRa 组一套不靠蜂窝和互联网的远距离网状通信；本页常青按总 star 排在嵌入式首位，总 star 8544，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 17 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

### AI

- [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)
  - 说明：智能体查企业数据时，快不算对。这个库从已有元数据生成语义本体，告诉代理指标在哪、含义是否一致、该不该用、查询是否对得上认证定义，并把出处一并返回。README 写明结果可以通过命令行、API 和 MCP 交给各种代理框架。描述里的 LLM 是强特征词。
  - 领域：AI
  - 总 star：8965
  - 24 小时新增 star：2005

嵌入式、功率器件、电力电子电源、自动控制在这 17 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4577
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验收成一个网页，能看实时引脚、跑交互模拟、读固件和实验记录，界面有 11 种语言。README 写明目前是 32 个动手实验。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：678
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：284
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：262
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32-S3 上做语音终端。README 写明板子负责听和说，电脑上的后端决定这句话交给 Grok，还是在本机放歌、暂停和调音量；刷过补丁固件的小米智能音箱 Pro 也能接进来。话题含 grok，没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：258
- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming)
  - 说明：给编程代理一套 STM32 技能，按标准库或 HAL、裸机或 FreeRTOS 四条轨写出带引脚表和烧录说明的工程，再用静态检查把时钟顺序、中断阻塞这类纪律清掉才交付。README 把九串 BQ76940 电池管理和 FOC 电机控制写成已经上板的样本；仓库本身是嵌入式开发技能，所以完整条目放在这里。描述里的 BMS 让它出现在电力电子检索里，FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。这是代码生成技能，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：38

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。话题含 llm。
  - 领域：AI
  - 总 star：7385
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4577。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵。代理已经能写出影片、演示和游戏的声音，却听不出按键廉价、撞击晚了 80 毫秒或配乐鼓错了地方。README 写明它把声音变成代理可以判断的证据，并且只在 CPU 上跑，也能让代理自己写声音再听一遍改。话题含 ai-agents。
  - 领域：AI
  - 总 star：4073
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上资源上限和诱饵，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。README 写明这是保护自己软件的防御工具。
  - 领域：AI
  - 总 star：2549
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：262。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 开关直流泵的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：8。

### 电力电子电源 Power Supply

本日没有以电力电子电源为最贴近领域的完整新项目。描述里带 BMS 的 STM32 代理技能，完整说明写在上方「嵌入式 Embedded」。

- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS，此处不展开。领域：电力电子电源 Power Supply。总 star：38。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室 2026 年 RoboMaster 哨兵的定位栈。README 写明它跑在 ROS 2 Humble 上，用激光和惯性做里程计、点云建图、先验地图定位、回环和重定位，也可以接入 UWB；实机和 rosbag 回放走同一套入口。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：122
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用非均匀 B 样条做多传感器里程计的状态估计。同一套框架覆盖激光惯性、激光视觉惯性、激光加腿部惯性，以及再加视觉的组合，并可做全局样条修正。README 写明这些组合都能实时跑，支持 ROS 2 Humble 和 Jazzy。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：53
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵走 MOSFET；固件里有通断、P 和 PI，并带溢流、干转和传感器保护，另有一套按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：8

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 4`，每页 5 条，本页是各查询按总 star 排序后的第 16 到第 20 条。

### 嵌入式 Embedded

- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的官方设备固件，用 LoRa 组一套不依赖蜂窝和互联网的远距离、低功耗网状网络，传文字、位置和遥测。README 写明支持 ESP32、nRF52、RP2040/RP2350 和 Linux。话题含 esp32 与 stm32。
  - 领域：嵌入式 Embedded
  - 总 star：8544
- [FreeRTOS/FreeRTOS](https://github.com/FreeRTOS/FreeRTOS)
  - 说明：经典 FreeRTOS 发行版，从当年的 SourceForge 仓库克隆而来，内核放在子模块里。名称和描述里的 FreeRTOS 计入。
  - 领域：嵌入式 Embedded
  - 总 star：7961
- [nodemcu/nodemcu-firmware](https://github.com/nodemcu/nodemcu-firmware)
  - 说明：给 ESP8266、ESP8285 和 ESP32 用的 Lua 交互固件。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：7954
- [FastLED/FastLED](https://github.com/FastLED/FastLED)
  - 说明：在 Arduino 上做可寻址彩色灯带动画的库。话题含 embedded 与 esp32。描述把使用问题指到 Reddit，仓库 issue 只跟踪库本身的缺陷。
  - 领域：嵌入式 Embedded
  - 总 star：7524
- [BruceDevices/firmware](https://github.com/BruceDevices/firmware)
  - 说明：面向 M5Stack、Cardputer 和 LILYGO 等板子的 ESP32 固件，把无线、射频、红外和 NFC 收成一台能揣走的设备，给现场安全测试用。话题含 embedded；话题里的 `esp32-c5`、`esp32-s3` 按词边界计入 esp32。README 写明官方开发板 RF REAPER 的主控是 ESP32-S3。这里只说明它是什么。
  - 领域：嵌入式 Embedded
  - 总 star：7164
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：546。

### AI

- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：Python 里的张量库，带自动求导和 GPU 加速，用来写和训练神经网络。名称 pytorch 计入。话题里没有 llm。
  - 领域：AI
  - 总 star：105217
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：做高吞吐、省内存的大模型推理和在线服务。名称 vllm 和描述里的 LLMs 按词边界都不等于 llm，靠话题 llm 计入；话题还有 pytorch 与 transformer。
  - 领域：AI
  - 总 star：96476
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：把网页抓成干净的 Markdown 或结构化结果，给代理和数据管道用。这个仓库是 Apache-2.0 的爬虫，可以自己托管，也对应一套托管 API。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：87011
- [pypose/pypose](https://github.com/pypose/pypose) — 见下方「自动控制 Control」完整条目。话题含 pytorch，此处不展开。领域：AI。总 star：1621。

### 功率器件 Power Devices

本页剔除后为空。名称是 `sic` 的生存分析仓库与碳化硅器件无关，见数据源状态。

### 电力电子电源 Power Supply

- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman)
  - 说明：把插了 Solarman 采集棒的光伏逆变器读进 Home Assistant。话题含 inverter。README 写明它基于异步的 pysolarmanv5，也支持经 Modbus TCP 接入。话题还有 modbus，嵌入式一节一行带过。逆变器读数比 Modbus 话题更贴近本领域。
  - 领域：电力电子电源 Power Supply
  - 总 star：546
- [fl4p/batmon-ha](https://github.com/fl4p/batmon-ha)
  - 说明：用蓝牙把 JK、JBD、Daly、ANT、SOK 等电池管理系统的电量、电流和单体电压送进 Home Assistant。话题含 bms。README 写明用主机自己的蓝牙，不另加 ESP32，所以不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：532

### 自动控制 Control

- [google-deepmind/mujoco_mpc](https://github.com/google-deepmind/mujoco_mpc)
  - 说明：在 MuJoCo 里实时做模型预测控制，用来编写和求解机器人任务。README 写明既有 iLQG 和梯度下降，也有不求导数的 Predictive Sampling。话题含 mpc 与 motor-control。
  - 领域：自动控制 Control
  - 总 star：1760
- [pypose/pypose](https://github.com/pypose/pypose)
  - 说明：面向机器人的 PyTorch 库，把感知网络和基于物理的优化放在一起，李群、扩展卡尔曼滤波和位姿图都在里面。话题含 slam 与 kalman-filter，定位和滤波比 pytorch 话题更贴近本领域。话题还有 pytorch，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：1621
- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用 MuJoCo 搭肌肉骨骼模型的任务环境，给运动控制、生物力学和康复相关的策略学习当试验场。话题含 motor-control。README 写明这些环境包成 Gymnasium 接口，同一任务也可以放到 GPU 上并行训练。
  - 领域：自动控制 Control
  - 总 star：1280

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`NVIDIA/auto-ontology`、`wangzan101/Mika`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Liu-zhongxian/zongzhu-bot`、`Leonxlnx/earshot`、`qybaihe/bla`、`marozols/SIC-existence`、`yayapa/sic`、`wdcjx/Embedded-programming`、`Samarth030312/arduino-water-level-control-lab`、`woolimi/robotics-roadmap`、`Vincentqyw/cv-arxiv-daily`、`BruceDevices/firmware`、`mozihe/z-localization`、`davidrapan/ha-solarman`、`fl4p/batmon-ha`、`ASIG-X/RESPLE2`、`google-deepmind/mujoco_mpc`、`pypose/pypose`、`MyoHub/myosuite`、`meshtastic/firmware`、`vllm-project/vllm`、`unclecode/crawl4ai`。这 24 次是 raw README，不计入上面 11 次搜索配额。`esp32-iphone-agent`、`esp32-thinks`、`FreeRTOS`、`nodemcu-firmware`、`FastLED` 和 `pytorch` 的说明没有超出搜索描述，未另读 README。`arduino-water-level-control-lab` 的说明也没有超出搜索描述，README 只用来确认它是带固件的实验，不是公开课清单。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 17 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。正文只收 `NVIDIA/auto-ontology`（总 star 8965，stars today 2005；描述含 LLM）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`cloudflare/security-audit-skill`（63915，2524；描述是 coding-agent，不等于 `ai-agents`，也没有 llm）、`mattpocock/skills`（316678，2058）、`google/skills`（22816，532；描述是 Agent Skills，不等于 `ai-agents`）、`microsoft/vscode`（195014，295）、`zed-industries/zed`（93594，292）、`react/react`（252246，244）、`astral-sh/ruff`（50682，213）、`rust-lang/rust`（121432，186）、`nushell/nushell`（40974，177）、`rails/rails`（59020，152）、`prometheus/prometheus`（67173，140）、`angular/angular`（101349，128）、`etcd-io/etcd`（52609，123）、`symfony/symfony`（31421，89）、`mpv-player/mpv`（37867，36）、`openssl/openssl`（31282，24）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-08 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-08 stars:>2`。`total_count=436`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4577）、`agharsallah/esp-labs-web`（678）、`ngxson/esp32-usb-to-airprint`（284）、`raullenchai/esp32-thinks`（262）、`Liu-zhongxian/zongzhu-bot`（258）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。`esp32-usb-to-airprint` 只有名称和描述里的 esp32，接口 `created_at` 为 `2026-10-26T16:18:54Z`，北京时间是 2026-10-27 00:18。另有 1 条完整条目来自电力电子检索：`wdcjx/Embedded-programming`（38），因为 STM32 技能比描述里的 BMS 更贴近本领域。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-08 stars:>2`。`total_count=2523`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 8。正文保留 `wangzan101/Mika`（7385）、`Leonxlnx/earshot`（4073）、`qybaihe/bla`（2549）。这 3 条是本页星数连续的前 3。另有 2 条跨领域一行：`esp32-iphone-agent`（4577）、`esp32-thinks`（262），来自嵌入式检索。这两条话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`benjitaylor/skills`（总 star 2237；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）、`DenisSergeevitch/ex-ussr-kinship-research`（总 star 2063；描述是 “skill for AI agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-08 stars:>2`。`total_count=6`，返回 5，规则保留 2，未命中 3。剩余配额 6。`per_page=5`，第 6 条不在本次返回里，正文不猜测它是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC。README 写明这是 Lean 对「任意有限维都存在 SIC-POVM」的形式化证明，与碳化硅器件无关，正文不收。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 8）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`Arafat-shuvo/Sicip-data-sciebce`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`First-Sick` 与 `Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-08 stars:>2`。`total_count=63`，返回 5，规则保留 1。剩余配额 9。规则保留的 1 条更贴近嵌入式，本节只留一行，因此没有以本领域为最贴近领域的完整新项目。
  - `wdcjx/Embedded-programming`（总 star 38）：描述列出 CAN/Modbus/BMS/FOC。话题含 embedded、stm32、freertos。完整条目在嵌入式，本节一行带过。描述里的 FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`Dreamyepruner97/gwffttqz`（317；描述声称提供 Acrobat Pro DC 的已激活副本，与电源无关，DC 不等于 `dc-dc`）、`Lida-V/3DCharaMakeSkills-Lida`（57）、`leftamber/grid-dca-bot`（48；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。分类按词边界没有计入。`Embedded-programming` 是本页星数最低的一条。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-08 stars:>2`。`total_count=74`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `mozihe/z-localization`（122）、`ASIG-X/RESPLE2`（53）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（8），因为水位控制比 MOSFET 开关更贴近本领域。`SampQOL-OS` 与 `FrankyRenderer` 夹在 `robotics-roadmap` 和 `RESPLE2` 之间，所以剔除后本页按总 star 不是连续的 2 个命中仓库。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 94）。话题含 `ros2` 与 `slam`，README 写明是 57 讲、约 120 小时的自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。它排在 `z-localization` 与 `RESPLE2` 之间。
  - 名称和 topics 未命中：`snarebes/SampQOL-OS`（总 star 73；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）、`mryx007/FrankyRenderer`（总 star 63；描述里的 MPC-BE 是播放器兼容，不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-31 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-31 stars:>3`。`total_count=1298`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。`page=4`、`per_page=5`，本页是总结果里的第 16 到第 20 条。本查询正文完整条目 5 条：`meshtastic/firmware`（8544）、`FreeRTOS/FreeRTOS`（7961）、`nodemcu/nodemcu-firmware`（7954）、`FastLED/FastLED`（7524）、`BruceDevices/firmware`（7164）。另有 1 条一行来自电力电子：`davidrapan/ha-solarman`（546，话题含 modbus）。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-31 stars:>3`。`total_count=9173`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 7。正文保留 `pytorch/pytorch`（105217）、`vllm-project/vllm`（96476）、`unclecode/crawl4ai`（87011）。`nexu-io/open-design` 排在本页第一，`pbakaus/impeccable` 夹在 `pytorch` 与 `vllm` 之间，所以本页按总 star 不是连续的 3 个命中仓库。另有 1 条一行来自自动控制：`pypose/pypose`（1621，话题含 pytorch）。`esp32-iphone-agent` 与 `esp32-thinks` 话题含 `llm`，但不在 AI 常青前 5，不从常青跨节；它们的一行在新项目里。
  - 未命中：`nexu-io/open-design`（总 star 106308；描述是 “with your team and AI agents”，空格写法不等于 `ai-agents`）、`pbakaus/impeccable`（总 star 104784；描述里的 coding agent 与 AI slop 都不是领域关键词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-31 stars:>3`。`total_count=27`，返回 5，规则保留 1，清单类排除 1，未命中 2，另有 1 条只命中别的领域。剩余配额 5。`page=4` 返回满 5 条，是总结果里的第 16 到第 20 条。规则保留的那条经人工剔除后，本页没有功率器件正文。
  - `yayapa/sic`（总 star 11）：名称是 sic，搜索描述为空。README 写明 SIC 是 Survival In-Context，用先验拟合网络做生存分析，与碳化硅器件无关，正文不收。
  - 名称词边界未命中：`ducroo/SICTIC-AI`（14；`SICTIC` 不等于 `sic`，描述是瑞士商业天使俱乐部的 AI 引擎）、`linuxserver/docker-sickgear`（12；`sickgear` 不等于 `sic`，描述为空）。
  - 清单类剔除：`satnamrsm/https-github.com-sickn33-antigravity-awesome-skills`（总 star 8）。名称含 awesome，脚本已按清单排除。`sickn33` 不等于 `sic`。
  - `ajtudela/sicks300_ros2`（总 star 7）：描述是 Sick S300 安全激光雷达的 ROS 2 驱动，`Sick` 不等于 `sic`。话题含 `ros2`，但不在自动控制常青前 5，不跨节。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-31 stars:>3`。`total_count=399`，返回 5，规则保留 2，未命中 3。剩余配额 9。`page=4` 是总结果里的第 16 到第 20 条。正文保留 `davidrapan/ha-solarman`（546）、`fl4p/batmon-ha`（532）。未命中的 `dcts-shipping`（641）排在 `ha-solarman` 前面，`consul-replicate`（525）和 `dcm4chee-arc-light`（507）排在 `batmon-ha` 后面，所以本页按总 star 不是连续的 2 个命中仓库。`batmon-ha` README 写明不另加 ESP32，不跨嵌入式。
  - 名称和 topics 未命中：`hackthedev/dcts-shipping`（641；名称里的 dcts 不等于 `dc-dc`）、`hashicorp/consul-replicate`（525；描述是跨数据中心的 KV 复制，DC 不等于 `dc-dc`）、`dcm4che/dcm4chee-arc-light`（507；DICOM 归档，名称里的 dcm 不等于 `dc-dc`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-31 stars:>3`。`total_count=226`，返回 5，规则保留 4，脚本清单类排除 1。剩余配额 8。正文保留 `google-deepmind/mujoco_mpc`（1760）、`pypose/pypose`（1621）、`MyoHub/myosuite`（1280）。`cv-arxiv-daily` 与 `awesome-lidar` 夹在 `pypose` 与 `myosuite` 之间，所以本页按总 star 不是连续的 3 个命中仓库。
  - 清单类剔除：`Vincentqyw/cv-arxiv-daily`（总 star 1514）。描述写明用 GitHub Actions 每天更新计算机视觉论文，README 是按 SLAM、NeRF 等分类的论文表。话题含 `slam`。脚本的清单规则没有命中这条描述，此处人工剔除。
  - 清单类剔除：`szenergy/awesome-lidar`（总 star 1368）。描述写明是激光雷达厂商、数据集和点云算法清单，名称含 awesome。话题含 `slam`，脚本已按清单排除。
