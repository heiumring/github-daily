# GitHub 领域日报 · 2026-11-23

生成时间：2026-11-23 07:40（北京时间）。数据拉取开始于 2026-11-23 07:35:17（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-24（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-16 及之后有推送、总 star > 3。轮换页 `page = (当年第 327 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 让人用自己的显卡从零训一个大约 64M 的小模型，而不是只调用现成的大模型；总 star 68626，24 小时新增 star 473。这是今日热度里唯一命中领域的仓库。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 9631，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) 把一本从零实现类 GPT 模型的书配上可运行的代码，用来自己走完预训练和微调；总 star 108839，没有 24 小时新增数据。这是本页常青里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 16 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

嵌入式、功率器件、电力电子电源、自动控制在这 16 条里都没有命中。

### AI

- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
  - 说明：把大模型的训练过程拆到个人显卡上能跑完，用来看懂预训练、微调和对齐，而不是只调一个封装好的接口。README 写主线最小版本大约 64M，并用 PyTorch 从零实现整条训练链路。同一段注明「2 小时」是监督微调阶段在单张 NVIDIA 3090 上跑完 1 个 epoch 的实测，「3 块钱」是这段时间的租卡费用。搜索描述里的 LLM 计入 AI。
  - 领域：AI
  - 总 star：68626
  - 24 小时新增 star：473

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [Kristian8606/esp32-airplay2-surround](https://github.com/Kristian8606/esp32-airplay2-surround)
  - 说明：用便宜的板子自己组一套无线环绕声。README 写明 Apple TV 只看到网关这一台 AirPlay 2 音箱，网关把 5.1 / 7.1 码流原样分给音箱板，每块 ESP32-S3 只解码自己的声道。目前写明网关加五只音箱（前左右、中置、两侧）已经能同步播放 5.1 和 7.1，iPhone 的立体声也能跟上；闪存建议买 16 MB 的 N16R8，8 MB 板仍能编译，音箱固件副本只剩大约 117 KB。搜索描述为空，话题也为空，只靠仓库名里的 esp32 归入嵌入式。`created_at` 为 `2026-10-24T16:13:06Z`。
  - 领域：嵌入式 Embedded
  - 总 star：407
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。表格里 MG2500 系列的 MG2550S 标成绿，意思是已在真机验证；其余型号标成黄，预期能用但还没上真机。
  - 领域：嵌入式 Embedded
  - 总 star：347
- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑；ESP-IDF 6.0.1 起，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：187
- [tahaalakhras53-boop/dma-firmware-customization](https://github.com/tahaalakhras53-boop/dma-firmware-customization)
  - 说明：仓库自称是一份给 PCIe DMA 板改写固件身份、让主机把它认成别的设备的说明。README 标题是 “DMA Firmware Customization — Security Tool”，搜索描述写成针对 PCIe Screamer Squirrel 的硬件混淆指南。这是在总线上隐瞒设备身份，正文不写安装、配置和改写步骤。话题含 embedded 与 esp32，仓库名含 firmware，因此归入嵌入式；README 全文没有 ESP32，不把话题里的 esp32 写成这块板的主控。话题里同时有 adc、battery-monitor、hub75、oled 等和这份说明对不上的标签。`created_at` 为 `2026-11-15T19:45:19Z`。
  - 领域：嵌入式 Embedded
  - 总 star：153
- [andrisgauracs/bevel-os](https://github.com/andrisgauracs/bevel-os)
  - 说明：在一块 ESP32-S3 上跑一个能开窗口的小桌面，用六只电阻把 640×480、64 色的画面送到 VGA 显示器。README 写它由模型 Claude Fable 5.2 写成，人负责接线和 3D 打印；开机到桌面 0.7 秒，窗口里的 Doom（共享版 E1M1）大约 32 帧。硬件写明 16 MB 闪存、8 MB 八线 PSRAM 的 N16R8，系统跑在 ESP-IDF 5.5.3 和 FreeRTOS 上。搜索描述里的 ESP32-S3 按词边界计入 esp32。`created_at` 为 `2026-11-14T14:18:34Z`。
  - 领域：嵌入式 Embedded
  - 总 star：128

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：9631
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
  - 说明：给团队自托管的一件工作引擎。提一句需求不算做完，要等提出的人签收；可以指定一个代理干活，另一个代理按验收标准复查，不过就退回。README 首页列出 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code、Codex Harness 和 Codex。展开的表标题写支持 9 个 harness，表里实际列出这 7 个，没有写出的两个不计入。README 写目前是公开测试。话题含 llm 与 ai-agents。`created_at` 为 `2026-10-29T02:43:14Z`。
  - 领域：AI
  - 总 star：6815
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给作者和安全团队保护自己即将发布的程序，让自动做逆向的语言模型代理在受保护的产物上得不到可用结果。README 徽章写 npm 包 `bla-agents` v3.5.7，并写明在 14 个对照目标上验证过。话题 `llm-security` 按词边界计入 llm。防护参数和绕过细节不写入正文。
  - 领域：AI
  - 总 star：6426
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、iOS、macOS、Android 和 Linux 上按各自的原生控件跑，编程代理可以自己建、自己跑、自己看、自己测。README 写界面用一种叫 Contract 的声明式语言，布局和属性名沿用 CSS；网页产物是大约 20 KB 的运行时。Android 写明已经能用，Material 3 的打磨还在进行；Windows 仍在早期。仓库仍是 pre-1.0，没有打包发布，并写 Bun 钉在 1.4.2。搜索描述只写了网页、macOS、iOS 和 Linux，Android 的状态来自 README。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：4918

### 功率器件 Power Devices

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

本窗口没有以功率器件为最贴近领域的完整新项目。名称撞上 `sic` 的课堂笔记本已剔除。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。返回的 5 条里，1 条是公司后缀 LLC，不是谐振变换器；另外 4 条的名称、话题和搜索描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`。详见数据源状态。

### 自动控制 Control

- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：给第一人称、野外长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参。README 写一套常规的离线光束法平差能缩小和行业系统的差距，但会停在公开提交的水平；把这两项物理现象放进同一条流水线后，LaMAria 训练集的控制点分数从 69.1 到 82.4。它在 LaMAria 测试集上与 Aria 的 SLAM 打平，并在五个类别里的三个上第一次超过 Aria，UZH-FPV 排行榜上排第二。仓库名里的 slam 计入自动控制。`created_at` 为 `2026-11-13T01:47:26Z`。
  - 领域：自动控制 Control
  - 总 star：157
- [be2rlab/ACCORD](https://github.com/be2rlab/ACCORD)
  - 说明：只用一台相机和一只 IMU，在线做出带闭环的度量稠密地图。README 写 OpenVINS 负责跟踪相机，Depth Anything 3 给关键帧窗口出深度，再放进位姿图里用回环修正。默认深度模型是 DA3-Giant，README 写显存大约 24 GB；换成 DA3-Base 大约 6 GB。话题含 slam。`created_at` 为 `2026-11-04T15:37:22Z`。
  - 领域：自动控制 Control
  - 总 star：72
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用一个水箱、超声测距和一台泵，把通断、P 和 PI 液位控制做成可以对照仿真的实验。README 写实验台是 15 L 罐子，由 500 L 水箱经一台约 0.5 马力、230 V 的泵补水，市电泵走 Fotek SSR-40DA，直流泵则用 MOSFET 做 PWM；MATLAB 应用的物理量来自你自己的水箱、出口和泵，徽章写 MATLAB R2023b 及以上。2026-10-26 的实测写明当天罐子还没有排水口，靠手倒空，超调是 2.8 cm（11% 到 13%）。话题含 control-systems，话题 `pid-control` 按词边界计入 pid。水位控制比 MOSFET 开关更贴近本领域，功率器件一节一行带过。这条来自功率器件新项目检索，不在自动控制本页前 5。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=4`、`per_page=5`，本页是各查询按总 star 排序后的第 16 到第 20 条。

### 嵌入式 Embedded

- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：把一块 ESP32 变成室内的 Wi-Fi 动作传感器。人走过会改变信号怎么传播，它据此报告有没有人在动，不用摄像头、麦克风或专用雷达。README 写可经 ESPHome 或 MQTT 进 Home Assistant，也能作为 Matter 占用传感器，并可用 C++ SDK 或 Arduino-ESP32 嵌进自己的固件。搜索描述写了 C++ SDK、ESPHome、Native、Matter 和一条管设备全生命周期的命令行。话题含 embedded；话题是 `esp-32`，不等于 `esp32`，描述里的 ESP32 计入。
  - 领域：嵌入式 Embedded
  - 总 star：9853
- [crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)
  - 说明：给几款电子纸阅读器写的开源固件，让这些机器能读 EPUB，而不只靠出厂软件。搜索描述写的就是开源电子纸阅读器固件。README 按芯片分成 ESP32-C3（Xteink X4、X3）和 ESP32-S3（X4Pro、X4Classic 等）两类机器。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：8931
- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的官方设备固件，用来做不依赖蜂窝和互联网的远距离、低功耗网格通信。搜索描述写的是 off-grid mesh。README 这一段列出的硬件是 ESP32、nRF52、RP2040/RP2350 和 Linux；话题另含 stm32，这段名单没有把 STM32 写进去。话题含 esp32，仓库名含 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：8620
- [nodemcu/nodemcu-firmware](https://github.com/nodemcu/nodemcu-firmware)
  - 说明：用 Lua 交互式地写 ESP8266、ESP8285 和 ESP32 的固件，不用从 C 工具链重头搭一套。搜索描述写明这三块芯片。README 写明 `release` 和 `dev` 分支面向 ESP8266，`dev-esp32` 才面向 ESP32。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：7961
- [FastLED/FastLED](https://github.com/FastLED/FastLED)
  - 说明：给灯带写彩色动画的库，换板子时不用重写时序。搜索描述写它面向 Arduino，并请人把求助发到 Reddit，GitHub issues 只跟踪缺陷和增强。README 写它也能跑在 ESP32、Teensy 和另外 50 多种平台上，并写 ESP32-C2 的支持是在 3.9.10 加上的。话题含 embedded 与 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：7539
- [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library) — 见下方「自动控制 Control」完整条目。话题含 embedded 与 mcu，此处不展开。领域：嵌入式 Embedded。总 star：1175。

### AI

- [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
  - 说明：把一本从零实现类 GPT 模型的书配上可运行的代码，用来自己走完预训练和微调，而不是只调现成接口。README 写这是 *Build a Large Language Model (From Scratch)* 的官方代码仓库，ISBN 9781633437166，并用 PyTorch 实现。话题含 llm 与 pytorch。这是一本书的配套代码，不是外部公开课清单，正文保留。
  - 领域：AI
  - 总 star：108839
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：给 Python 一套带 GPU 加速的张量计算和动态神经网络，训练和推理都从这里搭。README 写它提供类似 NumPy 的张量运算，以及基于磁带的自动求导。仓库名 `pytorch` 计入 AI。话题里没有再单独标 `pytorch`。
  - 领域：AI
  - 总 star：105828
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：把大模型的推理服务做成高吞吐、省显存的引擎，让请求连续进来也能打满 GPU。README 写它用 PagedAttention 管理注意力的键值缓存，并做连续批处理。仓库名 `vllm` 按词边界不等于 `llm`，归类靠话题 `llm`，话题里还有 pytorch 与 transformer。搜索描述写的是面向 LLMs 的推理和服务引擎，复数 LLMs 本身不等于 llm。
  - 领域：AI
  - 总 star：97361
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：给代理抓网页、抽成 Markdown 或结构化数据，也可以自己把爬虫架起来。README 写托管接口每月送 1000 额度、不需要信用卡；本仓库是驱动它的 Apache-2.0 爬虫，可以用 Python 或 Docker 自托管。话题含 llm 与 ai-agents。话题里的 mcp 不是本次 AI 关键词，不另计。
  - 领域：AI
  - 总 star：87676

### 功率器件 Power Devices

- [SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark)
  - 说明：给半导体器件的 SPICE 模型做一套自动核对，看模型在直流、瞬态、交流和噪声下是否站得住，而不是只靠人工点一次仿真。README 写重点是 MOSFET，并能把 HSPICE、Spectre 转成 ngspice 再跑。归类靠仓库名 `spice`。搜索描述里的 MOSFETs 是复数，词边界不等于 mosfet，不另计。README 的安装示例仍写着 `yourusername/spice_model_benchmark`，不是本仓库的组织名。`pushed_at` 为 `2026-11-22T11:06:13Z`。
  - 领域：功率器件 Power Devices
  - 总 star：10

### 电力电子电源 Power Supply

- [springfall2008/batpred](https://github.com/springfall2008/batpred)
  - 说明：在 Home Assistant 里预测家用电池什么时候充、什么时候放，并按电价去执行，而不是只看逆变器当前功率。README 列出 GivEnergy、Solis、华为、SolarEdge、SigEnergy、FoxESS、Sofar、Tesla Powerwall 等，并写另有一个付费的 PredBat Cloud，本仓库个人使用仍开源。话题 `solax-inverter` 按词边界计入 inverter；话题 `solis-pv-inverters` 是复数，不计入 inverter。搜索描述里的 “inverter types” 计入。`pushed_at` 为 `2026-11-22T22:18:21Z`。
  - 领域：电力电子电源 Power Supply
  - 总 star：380
- [patman15/BMS_BLE-HA](https://github.com/patman15/BMS_BLE-HA)
  - 说明：在 Home Assistant 里用蓝牙读电池管理系统的电芯电压和电流，装好后不用逐台填配置。README 写可以读单节电芯电压来看电池健康，并用 ESPHome 蓝牙代理扩大覆盖。话题含 `jikong-bms`、`daly-bms`、`jbd-bms`、`seplos-bms`，按词边界计入 bms。搜索话题没有 esp32，不跨到嵌入式。`pushed_at` 为 `2026-11-22T19:40:13Z`。
  - 领域：电力电子电源 Power Supply
  - 总 star：380

### 自动控制 Control

- [google-deepmind/mujoco_mpc](https://github.com/google-deepmind/mujoco_mpc)
  - 说明：在 MuJoCo 里实时做预测控制，用来编写和求解机器人任务，而不是只回放一段轨迹。README 写它来自 Google DeepMind，基于打靶的规划器里，要导数的有 iLQG 和梯度下降，不要导数的有 Predictive Sampling。话题含 mpc 与 motor-control。
  - 领域：自动控制 Control
  - 总 star：1774
- [NVIDIA-ISAAC-ROS/isaac_ros_visual_slam](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam)
  - 说明：给机器人一套用双目相机做的视觉 SLAM，在 GPS 不好用的室内或楼群里估计自己相对起点走了多远。README 写它可以用一路或多路双目，可选 IMU，GPU 加速，既能给地面机器人当附加里程计，也能给无人机当主里程计。话题含 ros2 与 slam。名称和描述里的 cuVSLAM 不等于 slam，归类靠话题。README 有一场按需研讨会，标题里写着 250 fps。
  - 领域：自动控制 Control
  - 总 star：1500
- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用肌肉骨骼模型在 MuJoCo 里做运动控制任务，研究对象是肌肉和关节，不是电机驱动器。搜索描述写这些环境包在 OpenAI gym API 里。README 写 MyoSuite 3 的同一个 env_id 可以走 Gymnasium 的 CPU 接口，也可以走 mjlab 在单张 GPU 上并行，另有一条实验性的 MJX 路径；2.x 训出来的策略可能要重训。话题含 motor-control。
  - 领域：自动控制 Control
  - 总 star：1290
- [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library)
  - 说明：在 MCU 上跑永磁同步电机的磁场定向控制，有感、无感和霍尔都能接，从坐标变换做到 SVPWM。README 徽章写版本 3.1.0，并写位置环、速度环、电流环可以单环或串级，控制器含 PID 和 LADRC。话题含 foc、motor-control 与 pid。磁场定向控制比「跑在 MCU 上」更贴近本领域，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：1175

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。本次跨节的是水位实验（功率器件一行，自动控制完整）和 SguanFOC（嵌入式一行，自动控制完整）。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API，下列仓库全部 HTTP 200，默认说明文件名都是 `README.md`：`jingyaogong/minimind`、`Kristian8606/esp32-airplay2-surround`、`ngxson/esp32-usb-to-airprint`、`FlashCat-Jordan/Flashduck`、`tahaalakhras53-boop/dma-firmware-customization`、`andrisgauracs/bevel-os`、`wangzan101/Mika`、`mdiri-ai/SoduWork`、`qybaihe/bla`、`expo/exact`、`Samarth030312/arduino-water-level-control-lab`、`sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`、`SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark`、`darkfibr/artex-forensics`、`springfall2008/batpred`、`patman15/BMS_BLE-HA`、`inmusic-software/mpc-plugin-builder-sdk`、`jacobvm04/slam-dunk`、`be2rlab/ACCORD`、`google-deepmind/mujoco_mpc`、`Vincentqyw/cv-arxiv-daily`、`NVIDIA-ISAAC-ROS/isaac_ros_visual_slam`、`MyoHub/myosuite`、`Sguan-ZhouQing/SguanFOC_Library`、`rasbt/LLMs-from-scratch`、`pytorch/pytorch`、`vllm-project/vllm`、`unclecode/crawl4ai`、`francescopace/espectre`、`crosspoint-reader/crosspoint-reader`、`meshtastic/firmware`、`nodemcu/nodemcu-firmware`、`FastLED/FastLED`。`dma-firmware-customization` 的 README 没有 ESP32，身份改写的安装、配置和步骤未写入正文。`artex-forensics` 的 README 只用来确认公司后缀，其中的漏洞复现步骤未写入正文。`bla` 的防护参数和绕过细节未写入正文。`Claude-BugHunter` 的攻击步骤未写入正文。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 16 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`jingyaogong/minimind`（68626，473；描述含 LLM）。
- 核对：脚本解析出 16 条后，另一次 GET 同一 URL 仍是 HTTP 200，`<article class="Box-row">` 仍是 16 个，仓库集合和顺序相同，stars today 全部不变。总 star 有变化的是：`Claude-BugHunter` 17726→17727，`CLI-Anything` 62751→62754，`plugins` 18426→18428，`firecrawl` 207004→207005，`last30days-skill` 72686→72687，`app-store-compliance` 3955→3956，`Ghost-Downloader-3` 15097→15099。`minimind`（68626，473）、`superpowers`（324138，785）、`nginx`（32881，168）、`openvino`（12087，155）、`diagram-design`（70278，513）、`stitch-skills`（11900，516）、`AFFiNE`（76801，537）、`autoclip`（13407，640）、`opensre`（14394，395）两次一致。正文用第一次解析的数字。今日页面本身有 16 条，不是解析丢条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`elementalsouls/Claude-BugHunter`（17726，1721；技能包，没有 `llm`，攻击步骤不写入正文）、`firecrawl/firecrawl`（207004，910；给代理做搜索和抓取，没有 `llm`）、`obra/superpowers`（324138，785；代理技能框架，没有 `llm`）、`XiaoYouChR/Ghost-Downloader-3`（15097，690）、`HKUDS/CLI-Anything`（62751，687；把软件做成代理能调用的命令行，没有 `llm`）、`mvanhorn/last30days-skill`（72686，673；“AI agent skill”，没有 `llm`）、`zhouxiaoka/autoclip`（13407，640；AI 视频剪辑，没有 `llm`）、`mjmirza/app-store-compliance`（3955，617；“AI coding agents” 是空格写法，不等于 `ai-agents`）、`toeverything/AFFiNE`（76801，537）、`google-labs-code/stitch-skills`（11900，516；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`cathrynlavery/diagram-design`（70278，513；图示设计，没有 `llm`）、`Tracer-Cloud/opensre`（14394，395；CI/CD 代理，没有 `llm`）、`cursor/plugins`（18426，301；Cursor 插件规范）、`nginx/nginx`（32881，168）、`openvinotoolkit/openvino`（12087，155；“AI inference” 是弱词，没有 `llm`）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-24 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-24 stars:>2`。HTTP 200。`total_count=437`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`Kristian8606/esp32-airplay2-surround`（407）、`ngxson/esp32-usb-to-airprint`（347）、`FlashCat-Jordan/Flashduck`（187）、`tahaalakhras53-boop/dma-firmware-customization`（153）、`andrisgauracs/bevel-os`（128）。`esp32-airplay2-surround` 的搜索描述和话题都为空，只靠仓库名 `esp32`。`Flashduck` 的 `created_at` 为 `2026-10-31T05:10:09Z`，搜索描述和话题都没有 `llm`，不跨到 AI。`dma-firmware-customization` 的 `created_at` 为 `2026-11-15T19:45:19Z`，话题含 `esp32`，README 全文没有 ESP32。`bevel-os` 的 `created_at` 为 `2026-11-14T14:18:34Z`，搜索描述里的 ESP32-S3 计入 esp32。窗口起点从昨日的 2026-10-23 移到 2026-10-24。这 5 条的 `created_at` 都晚于或等于 2026-10-24，仍在窗口内。昨日同查询的总 star 分别是 403、345、186、153、127；本次是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-24 stars:>2`。HTTP 200。`total_count=2786`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（9631）、`mdiri-ai/SoduWork`（6815）、`qybaihe/bla`（6426）、`expo/exact`（4918）。`exact` 的 `created_at` 为 `2026-11-02T01:29:01Z`。`Mika` 的 `created_at` 为 `2026-10-29T14:34:07Z`。`SoduWork` 的 `created_at` 为 `2026-10-29T02:43:14Z`。`bla` 的 npm 徽章仍为 v3.5.7。`SoduWork` 的表标题写 9 个 harness，表内列出 7 个。昨日同查询的总 star 是 Mika 9448、SoduWork 6439、bla 6378、exact 4874；本次都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
  - 未命中：`benjitaylor/skills`（总 star 4001；描述是 “Skills for AI coding agents.”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。按总 star 它是返回的第 5 条，排在 `exact`（4918）之后。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-24 stars:>2`。HTTP 200。`total_count=6`，返回 5，规则保留 2，未命中 3。剩余配额 25。`total_count` 比返回条数多 1，第 6 条没有返回，不猜测它是谁。规则保留的 2 条里，1 条是课堂笔记本，剔除；1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9），其次是课堂笔记本（7），然后是 `SicnuJw`（6），`DOKKHO-E_Commerce-Porject-SICIP`（4），`SicoAutoTerms`（3）。
  - `sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`（总 star 7）：名称含 SIC，搜索描述为空。README 标题写明这是 Samsung Innovation Campus 2026 的 PA-C 与 PA-D 课堂材料，含 Google Colab 笔记本，没有讲师姓名；正文有一处仍把项目写成 SIC 2025。与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-24T17:55:41Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（6；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`EngineerHabib/DOKKHO-E_Commerce-Porject-SICIP`（4；名称 `SICIP` 不等于 `sic`，搜索描述为空）、`SicoKaleb/SicoAutoTerms`（3；`Sico` 不等于 `sic`，描述与碳化硅无关）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-24 stars:>2`。HTTP 200。`total_count=79`，返回 5，规则保留 1，未命中 4。剩余配额 23。规则留下的 1 条是公司后缀，剔除后本日无新项目。按总 star，本页是 `acrobat-dc-win`（351）、`acrobat-dc-desktop`（210）、`acrobat-dc-win`（164）、`isometric-cities`（90）、`artex-forensics`（78）。
  - 撞名剔除：`darkfibr/artex-forensics`（总 star 78）。README 标题是 “ARTEX Forensics — Blackfish Security LLC”，搜索描述末尾也是 Blackfish Security LLC。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。搜索描述和话题没有 `llm`，不因 README 里的字样跨到 AI。漏洞复现步骤未写入正文。
  - 名称、话题和搜索描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`NileshLiu/acrobat-dc-win`（351；Acrobat DC 不等于 `dc-dc`）、`cindy-murray-39/acrobat-dc-desktop`（210；Acrobat DC 不等于 `dc-dc`）、`colealina/acrobat-dc-win`（164；Acrobat DC 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（90；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-24 stars:>2`。HTTP 200。`total_count=109`，返回 5，规则保留 3，未命中 2。剩余配额 21。正文保留 `jacobvm04/slam-dunk`（157）、`be2rlab/ACCORD`（72）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`ACCORD` 的 `created_at` 为 `2026-11-04T15:37:22Z`。按总 star，本页顺序是 `mpc-plugin-builder-sdk`（204）、`slam-dunk`（157）、`SampQOL-OS`（129）、`melodee-sample`（73）、`ACCORD`（72）。昨日报告里的 `ASIG-X/RESPLE2` 不在本次前 5，不猜它现在的 star。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 204）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。描述里的 “AI coding agent” 是空格写法，不等于 `ai-agents`。
  - 名称和 topics 未命中：`snarebes/SampQOL-OS`（总 star 129；描述里的 Akai MPC Sample 不是强特征词，名称也不含 `mpc`）、`keremimo/melodee-sample`（总 star 73；描述里的 Akai MPC Sample 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-16 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-16 stars:>3`。HTTP 200。`total_count=1339`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=4`、`per_page=5`，本页是总结果里按总 star 排序后的第 16 到第 20 条。本查询正文：`francescopace/espectre`（9853）、`crosspoint-reader/crosspoint-reader`（8931）、`meshtastic/firmware`（8620）、`nodemcu/nodemcu-firmware`（7961）、`FastLED/FastLED`（7539）。另有 1 条一行不在本页前 5：`Sguan-ZhouQing/SguanFOC_Library`（1175，话题含 embedded 与 mcu，完整条目在自动控制）。`espectre` 的话题是 `esp-32`，不等于 `esp32`，描述里的 ESP32 计入，话题 `embedded` 也计入。`nodemcu` 的 README 写 `release` 与 `dev` 面向 ESP8266，`dev-esp32` 才面向 ESP32。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-16 stars:>3`。HTTP 200。`total_count=9450`，返回 5，规则保留 4，排除清单 0，未命中 1。剩余配额 26。正文保留 `rasbt/LLMs-from-scratch`（108839）、`pytorch/pytorch`（105828）、`vllm-project/vllm`（97361）、`unclecode/crawl4ai`（87676）。按总 star，本页顺序是 LLMs-from-scratch、pytorch、vllm、crawl4ai、career-ops。`page=4` 是总结果里的第 16 到第 20 条。`vllm` 靠话题 `llm`，仓库名不等于 `llm`。`pytorch` 靠仓库名。`crawl4ai` 靠话题 `llm` 与 `ai-agents`。
  - 未命中：`career-ops-hq/career-ops`（总 star 84221；描述是 “AI job search agent”，空格写法不等于 `ai-agents`）。它是本页第 5 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-16 stars:>3`。HTTP 200。`total_count=35`，返回 5，规则保留 1，排除清单 1，未命中 3。剩余配额 24。`page=4` 是总结果里按总 star 排序后的第 16 到第 20 条。返回的星数是 13、12、10、10、8。`total_count=35`，本页 5 条不是末页，也不是接口失败。正文保留 `SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark`（10）。两个 10 星分别是这个基准仓库和下面的 awesome 镜像。脚本把保留和剔除分成两份列表，没有保存这两条在接口里的先后，本次不再补查。
  - 清单类排除：`satnamrsm/https-github.com-sickn33-antigravity-awesome-skills`（总 star 10；仓库名含 awesome，搜索描述为空，脚本已按 awesome 排除）。
  - 名称词边界未命中：`SickGear/SickGear.Docker`（13；SickGear 容器，`SickGear` 不等于 `sic`）、`linuxserver/docker-sickgear`（12；搜索描述为空，`sickgear` 不等于 `sic`）、`danhyun-jeong/sickle-cite`（8；韩文人文引用格式工具，`sickle` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-16 stars:>3`。HTTP 200。`total_count=417`，返回 5，规则保留 2，未命中 3。剩余配额 22。`page=4` 是总结果里按总 star 排序后的第 16 到第 20 条。正文保留 `springfall2008/batpred`（380）、`patman15/BMS_BLE-HA`（380）。按总 star，本页顺序是 `3dcitydb`、`dcs-bios`、`3dcodeverse`、batpred、BMS_BLE-HA。两条 380 在保留列表里的先后是 batpred 在前。
  - 名称和 topics 未命中电力电子：`3dcitydb/3dcitydb`（490；3D City Database，名称里的 3dcitydb 不等于 `dc-dc`）、`DCS-Skunkworks/dcs-bios`（441；DCS 飞行模拟的数据导出，`DCS` 不等于 `dc-dc`）、`gaoypeng/3dcodeverse`（414；名称里的 3dcodeverse 不等于 `dc-dc`）。
  - `batpred` 的话题 `solax-inverter` 计入 inverter，`solis-pv-inverters` 复数不计入。`BMS_BLE-HA` 靠话题和描述里的 bms；README 写了可选的 ESPHome 蓝牙代理，搜索话题没有 esp32，不跨嵌入式。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-16 stars:>3`。HTTP 200。`total_count=249`，返回 5，规则保留 5，未命中 0，排除清单 0。剩余配额 29。正文保留 `google-deepmind/mujoco_mpc`（1774）、`NVIDIA-ISAAC-ROS/isaac_ros_visual_slam`（1500）、`MyoHub/myosuite`（1290）、`Sguan-ZhouQing/SguanFOC_Library`（1175）。`SguanFOC` 在嵌入式一行。按总 star，本页顺序是 mujoco_mpc、cv-arxiv-daily、isaac_ros_visual_slam、myosuite、SguanFOC。本次响应头的剩余配额是 29，前一条自动控制新项目是 21，中间没有失败重试，按响应头原样记录。
  - 清单类剔除：`Vincentqyw/cv-arxiv-daily`（总 star 1520；话题含 slam，描述是用 GitHub Actions 每日更新计算机视觉论文）。README 首页写 “Updated on 2026.11.21”，下面按 SLAM、SFM、NeRF 等分成论文表。这是每日论文清单，脚本的清单规则没有命中仓库名和描述，人工剔除，不进正文。它是本页第 2 条。
  - `isaac_ros_visual_slam` 的描述含 cuVSLAM，不等于 slam，归类靠话题 ros2 与 slam。`myosuite` 靠话题 motor-control，对象是肌肉骨骼模型。`SguanFOC` 话题含 embedded 与 mcu，嵌入式一节一行带过。
