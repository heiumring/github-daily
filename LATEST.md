# GitHub 领域日报 · 2026-11-12

生成时间：2026-11-12 07:40（北京时间）。数据拉取开始于 2026-11-12 07:33:00（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-13（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-05 及之后有推送、总 star > 3。轮换页 `page = (当年第 316 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) 把 A 股、港股、美股、日股、韩股和台股的自选股收成一份每日决策看板，并推到企业微信、飞书、Telegram、Discord、Slack 或邮箱；总 star 70176，24 小时新增 star 429。这是今日热度里唯一命中领域的仓库。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 8241，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [expo/exact](https://github.com/expo/exact) 写一次界面，就在网页、macOS、iOS 和 Linux 上以原生方式运行，编程代理可以自己把应用建出来、跑起来、看见并测完；创建于 2026-11-02，总 star 2887，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 10 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

### AI

- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
  - 说明：用大模型看自选股。行情、新闻和基本面收成一份决策看板，给出结论、评分、趋势、买卖点和风险，并按计划推送。README 写明覆盖 A 股、港股、美股、日股、韩股、台股和 ETF，推送渠道包括企业微信、飞书、Telegram、Discord、Slack 和邮箱。描述以 LLM 开头，按强特征词计入 AI。
  - 领域：AI
  - 总 star：70176
  - 24 小时新增 star：429

嵌入式、功率器件、电力电子电源、自动控制在这 10 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 的实验台收成一个网页。能看实时引脚、在浏览器里跑交互模拟、逐行读固件，并记实验日志。README 写明目前是 32 个动手实验，界面有 11 种语言，阿拉伯语整页从右到左。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：818
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：292
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32-S3 上做语音终端。板子负责听和说，电脑上的后端决定这句话交给 Grok，还是在本机放歌、暂停和调音量；刷过补丁固件的小米智能音箱 Pro 也能接进来。README 写明这是社区项目，不是小智、Grok 或 xAI 的官方产品。话题含 grok，没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：261
- [andrisgauracs/whistle-esp32](https://github.com/andrisgauracs/whistle-esp32)
  - 说明：把开源语音模型 Whistle 做成一块 ESP32-S3 上的独立实现。按住按键说一句把灯闪成某种颜色，识别在板子上完成，不走网络。README 写明七种语言同时在板子上，模型约 14.5 MB，需要 16 MB 闪存和 8 MB 八线 PSRAM，并用 C99 对照官方引擎逐张量核对过。
  - 领域：嵌入式 Embedded
  - 总 star：226
- [zuiho-kai/bothouse](https://github.com/zuiho-kai/bothouse) — 见下方「AI」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：211。
- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming)
  - 说明：给编程代理一套 STM32 技能。README 写明按标准库或 HAL、裸机或 FreeRTOS 四条轨生成工程，带引脚表和烧录说明。检索描述列出 CAN、Modbus、BMS、FOC，以及 85 条实测坑和 29 份领域文档。仓库本身是嵌入式开发技能，所以完整条目放在这里。描述里的 BMS 让它出现在电力电子检索里，FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。这是代码生成技能，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：41

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 写明没有 Mika 自己的服务器，模型用自己的 API 密钥，或登录 ChatGPT、xAI、OpenRouter；安装包要求 Android 11 及以上。话题含 llm。
  - 领域：AI
  - 总 star：8241
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上投毒、资源耗尽和幻觉，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。README 写明只给软件作者保护自己的发布物，并在 14 个对照目标上验证过。
  - 领域：AI
  - 总 star：5305
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵。代理已经能写出影片、演示和游戏的声音，却听不出按键廉价、撞击晚了 80 毫秒或配乐鼓错了地方。README 写明它把声音变成代理可以判断的证据，并且只在 CPU 上跑，也能让代理自己写声音再听一遍改。话题含 ai-agents。
  - 领域：AI
  - 总 star：4528
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，就在网页、macOS、iOS 和 Linux 上以原生方式运行。编程代理不只要能生成代码，还要能把应用建出来、跑起来、看见界面并在这些平台上测完。话题含 ai-agents。接口 `created_at` 为 `2026-11-02T01:29:01Z`，北京时间是 2026-11-02 09:29。
  - 领域：AI
  - 总 star：2887
- [zuiho-kai/bothouse](https://github.com/zuiho-kai/bothouse)
  - 说明：把已经登录好的 Claude Code、Codex、Gemini、DeepSeek 等本地代理拉进同一个群，共享一份项目记忆，并自己分活。README 写明入口是 Discord、DSH 和 QQ；ESP32 出现在「下一步」，是给角色配一个小身体，仓库指向另一个项目 bothouse-iot。当前要解决的是多代理协作，所以完整条目放在 AI。话题同时含 ai-agents 与 esp32，嵌入式一节一行带过。它不在 AI 新项目检索的前 5 里，这条来自嵌入式检索。
  - 领域：AI
  - 总 star：211

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 做直流泵 PWM 的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

### 电力电子电源 Power Supply

- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS，此处不展开。领域：电力电子电源 Power Supply。总 star：41。
- [invisiblelevel/canifol](https://github.com/invisiblelevel/canifol)
  - 说明：给修电路的人一套工具。计算器覆盖电阻、电容、电感，其中 BMS 一节算均衡电阻、串并联电池组、电流分流器和 MOSFET 保护，旁边还有数据手册、引脚图、SMD 代码和 BoardView。README 写明 1.5.1 版带 6000 多份笔记本、显卡和游戏机图纸，超过 10 GB，SMD 代码库有 270974 条，安装包覆盖 Windows、Android 和 Linux。搜索描述里的 BMS 是强特征词，所以归入本领域。
  - 领域：电力电子电源 Power Supply
  - 总 star：26

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室 2026 年 RoboMaster 哨兵的定位栈。README 写明它跑在 Ubuntu 22.04 和 ROS 2 Humble 上，用激光和惯性做里程计、点云建图、先验地图定位、回环和重定位，也可以接入 UWB；实机和 rosbag 回放走同一套入口。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：125
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用非均匀 B 样条做多传感器里程计的状态估计。同一套框架覆盖激光惯性、激光视觉惯性、激光加腿部惯性，以及再加视觉的组合，并可做全局样条修正。README 写明这些组合都在实时约束内，支持 ROS 2 Humble 和 Jazzy。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：57
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵用 MOSFET 做 PWM；固件里有通断、P 和 PI，并带溢流、干转和传感器保护。README 写明实验台是 15 升罐，水来自 500 升水箱，用 0.5 马力级 230 伏泵和 Fotek SSR-40DA，并有按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 1`，每页 5 条，本页是各查询按总 star 排序后的第 1 到第 5 条。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：用普通 Wi-Fi 做人在不在、呼吸和心率，不用摄像头。README 写明人一动、一呼吸就会扰动电波，它用低成本 ESP32 采集信道状态信息，隔着墙、在暗处也能给出房间里的状态。话题含 esp32 与 firmware。话题里的 mcp 不是本次 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：104053
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：用纯 C 写游戏和图形小工具的库，依赖都放在仓库里。README 写明它适合原型、工具、图形应用、嵌入式和教育，平台包括 Windows、Linux、macOS、树莓派、Android 和网页。话题含 embedded 与 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：35634
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：跑在 ESP32 上的语音聊天入口。README 写明唤醒后走 Qwen、DeepSeek 这类大模型，用 MCP 控制喇叭、灯和舵机，也能把能力延伸到智能家居和桌面。搜索描述和话题没有 llm，话题里的 mcp 不是本次 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：33077
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：给从小 MCU 到能做 3D 的 MPU 用的嵌入式图形界面库，并带编辑器 LVGL Pro。话题含 embedded、esp32、stm32 与 zephyr。
  - 领域：嵌入式 Embedded
  - 总 star：25145
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：给 ESP8266 和 ESP32 设备换一套本地固件。用网页配置，可 OTA，用定时或规则做自动化，经 MQTT、HTTP、串口或 KNX 控制，不必把设备交给原厂云。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：24983
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13063。

### AI

- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
  - 说明：给代理提供网页上的上下文。README 写明它搜索、抓取并和网页交互，输出干净的 Markdown、结构化 JSON 和截图，可以自己托管，也有托管服务。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：200951
- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：用同一套模型定义做文本、视觉、音频和多模态模型的训练和推理。话题含 llm、pytorch 与 transformer。
  - 领域：AI
  - 总 star：168879
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：在一个工作区里搭代理流程和检索管道，接上模型和工具，部署到云、专有网络或自己的机器，从原型到上线不必换一套栈。话题含 llm。
  - 领域：AI
  - 总 star：160993

### 功率器件 Power Devices

本页没有留下功率器件仓库。星数最高的几条是 SickChill、SickGear 和 siconos 这类词边界撞名；唯一被规则留下的 `foresterre/imagineer` 是命令行图片工具，旧名 sic，与碳化硅器件无关。见数据源状态。

### 电力电子电源 Power Supply

本页没有留下电力电子电源仓库。返回的 5 条里，`inverters` 复数、`dcgm`、`dcm` 都没有按词边界计入；`Finbuckle LLC` 是公司后缀。见数据源状态。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：用 Python 把定位、建图、SLAM、路径规划这些机器人算法写成可运行的示例，并配一本在线教材。这是算法示例加教材，不是公开课清单。话题含 slam。
  - 领域：自动控制 Control
  - 总 star：30896
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：一台自己做的扫地机器人。用树莓派、可打印的外壳、二维激光雷达和 ROS 2 在家里建图并自己走，常规功能不依赖云。README 写明现在还不能按物料单装出来，今天只能在仿真里跑，装机说明要等第一套物料在真机上核对完。话题含 ros2、slam 与 esp32。扫地和定位比板上的 ESP32 更贴近本领域，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：13063
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：开源飞控固件，覆盖竞速、花式、航拍、远航、微型机和固定翼，固件跑在飞控板上。话题含 flight-controller。
  - 领域：自动控制 Control
  - 总 star：11778
- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：同时定位与建图的库，也能单独跑成一个应用，话题覆盖机器人、ROS 2、扫描和移动端。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：4097

## 数据源状态

11 次逻辑请求里，10 次最终成功。嵌入式新项目第一次遇到限流，脚本不保存第一次状态码，等 30 秒重试后 HTTP 200。电力电子常青第一次 HTTP 403，等 30 秒重试仍是 HTTP 403；限额窗口过后另一次补拉 HTTP 200，正文用的是这次补拉。相邻逻辑请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面；这个数字随每分钟窗口回升，中间出现过从 0 回到 9，不是失败。成功的搜索里 `incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 `HEAD/README.md` 中，下列仓库为 HTTP 200：`ZhuLinsen/daily_stock_analysis`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Liu-zhongxian/zongzhu-bot`、`andrisgauracs/whistle-esp32`、`zuiho-kai/bothouse`、`wangzan101/Mika`、`qybaihe/bla`、`Leonxlnx/earshot`、`expo/exact`、`Samarth030312/arduino-water-level-control-lab`、`wdcjx/Embedded-programming`、`invisiblelevel/canifol`、`mozihe/z-localization`、`woolimi/robotics-roadmap`、`ASIG-X/RESPLE2`、`profesor003-fundesteam/SIC-2026`、`foresterre/imagineer`、`ruvnet/RuView`、`78/xiaozhi-esp32`、`makerspet/oomwoo`、`introlab/rtabmap`、`AtsushiSakai/PythonRobotics`、`betaflight/betaflight`、`raysan5/raylib`、`lvgl/lvgl`、`arendst/Tasmota`、`firecrawl/firecrawl`、`huggingface/transformers`、`langgenius/dify`。`Aleksoid1978/MPC-BE` 的 `HEAD/README.md` 为 HTTP 404，排除依据是搜索描述，没有再调用内容接口。这 31 次 README 请求和下面 1 次 Trending 核对，不计入上面 11 次配额。`lvgl`、`transformers`、`dify` 的说明没有超出搜索描述，README 只用来核对。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 10 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 核对：脚本解析出 10 条后，另一次 GET 同一 URL 仍是 HTTP 200，页面上有 10 个 `article.Box-row`、10 处 “stars today”。这次核对不计入 11 次配额。今日页面本身只有 10 条，不是解析漏条。
- 命中：`ZhuLinsen/daily_stock_analysis`（70176，429；描述以 LLM 开头）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`meta/astryx`（24895，2842；描述是 agent ready，不等于 `ai-agents`）、`we-promise/sure`（12918，1079；个人理财）、`addyosmani/agent-skills`（115905，788；描述是 “skills for AI coding agents”，空格写法不等于 `ai-agents`）、`vercel-labs/agent-browser`（49839，712；描述是 “Browser automation CLI for AI agents”，空格写法不等于 `ai-agents`）、`homeassistant-ai/ha-mcp`（7332，640；名称里的 mcp 不是本次 AI 关键词，描述也没有 llm）、`shadcn/improve`（10831，333）、`GoogleChrome/modern-web-guidance-src`（1717，133；描述为空）、`TheAlgorithms/Java`（67001，108）、`openai/codex-security`（11690，20）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-13 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-13 stars:>2`。第一次为 403 或 429（脚本不保存第一次状态码），等 30 秒重试后 HTTP 200。`total_count=459`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 1。这 5 条都写入正文：`agharsallah/esp-labs-web`（818）、`ngxson/esp32-usb-to-airprint`（292）、`Liu-zhongxian/zongzhu-bot`（261）、`andrisgauracs/whistle-esp32`（226）、`zuiho-kai/bothouse`（211）。`bothouse` 同时话题含 `ai-agents`，完整条目在 AI，本节一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。另有 1 条完整条目来自电力电子检索：`wdcjx/Embedded-programming`（41），因为 STM32 技能比描述里的 BMS 更贴近本领域。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-13 stars:>2`。`total_count=2500`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 9。正文保留 `wangzan101/Mika`（8241）、`qybaihe/bla`（5305）、`Leonxlnx/earshot`（4528）、`expo/exact`（2887）。另有 1 条完整条目来自嵌入式检索：`zuiho-kai/bothouse`（211）。它话题含 `ai-agents`，但没有出现在本查询返回的前 5 里。`benjitaylor/skills` 夹在 earshot 和 exact 之间，所以 exact 与前三条在本页按总 star 不是连续的。
  - 未命中：`benjitaylor/skills`（总 star 3099；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-13 stars:>2`。`total_count=7`，返回 5，规则保留 2，未命中 3。剩余配额 9。`per_page=5`，第 6、第 7 条不在本次返回里，正文不猜测它们是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9）；其余 4 条总 star 都是 3。
  - `profesor003-fundesteam/SIC-2026`（总 star 3）：名称和描述含 SIC。README 标题写明这是 Samsung Innovation Campus 2026 的数据分析与人工智能课堂材料，含笔记本和数据集，讲师是 Danny Jose Delgado De Sousa，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-18T15:03:12Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（3；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3；`First-Sick` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-13 stars:>2`。`total_count=56`，返回 5，规则保留 2，未命中 3。剩余配额 7。正文保留 `invisiblelevel/canifol`（26）。`wdcjx/Embedded-programming`（41）更贴近嵌入式，本节一行带过。这两条是本页星数最低的两条，排在三条未命中之后。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`Lida-V/3DCharaMakeSkills-Lida`（62）、`leftamber/grid-dca-bot`（49；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-13 stars:>2`。`total_count=78`，返回 5，规则保留 3，未命中 2。剩余配额 8。正文保留 `mozihe/z-localization`（125）、`ASIG-X/RESPLE2`（57）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`FrankyRenderer` 与 `SampQOL-OS` 夹在 `z-localization` 和 `RESPLE2` 之间，所以剔除后本页按总 star 不是连续的 2 个命中仓库。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 97）。话题含 `ros2` 与 `slam`。README 徽章写 57 讲、120 小时，正文是 57 讲自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。它排在 `FrankyRenderer` 与 `SampQOL-OS` 之间。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 107；描述里的 MPC-BE 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 94；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-05 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-05 stars:>3`。`total_count=1330`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 0。`page=1`、`per_page=5`，本页是总结果里星数最高的 5 条。本查询正文：`ruvnet/RuView`（104053）、`raysan5/raylib`（35634）、`78/xiaozhi-esp32`（33077）、`lvgl/lvgl`（25145）、`arendst/Tasmota`（24983）。另有 1 条一行不在本页前 5：`makerspet/oomwoo`（13063，话题含 esp32，完整条目在自动控制）。`xiaozhi-esp32` 的 README 点名 Qwen 与 DeepSeek，搜索描述和话题没有 llm，话题 mcp 不是 AI 关键词，不跨 AI。`Tasmota` 的 README 写了 Modbus，搜索话题没有 modbus，不跨节。`OpenDTU` 话题含 esp32，但不在本页前 5，不跨节。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-05 stars:>3`。`total_count=9181`，返回 5，规则保留 3，排除清单 0，未命中 2。剩余配额 9。正文保留 `firecrawl/firecrawl`（200951）、`huggingface/transformers`（168879）、`langgenius/dify`（160993）。按总 star，本页顺序是 firecrawl、transformers、agency-agents、dify、langflow。`bothouse` 话题含 `ai-agents`，但不在 AI 常青本页前 5，不从常青跨节；它的完整条目在新项目里。`microsoft/Sico` 话题含 llm，但不在本页前 5，不跨节。
  - 未命中：`msitarzewski/agency-agents`（总 star 167773；名称 `agency-agents` 不等于 `ai-agents`）、`langflow-ai/langflow`（总 star 156549；描述是 “AI-powered agents”，不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-05 stars:>3`。`total_count=25`，返回 5，规则保留 1，未命中 3，另有 1 条只命中 AI。剩余配额 8。`page=1` 是总结果里星数最高的 5 条。规则保留的 1 条经人工剔除后，本页没有功率器件正文。
  - `foresterre/imagineer`（总 star 224）：话题和描述都含 sic，描述写明旧名是 sic。README 写明这是 `image-rs/image` 的命令行前端，sic 原来是 “simple image cli”，与碳化硅器件无关，正文不收。它排在 `microsoft/Sico` 与 `siconos` 之间。
  - 只命中其他领域：`microsoft/Sico`（总 star 284）。描述是企业数字员工平台，话题含 llm。`Sico` 不等于 `sic`。它不在 AI 常青本页前 5，不跨节。
  - 名称词边界未命中：`SickChill/sickchill`（2445；电视自动化，`SickChill` 不等于 `sic`）、`SickGear/SickGear`（799；`SickGear` 不等于 `sic`）、`siconos/siconos`（187；非光滑动力系统仿真，`siconos` 不等于 `sic`）。本页按总 star 的顺序是 sickchill、SickGear、Sico、imagineer、siconos。
- 电力电子电源：脚本内失败，补拉成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-05 stars:>3`。脚本第一次 HTTP 403，错误原文是 `API rate limit exceeded for 18.216.91.147`，`X-RateLimit-Remaining` 为 0；等 30 秒重试仍是 HTTP 403，同一错误。限额窗口过后另一次 GET 为 HTTP 200，`total_count=389`，`incomplete_results=false`，返回 5，剩余配额 4。这次补拉不在脚本的 11 次逻辑请求里，正文用的是这次返回。`page=1` 是总结果里星数最高的 5 条。5 条都没有进入正文。
  - 名称和 topics 未命中：`dalathegreat/Battery-Emulator`（3023；描述是 solar inverters，复数不等于 `inverter`）、`NVIDIA/dcgm-exporter`（1928；`dcgm` 不等于 `dc-dc`）、`dcm4che/dcm4che`（1466；`dcm` 不等于 `dc-dc`）。
  - 只命中其他领域：`tbnobody/OpenDTU`（2208）。描述是 ESP32 与 Hoymiles/TSUN/Solenso Inverters，`Inverters` 复数不等于 `inverter`，话题含 esp32。它不在嵌入式常青本页前 5，不跨节。
  - 人工剔除：`Finbuckle/Finbuckle.MultiTenant`（1634）。描述里的 LLC 是公司后缀，不是谐振变换器，正文不收。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-05 stars:>3`。`total_count=237`，返回 5，规则保留 5，未命中 0。剩余配额 9。正文保留 `AtsushiSakai/PythonRobotics`（30896）、`makerspet/oomwoo`（13063）、`betaflight/betaflight`（11778）、`introlab/rtabmap`（4097）。`MPC-BE` 夹在 betaflight 和 rtabmap 之间，所以本页按总 star 不是连续的 4 个命中仓库。`oomwoo` 话题含 esp32，嵌入式一节一行带过。`betaflight` 的 README 写了 STM32 F4/F7/G4/H5/H7 和实验性 ESP32，搜索话题没有这些词，不跨嵌入式。
  - 人工剔除：`Aleksoid1978/MPC-BE`（总 star 4701）。名称命中 `mpc`。搜索描述写明这是 Windows 上的通用音视频播放器，与模型预测控制无关，正文不收。`HEAD/README.md` 为 HTTP 404，没有用内容接口改写这条判断。
