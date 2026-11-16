# GitHub 领域日报 · 2026-11-17

生成时间：2026-11-17 07:38（北京时间）。数据拉取开始于 2026-11-17 07:34:27（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-18（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-10 及之后有推送、总 star > 3。轮换页 `page = (当年第 321 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [alibaba/open-code-review](https://github.com/alibaba/open-code-review) 读 Git 改动，用可配置的语言模型代理写出精确到行的审查意见，并配有不依赖模型的检查流水线；总 star 52912，24 小时新增 star 946。这是今日热度里唯一的领域命中。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 8854，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk) 给第一人称长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参；README 写 LaMAria 训练集控制点分数从 69.1 到 82.4，总 star 121，没有 24 小时新增数据。这是本次新进入自动控制前 5 的仓库。

## A. 今日热度

Trending 页面解析到 15 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条，在 AI。

### AI

- [alibaba/open-code-review](https://github.com/alibaba/open-code-review)
  - 说明：做代码审查，把通用编程代理留在审查流程外面。页面描述写明它是确定性流水线加语言模型代理的混合架构，能给出精确到行的意见，并内置空指针、线程安全、XSS 和 SQL 注入规则。README 写明它读 Git diff，代理可以读全文、搜代码库、看其他改动文件；`ocr scan` 也可以在没有有意义 diff 时审整份文件。前身是阿里集团内部审查助手，过去两年服务了数万名开发者，识别了数百万个代码缺陷。基准从 50 个热门仓库里选了 200 个真实 Pull Request、覆盖 10 种语言，由 80 多位资深工程师交叉标注，共 1505 个标注缺陷。同一底层模型下，它相对通用代理的准确率和 F1 更高，token 大约是九分之一，召回率更低。页面描述里的 “LLM Agent” 按强特征词计入 AI。
  - 领域：AI
  - 总 star：52912
  - 24 小时新增 star：946

嵌入式、功率器件、电力电子电源、自动控制在这 15 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 的实验台收成一个网页。README 写明目前是 32 个动手实验，每课先在浏览器里跑，带实时引脚、交互模拟、逐行讲解固件的阅读器，以及一块 3D 板；数据手册部分把芯片手册收成可引用的章节。搜索描述写 11 种语言；README 徽章写 12 languages，列出英语、法语、西班牙语、意大利语、德语、波兰语、土耳其语、简体中文、繁体中文、日语，以及从右到左的阿拉伯语和波斯语。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：878
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。表格里 MG2550S 标成已在真机验证，其余型号标成尚未上真机。
  - 领域：嵌入式 Embedded
  - 总 star：320
- [Kristian8606/esp32-airplay2-surround](https://github.com/Kristian8606/esp32-airplay2-surround)
  - 说明：用便宜的板子自己组一套无线环绕声。README 写明 Apple TV 只看到网关这一台 AirPlay 2 音箱，网关把 5.1 / 7.1 码流原样分给最多八块音箱板，每块 ESP32-S3 只解码自己的声道，并用接入点信标里的时钟对齐采样时刻。目前写明网关加五只音箱（前左右、中置、两侧）已经能同步播放 5.1 和 7.1，iPhone 的立体声也能跟上；闪存建议买 16 MB 的 N16R8，8 MB 板仍能编译，音箱固件副本只剩大约 117 KB。搜索描述为空，话题也为空，只靠仓库名里的 esp32 归入嵌入式。
  - 领域：嵌入式 Embedded
  - 总 star：289
- [andrisgauracs/whistle-esp32](https://github.com/andrisgauracs/whistle-esp32)
  - 说明：把开源语音模型 Whistle 做成一块 ESP32-S3 上的独立实现。按住按键说一句把灯闪成某种颜色，识别在板子上完成，不走网络。README 写明七种语言同时在板子上，模型约 14.5 MB，需要 16 MB 闪存和 8 MB 八线 PSRAM，并用 C99 对照官方引擎逐张量核对过。搜索描述和话题都没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：239
- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑；ESP-IDF 6.0.1 起，外壳可 3D 打印，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：184

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：8854
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给作者自己即将发布的程序加一层防护，让自动做逆向的语言模型代理在受保护的产物上得不到可用结果。README 徽章写 npm 包 `bla-agents` v3.4.2，并写明在 14 个对照目标上验证过，用途限定为作者保护自己的发布物。话题 `llm-security` 按词边界计入 llm。
  - 领域：AI
  - 总 star：5925
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、macOS、iOS 和 Linux 上原生跑，编程代理可以自己建、自己跑、自己看、自己测。README 写明 Android 和 Windows 还在早期，应用能编过并跑起来，缺的部分单独列着。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：4483

### 功率器件 Power Devices

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

本窗口没有以功率器件为最贴近领域的完整新项目。名称撞上 `sic` 的课堂笔记本已剔除。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。

本查询返回的 5 条里，唯一被规则留下的是公司后缀 LLC，已剔除。`dc-dc` 的搜索侧撞名仍在，分类按词边界没有收进正文。详见数据源状态。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 RoboMaster 哨兵的定位栈。README 写明这是一套 ROS 2 激光惯性定位，支持里程计、点云建图、先验地图定位、回环和重定位，实机和 rosbag 走同一入口。环境写明 Ubuntu 22.04 与 ROS 2 Humble，雷达驱动是 Livox。话题含 ros2 与 slam。`pushed_at` 为 `2026-10-22T09:21:49Z`。
  - 领域：自动控制 Control
  - 总 star：126
- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：补第一人称长轨迹上常规视觉惯性里程计掉下去的那一段精度。README 写常规离线光束法平差能接近公开成绩，但停在 Aria 的 SLAM 下面；把相机标定漂移和陀螺仪内参放进这条流水线后，LaMAria 训练集控制点分数从 69.1 到 82.4，测试集上与 Aria 的 SLAM 持平，并在五类里的三类上第一次超过它，UZH-FPV 排行榜第二。名称含 slam，话题为空。`created_at` 为 `2026-11-13T01:47:26Z`。
  - 领域：自动控制 Control
  - 总 star：121
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino 把一只会自己漏水的水箱做成可测量的开关、P 和 PI 水位回路。直流泵经 MOSFET 做 PWM，市电泵经固态继电器通断；固件里有溢流、干转和传感器保护。README 写实验台是 15 L 罐子、500 L 水箱和 0.5 马力级 230 V 泵，经 Fotek SSR-40DA，并有一次真机测量记录。话题含 control-systems 与 pid。水位回路比 MOSFET 开关更贴近本领域，功率器件一节一行带过。话题含 education，这是带固件和实测的实验台，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=2`、`per_page=5`，本页是各查询按总 star 排序后的第 6 到第 10 条。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：用 ESP32 经 Wi-Fi 控制可寻址灯带，从一条 WS2812B 到二维矩阵和 HUB75 面板。文件名是 `readme.md`。
  - 领域：嵌入式 Embedded
  - 总 star：19056
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：面向单片机、WebAssembly 和命令行的 Go 编译器，基于 LLVM。话题含 ESP32 与 STM32。
  - 领域：嵌入式 Embedded
  - 总 star：17919
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：ESP32 系列芯片的 Arduino 核心，让 Arduino 的写法跑在乐鑫芯片上。
  - 领域：嵌入式 Embedded
  - 总 star：17747
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：给 RepRap 3D 打印机用的固件，8 位和 32 位微控制器都能跑。话题含 ESP32 与 firmware。这是打印机固件，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：17665
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：Zephyr 项目的主仓库，面向多种硬件架构的可扩展实时操作系统。文件名是 `README.rst`。
  - 领域：嵌入式 Embedded
  - 总 star：17100
- [okalachev/flix](https://github.com/okalachev/flix) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：2515。
- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd)
  - 说明：给 Flipper Zero 和 ESP32 做的特斯拉 CAN 工具，能看电池管理系统仪表并抓取总线数据。设备本身是 CAN 与 ESP32，所以完整条目放在嵌入式；电力电子只因描述里的 BMS 仪表一行带过。
  - 领域：嵌入式 Embedded
  - 总 star：1283

### AI

- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：可扩展的编程代理外壳，自带统一的 LLM 接口、代理循环、终端界面和命令行。搜索话题为空，靠描述里的 LLM 计入。
  - 领域：AI
  - 总 star：122349
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：让模型在真实浏览器里把一件事做完的开源浏览器代理，另外提供隐匿浏览器和托管的代理 API。README 写它在浏览器里写 Python，用一个持久的解释器操作页面。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：121231
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
  - 说明：编程代理换一次会话就把上次做过的事忘了。它在旁边跑一个记笔记的代理，下次会话先给一份短索引，需要细节时再取。README 写明能配合 Claude Code、Codex、Cursor、OpenCode，以及另外 11 个代理。话题含 ai-agents。
  - 领域：AI
  - 总 star：117683
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2175。

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。返回的 5 条名称词边界都不等于 `sic`。详见数据源状态。

### 电力电子电源 Power Supply

- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS 仪表，此处不展开。领域：电力电子电源 Power Supply。总 star：1283。
- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：用 ESPHome 经串口或蓝牙监测并控制极空电池管理系统。README 写软件版本不低于 6.0 的机型走这套协议。话题 `jikong-bms` 按词边界计入 bms。README 的接线示例是 ESP32 或 ESP8266，搜索话题没有 esp32，不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：1054

### 自动控制 Control

- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：用外观做回环的建图和定位库，并带一个独立程序。话题含 ros2 与 slam。README 写 ROS 支持在另一个仓库 `rtabmap_ros`，ROS 2 文档在那个仓库的 `ros2` 分支。
  - 领域：自动控制 Control
  - 总 star：4110
- [luigifreda/pyslam](https://github.com/luigifreda/pyslam)
  - 说明：单目、双目和 RGB-D 都能跑的视觉 SLAM 流水线。README 标题是 pySLAM v2.12.0，Python 和 C++ 两套稀疏核心可以互读对方保存的地图。话题含 slam。
  - 领域：自动控制 Control
  - 总 star：3437
- [okalachev/flix](https://github.com/okalachev/flix)
  - 说明：用通用零件从零做一台 ESP32 四旋翼。README 写固件大约两千行 Arduino，通信用 MAVLink，Gazebo 里能仿真；1.1 版是 3D 打印的机架，并且真的能飞。话题含 flight-controller 与 esp32。飞控比板子更贴近本领域，嵌入式一节一行带过。物料表里的 MOSFET 不在搜索描述和话题里，不跨到功率器件。
  - 领域：自动控制 Control
  - 总 star：2515
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：移动机器人的 C++ 工具箱，把定位、建图和运动估计放在同一套库里。README 写它从 2005 年在马拉加大学起步。话题含 slam 与 computer-vision。定位建图比视觉话题更贴近本领域，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：2175

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取按 `README.md`、`readme.md`、`ReadMe.md`、`README.rst` 的顺序，命中即停。`wled/WLED` 的文件名是 `readme.md`，`zephyrproject-rtos/zephyr` 的文件名是 `README.rst`。其余仓库的 `README.md` 为 HTTP 200：`alibaba/open-code-review`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Kristian8606/esp32-airplay2-surround`、`andrisgauracs/whistle-esp32`、`FlashCat-Jordan/Flashduck`、`wangzan101/Mika`、`qybaihe/bla`、`expo/exact`、`Samarth030312/arduino-water-level-control-lab`、`profesor003-fundesteam/SIC-2026`、`darkfibr/artex-forensics`、`inmusic-software/mpc-plugin-builder-sdk`、`mozihe/z-localization`、`jacobvm04/slam-dunk`、`hypery11/flipper-tesla-fsd`、`syssi/esphome-jk-bms`、`tinygo-org/tinygo`、`espressif/arduino-esp32`、`MarlinFirmware/Marlin`、`earendil-works/pi`、`browser-use/browser-use`、`thedotmack/claude-mem`、`introlab/rtabmap`、`luigifreda/pyslam`、`okalachev/flix`、`MRPT/mrpt`。`esphome-jk-bms` 的 README 全文里有 ESP32/ESP8266 接线，搜索话题没有 esp32。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 15 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 核对：脚本解析出 15 条后，另一次 GET 同一 URL 仍是 HTTP 200，仓库集合和顺序相同，stars today 全部不变。10 个仓库的总 star 有增加：`plannotator` 12524→12527，`univer` 27752→27753，`claude-trading-skills` 6287→6288，`arcane` 8685→8686，`jiangshan-map` 6677→6678，`last30days-skill` 68098→68099，`SkillEvaluator` 2645→2648，`paper-orchestra` 1456→1457，`svelte` 88967→88968，`ffmpeg-skill` 6654→6655。`ag-ui`（18928，790）、`Claude-BugHunter`（7422，1057）、`stitch-skills`（9726，540）、`open-code-review`（52912，946）、`chrome-devtools-mcp`（57661，837）两次一致。正文用第一次解析的数字。今日页面本身只有 15 条，不是解析漏条。
- 命中：`alibaba/open-code-review`（52912，946；描述含 “LLM Agent”）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`dream-num/univer`（27752，1878；“AI agents” 是空格写法，不等于 `ai-agents`）、`elementalsouls/Claude-BugHunter`（7422，1057；Claude Code 技能包，没有 `llm`）、`NVIDIA/SkillEvaluator`（2645，953；评估 AI agent 技能，没有 `llm`）、`tradermonty/claude-trading-skills`（6287，841；Claude Code 技能，没有 `llm`）、`ChromeDevTools/chrome-devtools-mcp`（57661，837；名称里的裸 mcp 不是本报告的 AI 关键词）、`ag-ui-protocol/ag-ui`（18928，790；Agent-User Interaction Protocol，不等于 `ai-agents`）、`backnotprop/plannotator`（12524，689；围绕代理的工作区，没有 `llm`）、`google-labs-code/stitch-skills`（9726，540；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`kajisho5/ffmpeg-skill`（6654，475；给编程代理用的本地视频工具，名称里的裸 mcp 不计入）、`google-research/paper-orchestra`（1456，306；多智能体写论文，没有 `llm`）、`DeanChensj/jiangshan-map`（6677，285；中国历史地图）、`mvanhorn/last30days-skill`（68098，122；“AI agent skill”，没有 `llm`）、`sveltejs/svelte`（88967，58）、`getarcaneapp/arcane`（8685，31；Docker 管理）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-18 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-18 stars:>2`。HTTP 200。`total_count=450`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`agharsallah/esp-labs-web`（878）、`ngxson/esp32-usb-to-airprint`（320）、`Kristian8606/esp32-airplay2-surround`（289）、`andrisgauracs/whistle-esp32`（239）、`FlashCat-Jordan/Flashduck`（184）。`Flashduck` 的 `created_at` 为 `2026-10-31T05:10:09Z`。`whistle-esp32` 与 `Flashduck` 的搜索描述和话题都没有 `llm`，不跨到 AI。`esp32-airplay2-surround` 的搜索描述和话题都为空，只靠仓库名 `esp32`。`esp-labs-web` 话题含 `education`，是带模拟器的实验台，不是公开课清单，正文保留。窗口起点从昨日的 2026-10-17 移到 2026-10-18，本页不再返回昨日的 `douli-esp32`。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-18 stars:>2`。HTTP 200。`total_count=2858`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（8854）、`qybaihe/bla`（5925）、`expo/exact`（4483）。这 3 条是本页星数最高的连续 3 条。`exact` 的 `created_at` 为 `2026-11-02T01:29:01Z`。`Mika` 的 `created_at` 为 `2026-10-29T14:34:07Z`。
  - 未命中：`benjitaylor/skills`（总 star 3449；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）、`sarpstar/cinecode`（总 star 2604；描述是 “an AI coding agent writes the script”，不等于 `ai-agents`）。名称和 topics 都没有领域关键词。二者排在 `exact` 之后，是返回的第 4、第 5 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-18 stars:>2`。HTTP 200。`total_count=6`，返回 5，规则保留 2，未命中 3。剩余配额 25。`per_page=5`，第 6 条不在本次返回里，正文不猜测它是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9），其次是 `SicnuJw`（4），其余 3 条总 star 都是 3。
  - `profesor003-fundesteam/SIC-2026`（总 star 3）：名称和描述含 SIC。README 标题写明这是 Samsung Innovation Campus 2026 的定量分析、数据科学与人工智能课堂材料，含笔记本和数据集，讲师是 Danny Jose Delgado De Sousa，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-18T15:03:12Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（4；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3；`First-Sick` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-18 stars:>2`。HTTP 200。`total_count=73`，返回 5，规则保留 1，未命中 4。剩余配额 23。规则留下的 1 条是公司后缀，剔除后本日无新项目。按总 star，本页顺序是 `acrobat-dc-desktop`、`isometric-cities`、`artex-forensics`、`grid-dca-bot`、`DCore`。
  - 撞名剔除：`darkfibr/artex-forensics`（总 star 77）。描述末尾是 “Blackfish Security LLC”，README 标题同样是 Blackfish Security LLC。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。搜索描述和话题没有 `llm`，不因 README 里出现的模型字样跨到 AI。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（247；Acrobat DC 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（81；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`leftamber/grid-dca-bot`（49；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-18 stars:>2`。HTTP 200。`total_count=98`，返回 5，规则保留 3，未命中 2。剩余配额 21。正文保留 `mozihe/z-localization`（126）、`jacobvm04/slam-dunk`（121）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。按总 star，本页顺序是 `mpc-plugin-builder-sdk`、`FrankyRenderer`、`z-localization`、`slam-dunk`、`SampQOL-OS`。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 161）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 132；描述里的 MPC-BE 与 MPC-HC 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 115；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-10 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-10 stars:>3`。HTTP 200。`total_count=1344`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=2`、`per_page=5`，本页是总结果里按总 star 排序后的第 6 到第 10 条。本查询正文：`wled/WLED`（19056）、`tinygo-org/tinygo`（17919）、`espressif/arduino-esp32`（17747）、`MarlinFirmware/Marlin`（17665）、`zephyrproject-rtos/zephyr`（17100）。另有 1 条完整条目不在本页前 5：`hypery11/flipper-tesla-fsd`（1283，来自电力电子检索，话题含 can-bus、描述含 esp32，设备更贴近嵌入式）。另有 1 条一行不在本页前 5：`okalachev/flix`（2515，话题含 esp32，完整条目在自动控制）。`Marlin` 是 3D 打印机固件，不是公开课清单。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-10 stars:>3`。HTTP 200。`total_count=9694`，返回 5，规则保留 3，排除清单 1，未命中 1。剩余配额 26。正文保留 `earendil-works/pi`（122349）、`browser-use/browser-use`（121231）、`thedotmack/claude-mem`（117683）。另有 1 条一行不在本页前 5：`MRPT/mrpt`（2175，话题含 computer-vision，完整条目在自动控制）。按总 star，本页顺序是 awesome-llm-apps、pi、browser-use、agent-skills、claude-mem。
  - 清单类排除：`Shubhamsaboo/awesome-llm-apps`（总 star 144876；名称命中 awesome 与 llm，脚本已按合集排除）。
  - 未命中：`addyosmani/agent-skills`（总 star 118322；描述是 “skills for AI coding agents”，空格写法不等于 `ai-agents`）。它夹在 browser-use 与 claude-mem 之间。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-10 stars:>3`。HTTP 200。`total_count=28`，返回 5，规则保留 0，排除清单 0，未命中 5。剩余配额 24。`page=2` 是总结果里按总 star 排序后的第 6 到第 10 条。返回的星数是 187、136、114、30、25。本节没有完整条目。
  - 名称词边界未命中：`siconos/siconos`（187；非光滑动力系统仿真，`siconos` 不等于 `sic`）、`hexlet-boilerplates/sicp-racket`（136；描述为空，`sicp` 不等于 `sic`）、`hexlet-volunteers/hexlet-sicp`（114；SICP 读书进度服务，`sicp` 不等于 `sic`）、`opencad-abu/SiCo`（30；矽科集成电路设计助手，`SiCo` 不等于 `sic`）、`Zmy0312bry/BUPT_SICE_ARCHIVE`（25；北京邮电大学信息与通信工程学院作业资料，`SICE` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-10 stars:>3`。HTTP 200。`total_count=401`，返回 5，规则保留 2，未命中 3。剩余配额 22。`page=2` 是总结果里按总 star 排序后的第 6 到第 10 条。正文完整条目为 `syssi/esphome-jk-bms`（1054）。`hypery11/flipper-tesla-fsd`（1283）描述含 BMS，完整条目在嵌入式，本节一行。按总 star，本页顺序是 `flipper-tesla-fsd`、`iot-dc3`、`esphome-jk-bms`、`huawei_solar`、`dcmtk`。
  - `pnoker/iot-dc3`（总 star 1274）：话题含 modbus 与 ai-agents，但名称 `dc3` 不等于 `dc-dc`，不在嵌入式和 AI 常青本页前 5，不跨节。
  - 名称和 topics 未命中电力电子：`wlcrs/huawei_solar`（950；描述里的 `inverters` 是复数，不等于 `inverter`；话题含 modbus，不在嵌入式常青前 5，不跨节）、`DCMTK/dcmtk`（919；名称里的 dcm 不等于 `dc-dc`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-10 stars:>3`。HTTP 200。`total_count=230`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 29。正文保留 `introlab/rtabmap`（4110）、`luigifreda/pyslam`（3437）、`okalachev/flix`（2515）、`MRPT/mrpt`（2175）。`flix` 在嵌入式一行，`mrpt` 在 AI 一行。按总 star，本页顺序是 rtabmap、bldc、pyslam、flix、mrpt。
  - 名称和描述未命中：`vedderb/bldc`（总 star 3579）。描述是 “The VESC motor control firmware”，“motor control” 是空格写法，不等于 `motor-control`；名称 `bldc` 不在控制关键词表，正文不收。
