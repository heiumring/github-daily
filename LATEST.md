# GitHub 领域日报 · 2026-11-19

生成时间：2026-11-19 07:34（北京时间）。数据拉取开始于 2026-11-19 07:34:20（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-20（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-12 及之后有推送、总 star > 3。轮换页 `page = (当年第 323 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 9093，没有 24 小时新增数据。今日热度没有领域命中，这是近 30 天新项目里星数最高的命中仓库。
2. [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork) 把一件事交给团队里的人和代理，做完要等人签收，而不是聊完就算结束；创建于 2026-10-29，总 star 2868，没有 24 小时新增数据。这是本次 AI 新项目前 5 里新出现的一条。
3. [francescopace/espectre](https://github.com/francescopace/espectre) 用房间里现成的 Wi-Fi，把一块 ESP32 变成不上传云端的动作传感器；总 star 9836，没有 24 小时新增数据。这是本页嵌入式常青里星数最高的仓库。

## A. 今日热度

Trending 页面解析到 20 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。

嵌入式、AI、功率器件、电力电子电源、自动控制在这 20 条里都没有命中。`punkpeye/awesome-mcp-servers` 是合集，已排除；它的描述也没有本报告使用的 AI 关键词。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 的实验台收成一个网页。README 写明目前是 32 个动手实验，每课先在浏览器里跑，带实时引脚、交互模拟、逐行讲解固件的阅读器，以及一块 3D 板；数据手册部分把芯片手册收成可引用的章节。搜索描述写 11 种语言；README 徽章写 12 languages，列出英语、法语、西班牙语、意大利语、德语、波兰语、土耳其语、简体中文、繁体中文、日语，以及从右到左的阿拉伯语和波斯语。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：904
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。表格里 MG2500 系列的 MG2550S 标成绿，意思是已在真机验证；其余型号标成黄，预期能用但还没上真机。
  - 领域：嵌入式 Embedded
  - 总 star：333
- [Kristian8606/esp32-airplay2-surround](https://github.com/Kristian8606/esp32-airplay2-surround)
  - 说明：用便宜的板子自己组一套无线环绕声。README 写明 Apple TV 只看到网关这一台 AirPlay 2 音箱，网关把 5.1 / 7.1 码流原样分给音箱板，每块 ESP32-S3 只解码自己的声道。目前写明网关加五只音箱（前左右、中置、两侧）已经能同步播放 5.1 和 7.1，iPhone 的立体声也能跟上；闪存建议买 16 MB 的 N16R8，8 MB 板仍能编译，音箱固件副本只剩大约 117 KB。搜索描述为空，话题也为空，只靠仓库名里的 esp32 归入嵌入式。
  - 领域：嵌入式 Embedded
  - 总 star：306
- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑；ESP-IDF 6.0.1 起，外壳可 3D 打印，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：185
- [tahaalakhras53-boop/dma-firmware-customization](https://github.com/tahaalakhras53-boop/dma-firmware-customization)
  - 说明：仓库自称是一份给 PCIe DMA 板改写固件身份、让主机把它认成别的设备的说明。这是在总线上隐瞒设备身份，正文不写配置项、标识来源和构建步骤。话题含 embedded 与 esp32，仓库名含 firmware，因此归入嵌入式；README 全文没有 ESP32，不把话题里的 esp32 写成这块板的主控。`created_at` 为 `2026-11-15T19:45:19Z`。
  - 领域：嵌入式 Embedded
  - 总 star：153

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：9093
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给作者自己即将发布的程序加一层防护，让自动做逆向的语言模型代理在受保护的产物上得不到可用结果。README 徽章写 npm 包 `bla-agents` v3.5.1，并写明在 14 个对照目标上验证过，用途限定为作者保护自己的发布物。话题 `llm-security` 按词边界计入 llm。
  - 领域：AI
  - 总 star：6137
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、macOS、iOS 和 Linux 上原生跑，编程代理可以自己建、自己跑、自己看、自己测。README 写界面用一种叫 Contract 的声明式语言，布局和属性名沿用 CSS；网页产物是大约 20 KB 的运行时加上一个 ES 模块，各平台的界面都不走 webview。Android 和 Windows 还在早期，应用能编过并跑起来，缺的部分单独列着。仓库仍是 pre-1.0，没有打包发布。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：4678
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
  - 说明：给团队自托管的一件工作引擎。提一句需求不算做完，要等提出的人签收；可以指定一个代理干活，另一个代理按验收标准复查，不过就退回。README 写它能接上 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code 和 Codex。话题含 llm 与 ai-agents。`created_at` 为 `2026-10-29T02:43:14Z`。
  - 领域：AI
  - 总 star：2868

### 功率器件 Power Devices

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

本窗口没有以功率器件为最贴近领域的完整新项目。名称撞上 `sic` 的课堂笔记本已剔除。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。返回的 5 条里，1 条是公司后缀 LLC，不是谐振变换器；另外 4 条的名称、话题和搜索描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`。详见数据源状态。

### 自动控制 Control

- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：给第一人称、野外长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参。README 写一套常规的离线光束法平差能缩小和行业系统的差距，但会停在公开提交的水平；把这两项物理现象放进同一条流水线后，LaMAria 训练集的控制点分数从 69.1 到 82.4。它在 LaMAria 测试集上与 Aria 的 SLAM 打平，并在五个类别里的三个上第一次超过 Aria，UZH-FPV 排行榜上排第二。仓库名里的 slam 计入自动控制。`created_at` 为 `2026-11-13T01:47:26Z`。
  - 领域：自动控制 Control
  - 总 star：143
- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：给移动机器人一套 ROS 2 激光惯性定位，覆盖里程计、点云建图、先验地图定位、回环和重定位，也可以接 UWB。README 写这是 2026 年东北大学 T-DT 实验室 RoboMaster 超级对抗赛的哨兵定位开源，实机和 rosbag 回放走同一个入口，依赖徽章写 ROS 2 Humble、C++17。话题含 ros2 与 slam。`created_at` 为 `2026-10-22T08:49:49Z`。
  - 领域：自动控制 Control
  - 总 star：128
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用一个水箱、超声测距和一台泵，把通断、P 和 PI 液位控制做成可以对照仿真的实验。README 写实验台是 15 L 罐子，由 500 L 水箱经一台约 0.5 马力、230 V 的泵补水，市电泵走 Fotek SSR-40DA，直流泵则用 MOSFET 做 PWM；MATLAB 应用的物理量来自你自己的水箱、出口和泵，徽章写 MATLAB R2023b 及以上。话题含 control-systems，话题 `pid-control` 按词边界计入 pid。水位控制比 MOSFET 开关更贴近本领域，功率器件一节一行带过。这条来自功率器件新项目检索，不在自动控制本页前 5。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=4`、`per_page=5`，本页是各查询按总 star 排序后的第 16 到第 20 条。

### 嵌入式 Embedded

- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：人在房间里走动会改变 Wi-Fi 的传播，这块板子读这些变化，用来开灯、调暖和报一个不该有人的地方有了动静。README 写明测量和打分都在设备上完成，不上传云，一块板覆盖一个区域；它不识别是谁、不人数、也不代替安防或医疗认证。支持 ESP32-C6、C5、C3、S3、S2 和经典 ESP32，Matter 占用传感器已在 Google Home、Apple Home 和 Home Assistant 上测过。话题含 embedded。话题是 `esp-32`，词边界不等于 esp32，描述里的 ESP32 才计入。
  - 领域：嵌入式 Embedded
  - 总 star：9836
- [crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)
  - 说明：给几款墨水屏阅读器做可以自己刷的开源固件，让设备按读者的需要打开书，而不是只按出厂功能用。README 写它现在跑在基于 ESP32-C3 的 Xteink X4 和 X3，以及基于 ESP32-S3 的 Xteink X4Pro、X4Classic、Seeed reTerminal Sticky、M5PaperMono、Metalio E-Ink 4、EEGOREAD A4 和 Boox Picco 上。能读 EPUB、txt 和 bmp，也可以从浏览器传文件、连 Calibre 和 OPDS。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：8854
- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的官方设备固件，用 LoRa 组一个不依赖互联网和蜂窝网的远距离网格，用来传文字、位置和遥测。README 概述写固件支持 ESP32、nRF52、RP2040/RP2350 和基于 Linux 的设备。话题含 esp32 与 stm32，也含 lora 与 mesh。
  - 领域：嵌入式 Embedded
  - 总 star：8600
- [nodemcu/nodemcu-firmware](https://github.com/nodemcu/nodemcu-firmware)
  - 说明：用 Lua 写 ESP8266 上的无线节点，事件驱动，程序可以直接从闪存里跑。README 标题是 NodeMCU 3.0.0，并写明 `release` 与 `dev` 分支面向 ESP8266，`dev-esp32` 分支才面向 ESP32。搜索描述写的是 ESP8266、ESP8285 和 ESP32 的 Lua 固件。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：7961
- [FastLED/FastLED](https://github.com/FastLED/FastLED)
  - 说明：用同一套库驱动各家可寻址 LED，让单片机把灯动画跑起来。README 写高端器件可以带动 3 万颗以上的灯，也很小的芯片能用，并写它能跑在 Arduino、ESP32、Teensy 和另外 50 多种平台上。话题含 embedded 与 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：7536

### AI

- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)
  - 说明：给 Claude Code 和 Codex 加一层代理编排，让一次任务可以拉起一组带记忆和钩子的代理，而不是只在一次对话里做完。README 写在项目目录执行 `npx ruflo@latest init` 就会放进代理、钩子、记忆和 MCP 服务；只装 Claude Code 插件、不往项目里加文件的那条路，要求 Claude Code 2.1.287 或更新。话题含 ai-agents。描述里的 RAG 不是本报告的关键词。`created_at` 为 `2025-06-02T21:24:20Z`。
  - 领域：AI
  - 总 star：82051
- [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage)
  - 说明：让编程代理按一条制作流水线把片子做完，从找资料、写脚本、出素材到剪辑合成，而不是只吐一段画面。README 写流水线有 10 条以上，制作工具 100 个以上，技能和制作知识文件 700 个以上；搜索描述写的是 12 条生产流水线、100 多个工具和同样的 700 多个文件。话题 `stable-diffusion` 按词边界计入 diffusion。话题里没有 llm，也没有 ai-agents。`created_at` 为 `2026-03-29T15:23:22Z`。
  - 领域：AI
  - 总 star：81559
- [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
  - 说明：用一套放在本仓库里的课，把做 AI 代理要碰到的工具使用、规划和多智能体讲到能跟着写。搜索描述写 18 Lessons。README 标题写明这是一门课，课程表从第 1 课 Intro to AI Agents 收到第 18 课 Securing AI Agents，每课都有本仓库里的课文。后面另有一节链到别的课程，主体是这 18 课本身，不是一份外部公开课链接清单，正文保留。话题含 ai-agents。
  - 领域：AI
  - 总 star：80374
- [unslothai/unsloth](https://github.com/unslothai/unsloth)
  - 说明：在自己的电脑上跑和训练模型，不必先搭一套服务。README 标题写它是第一款用来跑和训练模型的桌面应用，并给出 Windows 与 macOS 的安装包。搜索描述写本地界面支持 GGUF、MLX、Qwen3.8、DeepSeek-V4.1、MiniMax-H3、Gemma 4、FLUX 等。话题含 llm 与 reinforcement-learning，话题 `stable-diffusion` 按词边界计入 diffusion。
  - 领域：AI
  - 总 star：79747
- [MOLAorg/mola](https://github.com/MOLAorg/mola) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：1068。

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。`libresidfp` 是 C64 的 SID 芯片仿真，话题里的 mosfet 不是功率器件，已剔除。详见数据源状态。

### 电力电子电源 Power Supply

- [springfall2008/batpred](https://github.com/springfall2008/batpred)
  - 说明：在 Home Assistant 里预测家里的电池该什么时候充，并按这个预测去调逆变器，用来跟上电价和日照，而不是到点固定充放。README 写支持的逆变器包括 GivEnergy、Solis、Huawei、SolarEdge、SigEnergy、FoxESS、Sofar、Tesla Powerwall 等，并写 Predbat Cloud 是获授权的付费托管版，本仓库的个人使用仍开源。话题 `solax-inverter` 按词边界计入 inverter；话题 `solis-pv-inverters` 是复数，词边界不等于 inverter。搜索描述写 supporting many inverter types。`pushed_at` 为 `2026-11-18T23:20:14Z`。
  - 领域：电力电子电源 Power Supply
  - 总 star：378

### 自动控制 Control

- [NVIDIA-ISAAC-ROS/isaac_ros_visual_slam](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam)
  - 说明：给机器人一条跑在 GPU 上的视觉定位，用立体相机估计自己相对起点走了多远，室内没有 GPS 时也能给导航提供里程计。README 写它是 ROS 2 包，输入是一路或多路立体相机，IMU 可选，地面机器人和无人机都可以拿它当里程计来源。搜索描述写它基于 NVIDIA 加速的 cuVSLAM。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：1500
- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用带肌肉的人体模型在 MuJoCo 里做控制任务，给生物力学和康复一类的研究一个能训练策略的环境。README 的 MyoSuite 3 一节写明可以在单张 GPU 上并行训练成千上万个环境，再把策略拿回 CPU 回放；同一个任务号可以走 Gymnasium、mjlab，也可以走实验性的 MJX。话题含 motor-control。
  - 领域：自动控制 Control
  - 总 star：1291
- [MOLAorg/mola](https://github.com/MOLAorg/mola)
  - 说明：把激光里程计、激光惯性里程计和建图收成可以换模块的一条流水线，用来在同一套框架里换定位方案。README 写它是模块化的 C++ 与 ROS 2 框架。搜索话题含 slam 与 computer-vision，没有 ros2。定位建图比视觉话题更贴近本领域，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：1068

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API（定位仓库默认说明文件），下列仓库全部 HTTP 200：`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Kristian8606/esp32-airplay2-surround`、`FlashCat-Jordan/Flashduck`、`tahaalakhras53-boop/dma-firmware-customization`、`francescopace/espectre`、`crosspoint-reader/crosspoint-reader`、`meshtastic/firmware`、`nodemcu/nodemcu-firmware`、`FastLED/FastLED`、`wangzan101/Mika`、`qybaihe/bla`、`expo/exact`、`mdiri-ai/SoduWork`、`ruvnet/ruflo`、`OpenMontageInc/OpenMontage`、`microsoft/ai-agents-for-beginners`、`unslothai/unsloth`、`Samarth030312/arduino-water-level-control-lab`、`sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`、`libsidplayfp/libresidfp`、`darkfibr/artex-forensics`、`springfall2008/batpred`、`inmusic-software/mpc-plugin-builder-sdk`、`jacobvm04/slam-dunk`、`mozihe/z-localization`、`Vincentqyw/cv-arxiv-daily`、`NVIDIA-ISAAC-ROS/isaac_ros_visual_slam`、`MyoHub/myosuite`、`MOLAorg/mola`。`dma-firmware-customization` 的 README 没有 ESP32，身份改写的配置和构建步骤未写入正文。`artex-forensics` 的 README 只用来确认公司后缀，其中的漏洞复现步骤未写入正文。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 20 条，规则命中 0 条，清单类排除 1 条。页面没有 `X-RateLimit-Remaining`。
- 核对：脚本解析出 20 条后，另一次 GET 同一 URL 仍是 HTTP 200，`<article class="Box-row">` 仍是 20 个，仓库集合和顺序相同，stars today 全部不变。12 个仓库的总 star 有变化：`Claude-BugHunter` 11319→11322，`CLI-Anything` 59711→59712，`SkillEvaluator` 3699→3700，`nvm` 96150→96149，`uv` 92213→92214，`paper-orchestra` 4241→4243，`stitch-skills` 10385→10386，`svelte` 89630→89627，`superpowers` 321296→321297，`ECC` 306462→306463，`jiangshan-map` 7913→7914，`awesome-mcp-servers` 98005→98006。`cursor/plugins`（17179，315）、`last30days-skill`（69964，1062）、`arcane`（9778，547）、`jquery`（60006，268）、`appwrite`（58225，239）、`openvino`（11312，18）、`n8n`（211052，315）、`solid`（36562，37）两次一致。正文用第一次解析的数字。今日页面本身有 20 条，不是解析多条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`elementalsouls/Claude-BugHunter`（11319，2322；技能包，没有 `llm`）、`google-research/paper-orchestra`（4241，1529；多智能体写论文，没有 `llm`）、`affaan-m/ECC`（306462，1109；代理性能框架，没有 `llm`）、`mvanhorn/last30days-skill`（69964，1062；“AI agent skill”，没有 `llm`）、`obra/superpowers`（321296，823；代理技能框架，没有 `llm`）、`sveltejs/svelte`（89630，694）、`getarcaneapp/arcane`（9778，547；Docker 管理）、`HKUDS/CLI-Anything`（59711，384；把软件做成代理能调用的命令行，没有 `llm`）、`google-labs-code/stitch-skills`（10385，369；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`NVIDIA/SkillEvaluator`（3699，323；评估代理技能，没有 `llm`）、`cursor/plugins`（17179，315；Cursor 插件规范）、`n8n-io/n8n`（211052，315；“native AI capabilities” 是弱词）、`DeanChensj/jiangshan-map`（7913，280；历史地图）、`jquery/jquery`（60006，268）、`astral-sh/uv`（92213，260）、`appwrite/appwrite`（58225，239；“cloud for agents” 不等于 `ai-agents`）、`nvm-sh/nvm`（96150，111）、`solidjs/solid`（36562，37）、`openvinotoolkit/openvino`（11312，18；“AI inference” 是弱词，没有 `llm`）。
- 清单类排除：`punkpeye/awesome-mcp-servers`（98005，52；名称命中 awesome，描述是 MCP 服务器合集。裸 mcp 本来就不是本报告的 AI 关键词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-20 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-20 stars:>2`。HTTP 200。`total_count=445`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`agharsallah/esp-labs-web`（904）、`ngxson/esp32-usb-to-airprint`（333）、`Kristian8606/esp32-airplay2-surround`（306）、`FlashCat-Jordan/Flashduck`（185）、`tahaalakhras53-boop/dma-firmware-customization`（153）。`Flashduck` 的 `created_at` 为 `2026-10-31T05:10:09Z`。`dma-firmware-customization` 的 `created_at` 为 `2026-11-15T19:45:19Z`。`Flashduck` 的搜索描述和话题都没有 `llm`，不跨到 AI。`esp32-airplay2-surround` 的搜索描述和话题都为空，只靠仓库名 `esp32`。`esp-labs-web` 话题含 `education`，是带模拟器的实验台，不是公开课清单，正文保留。`dma-firmware-customization` 的话题含 `esp32`，README 全文没有 ESP32。窗口起点从昨日的 2026-10-19 移到 2026-10-20。昨日 `whistle-esp32` 的 `created_at` 为 `2026-10-19T04:19:26Z`，落在新窗口之外；它昨日总 star 243，若仍在窗口内会排在本次 185 与 153 两条之前，本次前 5 没有它。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-20 stars:>2`。HTTP 200。`total_count=2864`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（9093）、`qybaihe/bla`（6137）、`expo/exact`（4678）、`mdiri-ai/SoduWork`（2868）。`exact` 的 `created_at` 为 `2026-11-02T01:29:01Z`。`Mika` 的 `created_at` 为 `2026-10-29T14:34:07Z`。`SoduWork` 的 `created_at` 为 `2026-10-29T02:43:14Z`。`bla` 的 npm 徽章现为 v3.5.1。
  - 未命中：`benjitaylor/skills`（总 star 3761；描述是 “Skills for AI coding agents.”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。它排在 `exact` 与 `SoduWork` 之间，是返回的第 4 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-20 stars:>2`。HTTP 200。`total_count=4`，返回 4，规则保留 2，未命中 2。剩余配额 25。`total_count` 等于返回条数，本次没有第 5 条。规则保留的 2 条里，1 条是课堂笔记本，剔除；1 条更贴近自动控制，本节只留一行。返回的 4 条里星数最高的是水位实验（9），其次是 `SicnuJw`（6），然后是课堂笔记本（4）和 `Sicip-data-science`（3）。
  - `sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`（总 star 4）：名称含 SIC，搜索描述为空。README 标题写明这是 Samsung Innovation Campus 2026 的 PA-C 与 PA-D 课堂材料，含 Google Colab 笔记本，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-24T17:55:41Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（6；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-20 stars:>2`。HTTP 200。`total_count=76`，返回 5，规则保留 1，未命中 4。剩余配额 23。规则留下的 1 条是公司后缀，剔除后本日无新项目。按总 star，本页是 `acrobat-dc-desktop`（249）、`isometric-cities`（84）、`artex-forensics`（77），然后 `3dcoat-setup-guide` 与 `mvc2-naomi-dc` 都是 55。
  - 撞名剔除：`darkfibr/artex-forensics`（总 star 77）。描述末尾是 “Blackfish Security LLC”，README 标题同样是 Blackfish Security LLC。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。搜索描述和话题没有 `llm`，不因 README 里出现的模型字样跨到 AI。
  - 名称、话题和搜索描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（249；Acrobat DC 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（84；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`schaefer675611/3dcoat-setup-guide`（55；3DCoat 桌面雕刻软件的安装说明）、`gibletto/mvc2-naomi-dc`（55；街机游戏反编译，名称里的 dc 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-20 stars:>2`。HTTP 200。`total_count=102`，返回 5，规则保留 3，未命中 2。剩余配额 21。正文保留 `jacobvm04/slam-dunk`（143）、`mozihe/z-localization`（128）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。按总 star，本页顺序是 `mpc-plugin-builder-sdk`（189）、`slam-dunk`（143）、`FrankyRenderer`（139）、`z-localization`（128）、`SampQOL-OS`（124）。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 189）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 139；描述里的 MPC-BE 与 MPC-HC 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 124；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-12 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-12 stars:>3`。HTTP 200。`total_count=1375`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=4`、`per_page=5`，本页是总结果里按总 star 排序后的第 16 到第 20 条。本查询正文：`francescopace/espectre`（9836）、`crosspoint-reader/crosspoint-reader`（8854）、`meshtastic/firmware`（8600）、`nodemcu/nodemcu-firmware`（7961）、`FastLED/FastLED`（7536）。`espectre` 的话题是 `esp-32`，描述里的 ESP32 计入。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-12 stars:>3`。HTTP 200。`total_count=9768`，返回 5，规则保留 4，排除清单 0，未命中 1。剩余配额 26。正文保留 `ruvnet/ruflo`（82051）、`OpenMontageInc/OpenMontage`（81559）、`microsoft/ai-agents-for-beginners`（80374）、`unslothai/unsloth`（79747）。另有 1 条一行不在本页前 5：`MOLAorg/mola`（1068，话题含 computer-vision，完整条目在自动控制）。按总 star，本页顺序是 career-ops、ruflo、OpenMontage、ai-agents-for-beginners、unsloth。
  - 未命中：`career-ops-hq/career-ops`（总 star 83551；描述是 “Open-source AI job search agent”，空格写法不等于 `ai-agents`）。它是本页星数最高的一条，夹在页首。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-12 stars:>3`。HTTP 200。`total_count=32`，返回 5，规则保留 1，排除清单 1，未命中 3。剩余配额 24。`page=4` 是总结果里按总 star 排序后的第 16 到第 20 条。返回的星数是 16、14、12、10、7。规则留下的 1 条是 SID 仿真，剔除。本节没有完整条目。
  - 撞名剔除：`libsidplayfp/libresidfp`（总 star 16）。话题含 mosfet。README 写明这是周期精确的 SID 仿真，覆盖 6581 和 8580，给 Commodore 64 用，不是功率器件，正文不收。
  - 清单类排除：`satnamrsm/https-github.com-sickn33-antigravity-awesome-skills`（总 star 10；名称含 awesome，脚本已按合集排除）。
  - 名称词边界未命中：`ducroo/SICTIC-AI`（14；瑞士商业天使俱乐部 SICTIC 的引擎，`SICTIC` 不等于 `sic`）、`linuxserver/docker-sickgear`（12；搜索描述为空，`sickgear` 不等于 `sic`）、`reekta92/sicth`（7；一个很小的终端文件浏览器，`sicth` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-12 stars:>3`。HTTP 200。`total_count=413`，返回 5，规则保留 1，未命中 4。剩余配额 22。`page=4` 是总结果里按总 star 排序后的第 16 到第 20 条。正文完整条目为 `springfall2008/batpred`（378）。按总 star，本页顺序是 `dcm4chee-arc-light`（508）、`3dcitydb`（491）、`3dcodeverse`（406）、`batpred`（378）、`openDCIM`（373）。
  - 名称和 topics 未命中电力电子：`dcm4che/dcm4chee-arc-light`（508；DICOM 归档，名称里的 dcm 不等于 `dc-dc`）、`3dcitydb/3dcitydb`（491；CityGML 数据库）、`gaoypeng/3dcodeverse`（406）、`opendcim/openDCIM`（373；数据中心资产管理系统，DCIM 不等于 `dc-dc`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-12 stars:>3`。HTTP 200。`total_count=241`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 29。正文保留 `NVIDIA-ISAAC-ROS/isaac_ros_visual_slam`（1500）、`MyoHub/myosuite`（1291）、`MOLAorg/mola`（1068）。`mola` 在 AI 一行。按总 star，本页顺序是 cuVSLAM、cv-arxiv-daily、isaac_ros_visual_slam、myosuite、mola。本次响应头的剩余配额是 29，前一条电力电子常青是 22，中间没有失败重试，按响应头原样记录。
  - 清单类排除：`Vincentqyw/cv-arxiv-daily`（总 star 1520；搜索描述是用 GitHub Actions 每天自动更新计算机视觉论文，话题含 slam。脚本的清单规则没有命中这个仓库名，按每日论文清单人工剔除）。
  - 名称词边界未命中：`nvidia-isaac/cuVSLAM`（总 star 1913；描述里的 “visual odometry and SLAM” 是空格写法，名称 `cuVSLAM` 的词边界不等于 `slam`。`slam` 不在强特征描述词里，正文不收）。
