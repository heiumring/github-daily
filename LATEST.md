# GitHub 领域日报 · 2026-11-25

生成时间：2026-11-25 07:37（北京时间）。数据拉取开始于 2026-11-25 07:32:00（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-26（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-18 及之后有推送、总 star > 3。轮换页 `page = (当年第 329 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 让人用自己的显卡从零训一个大约 64M 的小模型，而不是只调用现成的大模型；总 star 70152，24 小时新增 star 727。这是今日热度里唯一命中领域的仓库。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 9865，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [earendil-works/pi](https://github.com/earendil-works/pi) 给编程代理一个可改成自己工作流的外壳，搜索描述写它带统一的 LLM 接口、代理循环和命令行；总 star 123721，没有 24 小时新增数据。这是本页常青里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 16 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

嵌入式、功率器件、电力电子电源、自动控制在这 16 条里都没有命中。

### AI

- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
  - 说明：把大模型的训练过程拆到个人显卡上能跑完，用来看懂预训练、微调和对齐，而不是只调一个封装好的接口。README 写主线最小版本大约 64M，并用 PyTorch 从零实现整条训练链路。同一段注明「2 小时」是监督微调阶段在单张 NVIDIA 3090 上跑完 1 个 epoch 的实测，「3 块钱」是这段时间的租卡费用。搜索描述里的 LLM 计入 AI。
  - 领域：AI
  - 总 star：70152
  - 24 小时新增 star：727

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，Linux 不用另装驱动，浏览器里也能扫描，并要求新驱动先在真机上测过。表格里绿色（已在真机验证）只有 MG2550S；黄色的 MG2500 那行写的是 MG2510 到 MG2590（MG2500S 除外）。绿色型号是 MG2550S，黄色排除的是 MG2500S，两处写法不一致，按 README 原文记录。黄色表示预期能用但还没上真机。`created_at` 为 `2026-10-26T16:18:54Z`，落在窗口起点当天。
  - 领域：嵌入式 Embedded
  - 总 star：348
- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑，刷一套会覆盖另一套；ESP-IDF 6.0.1 起，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：189
- [tahaalakhras53-boop/dma-firmware-customization](https://github.com/tahaalakhras53-boop/dma-firmware-customization)
  - 说明：仓库自称是一份给 PCIe DMA 板改写固件身份、让主机把它认成别的设备的说明。README 标题是 “DMA Firmware Customization — Security Tool”，搜索描述写成针对 PCIe Screamer Squirrel 的硬件混淆指南。这是在总线上隐瞒设备身份，正文不写安装、配置和改写步骤。话题含 embedded 与 esp32，仓库名含 firmware，因此归入嵌入式；README 全文没有 ESP32，不把话题里的 esp32 写成这块板的主控。话题里同时有 adc、battery-monitor、hub75、oled 等和这份说明对不上的标签。`created_at` 为 `2026-11-15T19:45:19Z`。
  - 领域：嵌入式 Embedded
  - 总 star：153
- [zacharyinserra/deskhub](https://github.com/zacharyinserra/deskhub)
  - 说明：把一块 Waveshare ESP32-S3 触控屏放在桌上，看电脑的占用、日历、正在播放的媒体，以及 Claude Code 的用量，也能按屏幕上的按钮去操作这台电脑。搜索描述已经写了 Steam 和 3D 打印机。README 写固件是 ESP-IDF v5.5 加 LVGL，屏是 4.3 英寸 B 款、800×480 电容触摸，只连 2.4 GHz Wi-Fi；Windows 上的配套程序负责把电脑数据送过来，时钟和天气在电脑关机后仍由板子自己显示，另有 Codex 用量页。天气和 Codex 来自 README，不在搜索描述里。描述里的 Claude Code 不是 llm，不跨到 AI。`created_at` 为 `2026-11-17T16:57:49Z`。
  - 领域：嵌入式 Embedded
  - 总 star：146
- [andrisgauracs/bevel-os](https://github.com/andrisgauracs/bevel-os)
  - 说明：在一块 ESP32-S3 上跑一个能开窗口的小桌面，用六只电阻把 640×480、64 色的画面送到 VGA 显示器。README 写它由模型 Claude Fable 5.2 写成，人负责接线和 3D 打印；开机到桌面 0.7 秒，窗口里的 Doom（共享版 E1M1）大约 32 帧。硬件写明 16 MB 闪存、8 MB 八线 PSRAM 的 N16R8，系统跑在 ESP-IDF 5.5.3 和 FreeRTOS 上。搜索描述里的 ESP32-S3 按词边界计入 esp32。`created_at` 为 `2026-11-14T14:18:34Z`。
  - 领域：嵌入式 Embedded
  - 总 star：134

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：9865
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
  - 说明：给团队自托管的一件工作引擎。提一句需求不算做完，要等提出的人签收；可以指定一个代理干活，另一个代理按验收标准复查，不过就退回。README 首页列出 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code、Codex Harness 和 Codex。展开的表标题现在写 Supported harnesses (7)，表里就是这 7 个。话题含 llm 与 ai-agents。话题里的 mcp 不是本次 AI 关键词，不另计。`created_at` 为 `2026-10-29T02:43:14Z`。
  - 领域：AI
  - 总 star：7608
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、iOS、macOS、Android 和 Linux 上按各自的原生控件跑，编程代理可以自己建、自己跑、自己看、自己测。README 写界面用一种叫 Contract 的声明式语言，布局和属性名沿用 CSS；网页产物是大约 20 KB 的运行时。Android 写明已经能用，Material 3 的打磨还在进行；Windows 仍在早期。仓库仍是 pre-1.0，没有打包发布，并写 Bun 钉在 1.4.2。搜索描述只写了网页、macOS、iOS 和 Linux，Android 的状态来自 README。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：5056
- [simplexai-labs/linger](https://github.com/simplexai-labs/linger)
  - 说明：在自己的电脑上跑一个私人代理，模型和记忆留在本机，而不是按次把对话送到别人的服务器。README 写 MoE 推理把常用专家留在显卡上，其余放在内存或固态硬盘，并写 125B 的 Qwen3.8-Flash-Next 能在 12 GB 显卡加 64 GB 内存上跑。图注写这个模型的 2-bit 文件是 39 GB；速度表里 RTX 3060（12 GB）那一格是 45.5 token/s。这些数字是 README 的说法，不是本次实测。话题 `local-llm` 按词边界计入 llm。`created_at` 为 `2026-11-10T03:50:38Z`。
  - 领域：AI
  - 总 star：4354

### 功率器件 Power Devices

本日无新项目。`total_count=4`，4 条全部返回，名称都没落到 `sic` 的词边界上。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。返回的 5 条里，1 条描述末尾的 LLC 是公司名；另外 4 条的名称和搜索描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`。详见数据源状态。

### 自动控制 Control

- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：给第一人称、野外长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参。README 写一套常规的离线光束法平差能缩小和行业系统的差距，但会停在公开提交的水平；把这两项物理现象放进同一条流水线后，LaMAria 训练集的控制点分数从 69.1 到 82.4。它在 LaMAria 测试集上与 Aria 的 SLAM 打平，并在五个类别里的三个上第一次超过 Aria，UZH-FPV 排行榜上排第二。仓库名里的 slam 计入自动控制。`created_at` 为 `2026-11-13T01:47:26Z`。
  - 领域：自动控制 Control
  - 总 star：160
- [ekrrems/Stereo-inertial-slam](https://github.com/ekrrems/Stereo-inertial-slam)
  - 说明：用双目相机和 IMU 从零写一套视觉惯性 SLAM，同时出稀疏地图和稠密地图，并拿公开路测轨迹对一下误差。README 标题是 RigVis，实现是 C++17（Eigen、OpenCV、Ceres），IMU 融合用误差状态卡尔曼滤波。它在 KITTI 里程计序列 00（4544 帧，3.7 km）上写的相对平移误差是 1.20%，相对旋转是 0.50°/100 m，绝对轨迹误差均方根 2.81 m；同一张表引用的 ORB-SLAM2 双目论文数字是 0.70%、0.25°/100 m 和 1.3 m。仓库名里的 slam 计入自动控制。搜索描述没有这些数字。`created_at` 为 `2026-11-01T17:38:10Z`。
  - 领域：自动控制 Control
  - 总 star：89

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=2`、`per_page=5`，本页是各查询按总 star 排序后的第 6 到第 10 条。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：给 ESP32 做的灯带固件，用 Wi-Fi 控制可寻址灯珠，从一条灯带到二维矩阵都能配。搜索描述写的是用 ESP32 经 Wi-Fi 控制 WS2812B 等数字 RGB 灯。README 写支持 ESP32 原版以及 S2、S3、C3，并行输出最多 17 路。文件名是 `readme.md`。README 全文没有 ESP8266，话题仍含 esp8266。
  - 领域：嵌入式 Embedded
  - 总 star：19119
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：面向单片机、WebAssembly 和命令行的 Go 编译器，基于 LLVM，让同一段 Go 能在很小的板上跑。README 写可以编译到 150 种以上的微控制器板。话题含 esp32 与 stm32。
  - 领域：嵌入式 Embedded
  - 总 star：17938
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：ESP32 系列芯片的 Arduino 核心，让 Arduino 的写法跑在乐鑫芯片上。README 写有从 2.x 迁到 3.x 的说明。话题含 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：17801
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：给 RepRap 3D 打印机用的固件，8 位和 32 位微控制器都能跑。搜索描述写它覆盖常见平台，不少商品打印机出厂就装着它。README 写 2.1 支持 32 位 ARM 和 8 位 AVR，并写到最多 9 个联动轴、8 个挤出机。话题含 esp32 与 firmware。这是打印机固件，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：17684
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：给资源很少的设备用的实时操作系统，从简单传感器到网关都能跑，并按安全来设计。搜索描述写它是可扩展、经过优化的安全 RTOS。README 写内核覆盖 ARM Cortex-M/R/A、x86、RISC-V 等架构。话题含 embedded、rtos 与 zephyr。文件名是 `README.rst`。
  - 领域：嵌入式 Embedded
  - 总 star：17179
- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd)
  - 说明：给 Flipper Zero 和 ESP32 做的特斯拉 CAN 工具，搜索描述里包含电池管理系统仪表和总线抓取。设备本身是 CAN 与 ESP32，所以完整条目放在嵌入式；电力电子只因描述里的 BMS 仪表一行带过。搜索描述还写了区域解锁和 nag killer，这些做法不写入正文。这条来自电力电子常青检索，不在嵌入式本页前 5。话题含 can-bus，描述里的 ESP32 计入嵌入式。
  - 领域：嵌入式 Embedded
  - 总 star：1377

### AI

- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：给编程代理一个可以改成自己工作流的外壳，而不是逼人适应一套固定功能。搜索描述写的是统一的 LLM 接口、代理循环、终端界面和编程代理命令行。README 开头写它默认不做子代理和计划模式，缺的功能可以让它自己补，或装一个包。搜索话题为空，靠描述里的 LLM 计入。
  - 领域：AI
  - 总 star：123721
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：让模型在真实浏览器里把一件事做完的开源浏览器代理，另外提供隐匿浏览器和托管的代理 API。README 写模型在浏览器里写 Python，用一个持久的解释器和 Chrome 调试协议操作页面，并要求安装钉在 1.0.8（用 `==`，不要 `>=`）。话题含 llm 与 ai-agents。话题里的 mcp 不是本次 AI 关键词，不另计。
  - 领域：AI
  - 总 star：121935
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
  - 说明：给编程代理一套做网站的约束，用一套设计系统、真实照片和浏览器检查，而不是拼一个看起来像模板的落地页。README 写版本是 tasteskill 2.5.1，并写检查会在无头 Chrome 里按 1440、1024、768、390 四种宽度打开页面。话题含 ai-agents。搜索描述没有 llm 这个词。
  - 领域：AI
  - 总 star：121103

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。

- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：17。

### 电力电子电源 Power Supply

- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS 仪表，此处不展开。领域：电力电子电源 Power Supply。总 star：1377。
- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：用 ESPHome 经串口或蓝牙看一块极空电池管理系统的状态。搜索描述写的是监测并控制；README 开头写的是监测。README 写软件版本不低于 6.0 的机型走这套协议。话题 `jikong-bms` 按词边界计入 bms。README 的接线示例是 ESP32 或 ESP8266，搜索话题没有 esp32，不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：1057
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 主机和一台有线调制解调器做一套 12 V 磷酸铁锂直流不间断电源，停电时先撑住，电量见底前把主机关干净。README 写明威电源经 MOSFET 理想二极管浮充 10 Ah 电池，Victron BatteryProtect 做硬件低压断开，18 V 升压给现在的 N100DC 主机；这台主机从 2026-08-29 起改由本电源供电。监测固件是 ESPHome V1.20。2026-09-15 从起始到低压断开测得 2.5331 Ah / 31.821 Wh，并写明 2026 年 9 月以前包括约 4.18 Ah 在内的续航数字描述的是已经换掉的电池包和负载。搜索描述仍写 4.18 Ah。话题含 power-supply，所以完整条目放在电力电子；话题里的 mosfet 是理想二极管，功率器件一节一行带过。README 的监测板是 XIAO ESP32-C3，搜索话题没有 esp32，不跨到嵌入式。这条来自功率器件常青检索，不在电力电子本页前 5。
  - 领域：电力电子电源 Power Supply
  - 总 star：17

### 自动控制 Control

- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：用外观做回环的建图和定位库，并带一个独立程序。话题含 ros2 与 slam。README 写 ROS 支持在另一个仓库 `rtabmap_ros`，ROS 2 文档在那个仓库的 `ros2` 分支，ROS 1（Noetic）在另一条分支。
  - 领域：自动控制 Control
  - 总 star：4125
- [RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)
  - 说明：把机器人或视觉里的非线性误差画成图再一起优化，定位建图和光束法平差都能套这个框架，而不是每个问题重写求解器。搜索描述写的是通用图优化框架。话题含 slam。README 里的 “computer-vision” 不参与归类，搜索描述和话题没有这个词，不跨到 AI。
  - 领域：自动控制 Control
  - 总 star：3481
- [luigifreda/pyslam](https://github.com/luigifreda/pyslam)
  - 说明：一套视觉 SLAM 流水线，单目、双目和 RGB-D 都能跑，用来换特征、回环和稠密重建做实验，而不是只绑死一种算法。搜索描述写的就是这条混合 Python/C++ 流水线。README 标题是 pySLAM v2.13.0。话题含 slam。搜索描述和话题没有 computer-vision 或 pytorch，不跨到 AI。
  - 领域：自动控制 Control
  - 总 star：3439

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。本次跨节的是 flipper-tesla-fsd（嵌入式完整，电力电子一行）和 DIY-LiFePO4-UPS（电力电子完整，功率器件一行）。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API，下列仓库全部 HTTP 200。默认说明文件名是 `README.md` 的有：`jingyaogong/minimind`、`ngxson/esp32-usb-to-airprint`、`FlashCat-Jordan/Flashduck`、`tahaalakhras53-boop/dma-firmware-customization`、`zacharyinserra/deskhub`、`andrisgauracs/bevel-os`、`tinygo-org/tinygo`、`espressif/arduino-esp32`、`MarlinFirmware/Marlin`、`hypery11/flipper-tesla-fsd`、`wangzan101/Mika`、`mdiri-ai/SoduWork`、`expo/exact`、`simplexai-labs/linger`、`earendil-works/pi`、`browser-use/browser-use`、`Leonxlnx/taste-skill`、`wkcollis1-eng/DIY-LiFePO4-UPS`、`syssi/esphome-jk-bms`、`epilys/sic`、`darkfibr/artex-forensics`、`jacobvm04/slam-dunk`、`ekrrems/Stereo-inertial-slam`、`introlab/rtabmap`、`RainerKuemmerle/g2o`、`luigifreda/pyslam`、`inmusic-software/mpc-plugin-builder-sdk`、`EasyNavigation/StrataSLAM`、`vedderb/bldc`、`wlcrs/huawei_solar`。`wled/WLED` 的文件名是 `readme.md`。`zephyrproject-rtos/zephyr` 的文件名是 `README.rst`。`dma-firmware-customization` 的 README 没有 ESP32，身份改写的安装、配置和步骤未写入正文。`artex-forensics` 的漏洞步骤未写入正文。`flipper-tesla-fsd` 的区域解锁、封禁恢复和引脚接线未写入正文。`Claude-BugHunter` 的攻击步骤未写入正文。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 16 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`jingyaogong/minimind`（70152，727；描述含 LLM）。
- 核对：脚本解析出 16 条后，另一次 GET 同一 URL 仍是 HTTP 200，`<article class="Box-row">` 仍是 16 个，仓库集合和顺序相同，stars today 全部不变。总 star 有变化的是：`Claude-BugHunter` 21406→21411，`CLI-Anything` 64701→64702，`minimind` 70152→70155，`plugins` 19183→19186，`firecrawl` 208901→208902，`nginx` 33210→33212，`openvino` 12450→12451，`diagram-design` 71982→71986，`last30days-skill` 74167→74172，`stitch-skills` 12633→12635，`app-store-compliance` 5823→5825，`opensre` 15170→15172，`AFFiNE` 77965→77966，`Ghost-Downloader-3` 17283→17286，`autoclip` 15298→15300。`superpowers`（325769，1006）两次总 star 一致。正文用第一次解析的数字。今日页面本身有 16 条，不是解析丢条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`elementalsouls/Claude-BugHunter`（21406，1833；技能包，没有 `llm`，攻击步骤不写入正文）、`XiaoYouChR/Ghost-Downloader-3`（17283，1102）、`HKUDS/CLI-Anything`（64701，1075；把软件做成代理能调用的命令行，没有 `llm`）、`obra/superpowers`（325769，1006；代理技能框架，没有 `llm`）、`firecrawl/firecrawl`（208901，990；给代理做搜索和抓取，没有 `llm`）、`zhouxiaoka/autoclip`（15298，981；AI 视频剪辑，没有 `llm`）、`mjmirza/app-store-compliance`（5823，936；“AI coding agents” 是空格写法，不等于 `ai-agents`）、`cathrynlavery/diagram-design`（71982，794；图示设计，没有 `llm`）、`mvanhorn/last30days-skill`（74167，695；“AI agent skill”，没有 `llm`）、`toeverything/AFFiNE`（77965，589）、`Tracer-Cloud/opensre`（15170，408；CI/CD 代理，没有 `llm`）、`google-labs-code/stitch-skills`（12633，401；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`cursor/plugins`（19183，359；Cursor 插件规范）、`openvinotoolkit/openvino`（12450，187；“AI inference” 是弱词，没有 `llm`）、`nginx/nginx`（33210，158）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-26 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-26 stars:>2`。HTTP 200。`total_count=440`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`ngxson/esp32-usb-to-airprint`（348）、`FlashCat-Jordan/Flashduck`（189）、`tahaalakhras53-boop/dma-firmware-customization`（153）、`zacharyinserra/deskhub`（146）、`andrisgauracs/bevel-os`（134）。`deskhub` 的总 star 从昨日搜索的 131 到本次 146，排到 `bevel-os`（134）前面；昨日同页 `bevel-os` 是 132。`airprint` 的 `created_at` 为 `2026-10-26T16:18:54Z`，落在窗口起点当天。`Flashduck` 仍是 189，`dma-firmware-customization` 仍是 153。这些都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。窗口起点从昨日的 2026-10-25 移到 2026-10-26。`dma-firmware-customization` 的话题含 `esp32`，README 全文没有 ESP32。`Flashduck` 的搜索描述和话题都没有 `llm`。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-26 stars:>2`。HTTP 200。`total_count=2826`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（9865）、`mdiri-ai/SoduWork`（7608）、`expo/exact`（5056）、`simplexai-labs/linger`（4354）。`SoduWork` 的表标题现在写 Supported harnesses (7)，表内列出 7 个。`exact` 的 Bun 仍钉在 1.4.2。昨日同查询的总 star 是 Mika 9762、SoduWork 7050、exact 4970、linger 4184。这些都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。窗口起点移到 2026-10-26 后，昨日的 `qybaihe/bla`（`created_at` 为 `2026-10-25T05:25:45Z`）落在窗口外，本次前 5 没有它，不猜 star。
  - 未命中：`benjitaylor/skills`（总 star 4139；描述是 “Skills for AI coding agents.”，空格写法不等于 `ai-agents`，也没有 `llm`）。它排在 linger（4354）后面。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-26 stars:>2`。HTTP 200。`total_count=4`，返回 4，规则保留 0，未命中 4。剩余配额 25。4 条就是全部结果，不是接口少给。返回顺序按总 star 是 `zjy2968466837/SicnuJw`（7）、`EngineerHabib/DOKKHO-E_Commerce-Porject-SICIP`（4）、`SicoKaleb/SicoAutoTerms`（3）、`Arafat-shuvo/Sicip-data-science`（3）。两条 3 星的先后按接口返回，是 `SicoAutoTerms` 在前。星数与昨日这 4 条相同。
  - 名称词边界未命中：`SicnuJw`（四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`DOKKHO-E_Commerce-Porject-SICIP`（名称 `SICIP` 不等于 `sic`，搜索描述为空）、`SicoAutoTerms`（`Sico` 不等于 `sic`，描述与碳化硅无关）、`Sicip-data-science`（`Sicip` 不等于 `sic`，描述是署名，与碳化硅无关）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-26 stars:>2`。HTTP 200。`total_count=74`，返回 5，规则保留 1，未命中 4。剩余配额 23。规则留下的 1 条是公司后缀，剔除后没有新项目。按总 star，本页是 `acrobat-dc-desktop`（210）、`isometric-cities`（92）、`mvc2-naomi-dc`（80）、`artex-forensics`（78）、`grid-dca-bot`（49）。
  - 撞名剔除：`darkfibr/artex-forensics`（总 star 78，`created_at` 为 `2026-11-14T21:27:55Z`）。描述末尾是 Blackfish Security LLC。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。漏洞步骤不写入正文。
  - 名称和搜索描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（210；Acrobat DC 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（92；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`gibletto/mvc2-naomi-dc`（80；NAOMI 街机的反编译移植，名称里的 dc 不等于 `dc-dc`）、`leftamber/grid-dca-bot`（49；加密货币网格交易，名称里的 DCA 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-26 stars:>2`。HTTP 200。`total_count=105`，返回 5，规则保留 3，未命中 2。剩余配额 21。正文保留 `jacobvm04/slam-dunk`（160）、`ekrrems/Stereo-inertial-slam`（89）。`slam-dunk` 的总 star 与昨日搜索相同，仍是 160。`Stereo-inertial-slam` 昨日搜索是 80，本次是 89；这是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。昨日的 `be2rlab/ACCORD` 不在本次前 5，不猜 star。按总 star，本页顺序是 `mpc-plugin-builder-sdk`（217）、`slam-dunk`（160）、`SampQOL-OS`（133）、`Stereo-inertial-slam`（89）、`StrataSLAM`（86）。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 217）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。README 还写 MPC Sample 要固件 v1.4.0 或更新，只做效果。描述里的 “AI coding agent” 是空格写法，不等于 `ai-agents`。
  - 名称和 topics 未命中：`snarebes/SampQOL-OS`（总 star 133；描述里的 Akai MPC Sample 不是强特征词，名称也不含 `mpc`）。`EasyNavigation/StrataSLAM`（总 star 86；搜索描述为空，名称 `StrataSLAM` 里 slam 前面是字母，词边界不等于 `slam`）。README 写的是多层 ROS 2 SLAM，不参与归类，正文不收。

### C. 领域常青（`pushed:>=2026-11-18 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-18 stars:>3`。HTTP 200。`total_count=1353`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=2`、`per_page=5`，本页是总结果里按总 star 排序后的第 6 到第 10 条。本查询正文：`wled/WLED`（19119）、`tinygo-org/tinygo`（17938）、`espressif/arduino-esp32`（17801）、`MarlinFirmware/Marlin`（17684）、`zephyrproject-rtos/zephyr`（17179）。另有 1 条完整条目不在本页前 5：`hypery11/flipper-tesla-fsd`（1377，来自电力电子检索，话题含 can-bus、描述含 esp32，设备更贴近嵌入式）。`WLED` 的文件名是 `readme.md`，全文没有 ESP8266，话题仍含 esp8266。`zephyr` 的文件名是 `README.rst`。`Marlin` 是 3D 打印机固件，不是公开课清单。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-18 stars:>3`。HTTP 200。`total_count=9423`，返回 5，规则保留 3，排除清单 1，未命中 1。剩余配额 26。正文保留 `earendil-works/pi`（123721）、`browser-use/browser-use`（121935）、`Leonxlnx/taste-skill`（121103）。按总 star，本页顺序是 awesome-llm-apps、pi、browser-use、taste-skill、agent-skills。`page=2` 是总结果里的第 6 到第 10 条。`pi` 话题为空，靠描述里的 LLM 计入。`browser-use` 靠话题 `llm` 与 `ai-agents`；README 现在把安装钉在 1.0.8，不再是先前记录的 1.0.8rc1。`taste-skill` 靠话题 `ai-agents`，README 写版本 tasteskill 2.5.1。
  - 清单类排除：`Shubhamsaboo/awesome-llm-apps`（总 star 145602；仓库名命中 awesome，描述是合集）。它排在本页第 1，正文不收。
  - 未命中：`addyosmani/agent-skills`（总 star 120197；描述是 “skills for AI coding agents”，空格写法不等于 `ai-agents`，也没有 `llm`）。它排在 taste-skill 后面。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-18 stars:>3`。HTTP 200。`total_count=30`，返回 5，规则保留 2，未命中 3。剩余配额 24。`page=2` 是总结果里按总 star 排序后的第 6 到第 10 条。`total_count=30`，本页 5 条不是末页，也不是接口失败。规则保留的 2 条里，1 条撞名剔除，1 条更贴近电力电子，本节只留一行。本页按总 star 的顺序是 `SICAP.ai`（96）、`epilys/sic`（27）、`DIY-LiFePO4-UPS`（17）、`SICTIC-AI`（14）、`SickGear.Docker`（13）。
  - 撞名剔除：`epilys/sic`（总 star 27）。名称命中 `sic`。描述和 README 写明这是按标签组织的链接聚合，不用 JavaScript，不是碳化硅器件，正文不收。
  - 名称词边界未命中：`sicap-pro/SICAP.ai`（96；罗马尼亚公共采购检索，`SICAP` 不等于 `sic`）、`ducroo/SICTIC-AI`（14；瑞士商业天使俱乐部 SICTIC，`SICTIC` 不等于 `sic`）、`SickGear/SickGear.Docker`（13；`SickGear` 不等于 `sic`）。
  - `wkcollis1-eng/DIY-LiFePO4-UPS`（总 star 17）：话题含 mosfet 与 power-supply。完整条目在电力电子，本节一行带过。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-18 stars:>3`。HTTP 200。`total_count=419`，返回 5，规则保留 2，未命中 3。剩余配额 22。`page=2` 是总结果里按总 star 排序后的第 6 到第 10 条。正文完整条目为 `syssi/esphome-jk-bms`（1057）。`hypery11/flipper-tesla-fsd`（1377）描述含 BMS，完整条目在嵌入式，本节一行。另有 1 条完整条目来自功率器件检索：`DIY-LiFePO4-UPS`（17，话题含 power-supply 与 mosfet）。按总 star，本页顺序是 `flipper-tesla-fsd`、`dcm2niix`、`esphome-jk-bms`、`huawei_solar`、`dcmtk`。
  - 名称、话题和搜索描述未命中电力电子：`rordenlab/dcm2niix`（1212；DICOM 转 NIfTI，`dcm` 不等于 `dc-dc`）、`wlcrs/huawei_solar`（954；描述里的 “Solar inverters” 是复数，不等于 `inverter`；话题含 `modbus`，不在嵌入式常青前 5，不跨节）、`DCMTK/dcmtk`（920；DICOM 实现，`dcmtk` 不等于 `dc-dc`）。
  - `esphome-jk-bms` 的 README 写了 ESP32/ESP8266 接线，搜索话题没有 esp32，不跨嵌入式。`DIY-LiFePO4-UPS` 的 README 写了 XIAO ESP32-C3，搜索话题没有 esp32，不跨嵌入式；搜索描述仍写 4.18 Ah，README 写 2026-09-15 测得 2.5331 Ah。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-18 stars:>3`。HTTP 200。`total_count=233`，返回 5，规则保留 3，未命中 1，排除清单 1。剩余配额 29。正文保留 `introlab/rtabmap`（4125）、`RainerKuemmerle/g2o`（3481）、`luigifreda/pyslam`（3439）。按总 star，本页顺序是 rtabmap、bldc、g2o、pyslam、awesome-robotics-libraries。本次响应头的剩余配额是 29，前一条自动控制新项目是 21，中间没有失败重试。两次搜索间隔 7 秒，前面的请求已经跨过一分钟，配额窗口滚动，按响应头原样记录。
  - 未命中：`vedderb/bldc`（总 star 3590）。描述是 “The VESC motor control firmware”，“motor control” 是空格，不等于 `motor-control`。名称 `bldc` 不在控制关键词表里；`bldc` 只在强特征描述词里，这条描述没有 `bldc`，正文不收。它夹在 rtabmap（4125）和 g2o（3481）之间。
  - 清单类排除：`jslee02/awesome-robotics-libraries`（总 star 3121；仓库名命中 awesome，话题含 slam）。正文不收。
  - `g2o` 的 README 有 “computer-vision”，搜索描述和话题没有，不跨 AI。`pyslam` 的 README 标题是 v2.13.0，搜索描述和话题没有 computer-vision 或 pytorch，不跨 AI。`rtabmap` 的 README 写 ROS 2 文档在 `rtabmap_ros` 的 `ros2` 分支。
