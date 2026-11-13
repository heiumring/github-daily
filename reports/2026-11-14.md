# GitHub 领域日报 · 2026-11-14

生成时间：2026-11-14 07:39（北京时间）。数据拉取开始于 2026-11-14 07:32:37（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-15（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-07 及之后有推送、总 star > 3。轮换页 `page = (当年第 318 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) 把 A 股、港股、美股、日股、韩股和台股的自选股收成一份决策看板，定时推到企业微信、飞书、Telegram、Discord、Slack 或邮箱；总 star 71562，24 小时新增 star 272。这是今日热度里新增最多的领域命中。
2. [alibaba/open-code-review](https://github.com/alibaba/open-code-review) 读 Git 改动，用可配置的语言模型代理写出精确到行的审查意见，并配有不依赖模型的检查流水线；总 star 50574，24 小时新增 star 206。
3. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 8520，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 12 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 2 条，都在 AI。

### AI

- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
  - 说明：给自选股做每日分析，把多源行情和新闻收成决策看板再推送出去。README 写明覆盖 A 股、港股、美股、日股、韩股和台股，推送通道包括企业微信、飞书、Telegram、Discord、Slack 和邮箱，也可以用 GitHub Actions 零成本定时跑。页面描述以「LLM 驱动」开头，并有 “LLM-powered”，按强特征词计入 AI。
  - 领域：AI
  - 总 star：71562
  - 24 小时新增 star：272
- [alibaba/open-code-review](https://github.com/alibaba/open-code-review)
  - 说明：做代码审查，而不是再包一个通用编程代理。README 写明它读 Git diff，把改动文件交给带工具的语言模型代理，能读全文、搜代码库、看其他改动文件，并给出精确到行的意见；`ocr scan` 也可以在没有有意义 diff 时审整份文件。页面描述里的 “LLM Agent” 按强特征词计入 AI。
  - 领域：AI
  - 总 star：50574
  - 24 小时新增 star：206

嵌入式、功率器件、电力电子电源、自动控制在这 12 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 的实验台收成一个网页。能看实时引脚、在浏览器里跑交互模拟、逐行读固件，并记实验日志。README 写明目前是 32 个动手实验，还有一块可点亮零件的 3D 板。搜索描述写 11 种语言；README 徽章写 12 languages，正文列出英语、法语、西班牙语、意大利语、德语、波兰语、土耳其语、简体中文、繁体中文、日语、阿拉伯语和波斯语，后两种整页从右到左。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：851
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：303
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32-S3 上做语音终端。板子负责听和说，电脑上的后端决定这句话交给 Grok，还是在本机放歌、暂停和调音量；刷过补丁固件的小米智能音箱 Pro 也能接进来。README 写明这是社区项目，不是小智、Grok 或 xAI 的官方产品。话题含 grok，没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：265
- [andrisgauracs/whistle-esp32](https://github.com/andrisgauracs/whistle-esp32)
  - 说明：把开源语音模型 Whistle 做成一块 ESP32-S3 上的独立实现。按住按键说一句把灯闪成某种颜色，识别在板子上完成，不走网络。README 写明七种语言同时在板子上，模型约 14.5 MB，需要 16 MB 闪存和 8 MB 八线 PSRAM，并用 C99 对照官方引擎逐张量核对过。
  - 领域：嵌入式 Embedded
  - 总 star：231
- [Syfyivan/douli-esp32](https://github.com/Syfyivan/douli-esp32)
  - 说明：一只放在身边的实体电子宠物。喊「你好豆梨」，微雪 ESP32-S3 音频板负责唤醒、收音和播放，说到一半可以打断；电脑或支持的 Android 手机跑配套后台，调用使用者自己配置的模型，并把聊天和记忆存在本地。README 写明本仓库不包含自研基础大模型。搜索描述和话题都没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：200
- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming)
  - 说明：给编程代理一套 STM32 技能。README 写明按标准库或 HAL、裸机或 FreeRTOS 四条轨生成工程，带引脚表和烧录说明。检索描述列出 CAN、Modbus、BMS、FOC，以及 85 条实测坑和 29 份领域文档。仓库本身是嵌入式开发技能，所以完整条目放在这里。描述里的 BMS 让它出现在电力电子检索里，FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。这是代码生成技能，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：41

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 写明没有 Mika 自己的服务器，模型用自己的 API 密钥，或登录 ChatGPT、xAI、OpenRouter；安装包要求 Android 11 及以上。话题含 llm。
  - 领域：AI
  - 总 star：8520
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上投毒、资源耗尽和幻觉，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。README 写明只给软件作者保护自己的发布物，并在 14 个对照目标上验证过。
  - 领域：AI
  - 总 star：5560
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵。代理已经能写出影片、演示和游戏的声音，却听不出按键廉价、撞击晚了 80 毫秒或配乐鼓错了地方。README 写明它把声音变成代理可以判断的证据，并且只在 CPU 上跑，也能让代理自己写声音再听一遍改。话题含 ai-agents。创建日是 2026-10-15，正好落在本次 30 天窗口的边界上。
  - 领域：AI
  - 总 star：4753
- [expo/exact](https://github.com/expo/exact)
  - 说明：应用只写一份，就在网页、macOS、iOS 和 Linux 上以原生方式跑；编程代理可以在这些平台上构建、运行、看见并测试它。话题含 ai-agents。创建于 2026-11-02。
  - 领域：AI
  - 总 star：3989

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 做直流泵 PWM 的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

### 电力电子电源 Power Supply

- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS，此处不展开。领域：电力电子电源 Power Supply。总 star：41。
- [invisiblelevel/canifol](https://github.com/invisiblelevel/canifol)
  - 说明：给修电路的人一套工具。计算器覆盖电阻、电容、电感，其中 BMS 一节算均衡电阻、串并联电池组、电流分流器和 MOSFET 保护，旁边还有数据手册、引脚图、SMD 代码和 BoardView。README 徽章是 1.5.2，写明知识库有 6000 多个笔记本、显卡和游戏机图纸，超过 10 GB，SMD 代码库有 270974 条，安装包覆盖 Windows、Android 和 Linux。搜索描述里的 BMS 是强特征词，所以归入本领域。
  - 领域：电力电子电源 Power Supply
  - 总 star：26

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室 2026 年 RoboMaster 哨兵的定位栈。README 写明它跑在 Ubuntu 22.04 和 ROS 2 Humble 上，用激光和惯性做里程计、点云建图、先验地图定位、回环和重定位，也可以接入 UWB；实机和 rosbag 回放走同一套入口。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：125
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵用 MOSFET 做 PWM；固件里有通断、P 和 PI，并带溢流、干转和传感器保护。README 写明实验台是 15 升罐，水来自 500 升水箱，用 0.5 马力级 230 伏泵和 Fotek SSR-40DA，并有按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 3`，每页 5 条，本页是各查询按总 star 排序后的第 11 到第 15 条。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件源码。README 把用户文档、开发文档和贡献入口列在一起，话题含 stm32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：16888
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用一份配置文件描述 ESP32、ESP8266、BK72xx 和 RP2040 要做什么，再从家庭自动化系统远程控制它们。话题含 esp32，描述里的 ESP32 也是强特征词。
  - 领域：嵌入式 Embedded
  - 总 star：12099
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给小智 ESP32 语音硬件配的后端，用来尽快搭起设备控制服务器。README 写明支持 MQTT+UDP、WebSocket、声纹识别和知识库。话题含 mcp-server，裸 mcp 不是本报告的 AI 关键词，搜索描述也没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：11281
- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：把一块 ESP32 变成只在本地工作的 Wi-Fi 动作传感器。人走过房间会改变信号传播，它读信道状态并报出动作，不用摄像头、麦克风或专用雷达。README 写明固件可以走独立、ESPHome、Matter 或 MicroPython，支持 ESP32-C6、C5、C3、S3、S2 和经典 ESP32。话题是 `esp-32`，不等于 `esp32`；描述里的 ESP32 才计入，话题另有 embedded。
  - 领域：嵌入式 Embedded
  - 总 star：9815
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13093。
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：715。

### AI

- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
  - 说明：给编程代理一套做网页的审美。让它按业务类型定美术方向、用参考图，并用浏览器检查，避免交出千篇一律的页面。README 写明用 Node 22 和本机的 Chrome、Edge 或 Chromium 跑检查，不需要 API 密钥。话题含 ai-agents。
  - 领域：AI
  - 总 star：115024
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
  - 说明：让编程代理读到它自己搜不到的网站。一条命令可以查 B 站、小红书、X、YouTube、Reddit、雪球和 GitHub 的帖子或字幕。README 写明要登录的平台用它自己的浏览器，第一次会复制 Chrome 里该站的登录，不读密码库。话题 `llm-tools` 按词边界计入 llm。
  - 领域：AI
  - 总 star：111568
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：给已购买 Gemini Code Assist 标准版、企业版或 GitHub 上 Code Assist 的组织用的终端编程代理。README 写明 2026-06-18 起，个人免费和 Google AI Pro、Ultra 改走 Antigravity CLI，本仓库也不针对 Gemini 4 系列调优。话题含 ai-agents。
  - 领域：AI
  - 总 star：108819
- [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
  - 说明：一本讲语言模型怎么搭出来的书的官方代码。用 PyTorch 从零做预训练和微调，一步一步得到一个小型 GPT。话题含 llm 与 pytorch，描述里的 LLM 也是强特征词。这是书的代码仓库，不是公开课清单。
  - 领域：AI
  - 总 star：108363

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。名称或话题撞上 `sic`、`mosfet` 的返回项，要么是 Commodore 64 的 SID 芯片仿真，要么词边界不等于 `sic`。详见数据源状态。

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：在 Home Assistant 里读阳光电源逆变器。搜索描述覆盖 SH*RT、SHx.RS、SH*K 和 SxT 系列。README 在 2026-11-07 写明，用来替换这套 YAML 的正式集成正在 `proper-ha-integration` 分支上做，目标是 2026 年 12 月，并会保留实体 ID；在那之前这套 YAML 继续维护。话题含 inverter。Modbus 让它也命中嵌入式，逆变器集成比总线话题更贴近本领域，嵌入式一节一行带过。
  - 领域：电力电子电源 Power Supply
  - 总 star：715

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：一台自己组装的家用扫地机器人，用二维激光雷达建图，并靠 ROS 2 / Nav2 自己导航，常规功能不走云。README 写明现在还不能按物料单组装，今天只能跑仿真，物料在真机上核对之后才会给出组装说明。话题含 ros2、slam 与 esp32。扫地和导航比板上的 ESP32 更贴近本领域，嵌入式一节一行带过。它的总 star 高于本页控制检索的第 11 条，所以没有出现在控制查询的这一页，数字来自嵌入式常青检索。
  - 领域：自动控制 Control
  - 总 star：13093
- [ROBOTIS-GIT/turtlebot3](https://github.com/ROBOTIS-GIT/turtlebot3)
  - 说明：ROBOTIS TurtleBot3 小型移动机器人的 ROS 软件包。README 把同系列的仿真、机械臂和应用仓库列在一起，并指向官方手册。话题含 slam。
  - 领域：自动控制 Control
  - 总 star：2105
- [ShisatoYano/AutonomousVehicleControlBeginnersGuide](https://github.com/ShisatoYano/AutonomousVehicleControlBeginnersGuide)
  - 说明：用可以替换的 Python 仿真学自动驾驶。定位、建图、规划和跟踪放在同一套系统里比较，每个算法都能单独跑出动画。话题含 slam 与 kalman-filter。它是开源教材加示例代码，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：1942

## 数据源状态

11 次逻辑请求里，10 次最终成功，1 次失败。嵌入式新项目在脚本里第一次和 30 秒重试都失败，最终 HTTP 403，`X-RateLimit-Remaining` 为 0，错误是 `API rate limit exceeded`（未认证 IP `3.149.197.192`）。脚本不保存第一次状态码。电力电子新项目、自动控制常青也各遇到一次限流，等 30 秒重试后 HTTP 200。其余 8 次第一次即 HTTP 200。脚本实际 HTTP 14 次，逻辑请求 11 次。窗口过后补拉嵌入式新项目，HTTP 200，正文用这次补拉。另一次 Trending 核对不计入配额。相邻逻辑请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面；这个数字随每分钟窗口回升，控制新项目之后剩 1，控制常青重试成功后回到 9，不是失败。成功的搜索里 `incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取里，下列仓库的 `HEAD/README.md` 为 HTTP 200：`ZhuLinsen/daily_stock_analysis`、`alibaba/open-code-review`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Liu-zhongxian/zongzhu-bot`、`andrisgauracs/whistle-esp32`、`Syfyivan/douli-esp32`、`wdcjx/Embedded-programming`、`makerspet/oomwoo`、`esphome/esphome`、`xinnan-tech/xiaozhi-esp32-server`、`francescopace/espectre`、`wangzan101/Mika`、`qybaihe/bla`、`Leonxlnx/earshot`、`expo/exact`、`Leonxlnx/taste-skill`、`Panniantong/Agent-Reach`、`google-gemini/gemini-cli`、`rasbt/LLMs-from-scratch`、`Samarth030312/arduino-water-level-control-lab`、`profesor003-fundesteam/SIC-2026`、`libsidplayfp/libresidfp`、`invisiblelevel/canifol`、`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`、`mozihe/z-localization`、`woolimi/robotics-roadmap`、`ROBOTIS-GIT/turtlebot3`、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`、`Vincentqyw/cv-arxiv-daily`、`inmusic-software/mpc-plugin-builder-sdk`。`flipperdevices/flipperzero-firmware` 的 `HEAD/README.md` 和 `readme.md` 为 404，文件名是 `ReadMe.md`，该地址 HTTP 200。`esphome/esphome` 的说明没有超出搜索描述，README 只用来核对。这 32 个仓库的 README 请求、1 次嵌入式新项目补拉和下面 1 次 Trending 核对，不计入上面 11 次配额。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 12 条，规则命中 2 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 核对：脚本解析出 12 条后，另一次 GET 同一 URL 仍是 HTTP 200，页面上有 12 个 `article.Box-row`、12 处 “stars today”，仓库名与第一次相同。这次核对不计入 11 次配额。stars today 与第一次一致；部分总 star 多了 1 到 4。正文用第一次解析的数字。今日页面本身只有 12 条，不是解析漏条。
- 命中：`ZhuLinsen/daily_stock_analysis`（71562，272；描述以「LLM 驱动」开头，并有 “LLM-powered”）、`alibaba/open-code-review`（50574，206；描述含 “LLM Agent”）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`GoogleChrome/modern-web-guidance-src`（4790，1875；描述是 “coding agent”，不等于 `ai-agents`）、`we-promise/sure`（14715，944；个人理财）、`openai/codex-security`（13110，754）、`tailscale/tailcat`（9437，324）、`Likely7/Veyra-NRVideo`（1608，245；视频播放与采集增强）、`ChromeDevTools/chrome-devtools-mcp`（55438，145；名称里的裸 mcp 不是本报告的 AI 关键词）、`backnotprop/plannotator`（10437，100）、`block/buzz`（37291，95）、`louislam/uptime-kuma`（93845，61）、`tradermonty/claude-trading-skills`（4145，60；描述点名 Claude Code，没有 `llm`）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-15 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：脚本内失败，补拉成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-15 stars:>2`。脚本第一次为 403 或 429（不保存第一次状态码），等 30 秒重试后仍是 HTTP 403，剩余配额 0，错误为未认证搜索限流。窗口过后补拉 HTTP 200，`total_count=462`，`incomplete_results=false`，返回 5，规则保留 5，排除清单 0，未命中 0，剩余配额 9。正文用补拉的数字。这 5 条都写入正文：`agharsallah/esp-labs-web`（851）、`ngxson/esp32-usb-to-airprint`（303）、`Liu-zhongxian/zongzhu-bot`（265）、`andrisgauracs/whistle-esp32`（231）、`Syfyivan/douli-esp32`（200）。`zongzhu-bot` 话题含 `grok`，没有 `llm`，不跨到 AI。`whistle-esp32` 与 `douli-esp32` 的搜索描述和话题都没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，是带模拟器的实验台，不是公开课清单，正文保留。另有 1 条完整条目来自电力电子检索：`wdcjx/Embedded-programming`（41），因为 STM32 技能比描述里的 BMS 更贴近本领域。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-15 stars:>2`。HTTP 200。`total_count=2919`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 7。正文保留 `wangzan101/Mika`（8520）、`qybaihe/bla`（5560）、`Leonxlnx/earshot`（4753）、`expo/exact`（3989）。这 4 条是本页星数最高的连续 4 条。`earshot` 的 `created_at` 为 `2026-10-15T06:52:46Z`，落在 `created:>=2026-10-15` 上。
  - 未命中：`benjitaylor/skills`（总 star 3268；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。它排在 `exact` 之后，是返回的第 5 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-15 stars:>2`。HTTP 200。`total_count=6`，返回 5，规则保留 2，未命中 3。剩余配额 7。`per_page=5`，第 6 条不在本次返回里，正文不猜测它是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9），其次是 `SicnuJw`（4），其余 3 条总 star 都是 3。
  - `profesor003-fundesteam/SIC-2026`（总 star 3）：名称和描述含 SIC。README 标题写明这是 Samsung Innovation Campus 2026 的数据分析、数据科学与人工智能课堂材料，含笔记本和数据集，讲师是 Danny Jose Delgado De Sousa，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-18T15:03:12Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（4；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3；`First-Sick` 不等于 `sic`）。
- 电力电子电源：成功，经过一次重试。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-15 stars:>2`。第一次为 403 或 429（脚本不保存第一次状态码），等 30 秒重试后 HTTP 200。`total_count=62`，返回 5，规则保留 2，未命中 3。剩余配额 8。正文保留 `invisiblelevel/canifol`（26）。`wdcjx/Embedded-programming`（41）更贴近嵌入式，本节一行带过。按总 star，本页顺序是 `isometric-cities`、`grid-dca-bot`、`DCore`、`Embedded-programming`、`canifol`。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`Statecraft-Labs/isometric-cities`（67；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`leftamber/grid-dca-bot`（49；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-15 stars:>2`。HTTP 200。`total_count=87`，返回 5，规则保留 3，未命中 2。剩余配额 1。正文保留 `mozihe/z-localization`（125）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`mpc-plugin-builder-sdk`、`FrankyRenderer`、`SampQOL-OS` 与 `robotics-roadmap` 夹在 `z-localization` 之后，剔除 Akai MPC 和课程清单后，本查询自己留下的命中只有 `z-localization`。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 121）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，不是模型预测控制，正文不收。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 101）。话题含 `ros2` 与 `slam`。README 徽章写 57 讲、120 小时，正文是 57 讲自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 118；描述里的 MPC-BE 与 MPC-HC 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 105；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-07 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-07 stars:>3`。HTTP 200。`total_count=1305`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 9。`page=3`、`per_page=5`，本页是总结果里按总 star 排序后的第 11 到第 15 条。本查询正文：`flipperdevices/flipperzero-firmware`（16888）、`esphome/esphome`（12099）、`xinnan-tech/xiaozhi-esp32-server`（11281）、`francescopace/espectre`（9815）。`makerspet/oomwoo`（13093）更贴近自动控制，本节一行带过。另有 1 条一行不在本页前 5：`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（715，话题含 modbus，完整条目在电力电子）。`espectre` 的话题是 `esp-32`，不等于 `esp32`，靠话题 `embedded` 和描述里的 ESP32 计入。`xiaozhi-esp32-server` 话题含 `mcp-server`，不是 AI 关键词。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-07 stars:>3`。HTTP 200。`total_count=9623`，返回 5，规则保留 4，排除清单 0，未命中 1。剩余配额 8。正文保留 `Leonxlnx/taste-skill`（115024）、`Panniantong/Agent-Reach`（111568）、`google-gemini/gemini-cli`（108819）、`rasbt/LLMs-from-scratch`（108363）。按总 star，本页顺序是 taste-skill、Agent-Reach、impeccable、gemini-cli、LLMs-from-scratch。`Agent-Reach` 话题 `llm-tools` 按词边界计入 llm。
  - 未命中：`pbakaus/impeccable`（总 star 109575；描述是 “coding agent”，不等于 `ai-agents`）。它夹在 Agent-Reach 与 gemini-cli 之间。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-07 stars:>3`。HTTP 200。`total_count=26`，返回 5，规则保留 1，排除清单 1，未命中 3。剩余配额 6。`page=3` 是总结果里按总 star 排序后的第 11 到第 15 条。规则保留的 1 条撞名剔除后，本节没有完整条目。本页按总 star 的顺序是 `libresidfp`、`SICTIC-AI`、`docker-sickgear`、`antigravity-awesome-skills`、`SICdb_MEDS`。
  - `libsidplayfp/libresidfp`（总 star 16）：话题含 mosfet。README 写明这是 MOS6581/8580 SID 声音芯片的周期精确仿真，话题里的 mosfet 是芯片模型，不是功率器件，正文不收。
  - 名称词边界未命中：`ducroo/SICTIC-AI`（14；瑞士商业天使俱乐部 SICTIC，`SICTIC` 不等于 `sic`）、`linuxserver/docker-sickgear`（12；空描述，`sickgear` 不等于 `sic`）、`rvandewater/SICdb_MEDS`（6；萨尔茨堡重症监护数据库，`SICdb` 不等于 `sic`）。
  - 清单类剔除：`satnamrsm/https-github.com-sickn33-antigravity-awesome-skills`（总 star 10）。名称含 awesome，脚本已排除。名称里的 sick 也不等于 `sic`，分类本身没有命中。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-07 stars:>3`。HTTP 200。`total_count=381`，返回 5，规则保留 1，未命中 4。剩余配额 7。`page=3` 是总结果里按总 star 排序后的第 11 到第 15 条。本查询正文：`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（715）。按总 star，本页顺序是 `dcmtk`、`rum`、`dcs_liberation`、`Sungrow`、`dcts-shipping`。
  - 名称和 topics 未命中：`DCMTK/dcmtk`（919；DICOM 工具包镜像，名称里的 DC 不等于 `dc-dc`）、`postgrespro/rum`（849；描述是 inverted index，`inverted` 不等于 `inverter`）、`dcs-liberation/dcs_liberation`（802；DCS World 战役，`DCS` 不等于 `dc-dc`）、`hackthedev/dcts-shipping`（644；名称里的 DCTS 不等于 `dc-dc`）。
- 自动控制：成功，经过一次重试。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-07 stars:>3`。第一次为 403 或 429（脚本不保存第一次状态码），等 30 秒重试后 HTTP 200。`total_count=234`，返回 5，规则保留 3，未命中 1，排除清单 1。剩余配额 9。正文保留 `ROBOTIS-GIT/turtlebot3`（2105）、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`（1942）。另有 1 条完整条目来自嵌入式检索：`makerspet/oomwoo`（13093），因为 ROS 2 扫地导航比 ESP32 更贴近本领域；它不在控制查询本页，总 star 更高，应在更靠前的页。按总 star，本页顺序是 `awesome-NeRF-and-3DGS-SLAM`、`turtlebot3`、`AutonomousVehicleControlBeginnersGuide`、`cuVSLAM`、`cv-arxiv-daily`。
  - 清单类剔除：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2164）。名称含 awesome，脚本已排除，不进正文。
  - 清单类剔除：`Vincentqyw/cv-arxiv-daily`（总 star 1519）。话题含 slam。README 标题是按日期更新的计算机视觉论文表，2026-11-11 仍在追加，属每日论文清单，不进正文。脚本的清单规则没有命中这条描述，此处人工剔除。
  - 名称和 topics 未命中：`nvidia-isaac/cuVSLAM`（总 star 1905）。名称 `cuVSLAM` 不等于 `slam`，描述里的 “visual odometry and SLAM” 是空格写法，而 `slam` 也不是强特征描述词。
