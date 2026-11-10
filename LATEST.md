# GitHub 领域日报 · 2026-11-11

生成时间：2026-11-11 07:38（北京时间）。数据拉取开始于 2026-11-11 07:33:56（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-12（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-04 及之后有推送、总 star > 3。轮换页 `page = (当年第 315 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 8070，没有 24 小时新增数据。这是今日新项目里星数最高的命中仓库。
2. [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) 给编程代理补上耳朵，让它听得出自己生成的按键、撞击和配乐哪里不对，并且只在 CPU 上跑；总 star 4451，没有 24 小时新增数据。
3. [andrisgauracs/whistle-esp32](https://github.com/andrisgauracs/whistle-esp32) 按住按键说一句变灯颜色的话，语音识别完全在一块 ESP32-S3 上完成，不联网；总 star 224，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 12 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。

嵌入式、AI、功率器件、电力电子电源、自动控制在这 12 条里都没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验收成一个网页。能看实时引脚、在浏览器里跑交互模拟、逐行读固件，并记实验日志。README 写明目前是 32 个动手实验，界面有 11 种语言，含从右到左。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：782
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：289
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手。唤醒词或旋钮都能开口，识别、对话和合成可以分别指向任何兼容 OpenAI 的服务，并边生成边朗读。README 写明默认唤醒词是 “Hi, ESP”，参考板是 SenseCAP Watcher。话题含 llm，硬件助手更贴近本领域，AI 一节一行带过。
  - 领域：嵌入式 Embedded
  - 总 star：262
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32-S3 上做语音终端。板子负责听和说，电脑上的后端决定这句话交给 Grok，还是在本机放歌、暂停和调音量；刷过补丁固件的小米智能音箱 Pro 也能接进来。话题含 grok，没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：260
- [andrisgauracs/whistle-esp32](https://github.com/andrisgauracs/whistle-esp32)
  - 说明：把开源语音模型 Whistle 做成一块 ESP32-S3 上的独立实现。按住按键说一句把灯闪成某种颜色，识别在板子上完成，不走网络。README 写明七种语言同时在板子上，模型约 14.5 MB，需要 16 MB 闪存和 8 MB 八线 PSRAM，并对照官方引擎逐张量核对过。
  - 领域：嵌入式 Embedded
  - 总 star：224
- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming)
  - 说明：给编程代理一套 STM32 技能。README 写明按标准库或 HAL、裸机或 FreeRTOS 四条轨生成工程，带引脚表和烧录说明。检索描述列出 CAN、Modbus、BMS、FOC，以及 85 条实测坑和 29 份领域文档。README 里的电池样本是 STM32F103 加 BQ76940 的 9 串管理，电机样本是 SimpleFOC 的 HAL 移植。仓库本身是嵌入式开发技能，所以完整条目放在这里。描述里的 BMS 让它出现在电力电子检索里，FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。这是代码生成技能，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：39

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 写明没有 Mika 自己的服务器，模型用自己的 API 密钥，或登录 ChatGPT、xAI、OpenRouter；安装包要求 Android 11 及以上。话题含 llm。
  - 领域：AI
  - 总 star：8070
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上投毒、资源耗尽和幻觉，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。README 写明只给软件作者保护自己的发布物，并带 14 个对照目标。
  - 领域：AI
  - 总 star：4992
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵。代理已经能写出影片、演示和游戏的声音，却听不出按键廉价、撞击晚了 80 毫秒或配乐鼓错了地方。README 写明它把声音变成代理可以判断的证据，并且只在 CPU 上跑，也能让代理自己写声音再听一遍改。话题含 ai-agents。
  - 领域：AI
  - 总 star：4451
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：262。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 做直流泵 PWM 的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

### 电力电子电源 Power Supply

- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS，此处不展开。领域：电力电子电源 Power Supply。总 star：39。
- [invisiblelevel/canifol](https://github.com/invisiblelevel/canifol)
  - 说明：给修电路的人一套离线工具。计算器覆盖电阻、电容、电感，其中 BMS 一节算均衡电阻、串并联电池组、电流分流器和 MOSFET 保护，旁边还有数据手册、引脚图、SMD 代码和 BoardView。README 写明 1.5.1 版带 6000 多份笔记本、显卡和游戏机图纸，超过 10 GB，SMD 代码库有 270974 条，第一次打开之后可以离线用，安装包覆盖 Windows、Android 和 Linux。搜索描述里的 BMS 是强特征词，所以归入本领域。
  - 领域：电力电子电源 Power Supply
  - 总 star：24

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室 2026 年 RoboMaster 哨兵的定位栈。README 写明它跑在 Ubuntu 22.04 和 ROS 2 Humble 上，用激光和惯性做里程计、点云建图、先验地图定位、回环和重定位，也可以接入 UWB；实机和 rosbag 回放走同一套入口。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：125
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用非均匀 B 样条做多传感器里程计的状态估计。同一套框架覆盖激光惯性、激光视觉惯性、激光加腿部惯性，以及再加视觉的组合，并可做全局样条修正。README 写明这些组合都能实时跑，支持 ROS 2 Humble 和 Jazzy。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：57
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵用 MOSFET 做 PWM；固件里有通断、P 和 PI，并带溢流、干转和传感器保护。README 写明实验台是 15 升罐、0.5 马力级 230 伏泵和 Fotek SSR-40DA，并有按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 4`，每页 5 条，本页是各查询按总 star 排序后的第 16 到第 20 条。

### 嵌入式 Embedded

- [platformio/platformio-core](https://github.com/platformio/platformio-core)
  - 说明：PlatformIO 的核心命令行。用同一套声明式工程在多种架构上编译、烧录和调试固件，并带库管理、静态检查和远程单元测试。README 文件名是 `README.rst`，许可是 Apache 2.0。话题含 embedded、esp32、rtos、firmware、risc-v；话题 `zephyr-rtos` 按词边界计入 zephyr。
  - 领域：嵌入式 Embedded
  - 总 star：9595
- [crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)
  - 说明：开源电纸书固件，让阅读器按读者自己的方式工作。README 写明能排 EPUB，也读 txt 和 bmp，目前跑在基于 ESP32-C3 的 Xteink X4、X3，以及基于 ESP32-S3 的 X4 Pro 等板上。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：8725
- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的官方设备固件。用 LoRa 组一个不靠互联网和蜂窝网的远距离、低功耗网格，传文字、位置和遥测。README 写明支持 ESP32、nRF52、RP2040/RP2350 和 Linux。话题含 esp32 与 stm32。
  - 领域：嵌入式 Embedded
  - 总 star：8559
- [FreeRTOS/FreeRTOS](https://github.com/FreeRTOS/FreeRTOS)
  - 说明：FreeRTOS 的经典发行包，给微控制器提供实时内核和配套库。搜索描述写明内核以子模块引入。名称和描述里的 freertos 计入嵌入式。
  - 领域：嵌入式 Embedded
  - 总 star：7975
- [FastLED/FastLED](https://github.com/FastLED/FastLED)
  - 说明：在 Arduino 和其他微控制器上驱动可寻址彩色灯带。README 写明高端设备可以带动 3 万颗以上的灯，不到 1 美元的小芯片也能用，并覆盖多种灯珠芯片。话题含 embedded 与 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：7530
- [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library) — 见下方「自动控制 Control」完整条目。话题含 embedded 与 mcu，此处不展开。领域：嵌入式 Embedded。总 star：1159。
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：551。

### AI

- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：用 Python 做张量计算和动态神经网络。计算可以上 GPU，网络靠一条磁带式的自动求导来训练。名称 pytorch 计入 AI。
  - 领域：AI
  - 总 star：105329
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：把大语言模型高吞吐、省内存地部署成推理服务。README 写明用 PagedAttention 管理注意力的键值缓存，并连续组批。名称 `vllm` 按词边界不等于 llm，计入靠的是话题 llm，话题里还有 pytorch 与 transformer。
  - 领域：AI
  - 总 star：96689
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：把网页抓成干净的 Markdown 或结构化结果，给代理和数据管道用。README 写明仓库本体是 Apache-2.0 的爬虫，可以用 Python 或 Docker 自己托管；同一篇说明也提供托管接口，免费额度是每月 1000 个额度、不需要信用卡。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：87192
- [pypose/pypose](https://github.com/pypose/pypose) — 见下方「自动控制 Control」完整条目。话题含 pytorch，此处不展开。领域：AI。总 star：1621。

### 功率器件 Power Devices

本页没有留下功率器件仓库。星数最高的 `yayapa/sic` 是生存分析的论文实现，与碳化硅器件无关，见数据源状态。

### 电力电子电源 Power Supply

- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman)
  - 说明：把 Solarman 棒式记录仪接进 Home Assistant，用来读逆变器数据。README 写明建在异步的 pysolarmanv5 上，也支持 Modbus TCP，例子里有 ESP、Waveshare 和以太网记录仪。话题含 inverter 与 modbus，并带 deye、sofar、solis、solax、sunsynk 等设备名。逆变器接入比 Modbus 话题更贴近本领域，嵌入式一节一行带过。
  - 领域：电力电子电源 Power Supply
  - 总 star：551
- [fl4p/batmon-ha](https://github.com/fl4p/batmon-ha)
  - 说明：在 Home Assistant 里通过蓝牙读取电池管理系统。搜索描述列出 JK、JBD、Daly、ANT、SOK、Supervolt 等。README 写明用主机自己的蓝牙，不另加 USB、串口、RS485 或 ESP32，所以不跨到嵌入式；也可以离开 Home Assistant，在 Linux、macOS 和 Windows 上跑。话题含 bms。
  - 领域：电力电子电源 Power Supply
  - 总 star：533

### 自动控制 Control

- [pypose/pypose](https://github.com/pypose/pypose)
  - 说明：在流形上做可微分机器人学。README 写它基于 PyTorch，把深度感知模型和基于物理的优化放在一个库里，并带 EKF、UKF、粒子滤波和 LQR。话题含 slam、kalman-filter 与 pytorch。定位和滤波比 PyTorch 依赖更贴近本领域，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：1621
- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用 MuJoCo 搭一套肌肉骨骼模型和任务，给生物力学、神经科学、机器学习和康复做控制实验。搜索描述写明包一层 OpenAI gym 接口。README 写明第 3 版可以在一块 GPU 上并行训练上千个环境，再把策略放回 CPU 回放。话题含 motor-control。
  - 领域：自动控制 Control
  - 总 star：1283
- [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library)
  - 说明：用纯 C 在 MCU 里跑永磁同步电机的磁场定向控制。搜索描述写明覆盖有感和无感，基于 SVPWM 做位置环、速度环、电流环，并提供 PID 和 LADRC。README 写明版本 3.1.0、MIT，从有感三环做到高频注入加高速无感。电机控制比嵌入式话题更贴近本领域，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：1159

## 数据源状态

11 次逻辑请求全部第一次就是 HTTP 200，无重试。相邻请求按脚本间隔 7 秒。无一次失败。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面；这个数字随每分钟窗口回升，中间出现过从 8 回到 9，不是失败。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 `HEAD/README.md` 中，下列仓库为 HTTP 200：`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`raullenchai/esp32-thinks`、`Liu-zhongxian/zongzhu-bot`、`andrisgauracs/whistle-esp32`、`wdcjx/Embedded-programming`、`wangzan101/Mika`、`qybaihe/bla`、`Leonxlnx/earshot`、`Samarth030312/arduino-water-level-control-lab`、`profesor003-fundesteam/SIC-2026`、`invisiblelevel/canifol`、`mozihe/z-localization`、`woolimi/robotics-roadmap`、`ASIG-X/RESPLE2`、`crosspoint-reader/crosspoint-reader`、`meshtastic/firmware`、`FreeRTOS/FreeRTOS`、`FastLED/FastLED`、`pytorch/pytorch`、`vllm-project/vllm`、`unclecode/crawl4ai`、`yayapa/sic`、`fl4p/batmon-ha`、`pypose/pypose`、`Vincentqyw/cv-arxiv-daily`、`MyoHub/myosuite`、`Sguan-ZhouQing/SguanFOC_Library`。`platformio/platformio-core` 与 `davidrapan/ha-solarman` 的 `HEAD/README.md` 为 HTTP 404；随后用仓库内容接口取 README，前者文件名是 `README.rst`，后者是 `readme.md`，两次都是 HTTP 200。这 30 次 README 页面、2 次内容接口和下面 1 次 Trending 核对，不计入上面 11 次配额。`zongzhu-bot`、`FreeRTOS`、`pytorch` 的说明没有超出搜索描述或标题，README 只用来核对。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 12 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 核对：脚本解析出 12 条后，另一次 GET 同一 URL 仍是 HTTP 200，页面上有 12 个 `article.Box-row`、12 处 “stars today”。这次核对不计入 11 次配额。今日页面本身只有 12 条，不是解析漏条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`meta/astryx`（22693，3111；描述是 agent ready，不等于 `ai-agents`）、`sherlock-project/sherlock`（108902，2387）、`anthropics/skills`（192273，1676；描述是 Agent Skills，不等于 `ai-agents`）、`mattpocock/skills`（320872，1223；Skills for Real Engineers，名称和描述没有领域词）、`homeassistant-ai/ha-mcp`（6610，792；名称里的 mcp 不是本次 AI 关键词，描述也没有 llm）、`vercel-labs/agent-browser`（49171，775；描述是 “Browser automation CLI for AI agents”，空格写法不等于 `ai-agents`）、`anthropics/claude-quickstarts`（20472，530；入门示例合集）、`addyosmani/agent-skills`（115125，465；描述是 “skills for AI coding agents”，空格写法不等于 `ai-agents`）、`google-deepmind/mujoco`（17333，453；物理仿真，名称和描述没有控制关键词）、`ranxianglei/billion-context`（6283，374；上下文压缩插件，名称和描述没有 llm）、`tokio-rs/topcoat`（6779，192）、`we-promise/sure`（11892，184；个人理财）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-12 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-12 stars:>2`。`total_count=458`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 9。这 5 条都写入正文：`agharsallah/esp-labs-web`（782）、`ngxson/esp32-usb-to-airprint`（289）、`raullenchai/esp32-thinks`（262）、`Liu-zhongxian/zongzhu-bot`（260）、`andrisgauracs/whistle-esp32`（224）。`esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。`esp32-usb-to-airprint` 只有名称和描述里的 esp32，接口 `created_at` 为 `2026-10-26T16:18:54Z`，北京时间是 2026-10-27 00:18。另有 1 条完整条目来自电力电子检索：`wdcjx/Embedded-programming`（39），因为 STM32 技能比描述里的 BMS 更贴近本领域。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-12 stars:>2`。`total_count=2478`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `wangzan101/Mika`（8070）、`qybaihe/bla`（4992）、`Leonxlnx/earshot`（4451）。这 3 条是本页星数连续的前 3。另有 1 条跨领域一行：`esp32-thinks`（262），来自嵌入式检索。它话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`benjitaylor/skills`（总 star 3005；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）、`DenisSergeevitch/ex-ussr-kinship-research`（总 star 2325；描述是 “skill for AI agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-12 stars:>2`。`total_count=7`，返回 5，规则保留 2，未命中 3。剩余配额 8。`per_page=5`，第 6、第 7 条不在本次返回里，正文不猜测它们是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9）；其余 4 条总 star 都是 3。
  - `profesor003-fundesteam/SIC-2026`（总 star 3）：名称和描述含 SIC。README 标题写明这是 Samsung Innovation Campus 2026 的数据分析与人工智能课堂材料，含笔记本和数据集，讲师是 Danny Jose Delgado De Sousa，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-18T15:03:12Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（3；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3；`First-Sick` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-12 stars:>2`。`total_count=58`，返回 5，规则保留 2，未命中 3。剩余配额 7。正文保留 `invisiblelevel/canifol`（24）。`wdcjx/Embedded-programming`（39）更贴近嵌入式，本节一行带过。这两条是本页星数最低的两条，排在三条未命中之后。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`Lida-V/3DCharaMakeSkills-Lida`（62）、`leftamber/grid-dca-bot`（49；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-12 stars:>2`。`total_count=75`，返回 5，规则保留 3，未命中 2。剩余配额 6。正文保留 `mozihe/z-localization`（125）、`ASIG-X/RESPLE2`（57）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`FrankyRenderer` 与 `SampQOL-OS` 夹在 `z-localization` 和 `RESPLE2` 之间，所以剔除后本页按总 star 不是连续的 2 个命中仓库。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 96）。话题含 `ros2` 与 `slam`。README 徽章写 57 讲、120 小时，正文是自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。它排在 `FrankyRenderer` 与 `SampQOL-OS` 之间。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 101；描述里的 MPC-BE 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 92；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-04 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-04 stars:>3`。`total_count=1283`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 8。`page=4`、`per_page=5`，本页是总结果里的第 16 到第 20 条。本查询正文：`platformio/platformio-core`（9595）、`crosspoint-reader/crosspoint-reader`（8725）、`meshtastic/firmware`（8559）、`FreeRTOS/FreeRTOS`（7975）、`FastLED/FastLED`（7530）。另有 2 条一行不在本页前 5：`Sguan-ZhouQing/SguanFOC_Library`（1159，话题含 embedded 与 mcu，完整条目在自动控制）、`davidrapan/ha-solarman`（551，话题含 modbus，完整条目在电力电子）。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-04 stars:>3`。`total_count=9113`，返回 5，规则保留 3，排除清单 0，未命中 2。剩余配额 9。正文保留 `pytorch/pytorch`（105329）、`vllm-project/vllm`（96689）、`unclecode/crawl4ai`（87192）。这 3 条在本页按总 star 是连续的中间 3 条，前后各有 1 条未命中。另有 1 条一行来自自动控制：`pypose/pypose`（1621，话题含 pytorch），它不在 AI 常青本页前 5。`esp32-thinks` 话题含 `llm`，但不在 AI 常青本页前 5，不从常青跨节；它的一行在新项目里。
  - 未命中：`nexu-io/open-design`（总 star 107031；描述是 “with your team and AI agents”，空格写法不等于 `ai-agents`）、`career-ops-hq/career-ops`（总 star 81736；描述是 “AI job search agent”，空格和弱词都不等于 `ai-agents` 或 llm）。名称和 topics 都没有领域关键词。按总 star，本页顺序是 open-design、pytorch、vllm、crawl4ai、career-ops。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-04 stars:>3`。`total_count=26`，返回 5，规则保留 1，清单类排除 1，未命中 2，另有 1 条只命中自动控制。剩余配额 9。`page=4` 是总结果里的第 16 到第 20 条。规则保留的 1 条经人工剔除后，本页没有功率器件正文。
  - `yayapa/sic`（总 star 11）：名称是 sic，描述为空。README 写明这是论文《Survival In-Context》的实现，用先验拟合网络做生存分析，与碳化硅器件无关，正文不收。它是本页星数最高的一条。
  - 清单类剔除：`satnamrsm/https-github.com-sickn33-antigravity-awesome-skills`（总 star 9）。名称含 awesome-skills，描述为空，脚本已按 awesome 排除。`sickn33` 按词边界不等于 `sic`。
  - 只命中其他领域：`ajtudela/sicks300_ros2`（总 star 7）。描述是 Sick S300 安全激光雷达的 ROS 2 驱动，话题含 ros2。`sicks300` 不等于 `sic`。它不在自动控制常青本页前 5，不跨节。
  - 名称词边界未命中：`rvandewater/SICdb_MEDS`（6；萨尔茨堡重症监护数据库，`SICdb` 不等于 `sic`）、`Sizerta/SiCell.jl`（6；单细胞 RNA 工具，`SiCell` 不等于 `sic`）。这两条总 star 相同，本次不区分它们在页内的先后。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-04 stars:>3`。`total_count=382`，返回 5，规则保留 2，未命中 3。剩余配额 8。`page=4` 是总结果里的第 16 到第 20 条。正文保留 `davidrapan/ha-solarman`（551）、`fl4p/batmon-ha`（533）。这两条在本页按总 star 连续，夹在 `AAFFamilyDCHAudio` 与 `consul-replicate` 之间。
  - 名称和 topics 未命中：`AAFOptimus/AAFFamilyDCHAudio`（581；声卡驱动，名称里的 DCH 不等于 `dc-dc`）、`hashicorp/consul-replicate`（525；跨数据中心复制，名称里的跨 DC 不等于 `dc-dc`）、`dcm4che/dcm4chee-arc-light`（507；DICOM 归档，名称里的 dcm 不等于 `dc-dc`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-04 stars:>3`。`total_count=226`，返回 5，规则保留 4，清单类排除 1，未命中 0。剩余配额 9。正文保留 `pypose/pypose`（1621）、`MyoHub/myosuite`（1283）、`Sguan-ZhouQing/SguanFOC_Library`（1159）。`cv-arxiv-daily` 与 `awesome-lidar` 夹在 pypose 和 myosuite 之间，所以本页按总 star 不是连续的 3 个命中仓库。
  - 清单类剔除：`szenergy/awesome-lidar`（总 star 1369）。名称命中 awesome，话题含 slam，描述是雷达厂商、数据集和算法清单，脚本已排除，不进正文。
  - 人工剔除：`Vincentqyw/cv-arxiv-daily`（总 star 1517）。话题含 slam。README 写明用 GitHub Actions 每天更新计算机视觉论文，页首日期是 2026.11.09，正文是按年分栏的论文表，属每日论文清单，不进正文。脚本的清单规则没有命中这条描述。
