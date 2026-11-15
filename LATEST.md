# GitHub 领域日报 · 2026-11-16

生成时间：2026-11-16 07:38（北京时间）。数据拉取开始于 2026-11-16 07:33:52（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-17（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-09 及之后有推送、总 star > 3。轮换页 `page = (当年第 320 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [alibaba/open-code-review](https://github.com/alibaba/open-code-review) 读 Git 改动，用可配置的语言模型代理写出精确到行的审查意见，并配有不依赖模型的检查流水线；总 star 52032，24 小时新增 star 688。这是今日热度里唯一的领域命中。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 8717，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [Kristian8606/esp32-airplay2-surround](https://github.com/Kristian8606/esp32-airplay2-surround) 用几块 ESP32-S3 把 Apple TV 的一条 AirPlay 2 输出拆成无线 5.1 / 7.1，每块板只解码并播放自己那一个声道；总 star 233，没有 24 小时新增数据。搜索描述为空，仓库名里的 esp32 让它进入嵌入式。

## A. 今日热度

Trending 页面解析到 12 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条，在 AI。

### AI

- [alibaba/open-code-review](https://github.com/alibaba/open-code-review)
  - 说明：做代码审查，而把通用编程代理留在审查流程外面。页面描述写明它是确定性流水线加语言模型代理的混合架构，能给出精确到行的意见，并内置空指针、线程安全、XSS 和 SQL 注入规则。README 写明它读 Git diff，代理可以读全文、搜代码库、看其他改动文件；`ocr scan` 也可以在没有有意义 diff 时审整份文件。中文 README 写明前身是阿里集团内部审查助手，过去两年服务了数万名开发者，识别了数百万个代码缺陷；基准从 50 个热门仓库里选了 200 个真实 Pull Request、覆盖 10 种语言，由 80 多位资深工程师交叉标注，共 1505 个标注缺陷。同一底层模型下，它相对通用代理的准确率和 F1 更高，token 大约是九分之一，召回率更低。页面描述里的 “LLM Agent” 按强特征词计入 AI。
  - 领域：AI
  - 总 star：52032
  - 24 小时新增 star：688

嵌入式、功率器件、电力电子电源、自动控制在这 12 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 的实验台收成一个网页。README 写明目前是 32 个动手实验，每课先在浏览器里跑，带实时引脚、交互模拟、逐行讲解固件的阅读器，以及一块 3D 板；数据手册部分把芯片手册收成可引用的章节。搜索描述写 11 种语言；README 徽章写 12 languages，含从右到左的阿拉伯语和波斯语，简体中文和繁体中文分开计。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：872
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。表格里 MG2550S 标成已在真机验证，其余型号标成尚未上真机。
  - 领域：嵌入式 Embedded
  - 总 star：318
- [andrisgauracs/whistle-esp32](https://github.com/andrisgauracs/whistle-esp32)
  - 说明：把开源语音模型 Whistle 做成一块 ESP32-S3 上的独立实现。按住按键说一句把灯闪成某种颜色，识别在板子上完成，不走网络。README 写明七种语言同时在板子上，模型约 14.5 MB，需要 16 MB 闪存和 8 MB 八线 PSRAM，并用 C99 对照官方引擎逐张量核对过。搜索描述和话题都没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：235
- [Kristian8606/esp32-airplay2-surround](https://github.com/Kristian8606/esp32-airplay2-surround)
  - 说明：用便宜的板子自己组一套无线环绕声。README 写明 Apple TV 只看到网关这一台 AirPlay 2 音箱，网关把 5.1 / 7.1 码流原样分给最多八块音箱板，每块 ESP32-S3 只解码自己的声道，并用接入点信标里的时钟对齐采样时刻。目前写明网关加两只音箱已经能同步播放一条 7.1 流，功能仍在改；闪存建议买 16 MB 的 N16R8。搜索描述为空，话题也为空，只靠仓库名里的 esp32 归入嵌入式。
  - 领域：嵌入式 Embedded
  - 总 star：233
- [Syfyivan/douli-esp32](https://github.com/Syfyivan/douli-esp32)
  - 说明：一只放在身边的实体电子宠物。喊「你好豆梨」，微雪 ESP32-S3 音频板负责唤醒、收音和播放，说到一半可以打断；电脑或支持的 Android 手机跑配套后台，调用使用者自己配置的模型，并把聊天和记忆存在本地。README 写明本仓库不包含自研基础大模型。搜索描述和话题都没有 llm，不跨到 AI。`created_at` 为 `2026-10-17T13:54:12Z`，落在本次 30 天窗口的边界上。
  - 领域：嵌入式 Embedded
  - 总 star：200

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：8717
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上投毒、资源耗尽和幻觉。README 徽章写 npm 包 `bla-agents` v3.4.1，并写明在 14 个对照目标上验证过，用途限定为作者保护自己的发布物。话题 `llm-security` 按词边界计入 llm。
  - 领域：AI
  - 总 star：5795
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、macOS、iOS 和 Linux 上原生跑，编程代理可以自己建、自己跑、自己看、自己测。README 写明 Android 和 Windows 还在早期，应用能编过并跑起来，缺的部分单独列着。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：4309

### 功率器件 Power Devices

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

本窗口没有以功率器件为最贴近领域的完整新项目。名称撞上 `sic` 的课堂笔记本已剔除。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。

本查询返回的 5 条里，唯一被规则留下的是公司后缀 LLC，已剔除。`dc-dc` 的搜索侧撞名仍在，分类按词边界没有收进正文。详见数据源状态。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室 2026 年 RoboMaster 哨兵的定位栈。README 写明它跑在 Ubuntu 22.04 和 ROS 2 Humble 上，用激光和惯性做里程计、点云建图、先验地图定位、回环和重定位，也可以接入 UWB；实机和 rosbag 回放走同一套入口。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：126
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵用 MOSFET 做 PWM；固件里有通断、P 和 PI，并带溢流、干转和传感器保护。README 写明实验台是 15 升罐，水来自 500 升水箱，用 0.5 马力级 230 伏泵和 Fotek SSR-40DA，并有按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。它不在控制查询本页，数字来自功率器件新项目检索。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 1`，每页 5 条，本页是各查询按总 star 排序后的第 1 到第 5 条。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：用普通 Wi-Fi 做人的存在、呼吸和心率感知，不靠摄像头。README 写明可以接到 Home Assistant，也可以作为 Apple Home、Google Home 和 Alexa 能发现的设备。话题含 esp32 与 firmware，也含 mcp。裸 mcp 不是本报告的 AI 关键词，搜索描述没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：104371
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：用来写游戏和图形程序的 C 库。README 写明它适合做原型、工具、图形应用、嵌入式和教育，接口保持直接写代码，没有可视化设计器。话题含 embedded 与 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：35693
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：板上的语音聊天入口。README 写明默认连接官方服务器，可以用 Qwen、DeepSeek 这类模型做语音对话，并用 MCP 控制音箱、灯和舵机；本次还写明需要 ESP-IDF v6.0.1 或更新，推荐 `release/v6.1`，构建矩阵有 171 个变体。搜索描述和话题没有 llm，话题里的 mcp 不是 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：33265
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：给各种 MCU 和 MPU 做图形界面。README 写明没有外部依赖，一块典型界面大约要 100 kB RAM、200 到 300 kB 闪存，渲染缓冲大约是屏幕的十分之一。话题含 embedded、esp32、stm32 与 zephyr。
  - 领域：嵌入式 Embedded
  - 总 star：25172
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：ESP8266 和 ESP32 的替代固件。搜索描述写明用网页配置、OTA、定时或规则，并通过 MQTT、HTTP、串口或 KNX 做本地控制。README 写明覆盖 ESP32、S2、S3、C2、C3、C5、C6、C61 和 P4。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：24990
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13106。

### AI

- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
  - 说明：给代理搜网页、抓页面，并把结果收成可用的上下文。README 写明它是面向 AI agent 的 context API，有托管服务；仓库按 AGPL-3.0 开源，也可以自托管。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：202052
- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：给文本、视觉、音频、视频和多模态模型放一套统一的模型定义，训练和推理都走这套定义。README 写明 Hub 上有超过 100 万个检查点，并要求 Python 3.11+ 与 PyTorch 2.6+。话题含 llm、pytorch 与 transformer。
  - 领域：AI
  - 总 star：169020
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：搭语言模型应用的平台。README 写明把工作流、检索流水线、代理、模型管理和观测放在同一套界面里，可以从原型走到生产，也能自托管；安装说明写最低 2 核 CPU、4 GiB 内存。话题含 llm。搜索描述里的 RAG 是产品功能，本报告不把裸 rag 当作 AI 关键词。
  - 领域：AI
  - 总 star：161213

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。旧名撞上 `sic` 的图片命令行工具已剔除，其余返回项的词边界不等于 `sic`。详见数据源状态。

### 电力电子电源 Power Supply

本页没有以电力电子电源为最贴近领域的完整条目。公司后缀 LLC 已剔除。`inverters` 的复数、`DC` 和 `dcm` 都没有按 `inverter` 或 `dc-dc` 计入。详见数据源状态。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：用 Python 示例和一本在线教材讲机器人算法。README 目录含扩展卡尔曼滤波、粒子滤波、ICP、FastSLAM 和多种路径规划。话题含 slam。这是算法示例加教材，不是多门课的公开课清单，正文保留。
  - 领域：自动控制 Control
  - 总 star：30922
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：一台可以自己做的扫地机器人。README 写明用树莓派、3D 打印、Home Assistant、Arduino 和 ROS 2，靠二维激光建图和导航，常规功能不依赖云。开头同时写明现在还不能按物料单组装，今天只能跑仿真，物料单要等真机验证之后才给。话题含 ros2 与 slam，也含 esp32。扫地导航比板子更贴近本领域，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：13106
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：穿越机、花飞、航拍、长航时和小翼用的开源飞控固件。README 写明支持 DShot、黑匣子、OSD，以及飞行中改 PID。话题含 flight-controller。
  - 领域：自动控制 Control
  - 总 star：11793
- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：同时提供定位建图的库和可以单独跑的程序。README 把论文和主要更新指向项目主页，把安装和例子指向 wiki，把 ROS 用法指向 ROS wiki。话题含 slam 与 ros2，也含 localization、mapping 与 scanning。
  - 领域：自动控制 Control
  - 总 star：4106

## 数据源状态

11 次逻辑请求全部第一次成功，没有重试。实际 HTTP 11 次。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面；这个数字随每分钟窗口回升，控制新项目之后剩 21，控制常青回到 29，不是失败。成功的搜索里 `incomplete_results` 均为 false。本次通过环境变量 `GH_TOKEN` 使用本机 `gh` 登录令牌，令牌没有写入脚本、报告或提交。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取按 `README.md`、`readme.md`、`ReadMe.md`、`README.rst` 的顺序，命中即停。`Aleksoid1978/MPC-BE` 这四个文件名都是 HTTP 404，按搜索描述剔除。其余仓库的 `README.md` 为 HTTP 200：`alibaba/open-code-review`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`andrisgauracs/whistle-esp32`、`Kristian8606/esp32-airplay2-surround`、`Syfyivan/douli-esp32`、`ruvnet/RuView`、`raysan5/raylib`、`78/xiaozhi-esp32`、`lvgl/lvgl`、`arendst/Tasmota`、`wangzan101/Mika`、`qybaihe/bla`、`expo/exact`、`firecrawl/firecrawl`、`huggingface/transformers`、`langgenius/dify`、`Samarth030312/arduino-water-level-control-lab`、`mozihe/z-localization`、`AtsushiSakai/PythonRobotics`、`makerspet/oomwoo`、`betaflight/betaflight`、`introlab/rtabmap`、`profesor003-fundesteam/SIC-2026`、`foresterre/imagineer`、`darkfibr/artex-forensics`、`Finbuckle/Finbuckle.MultiTenant`、`inmusic-software/mpc-plugin-builder-sdk`、`woolimi/robotics-roadmap`。另读 `alibaba/open-code-review` 的 `docs/i18n/README.zh-CN.md`，HTTP 200。上述 README 读取（含 `MPC-BE` 的 4 次 404）和下面 1 次 Trending 核对，不计入上面 11 次配额。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 12 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 核对：脚本解析出 12 条后，另一次 GET 同一 URL 仍是 HTTP 200，仓库集合相同，stars today 全部不变。8 个仓库的总 star 有增加：`univer` 25585→25586，`ag-ui` 17823→17824，`stitch-skills` 9269→9272，`plannotator` 11814→11815，`open-code-review` 52032→52034，`LoopForge` 1448→1450，`modern-web-guidance-src` 7116→7118，`claude-trading-skills` 5508→5510。`chrome-devtools-mcp`（56889，718）、`ggml`（15896，53）、`Claude-BugHunter`（6390，221）、`SkillEvaluator`（1640，205）两次一致。正文用第一次解析的数字。今日页面本身只有 12 条，不是解析漏条。
- 命中：`alibaba/open-code-review`（52032，688；描述含 “LLM Agent”）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`GoogleChrome/modern-web-guidance-src`（7116，1220；描述是 “coding agent”，不等于 `ai-agents`）、`dream-num/univer`（25585，1041；“AI agents” 是空格写法，不等于 `ai-agents`）、`backnotprop/plannotator`（11814，860）、`ChromeDevTools/chrome-devtools-mcp`（56889，718；名称里的裸 mcp 不是本报告的 AI 关键词）、`tradermonty/claude-trading-skills`（5508，707；描述点名 Claude Code，没有 `llm`）、`Tencent/LoopForge`（1448，484；coding-agent 工作流）、`ag-ui-protocol/ag-ui`（17823，393；Agent-User Interaction Protocol，不等于 `ai-agents`）、`google-labs-code/stitch-skills`（9269，248；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`elementalsouls/Claude-BugHunter`（6390，221；Claude Code 技能包，没有 `llm`）、`NVIDIA/SkillEvaluator`（1640，205；评估 AI agent 技能，没有 `llm`）、`ggml-org/ggml`（15896，53；机器学习张量库，没有 `llm`）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-17 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-17 stars:>2`。HTTP 200。`total_count=457`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`agharsallah/esp-labs-web`（872）、`ngxson/esp32-usb-to-airprint`（318）、`andrisgauracs/whistle-esp32`（235）、`Kristian8606/esp32-airplay2-surround`（233）、`Syfyivan/douli-esp32`（200）。`douli-esp32` 的 `created_at` 为 `2026-10-17T13:54:12Z`。`whistle-esp32` 与 `douli-esp32` 的搜索描述和话题都没有 `llm`，不跨到 AI。`esp32-airplay2-surround` 的搜索描述和话题都为空，只靠仓库名 `esp32`。`esp-labs-web` 话题含 `education`，是带模拟器的实验台，不是公开课清单，正文保留。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-17 stars:>2`。HTTP 200。`total_count=2879`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（8717）、`qybaihe/bla`（5795）、`expo/exact`（4309）。这 3 条是本页星数最高的连续 3 条。`exact` 的 `created_at` 为 `2026-11-02T01:29:01Z`。`Mika` 的 `created_at` 为 `2026-10-29T14:34:07Z`。
  - 未命中：`benjitaylor/skills`（总 star 3367；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）、`sarpstar/cinecode`（总 star 2557；描述是 “an AI coding agent writes the script”，不等于 `ai-agents`）。名称和 topics 都没有领域关键词。二者排在 `exact` 之后，是返回的第 4、第 5 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-17 stars:>2`。HTTP 200。`total_count=6`，返回 5，规则保留 2，未命中 3。剩余配额 25。`per_page=5`，第 6 条不在本次返回里，正文不猜测它是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9），其次是 `SicnuJw`（4），其余 3 条总 star 都是 3。
  - `profesor003-fundesteam/SIC-2026`（总 star 3）：名称和描述含 SIC。README 标题写明这是 Samsung Innovation Campus 2026 的定量分析、数据科学与人工智能课堂材料，含笔记本和数据集，讲师是 Danny Jose Delgado De Sousa，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-18T15:03:12Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（4；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3；`First-Sick` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-17 stars:>2`。HTTP 200。`total_count=69`，返回 5，规则保留 1，未命中 4。剩余配额 23。规则留下的 1 条是公司后缀，剔除后本日无新项目。按总 star，本页顺序是 `acrobat-dc-desktop`、`isometric-cities`、`artex-forensics`、`grid-dca-bot`、`DCore`。
  - 撞名剔除：`darkfibr/artex-forensics`（总 star 57）。描述末尾是 “Blackfish Security LLC”，README 标题同样是 Blackfish Security LLC。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。搜索描述和话题没有 `llm`，不因 README 里出现的 LLM 字样跨到 AI。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（349；Acrobat DC 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（80；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`leftamber/grid-dca-bot`（49；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-17 stars:>2`。HTTP 200。`total_count=94`，返回 5，规则保留 3，未命中 2。剩余配额 21。正文保留 `mozihe/z-localization`（126）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。按总 star，本页顺序是 `mpc-plugin-builder-sdk`、`FrankyRenderer`、`z-localization`、`SampQOL-OS`、`robotics-roadmap`。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 157）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 101）。话题含 `ros2` 与 `slam`。README 徽章写 57 讲、120 小时，正文是 57 讲自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 130；描述里的 MPC-BE 与 MPC-HC 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 112；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-09 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-09 stars:>3`。HTTP 200。`total_count=1355`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=1`、`per_page=5`，本页是总结果里按总 star 排序后的第 1 到第 5 条。本查询正文：`ruvnet/RuView`（104371）、`raysan5/raylib`（35693）、`78/xiaozhi-esp32`（33265）、`lvgl/lvgl`（25172）、`arendst/Tasmota`（24990）。另有 1 条一行不在本页前 5：`makerspet/oomwoo`（13106，话题含 esp32，完整条目在自动控制）。`RuView` 话题含 mcp，搜索描述没有 llm，不跨到 AI。`xiaozhi-esp32` 的 README 点名 Qwen 与 DeepSeek，搜索描述和话题没有 llm，话题 mcp 不是 AI 关键词，不跨到 AI。`raylib` 话题里的 `riscv` 不等于 `risc-v`。`Tasmota` 的 README 写了 Modbus 桥，搜索话题没有 modbus，不另开一节。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-09 stars:>3`。HTTP 200。`total_count=9774`，返回 5，规则保留 3，排除清单 0，未命中 2。剩余配额 26。正文保留 `firecrawl/firecrawl`（202052）、`huggingface/transformers`（169020）、`langgenius/dify`（161213）。按总 star，本页顺序是 firecrawl、transformers、agency-agents、dify、langflow。
  - 未命中：`msitarzewski/agency-agents`（总 star 168578；名称 `agency-agents` 不等于 `ai-agents`）、`langflow-ai/langflow`（总 star 156682；描述是 “AI-powered agents”，不等于 `ai-agents`）。agency-agents 夹在 transformers 与 dify 之间，langflow 是本页第 5 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-09 stars:>3`。HTTP 200。`total_count=29`，返回 5，规则保留 1，排除清单 0，未命中 4。剩余配额 24。`page=1` 是总结果里按总 star 排序后的第 1 到第 5 条。规则保留的 1 条撞名剔除后，本节没有完整条目。返回的星数是 2447、1026、803、284、224。
  - `foresterre/imagineer`（总 star 224）：话题和描述含 sic。README 写明这是图片处理命令行工具，旧名 `sic`，原先是 “simple image cli”，与碳化硅器件无关，正文不收。
  - 名称词边界未命中：`SickChill/sickchill`（2447；`SickChill` 不等于 `sic`）、`source-academy/sicp`（1026；`sicp` 不等于 `sic`）、`SickGear/SickGear`（803；`SickGear` 不等于 `sic`）、`microsoft/Sico`（284；`Sico` 不等于 `sic`）。`Sico` 的话题含 llm，但不在 AI 常青本页前 5，不跨节。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-09 stars:>3`。HTTP 200。`total_count=406`，返回 5，规则保留 1，未命中 4。剩余配额 22。`page=1` 是总结果里按总 star 排序后的第 1 到第 5 条。规则保留的 1 条是公司后缀，剔除后本节没有完整条目。按总 star，本页顺序是 `Battery-Emulator`、`OpenDTU`、`Finbuckle.MultiTenant`、`dcm4che`、`moteus`。
  - 撞名剔除：`Finbuckle/Finbuckle.MultiTenant`（总 star 1635）。描述和 README 写明这是 Finbuckle LLC 维护的 .NET 多租户库，README 标题版本是 10.1.3，并写明支持 .NET 10。LLC 是公司后缀，不是谐振变换器，正文不收。
  - 名称和 topics 未命中：`dalathegreat/Battery-Emulator`（3032；描述里的 `inverters` 是复数，不等于 `inverter`）、`tbnobody/OpenDTU`（2209；描述里的 `Inverters` 是复数，不等于 `inverter`；话题含 esp32，不在嵌入式常青前 5，不跨节）、`dcm4che/dcm4che`（1466；名称里的 dcm 不等于 `dc-dc`）、`mjbots/moteus`（1382；描述是 “Brushless DC motor controller”，空格写法不等于 `motor-control`，`DC` 也不等于 `dc-dc`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-09 stars:>3`。HTTP 200。`total_count=233`，返回 5，规则保留 5，未命中 0，排除清单 0。剩余配额 29。剔除播放器后，正文保留 `AtsushiSakai/PythonRobotics`（30922）、`makerspet/oomwoo`（13106）、`betaflight/betaflight`（11793）、`introlab/rtabmap`（4106）。`oomwoo` 在嵌入式一行。按总 star，本页顺序是 PythonRobotics、oomwoo、betaflight、MPC-BE、rtabmap。
  - 撞名剔除：`Aleksoid1978/MPC-BE`（总 star 4719）。名称命中 `mpc`。搜索描述写明这是 Windows 上的通用音视频播放器，不是模型预测控制，正文不收。`README.md`、`readme.md`、`ReadMe.md`、`README.rst` 均为 HTTP 404，剔除依据是搜索描述和仓库名。
  - `betaflight` 的 README 写了 STM32 F4/F7/G4/H5/H7，以及实验性 ESP32。搜索话题只有 `betaflight`、`cleanflight`、`flight-controller`、`hacktoberfest`，没有这些芯片词，不跨到嵌入式。
  - `oomwoo` 的 README 仍写明现在不能按物料单组装，只能仿真。
