# GitHub 领域日报 · 2026-11-08

生成时间：2026-11-08 07:38（北京时间）。数据拉取开始于 2026-11-08 07:33:46（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-09（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-01 及之后有推送、总 star > 3。轮换页 `page = (当年第 312 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 7600，没有 24 小时新增数据。
2. [ruvnet/RuView](https://github.com/ruvnet/RuView) 用廉价 ESP32 读 Wi-Fi 信道状态，在没有摄像头的情况下估计房间里有没有人、呼吸和心率；本页常青按总 star 排在嵌入式首位，总 star 102869，没有 24 小时新增数据。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块 7 美元的 ESP32；总 star 4630，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 15 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。

嵌入式、AI、功率器件、电力电子电源、自动控制在这 15 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4630
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验收成一个网页，能看实时引脚、跑交互模拟、读固件和实验记录，界面有 11 种语言。README 写明目前是 32 个动手实验。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：686
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：286
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：262
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32-S3 上做语音终端。README 写明板子负责听和说，电脑上的后端决定这句话交给 Grok，还是在本机放歌、暂停和调音量；刷过补丁固件的小米智能音箱 Pro 也能接进来。话题含 grok，没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：257
- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming)
  - 说明：给编程代理一套 STM32 技能，按标准库或 HAL、裸机或 FreeRTOS 四条轨写出带引脚表和烧录说明的工程，再用静态检查把时钟顺序、中断阻塞这类纪律清掉才交付。README 把九串 BQ76940 电池管理和 FOC 电机控制写成已经上板的样本；仓库本身是嵌入式开发技能，所以完整条目放在这里。描述里的 BMS 让它出现在电力电子检索里，FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。这是代码生成技能，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：39

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 写明没有 Mika 自己的服务器，模型用你的 API 密钥或已登录的账号。话题含 llm。
  - 领域：AI
  - 总 star：7600
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4630。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵。代理已经能写出影片、演示和游戏的声音，却听不出按键廉价、撞击晚了 80 毫秒或配乐鼓错了地方。README 写明它把声音变成代理可以判断的证据，并且只在 CPU 上跑，也能让代理自己写声音再听一遍改。话题含 ai-agents。
  - 领域：AI
  - 总 star：4179
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上资源上限和诱饵，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。README 写明这是保护自己软件的防御工具。
  - 领域：AI
  - 总 star：2759
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
  - 总 star：53
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵走 MOSFET；固件里有通断、P 和 PI，并带溢流、干转和传感器保护，另有一套按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 1`，每页 5 条，本页是各查询按总 star 排序后的第 1 到第 5 条。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：把普通 Wi-Fi 变成不靠摄像头的空间感知。README 写明用廉价 ESP32 采集信道状态，估计房间里有没有人、人怎么动、呼吸和心率。话题含 esp32 与 firmware，也含 awesome；仓库是这套感知软件和固件，不是合集，正文保留。
  - 领域：嵌入式 Embedded
  - 总 star：102869
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：用来写游戏和图形程序的 C 库。README 写明它也适合做原型、工具和嵌入式上的图形。话题含 embedded 与 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：35582
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：跑在 ESP32 上的语音聊天固件，用 MCP 控制喇叭、灯和舵机这类外设。README 写到千问、DeepSeek 和语音识别加语言模型再加合成的链路，搜索描述和话题里没有 llm，话题里的 mcp 也不是 AI 关键词，所以不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：32842
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：给小单片机到带 3D 的处理器做界面的开源图形库。README 写明一个典型界面大约要 100kB 内存。话题含 embedded、esp32、stm32 与 zephyr。
  - 领域：嵌入式 Embedded
  - 总 star：25110
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：给 ESP8266 和 ESP32 设备用的替代固件，用网页配置，可 OTA 升级，定时和规则做本地自动化，经 MQTT、HTTP、串口或 KNX 控制，不强制连云。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：24970
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13007。

### AI

- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
  - 说明：把网页搜索、抓取和交互收成给代理用的上下文。README 写明输出可以是干净的 Markdown、结构化 JSON 或截图，仓库开源，也有托管服务。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：199520
- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：给文本、视觉、音频和多模态模型放一份大家共用的模型定义，训练和推理都走这一份。README 写明 Hub 上有超过 100 万个可用的模型检查点。话题含 llm、pytorch 与 transformer。
  - 领域：AI
  - 总 star：168633
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：搭智能体工作流和检索管道的工作台，模型工具都接在同一处，可以上云、放进 VPC，也可以自己托管，免得原型和生产各写一套。话题含 llm。
  - 领域：AI
  - 总 star：160632

### 功率器件 Power Devices

本页没有命中功率器件仓库。返回的 5 条里，名称里的 Sick、sicp、Sico、SICK 按词边界都不等于 sic。

### 电力电子电源 Power Supply

本页剔除后为空。描述里的 LLC 是维护公司的后缀，见数据源状态。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：用尽量少的依赖，把定位、建图、SLAM 和路径规划写成可读的 Python 示例，并配一份讲这些算法的教材。示例代码就是这个仓库，不是向外收集的公开课清单。话题含 slam。
  - 领域：自动控制 Control
  - 总 star：30873
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：打算做成可自行打印、本地运行的扫地机器人，用二维激光在 ROS 2 里建图和导航。README 写明现在还不能按清单装出整机，今天只能跑仿真。话题含 ros2 与 slam，也含 esp32，嵌入式一节一行带过。扫地定位比这块板的话题更贴近本领域。
  - 领域：自动控制 Control
  - 总 star：13007
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：开源飞控固件，跑在飞控板上，覆盖竞速、花式、航拍、远航和固定翼。话题含 flight-controller。README 列出 STM32 与实验性 ESP32，搜索话题没有这些词，不跨到嵌入式。
  - 领域：自动控制 Control
  - 总 star：11753
- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：RTAB-Map 的库和可单独运行的程序，用来做同步定位与建图。README 把 ROS 用法指到 ROS 维基。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：4086

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`wangzan101/Mika`、`Leonxlnx/earshot`、`qybaihe/bla`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Liu-zhongxian/zongzhu-bot`、`wdcjx/Embedded-programming`、`Samarth030312/arduino-water-level-control-lab`、`mozihe/z-localization`、`ASIG-X/RESPLE2`、`woolimi/robotics-roadmap`、`marozols/SIC-existence`、`ruvnet/RuView`、`78/xiaozhi-esp32`、`lvgl/lvgl`、`arendst/Tasmota`、`firecrawl/firecrawl`、`huggingface/transformers`、`langgenius/dify`、`AtsushiSakai/PythonRobotics`、`makerspet/oomwoo`、`betaflight/betaflight`、`introlab/rtabmap`、`raysan5/raylib`、`onehumanbeing/esp32-iphone-agent`、`raullenchai/esp32-thinks`。这 26 次是 raw README，不计入上面 11 次搜索配额。`esp32-iphone-agent` 与 `esp32-thinks` 的说明没有超出搜索描述，README 只用来核对。`arduino-water-level-control-lab` 的说明也没有超出搜索描述，README 只用来确认它是带固件的实验，不是公开课清单。`Tasmota` 正文用的是搜索描述；README 写了 Modbus 电表和 Modbus 桥，搜索话题没有 modbus，不跨节。`dify` 正文用的是搜索描述。`rtabmap` 的 README 没有展开算法，只确认它是库和独立程序，并把 ROS 用法指到维基。`PythonRobotics` 的 README 用来确认它是算法示例加教材，不是公开课清单。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 15 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。正文为空。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`cloudflare/security-audit-skill`（65659，2088；描述是 coding-agent，不等于 `ai-agents`，也没有 llm）、`milind-soni/OpenMausBot`（16929，1986；Grok Bot，名称和描述没有 llm）、`sherlock-project/sherlock`（100386，1819）、`zed-industries/zed`（94256，1119）、`mattpocock/skills`（317670，1111）、`google/skills`（23373，449；描述是 Agent Skills，不等于 `ai-agents`）、`anthropics/skills`（188755，386；描述是 Agent Skills，不等于 `ai-agents`）、`astral-sh/ruff`（50967，350）、`prometheus/prometheus`（67441，325）、`meta/astryx`（14463，185）、`ranxianglei/billion-context`（4590，185；上下文压缩，名称和描述没有 llm）、`mbillow/localthings`（1049，184）、`tailwindlabs/tailwindcss`（98449，181）、`vercel-labs/agent-browser`（46799，180；描述是 “Browser automation CLI for AI agents”，空格写法不等于 `ai-agents`）、`dsx-ai-factory/nvke`（545，125；描述是 “bare metal”，空格不等于 `bare-metal`）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-09 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-09 stars:>2`。`total_count=435`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4630）、`agharsallah/esp-labs-web`（686）、`ngxson/esp32-usb-to-airprint`（286）、`raullenchai/esp32-thinks`（262）、`Liu-zhongxian/zongzhu-bot`（257）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。`esp32-usb-to-airprint` 只有名称和描述里的 esp32，接口 `created_at` 为 `2026-10-26T16:18:54Z`，北京时间是 2026-10-27 00:18。另有 1 条完整条目来自电力电子检索：`wdcjx/Embedded-programming`（39），因为 STM32 技能比描述里的 BMS 更贴近本领域。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-09 stars:>2`。`total_count=2524`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 7。正文保留 `wangzan101/Mika`（7600）、`Leonxlnx/earshot`（4179）、`qybaihe/bla`（2759）。这 3 条是本页星数连续的前 3。另有 2 条跨领域一行：`esp32-iphone-agent`（4630）、`esp32-thinks`（262），来自嵌入式检索。这两条话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`benjitaylor/skills`（总 star 2469；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）、`DenisSergeevitch/ex-ussr-kinship-research`（总 star 2140；描述是 “skill for AI agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-09 stars:>2`。`total_count=6`，返回 5，规则保留 2，未命中 3。剩余配额 9。`per_page=5`，第 6 条不在本次返回里，正文不猜测它是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC。README 写明这是 Lean 对任意有限维都存在 SIC-POVM 的形式化证明，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-09T19:01:28Z`，落在 `created:>=2026-10-09` 上。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`Arafat-shuvo/Sicip-data-sciebce`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`First-Sick` 与 `Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-09 stars:>2`。`total_count=61`，返回 5，规则保留 1。剩余配额 8。规则保留的 1 条更贴近嵌入式，本节只留一行，因此没有以本领域为最贴近领域的完整新项目。
  - `wdcjx/Embedded-programming`（总 star 39）：描述列出 CAN/Modbus/BMS/FOC。话题含 embedded、stm32、freertos。完整条目在嵌入式，本节一行带过。描述里的 FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`Dreamyepruner97/gwffttqz`（317；描述声称提供 Acrobat Pro DC 的已激活副本，与电源无关，DC 不等于 `dc-dc`）、`Lida-V/3DCharaMakeSkills-Lida`（60）、`leftamber/grid-dca-bot`（48；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。分类按词边界没有计入。`Embedded-programming` 是本页星数最低的一条。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-09 stars:>2`。`total_count=73`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `mozihe/z-localization`（123）、`ASIG-X/RESPLE2`（53）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`SampQOL-OS` 与 `FrankyRenderer` 夹在 `robotics-roadmap` 和 `RESPLE2` 之间，所以剔除后本页按总 star 不是连续的 2 个命中仓库。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 95）。话题含 `ros2` 与 `slam`，README 写明是 57 讲、约 120 小时的自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。它排在 `z-localization` 与 `SampQOL-OS` 之间。
  - 名称和 topics 未命中：`snarebes/SampQOL-OS`（总 star 81；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）、`mryx007/FrankyRenderer`（总 star 78；描述里的 MPC-BE 是播放器兼容，不是强特征词）。

### C. 领域常青（`pushed:>=2026-11-01 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-01 stars:>3`。`total_count=1269`，返回 5，规则保留 5，清单类排除 0。剩余配额 8。`page=1`、`per_page=5`，本页是总结果里的第 1 到第 5 条。本查询正文完整条目 5 条：`ruvnet/RuView`（102869）、`raysan5/raylib`（35582）、`78/xiaozhi-esp32`（32842）、`lvgl/lvgl`（25110）、`arendst/Tasmota`（24970）。`RuView` 话题含 awesome，README 写的是 Wi-Fi 感知软件和 ESP32 固件，不是合集，正文保留。另有 1 条一行来自自动控制：`makerspet/oomwoo`（13007，话题含 esp32）。`OpenDTU` 话题含 esp32，但不在本页前 5，不跨节。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-01 stars:>3`。`total_count=9251`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 6。正文保留 `firecrawl/firecrawl`（199520）、`huggingface/transformers`（168633）、`langgenius/dify`（160632）。`msitarzewski/agency-agents` 夹在 `transformers` 与 `dify` 之间，`langflow-ai/langflow` 排在 `dify` 后面，所以本页按总 star 不是连续的 3 个命中仓库。`esp32-iphone-agent` 与 `esp32-thinks` 话题含 `llm`，但不在 AI 常青前 5，不从常青跨节；它们的一行在新项目里。`microsoft/Sico` 话题含 `llm`，也不在前 5，不跨节。
  - 未命中：`msitarzewski/agency-agents`（总 star 167119；名称 `agency-agents` 不等于 `ai-agents`，描述是 “A complete AI agency”，没有领域关键词）、`langflow-ai/langflow`（总 star 156422；描述是 “AI-powered agents”，不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-01 stars:>3`。`total_count=27`，返回 5，规则保留 0，未命中 4，另有 1 条只命中别的领域。剩余配额 9。`page=1` 是总结果里的第 1 到第 5 条。本页没有功率器件正文。
  - 名称词边界未命中：`SickChill/sickchill`（2445；`sickchill` 不等于 `sic`）、`mdhiggins/sickbeard_mp4_automator`（1589；`sickbeard` 不等于 `sic`）、`source-academy/sicp`（1026；`sicp` 不等于 `sic`）、`Yuri-NagaSaki/SICK`（245；`SICK` 不等于 `sic`，描述是 Server Info & Check Kit）。
  - `microsoft/Sico`（总 star 284）：描述是企业数字员工平台，`Sico` 不等于 `sic`。话题含 `llm`，但不在 AI 常青前 5，不跨节。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-01 stars:>3`。`total_count=404`，返回 5，规则保留 1，未命中 3，另有 1 条只命中别的领域。剩余配额 5。`page=1` 是总结果里的第 1 到第 5 条。规则保留的那条经人工剔除后，本页没有电力电子正文。
  - `Finbuckle/Finbuckle.MultiTenant`（总 star 1633）：描述写明由 Finbuckle LLC 维护。LLC 是公司后缀，不是谐振变换器，正文不收。它排在 `dcgm-exporter` 与 `dcm4che` 之间。
  - 名称和 topics 未命中：`dalathegreat/Battery-Emulator`（3015；描述里的 inverters 是复数，不等于 `inverter`）、`NVIDIA/dcgm-exporter`（1924；名称里的 dcgm 不等于 `dc-dc`）、`dcm4che/dcm4che`（1465；DICOM 实现，名称里的 dcm 不等于 `dc-dc`）。
  - `tbnobody/OpenDTU`（总 star 2206）：描述里的 Inverters 是复数，不等于 `inverter`。话题含 `esp32`，但不在嵌入式常青前 5，不跨节。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-01 stars:>3`。`total_count=228`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。正文保留 `AtsushiSakai/PythonRobotics`（30873）、`makerspet/oomwoo`（13007）、`betaflight/betaflight`（11753）、`introlab/rtabmap`（4086）。`MPC-BE` 夹在 `betaflight` 与 `rtabmap` 之间，所以本页按总 star 不是连续的 4 个命中仓库。
  - 撞名剔除：`Aleksoid1978/MPC-BE`（总 star 4683）。名称里的 mpc 是 Windows 上的音视频播放器，描述写明播放音频和视频文件，不是模型预测控制，正文不收。
