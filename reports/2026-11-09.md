# GitHub 领域日报 · 2026-11-09

生成时间：2026-11-09 07:35（北京时间）。数据拉取开始于 2026-11-09 07:31:20（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-10（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-02 及之后有推送、总 star > 3。轮换页 `page = (当年第 313 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 7737，没有 24 小时新增数据。
2. [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms) 把极空电池管理系统接到 ESPHome，用串口或蓝牙读电芯；本页常青里，这是电力电子电源唯一留下的仓库，总 star 1050，没有 24 小时新增数据。
3. [okalachev/flix](https://github.com/okalachev/flix) 用通用零件从零做一台 ESP32 四旋翼，固件大约两千行，README 写明已经飞起来；总 star 2463，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 9 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。

嵌入式、AI、功率器件、电力电子电源、自动控制在这 9 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4692
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验收成一个网页，能看实时引脚、跑交互模拟、读固件和实验记录，界面有 11 种语言。README 写明目前是 32 个动手实验。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：695
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：287
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：262
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32-S3 上做语音终端。README 写明板子负责听和说，电脑上的后端决定这句话交给 Grok，还是在本机放歌、暂停和调音量；刷过补丁固件的小米智能音箱 Pro 也能接进来。话题含 grok，没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：259
- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming)
  - 说明：给编程代理一套 STM32 技能，按标准库或 HAL、裸机或 FreeRTOS 四条轨写出带引脚表和烧录说明的工程，再用静态检查把时钟顺序、中断阻塞这类纪律清掉才交付。README 把九串 BQ76940 电池管理和 FOC 电机控制写成已经上板的样本；仓库本身是嵌入式开发技能，所以完整条目放在这里。描述里的 BMS 让它出现在电力电子检索里，FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。这是代码生成技能，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：39

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 写明没有 Mika 自己的服务器，模型用你的 API 密钥，或登录 ChatGPT、xAI、OpenRouter 账号。话题含 llm。
  - 领域：AI
  - 总 star：7737
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4692。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵。代理已经能写出影片、演示和游戏的声音，却听不出按键廉价、撞击晚了 80 毫秒或配乐鼓错了地方。README 写明它把声音变成代理可以判断的证据，并且只在 CPU 上跑，也能让代理自己写声音再听一遍改。话题含 ai-agents。
  - 领域：AI
  - 总 star：4273
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上投毒、资源耗尽和幻觉，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。README 写明这是保护自己软件的防御工具。
  - 领域：AI
  - 总 star：3775
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：262。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 开关直流泵的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

### 电力电子电源 Power Supply

本日没有以电力电子电源为最贴近领域的完整新项目。描述里带 BMS 的 STM32 代理技能，完整说明写在上方「嵌入式 Embedded」。

- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS，此处不展开。领域：电力电子电源 Power Supply。总 star：39。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室 2026 年 RoboMaster 哨兵的定位栈。README 写明它跑在 ROS 2 Humble 上，用激光和惯性做里程计、点云建图、先验地图定位、回环和重定位，也可以接入 UWB；实机和 rosbag 回放走同一套入口。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：123
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用非均匀 B 样条做多传感器里程计的状态估计。同一套框架覆盖激光惯性、激光视觉惯性、激光加腿部惯性，以及再加视觉的组合，并可做全局样条修正。README 写明这些组合都能实时跑，支持 ROS 2 Humble 和 Jazzy。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：55
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵走 MOSFET；固件里有通断、P 和 PI，并带溢流、干转和传感器保护，另有一套按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 2`，每页 5 条，本页是各查询按总 star 排序后的第 6 到第 10 条。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：用 ESP32 经 Wi-Fi 控制可寻址灯。README 写这是灯带到二维矩阵和 HUB75 面板的固件，内置 200 多种效果。话题含 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：19000
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：把 Go 编译到单片机、WebAssembly 和命令行小工具上，后端用 LLVM。话题含 esp32 与 stm32。
  - 领域：嵌入式 Embedded
  - 总 star：17904
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：让 Arduino 写法跑在 ESP32 系列上的核心库。README 列出 ESP32、C3、C5、C6、H2、P4、S2、S3；C2 与 C61 要当作 ESP-IDF 组件，或重编静态库。话题含 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：17692
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：给 RepRap 一类 3D 打印机用的固件，8 位和 32 位微控制器都能编。README 写 Marlin 2.1 同一套代码覆盖 8 位 AVR 和 32 位 ARM，最多 9 个协同轴、8 个挤出机。检索描述写明不少商用打印机出厂就带它。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：17652
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：面向资源受限设备的实时操作系统，从小传感器、可穿戴灯到智能手表和物联网网关。README 写架构包括 ARM Cortex-M 和 RISC-V。话题含 embedded、rtos、zephyr 与 mcu。
  - 领域：嵌入式 Embedded
  - 总 star：17040
- [okalachev/flix](https://github.com/okalachev/flix) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：2463。

### AI

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图在本地跑扩散模型，做图像、视频、三维、音频和文本工作流，不必为每条链路重写推理代码。README 写核心默认可离线，只有主动请求时才下载。话题含 pytorch，`stable-diffusion` 按词边界计入 diffusion。
  - 领域：AI
  - 总 star：145793
- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：一套可改的编程代理外壳：统一的语言模型接口、代理循环、终端界面和命令行。README 写它自带默认能力，子代理和计划模式留给扩展或包去补。话题为空，检索描述里的 LLM 是强特征词，因此计入。
  - 领域：AI
  - 总 star：120841
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：让语言模型代理像人一样操作浏览器的 Python 库，另外提供隐身浏览器和托管代理接口。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：120344
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
  - 说明：把代理每次会话里做过的事记下来，压缩后再把相关片段注回以后的会话，换会话也不丢上下文。检索描述写明可用于 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等。话题含 ai-agents。
  - 领域：AI
  - 总 star：114881

### 功率器件 Power Devices

本页没有命中功率器件仓库。脚本按词边界留下的两条，分别是教材里的 SIC/XE 教学计算机和名为 sic 的链接聚合站，都与碳化硅器件无关，见数据源状态。

### 电力电子电源 Power Supply

- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：给 ESPHome 加一个组件，经 UART 或蓝牙读极空 JK-BMS。检索描述写的是监测并控制。README 要求软件版本不低于 6.0，ESPHome 2026.1.0 或更高，板子可以是 ESP32 或 ESP8266。话题没有 esp32，不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：1050

### 自动控制 Control

- [RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)
  - 说明：把能画成图的非线性最小二乘做成可扩展的 C++ 框架。README 写现成解覆盖多种 SLAM 和光束法平差，新问题通常几行就能接上。话题含 slam。
  - 领域：自动控制 Control
  - 总 star：3478
- [SteveMacenski/slam_toolbox](https://github.com/SteveMacenski/slam_toolbox)
  - 说明：做二维激光的长期建图和定位，地图可以很大，也可以载入已保存的位姿图接着建、接着修。README 写它是目前 ROS 2 里被支持的 SLAM 库。名称含 slam，话题为空。检索描述写的是 ROS。
  - 领域：自动控制 Control
  - 总 star：2706
- [okalachev/flix](https://github.com/okalachev/flix)
  - 说明：用通用零件从零做一台基于 ESP32 的四旋翼。固件大约两千行 Arduino 代码，通信用 MAVLink，走 Wi-Fi 或 ESP-NOW，可用手柄、遥控或手机。README 写明已经飞起来，并带 Gazebo 仿真。话题含 flight-controller 与 esp32。飞控比这块板更贴近本领域，嵌入式一节一行带过。话题里的 education 指教学和研究用途，仓库是能飞的飞行器，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：2463

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`wangzan101/Mika`、`Leonxlnx/earshot`、`qybaihe/bla`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Liu-zhongxian/zongzhu-bot`、`wdcjx/Embedded-programming`、`Samarth030312/arduino-water-level-control-lab`、`mozihe/z-localization`、`ASIG-X/RESPLE2`、`woolimi/robotics-roadmap`、`profesor003-fundesteam/SIC-2026`、`wled/WLED`、`tinygo-org/tinygo`、`espressif/arduino-esp32`、`MarlinFirmware/Marlin`、`zephyrproject-rtos/zephyr`、`Comfy-Org/ComfyUI`、`earendil-works/pi`、`browser-use/browser-use`、`thedotmack/claude-mem`、`syssi/esphome-jk-bms`、`RainerKuemmerle/g2o`、`SteveMacenski/slam_toolbox`、`okalachev/flix`、`jurem/SicTools`、`epilys/sic`、`vedderb/bldc`、`SICKAG/sick_scan_xd`、`onehumanbeing/esp32-iphone-agent`、`raullenchai/esp32-thinks`。这 31 次是 raw README，不计入上面 11 次搜索配额。`esp32-iphone-agent` 与 `esp32-thinks` 的说明没有超出搜索描述，README 只用来核对。`arduino-water-level-control-lab` 的说明也没有超出搜索描述，README 只用来确认它是带固件的实验，不是公开课清单。`tinygo`、`browser-use`、`claude-mem` 的正文用的是搜索描述。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 9 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。正文为空。
- 核对：脚本解析出 9 条后，另一次 GET 同一 URL 仍是 HTTP 200，页面上有 9 个 `article.Box-row`、9 处 “stars today”。这次核对不计入 11 次配额。今日页面本身只有 9 条，不是解析漏条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`sherlock-project/sherlock`（103359，2372）、`milind-soni/OpenMausBot`（18197，1437；Grok Bot，名称和描述没有 llm）、`meta/astryx`（16601，863；描述是 agent ready，不等于 `ai-agents`）、`vercel-labs/agent-browser`（47552，812；描述是 “Browser automation CLI for AI agents”，空格写法不等于 `ai-agents`）、`anthropics/skills`（189589，793；描述是 Agent Skills，不等于 `ai-agents`）、`ranxianglei/billion-context`（5110，460；上下文压缩，名称和描述没有 llm）、`dsx-ai-factory/nvke`（828，345；描述是 “bare metal”，空格不等于 `bare-metal`）、`anthropics/claude-quickstarts`（19394，28；入门示例合集，名称和描述没有领域词）、`google-deepmind/mujoco`（16382，26；物理仿真，名称和描述没有控制关键词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-10 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-10 stars:>2`。`total_count=443`，返回 5，规则保留 5，排除清单 0。剩余配额 8。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4692）、`agharsallah/esp-labs-web`（695）、`ngxson/esp32-usb-to-airprint`（287）、`raullenchai/esp32-thinks`（262）、`Liu-zhongxian/zongzhu-bot`（259）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。`esp32-usb-to-airprint` 只有名称和描述里的 esp32，接口 `created_at` 为 `2026-10-26T16:18:54Z`，北京时间是 2026-10-27 00:18。另有 1 条完整条目来自电力电子检索：`wdcjx/Embedded-programming`（39），因为 STM32 技能比描述里的 BMS 更贴近本领域。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-10 stars:>2`。`total_count=2443`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 7。正文保留 `wangzan101/Mika`（7737）、`Leonxlnx/earshot`（4273）、`qybaihe/bla`（3775）。这 3 条是本页星数连续的前 3。另有 2 条跨领域一行：`esp32-iphone-agent`（4692）、`esp32-thinks`（262），来自嵌入式检索。这两条话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`benjitaylor/skills`（总 star 2678；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）、`DenisSergeevitch/ex-ussr-kinship-research`（总 star 2207；描述是 “skill for AI agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-10 stars:>2`。`total_count=6`，返回 5，规则保留 2，未命中 3。剩余配额 9。`per_page=5`，第 6 条不在本次返回里，正文不猜测它是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `profesor003-fundesteam/SIC-2026`（总 star 3）：名称和描述含 SIC。README 写明这是 Samsung Innovation Campus 2026 的数据分析与人工智能课堂材料，含笔记本和数据集，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-18T15:03:12Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`Arafat-shuvo/Sicip-data-sciebce`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`First-Sick` 与 `Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-10 stars:>2`。`total_count=60`，返回 5，规则保留 1。剩余配额 8。规则保留的 1 条更贴近嵌入式，本节只留一行，因此没有以本领域为最贴近领域的完整新项目。
  - `wdcjx/Embedded-programming`（总 star 39）：描述列出 CAN/Modbus/BMS/FOC。话题含 embedded、stm32、freertos。完整条目在嵌入式，本节一行带过。描述里的 FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`Lida-V/3DCharaMakeSkills-Lida`（61）、`leftamber/grid-dca-bot`（49；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）、`seuclkzsd/hsolve`（38；电磁仿真特征值求解，名称和描述没有电源关键词）。分类按词边界没有计入。`Embedded-programming` 排在 `DCore` 与 `hsolve` 之间，不是本页星数最高的一条。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-10 stars:>2`。`total_count=68`，返回 5，规则保留 3，未命中 2。剩余配额 8。正文保留 `mozihe/z-localization`（123）、`ASIG-X/RESPLE2`（55）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`FrankyRenderer` 与 `SampQOL-OS` 夹在 `robotics-roadmap` 和 `RESPLE2` 之间，所以剔除后本页按总 star 不是连续的 2 个命中仓库。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 95）。话题含 `ros2` 与 `slam`，README 写明是 57 讲、约 120 小时的自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。它排在 `z-localization` 与 `FrankyRenderer` 之间。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 90；描述里的 MPC-BE 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 85；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-02 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-02 stars:>3`。`total_count=1268`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。`page=2`、`per_page=5`，本页是总结果里的第 6 到第 10 条。本查询正文完整条目 5 条：`wled/WLED`（19000）、`tinygo-org/tinygo`（17904）、`espressif/arduino-esp32`（17692）、`MarlinFirmware/Marlin`（17652）、`zephyrproject-rtos/zephyr`（17040）。另有 1 条一行来自自动控制：`okalachev/flix`（2463，话题含 esp32）。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-02 stars:>3`。`total_count=9099`，返回 5，规则保留 4，排除清单 1，未命中 0。剩余配额 9。正文保留 `Comfy-Org/ComfyUI`（145793）、`earendil-works/pi`（120841）、`browser-use/browser-use`（120344）、`thedotmack/claude-mem`（114881）。`awesome-llm-apps` 夹在 `ComfyUI` 与 `pi` 之间，所以本页按总 star 不是连续的 4 个命中仓库。`esp32-iphone-agent` 与 `esp32-thinks` 话题含 `llm`，但不在 AI 常青本页前 5，不从常青跨节；它们的一行在新项目里。
  - 清单类剔除：`Shubhamsaboo/awesome-llm-apps`（总 star 144215）。名称命中 awesome，描述是 AI Agents 与应用合集，不进正文。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-02 stars:>3`。`total_count=30`，返回 5，规则保留 2，未命中 2，另有 1 条只命中别的领域。剩余配额 8。`page=2` 是总结果里的第 6 到第 10 条。规则保留的 2 条经人工剔除后，本页没有功率器件正文。
  - `jurem/SicTools`（总 star 57）：描述含 SIC。README 写明这是 Leland Beck《System Software》里 SIC/XE 假设计算机的汇编器、仿真器和链接器，与碳化硅器件无关，正文不收。
  - `epilys/sic`（总 star 27）：名称是 sic。README 写明这是按标签聚合的链接站，公开实例在 sic.pm，与碳化硅器件无关，正文不收。
  - 名称词边界未命中：`siconos/siconos`（187；`siconos` 不等于 `sic`，描述是非光滑动力系统仿真）、`hexlet-volunteers/hexlet-sicp`（114；`sicp` 不等于 `sic`，描述是 SICP 读书进度服务）。
  - `SICKAG/sick_scan_xd`（总 star 179）：名称里的 SICK 不等于 `sic`，描述是西克激光雷达和雷达驱动。话题含 `ros2`，但不在自动控制常青本页前 5，不跨节。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-02 stars:>3`。`total_count=391`，返回 5，规则保留 1，未命中 4。剩余配额 9。`page=2` 是总结果里的第 6 到第 10 条。正文保留 `syssi/esphome-jk-bms`（1050）。它排在 `dcm2niix` 与 `dcmtk` 之间，所以本页按总 star 不是从第 6 名连续数下来的唯一命中，前面三条未命中。
  - 名称和 topics 未命中：`Evalle/DCA`（1413；Docker 认证备考，DCA 不等于 `dc-dc`）、`mjbots/moteus`（1372；描述是 “Brushless DC motor controller”，Brushless DC 不等于 `dc-dc`，名称也不含 `motor-control`）、`rordenlab/dcm2niix`（1210；DICOM 转 NIfTI，名称里的 dcm 不等于 `dc-dc`）、`DCMTK/dcmtk`（920；DICOM 工具包，名称里的 dcm 不等于 `dc-dc`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-02 stars:>3`。`total_count=219`，返回 5，规则保留 3，清单类排除 1，未命中 1。剩余配额 7。正文保留 `RainerKuemmerle/g2o`（3478）、`SteveMacenski/slam_toolbox`（2706）、`okalachev/flix`（2463）。`vedderb/bldc` 排在 `g2o` 前面，`awesome-robotics-libraries` 夹在 `g2o` 与 `slam_toolbox` 之间，所以本页按总 star 不是连续的 3 个命中仓库。
  - 名称和 topics 未命中：`vedderb/bldc`（总 star 3566）。检索描述是 “The VESC motor control firmware”，空格写法不等于 `motor-control`。名称 `bldc` 不在自动控制的话题/仓库名关键词表里（`bldc` 只在强特征描述词中）。README 写明这是 VESC 的 DC/BLDC/FOC 固件，但归类只看话题、仓库名和检索描述，不把 README 当作命中依据，正文不收。
  - 清单类剔除：`jslee02/awesome-robotics-libraries`（总 star 3110）。名称命中 awesome，话题含 slam，描述是机器人库合集，不进正文。
