# GitHub 领域日报 · 2026-11-10

生成时间：2026-11-10 07:36（北京时间）。数据拉取开始于 2026-11-10 07:32:00（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-11（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-03 及之后有推送、总 star > 3。轮换页 `page = (当年第 314 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) 用语言模型给 A 股、港股、美股、日股、韩股和台股的自选股做每日分析，并把决策仪表盘推出去；这是今日热度里唯一命中领域的仓库，总 star 68799，24 小时新增 star 505。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 7904，没有 24 小时新增数据。
3. [makerspet/oomwoo](https://github.com/makerspet/oomwoo) 想做一台本地建图的开源扫地机器人，总 star 13031；README 写明现在还不能按物料单装出来，今天只能跑仿真，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 11 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

### AI

- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
  - 说明：给自选股做每日分析。覆盖 A 股、港股、美股、日股、韩股和台股，把结论、评分和风险收成决策仪表盘，推到企业微信、飞书、Telegram、Discord、Slack 或邮箱。页面描述写明由 LLM 驱动，并支持零成本定时运行。
  - 领域：AI
  - 总 star：68799
  - 24 小时新增 star：505

嵌入式、功率器件、电力电子电源、自动控制在这 11 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone。眼睛走 AirPlay，手走 USB HID，中间是一块约 7 美元的 ESP32，不用 Mac、开发者账号或越狱。话题含 llm，硬件桥更贴近本领域，AI 一节一行带过。
  - 领域：嵌入式 Embedded
  - 总 star：4757
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验收成一个网页，能看实时引脚、跑交互模拟、读固件和实验记录。README 写明目前是 32 个动手实验，徽章写界面有 11 种语言，含从右到左。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：722
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：289
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手。唤醒词或旋钮都能开口，识别、对话和合成可以分别指向任何兼容 OpenAI 的服务，并边生成边朗读。话题含 llm，完整条目放在这里。
  - 领域：嵌入式 Embedded
  - 总 star：262
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32-S3 上做语音终端。README 写明板子负责听和说，电脑上的后端决定这句话交给 Grok，还是在本机放歌、暂停和调音量；刷过补丁固件的小米智能音箱 Pro 也能接进来。话题含 grok，没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：259
- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming)
  - 说明：给编程代理一套 STM32 技能。README 写明按标准库或 HAL、裸机或 FreeRTOS 四条轨生成工程，带引脚表和烧录说明，再用静态检查看时钟是否先开、中断里有没有阻塞。检索描述列出 CAN、Modbus、BMS、FOC。仓库本身是嵌入式开发技能，所以完整条目放在这里。描述里的 BMS 让它出现在电力电子检索里，FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。这是代码生成技能，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：39

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。搜索描述写明是在设备上操作 App 和网页。话题含 llm。
  - 领域：AI
  - 总 star：7904
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4757。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵。代理已经能写出影片、演示和游戏的声音，却听不出按键廉价、撞击晚了 80 毫秒或配乐鼓错了地方。README 写明它把声音变成代理可以判断的证据，并且只在 CPU 上跑，也能让代理自己写声音再听一遍改。话题含 ai-agents。
  - 领域：AI
  - 总 star：4369
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上投毒、资源耗尽和幻觉，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。README 写明这是针对这类逆向代理的防御工具。
  - 领域：AI
  - 总 star：4346
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：262。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 做直流泵 PWM 的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

### 电力电子电源 Power Supply

本日没有以电力电子电源为最贴近领域的完整新项目。描述里带 BMS 的 STM32 代理技能，完整说明写在上方「嵌入式 Embedded」。

- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS，此处不展开。领域：电力电子电源 Power Supply。总 star：39。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室 2026 年 RoboMaster 哨兵的定位栈。README 写明它跑在 Ubuntu 22.04 和 ROS 2 Humble 上，用激光和惯性做里程计、点云建图、先验地图定位、回环和重定位，也可以接入 UWB；实机和 rosbag 回放走同一套入口。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：124
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用非均匀 B 样条做多传感器里程计的状态估计。同一套框架覆盖激光惯性、激光视觉惯性、激光加腿部惯性，以及再加视觉的组合，并可做全局样条修正。README 写明这些组合都能实时跑，支持 ROS 2 Humble 和 Jazzy。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：56
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵用 MOSFET 做 PWM；固件里有通断、P 和 PI，并带溢流、干转和传感器保护。README 写明实验台是 15 升罐、0.5 马力级 230 伏泵和 Fotek SSR-40DA，并有一次真机测量记录，另有按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 3`，每页 5 条，本页是各查询按总 star 排序后的第 11 到第 15 条。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件源码。根目录文件名是 `ReadMe.md`，正文主要是官网、升级、用户文档和贡献入口，没有另列功能清单。话题含 stm32 与 firmware，也有 infrared、nfc、rfid、subghz。
  - 领域：嵌入式 Embedded
  - 总 star：16861
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13031。
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用一份配置文件描述 ESP32、ESP8266、BK72xx 和 RP2040，再远程接到家庭自动化系统。README 几乎只有项目标识和文档链接，这段说明用的是搜索描述。话题含 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：12080
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给开源硬件小智 ESP32 配后端，让人自己搭一台设备控制服务器。README 写明按小智通信协议，用 Python、Java 和 Vue 实现，支持 MQTT+UDP、WebSocket、MCP 接入点、声纹识别和知识库。话题是 mcp-server，不是 AI 关键词；搜索描述和话题都没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：11224
- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：人在房间里走动会改变 Wi-Fi 怎么传播，这块固件读这些变化，把一块 ESP32 变成不靠摄像头、麦克风或雷达的本地动作传感器。README 写明还带可嵌入的 C++ SDK、MicroPython、浏览器工具和命令行。话题含 embedded；话题里的 `esp-32` 按词边界不等于 esp32，计入靠的是描述里的 ESP32。
  - 领域：嵌入式 Embedded
  - 总 star：9790
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：714。

### AI

- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
  - 说明：给编程代理一套审美技能，用美术方向、参考图和浏览器检查来挡住千篇一律的页面。话题含 ai-agents。
  - 领域：AI
  - 总 star：112518
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
  - 说明：让编程代理自己去读和搜它本来打不开的网站，一条命令覆盖 X、Reddit、YouTube、GitHub、Bilibili 和小红书。搜索描述写明不收 API 费用。话题 `llm-tools` 按词边界计入 llm。
  - 领域：AI
  - 总 star：110612
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：把 Gemini 放进终端的开源代理。README 写明个人免费额度和 Google AI Pro/Ultra 已于 2026-06-18 转到 Antigravity CLI，这个仓库现在面向 Gemini Code Assist 的标准版和企业版。话题含 ai-agents。
  - 领域：AI
  - 总 star：108748
- [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
  - 说明：跟着一本书把一个类似 GPT 的模型从零写出来，覆盖预训练和微调，也是该书的官方代码。这是书配套仓库，不是公开课清单。话题含 llm 与 pytorch，描述里的 LLM 是强特征词。
  - 领域：AI
  - 总 star：108108
- [pypose/pypose](https://github.com/pypose/pypose) — 见下方「自动控制 Control」完整条目。话题含 pytorch，此处不展开。领域：AI。总 star：1621。

### 功率器件 Power Devices

本页没有留下功率器件仓库。脚本按词边界留下的两条，分别是教材里的 SIC/XE 教学计算机和名为 sic 的链接聚合站，都与碳化硅器件无关，见数据源状态。

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：用 YAML 把阳光电源逆变器接进 Home Assistant。搜索描述列出 SH*RT（如 SH10RT）、SHx.RS（如 SH3.RS）、SH*K（如 SH4K6）和 SxT（如 S20T）。README 写明一个正式集成正在 `proper-ha-integration` 分支上做，目标是 2026 年 12 月，现有 YAML 包会继续维护到那个集成补齐。话题含 inverter。逆变器接入比 Modbus 话题更贴近本领域，嵌入式一节一行带过。
  - 领域：电力电子电源 Power Supply
  - 总 star：714

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：自己做的开源扫地机器人，用树莓派、3D 打印、Home Assistant、Arduino、ROS 2 和一块便宜的二维激光雷达在本地建图导航，常规功能不依赖云。README 写明现在还不能按物料单装出来，今天只能跑仿真；第一版物料在真机上核对之后才会给组装说明。话题含 ros2、slam 与 esp32。扫地定位比这块 ESP32 更贴近本领域，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：13031
- [ShisatoYano/AutonomousVehicleControlBeginnersGuide](https://github.com/ShisatoYano/AutonomousVehicleControlBeginnersGuide)
  - 说明：用 Python 仿真把自动驾驶拆开建。定位、建图、规划、跟踪、感知和控制可以在同一套系统里替换比较，旁边有一本开放教材。话题含 slam 与 kalman-filter，也有 textbook 和 education。这是可运行的仿真加教材，不是公开课清单，正文保留。
  - 领域：自动控制 Control
  - 总 star：1938
- [google-deepmind/mujoco_mpc](https://github.com/google-deepmind/mujoco_mpc)
  - 说明：在 MuJoCo 里做实时预测控制，用来编写和求解机器人任务。README 写明基于打靶的规划器包括 iLQG、梯度下降，以及不依赖导数的 Predictive Sampling。话题含 mpc 与 motor-control。
  - 领域：自动控制 Control
  - 总 star：1761
- [pypose/pypose](https://github.com/pypose/pypose)
  - 说明：在流形上做可微分机器人学。README 写它基于 PyTorch，把深度感知模型和基于物理的优化放在一个库里。话题含 slam、kalman-filter 与 pytorch。定位和滤波比 PyTorch 依赖更贴近本领域，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：1621

## 数据源状态

11 次逻辑请求里，10 次第一次就是 HTTP 200。功率器件常青第一次被脚本判定为限流（HTTP 403 或 429；脚本不保存第一次的状态码），等待 30 秒后重试，最终 HTTP 200。因此实际 HTTP 是 12 次。其余相邻请求按脚本间隔 7 秒。无一次最终失败。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面；这个数字随每分钟窗口回升，中间出现过从 8 回到 9，不是失败。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README：`ZhuLinsen/daily_stock_analysis`、`onehumanbeing/esp32-iphone-agent`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`raullenchai/esp32-thinks`、`Liu-zhongxian/zongzhu-bot`、`wdcjx/Embedded-programming`、`wangzan101/Mika`、`Leonxlnx/earshot`、`qybaihe/bla`、`Samarth030312/arduino-water-level-control-lab`、`profesor003-fundesteam/SIC-2026`、`mozihe/z-localization`、`woolimi/robotics-roadmap`、`ASIG-X/RESPLE2`、`makerspet/oomwoo`、`esphome/esphome`、`xinnan-tech/xiaozhi-esp32-server`、`francescopace/espectre`、`Leonxlnx/taste-skill`、`Panniantong/Agent-Reach`、`google-gemini/gemini-cli`、`rasbt/LLMs-from-scratch`、`jurem/SicTools`、`epilys/sic`、`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`、`google-deepmind/mujoco_mpc`、`pypose/pypose`，以上 `HEAD/README.md` 均 HTTP 200。`flipperdevices/flipperzero-firmware` 的 `HEAD/README.md` 返回 404，默认分支是 `dev`，根目录文件名是 `ReadMe.md`；随后 `dev/ReadMe.md` 为 HTTP 200。仓库元数据接口也是 HTTP 200，返回的总 star 16861 与搜索一致。这 31 次 README 与 1 次仓库元数据不计入上面 11 次搜索配额。`esp32-iphone-agent` 与 `esp32-thinks` 的说明没有超出搜索描述，README 只用来核对。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 11 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。正文为 `ZhuLinsen/daily_stock_analysis`（总 star 68799，24 小时新增 star 505，描述含 LLM）。
- 核对：脚本解析出 11 条后，另一次 GET 同一 URL 仍是 HTTP 200，页面上有 11 个 `article.Box-row`、11 处 “stars today”。这次核对不计入 11 次配额。今日页面本身只有 11 条，不是解析漏条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`sherlock-project/sherlock`（106940，4294）、`meta/astryx`（19902，3324；描述是 agent ready，不等于 `ai-agents`）、`milind-soni/OpenMausBot`（19626，1589；Grok Bot，名称和描述没有 llm）、`anthropics/skills`（190901，1052；描述是 Agent Skills，不等于 `ai-agents`）、`vercel-labs/agent-browser`（48432，914；描述是 “Browser automation CLI for AI agents”，空格写法不等于 `ai-agents`）、`google-deepmind/mujoco`（16888，579；物理仿真，名称和描述没有控制关键词。这与常青里的 `mujoco_mpc` 不是同一个仓库）、`anthropics/claude-quickstarts`（19990，560；入门示例合集，名称和描述没有领域词）、`ruvnet/RuView`（103414，245；Wi-Fi 感知，页面没有 topics，名称和描述没有强特征词）、`garrytan/gbrain`（32118，215；OpenClaw/Hermes Agent Brain，名称和描述没有 llm）、`homeassistant-ai/ha-mcp`（5927，31；名称里的 mcp 不是本次 AI 关键词，描述也没有 llm）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-11 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-11 stars:>2`。`total_count=444`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 9。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4757）、`agharsallah/esp-labs-web`（722）、`ngxson/esp32-usb-to-airprint`（289）、`raullenchai/esp32-thinks`（262）、`Liu-zhongxian/zongzhu-bot`（259）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。`esp32-usb-to-airprint` 只有名称和描述里的 esp32，接口 `created_at` 为 `2026-10-26T16:18:54Z`，北京时间是 2026-10-27 00:18。另有 1 条完整条目来自电力电子检索：`wdcjx/Embedded-programming`（39），因为 STM32 技能比描述里的 BMS 更贴近本领域。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-11 stars:>2`。`total_count=2447`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `wangzan101/Mika`（7904）、`Leonxlnx/earshot`（4369）、`qybaihe/bla`（4346）。这 3 条是本页星数连续的前 3。另有 2 条跨领域一行：`esp32-iphone-agent`（4757）、`esp32-thinks`（262），来自嵌入式检索。这两条话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`benjitaylor/skills`（总 star 2893；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）、`DenisSergeevitch/ex-ussr-kinship-research`（总 star 2274；描述是 “skill for AI agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-11 stars:>2`。`total_count=7`，返回 5，规则保留 2，未命中 3。剩余配额 9。`per_page=5`，第 6、第 7 条不在本次返回里，正文不猜测它们是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `profesor003-fundesteam/SIC-2026`（总 star 3）：名称和描述含 SIC。README 标题写明这是 Samsung Innovation Campus 2026 的数据分析与人工智能课堂材料，含笔记本和数据集，讲师是 Danny Jose Delgado De Sousa，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-18T15:03:12Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。它是本页返回里星数最高的一条。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（3；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`Arafat-shuvo/Sicip-data-sciebce`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3；`First-Sick` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-11 stars:>2`。`total_count=60`，返回 5，规则保留 1，未命中 4。剩余配额 9。规则保留的 1 条更贴近嵌入式，本节只留一行，因此没有以本领域为最贴近领域的完整新项目。
  - `wdcjx/Embedded-programming`（总 star 39）：描述列出 CAN/Modbus/BMS/FOC。话题含 embedded、stm32、freertos。完整条目在嵌入式，本节一行带过。描述里的 FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。它是本页 5 条里星数最低的一条。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`seuclkzsd/hsolve`（77；电磁仿真特征值求解）、`Lida-V/3DCharaMakeSkills-Lida`（62）、`leftamber/grid-dca-bot`（49；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-11 stars:>2`。`total_count=74`，返回 5，规则保留 3，未命中 2。剩余配额 7。正文保留 `mozihe/z-localization`（124）、`ASIG-X/RESPLE2`（56）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`FrankyRenderer` 与 `SampQOL-OS` 夹在 `z-localization` 和 `RESPLE2` 之间，所以剔除后本页按总 star 不是连续的 2 个命中仓库。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 96）。话题含 `ros2` 与 `slam`。README 徽章写 57 讲、120 小时，正文是自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。它排在 `FrankyRenderer` 与 `SampQOL-OS` 之间。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 97；描述里的 MPC-BE 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 88；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-03 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-03 stars:>3`。`total_count=1282`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 9。`page=3`、`per_page=5`，本页是总结果里的第 11 到第 15 条。本查询正文：`flipperdevices/flipperzero-firmware`（16861）、`makerspet/oomwoo`（13031，一行，完整条目在自动控制）、`esphome/esphome`（12080）、`xinnan-tech/xiaozhi-esp32-server`（11224）、`francescopace/espectre`（9790）。另有 1 条一行来自电力电子：`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（714，话题含 modbus），它不在嵌入式本页前 5。`xiaozhi-esp32-server` 话题含 `mcp-server`，不是 AI 关键词，不跨节。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-03 stars:>3`。`total_count=9091`，返回 5，规则保留 4，排除清单 0，未命中 1。剩余配额 8。正文保留 `Leonxlnx/taste-skill`（112518）、`Panniantong/Agent-Reach`（110612）、`google-gemini/gemini-cli`（108748）、`rasbt/LLMs-from-scratch`（108108）。这 4 条是本页星数连续的前 4，第 5 条未命中。另有 1 条一行来自自动控制：`pypose/pypose`（1621，话题含 pytorch），它不在 AI 常青本页前 5。`esp32-iphone-agent` 与 `esp32-thinks` 话题含 `llm`，但不在 AI 常青本页前 5，不从常青跨节；它们的一行在新项目里。
  - 未命中：`pbakaus/impeccable`（总 star 106866）。描述是 “coding agent” 和 “AI slop”，空格和弱词都不等于 `ai-agents` 或 llm。名称和 topics 都没有领域关键词。
- 功率器件：成功，但是限流后重试才成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-03 stars:>3`。第一次请求被脚本判定为 403 或 429，等待 30 秒重试后 HTTP 200。`total_count=30`，返回 5，规则保留 2，未命中 3。剩余配额 8。`page=3` 是总结果里的第 11 到第 15 条。规则保留的 2 条经人工剔除后，本页没有功率器件正文。
  - `jurem/SicTools`（总 star 57）：描述含 SIC。README 写明这是 Leland Beck《System Software》里 SIC/XE 假设计算机的汇编器、仿真器和链接器，与碳化硅器件无关，正文不收。
  - `epilys/sic`（总 star 27）：名称是 sic。README 写明这是按标签聚合的链接站，公开实例在 sic.pm，与碳化硅器件无关，正文不收。
  - 名称词边界未命中：`iChocko/Datos-Viales-SICT`（24；墨西哥联邦公路流量，`SICT` 不等于 `sic`）、`vfat-io/sickle-public`（19；`sickle` 不等于 `sic`）、`mira-x/SicMu`（19；安卓音乐播放器分支，`SicMu` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-03 stars:>3`。`total_count=374`，返回 5，规则保留 1，未命中 4。剩余配额 8。`page=3` 是总结果里的第 11 到第 15 条。正文保留 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（714）。它排在 `decred/dcrd` 与 `hackthedev/dcts-shipping` 之间，所以本页按总 star 不是从第 11 名连续数下来的唯一命中，前面两条未命中。
  - 名称和 topics 未命中：`postgrespro/rum`（849；倒排索引，`inverted` 不等于 `inverter`）、`decred/dcrd`（777；名称里的 dcrd 不等于 `dc-dc`）、`hackthedev/dcts-shipping`（641；名称里的 dcts 不等于 `dc-dc`）、`AAFOptimus/AAFFamilyDCHAudio`（581；声卡驱动，名称里的 DCH 不等于 `dc-dc`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-03 stars:>3`。`total_count=222`，返回 5，规则保留 3，清单类排除 1，未命中 1。剩余配额 7。正文保留 `ShisatoYano/AutonomousVehicleControlBeginnersGuide`（1938）、`google-deepmind/mujoco_mpc`（1761）、`pypose/pypose`（1621）。另有 1 条完整条目来自嵌入式检索：`makerspet/oomwoo`（13031），因为 ROS 2 / SLAM 扫地比 ESP32 话题更贴近本领域；它不在自动控制本页返回的 5 条里。`awesome-NeRF-and-3DGS-SLAM` 排在本页第 1，`cuVSLAM` 夹在入门指南和 `mujoco_mpc` 之间，所以本页按总 star 不是连续的 3 个命中仓库。
  - 清单类剔除：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2161）。名称命中 awesome，话题含 slam，描述是论文合集，不进正文。
  - 名称和 topics 未命中：`nvidia-isaac/cuVSLAM`（总 star 1901）。名称 `cuVSLAM` 按词边界不等于 `slam`。描述里的 “SLAM” 不是强特征词，话题也没有 slam，正文不收。
