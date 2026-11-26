# GitHub 领域日报 · 2026-11-27

生成时间：2026-11-27 07:37（北京时间）。数据拉取开始于 2026-11-27 07:32:12（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-28（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-20 及之后有推送、总 star > 3。轮换页 `page = (当年第 331 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 让人用自己的显卡从零训一个大约 64M 的小模型，而不是只调用现成的大模型；总 star 71604，24 小时新增 star 701。这是今日热度里唯一命中领域的仓库。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 10076，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [pytorch/pytorch](https://github.com/pytorch/pytorch) 用 Python 写张量和动态神经网络，计算可以放到 GPU 上；总 star 105786，没有 24 小时新增数据。这是本页常青里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 16 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

嵌入式、功率器件、电力电子电源、自动控制在这 16 条里都没有命中。

### AI

- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
  - 说明：把大模型的训练过程拆到个人显卡上能跑完，用来看懂预训练、微调和对齐，而不是只调一个封装好的接口。README 写主线最小版本大约 64M，并用 PyTorch 从零实现整条训练链路。同一段注明「2 小时」是监督微调阶段在单张 NVIDIA 3090 上跑完 1 个 epoch 的实测，「3 块钱」是这段时间的租卡费用。搜索描述里的 LLM 计入 AI。
  - 领域：AI
  - 总 star：71604
  - 24 小时新增 star：701

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑，刷一套会覆盖另一套；ESP-IDF 6.0.1 起，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：192
- [zacharyinserra/deskhub](https://github.com/zacharyinserra/deskhub)
  - 说明：把一块 Waveshare ESP32-S3 触控屏放在桌上，看电脑的占用、日历、正在播放的媒体，以及 Claude Code 的用量，也能按屏幕上的按钮去操作这台电脑。搜索描述已经写了 Steam 和 3D 打印机。README 写固件是 ESP-IDF v5.5 加 LVGL，屏是 4.3 英寸 B 款、800×480 电容触摸，只连 2.4 GHz Wi-Fi；Windows 上的配套程序负责把电脑数据送过来，时钟和天气在电脑关机后仍由板子自己显示。README 的页面表里还有计时器、GitHub 贡献图，以及 Plex 或 Jellyfin。描述里的 Claude Code 不是 llm，不跨到 AI。`created_at` 为 `2026-11-17T16:57:49Z`。
  - 领域：嵌入式 Embedded
  - 总 star：161
- [tahaalakhras53-boop/dma-firmware-customization](https://github.com/tahaalakhras53-boop/dma-firmware-customization)
  - 说明：仓库自称是一份给 PCIe DMA 板改写固件身份、让主机把它认成别的设备的说明。README 标题是 “DMA Firmware Customization — Security Tool”，搜索描述写成针对 PCIe Screamer Squirrel 的硬件混淆指南。这是在总线上隐瞒设备身份，正文不写安装、配置和改写步骤。话题含 embedded 与 esp32，仓库名含 firmware，因此归入嵌入式；README 全文没有 ESP32，不把话题里的 esp32 写成这块板的主控。话题里同时有 adc、battery-monitor、hub75、oled 等和这份说明对不上的标签，也有 xilinx-vivado。`created_at` 为 `2026-11-15T19:45:19Z`。
  - 领域：嵌入式 Embedded
  - 总 star：153
- [andrisgauracs/bevel-os](https://github.com/andrisgauracs/bevel-os)
  - 说明：在一块 ESP32-S3 上跑一个能开窗口的小桌面，用六只电阻把 640×480、64 色的画面送到 VGA 显示器。搜索描述写它由模型 Claude Fable 5.2 写成。README 写人负责接线和 3D 打印；开机到桌面 0.7 秒，窗口里的 Doom（共享版 E1M1）大约 32 帧。硬件写明 16 MB 闪存、8 MB 八线 PSRAM 的 N16R8，系统跑在 ESP-IDF 5.5.3 和 FreeRTOS 上。搜索描述里的 ESP32-S3 按词边界计入 esp32。`created_at` 为 `2026-11-14T14:18:34Z`。
  - 领域：嵌入式 Embedded
  - 总 star：139
- [jthwho/bmds](https://github.com/jthwho/bmds)
  - 说明：把一块没有无线的 ESP32-P4 板做成一台自己能用的小电脑。插上显示器、键盘和网线，就有窗口、命令行，以及能在机器上写脚本的编辑器。搜索描述写的是给 Olimex ESP32-P4-PC 做的一个像 DOS 的小操作系统。README 写芯片是 360 MHz 双核 RISC-V、没有射频，内核用 ESP-IDF 里的 FreeRTOS，画面写的是 1280×720，并写程序之间没有内存保护。搜索描述里的 ESP32-P4 按词边界计入 esp32。搜索描述里的 “Bare Metal Do Stuff” 是空格写法，不等于 bare-metal，而且 bare-metal 不在强特征描述词里。仓库名是 bmds。`created_at` 为 `2026-11-02T03:03:38Z`。
  - 领域：嵌入式 Embedded
  - 总 star：130

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：10076
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
  - 说明：给团队自托管的一件工作引擎。提一句需求不算做完，要等提出的人签收；可以指定一个代理干活，另一个代理按验收标准复查，不过就退回。README 首页列出 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code、Codex Harness 和 Codex。展开的表标题现在写 Supported harnesses (7)，表里就是这 7 个。话题含 llm 与 ai-agents。话题里的 mcp 不是本次 AI 关键词，不另计。`created_at` 为 `2026-10-29T02:43:14Z`。
  - 领域：AI
  - 总 star：8233
- [simplexai-labs/linger](https://github.com/simplexai-labs/linger)
  - 说明：在自己的电脑上跑一个私人代理，模型和记忆留在本机，而不是按次把对话送到别人的服务器。README 写 MoE 推理把常用专家留在显卡上，其余放在内存或固态硬盘，并写 125B 的 Qwen3.8-Flash-Next 能在 12 GB 显卡加 64 GB 内存上跑。图注写这个模型的 2-bit 文件是 39 GB；速度表里 RTX 3060（12 GB）那一格是 45.5 token/s。这些数字是 README 的说法，不是本次实测。话题 `local-llm` 按词边界计入 llm。`created_at` 为 `2026-11-10T03:50:38Z`。
  - 领域：AI
  - 总 star：4874

### 功率器件 Power Devices

本日无新项目。`total_count=3`，3 条全部返回，名称都没落到 `sic` 的词边界上。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。返回的 5 条里，唯一被规则留下的是公司名后缀 LLC，不是谐振变换器，正文不收。其余 4 条的名称和搜索描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`。详见数据源状态。

### 自动控制 Control

- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：给第一人称、野外长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参。README 写一套常规的离线光束法平差能缩小和行业系统的差距，但会停在公开提交的水平；把这两项物理现象放进同一条流水线后，LaMAria 训练集的控制点分数从 69.1 到 82.4。它在 LaMAria 测试集上与 Aria 的 SLAM 打平，并在五个类别里的三个上第一次超过 Aria，UZH-FPV 排行榜上排第二。仓库名里的 slam 计入自动控制。`created_at` 为 `2026-11-13T01:47:26Z`。
  - 领域：自动控制 Control
  - 总 star：163
- [ekrrems/Stereo-inertial-slam](https://github.com/ekrrems/Stereo-inertial-slam)
  - 说明：用双目相机和 IMU 从零写一套视觉惯性 SLAM，同时出稀疏地图和稠密地图，并拿公开路测轨迹对一下误差。README 标题是 RigVis，实现是 C++17（Eigen、OpenCV、Ceres），IMU 融合用误差状态卡尔曼滤波。它在 KITTI 里程计序列 00（4544 帧，3.7 km）上写的相对平移误差是 1.20%，相对旋转是 0.50°/100 m，绝对轨迹误差均方根 2.81 m；同一张表引用的 ORB-SLAM2 双目论文数字是 0.70%、0.25°/100 m 和 1.3 m。仓库名里的 slam 计入自动控制。搜索描述没有这些数字。`created_at` 为 `2026-11-01T17:38:10Z`。
  - 领域：自动控制 Control
  - 总 star：95

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=4`、`per_page=5`，本页是各查询按总 star 排序后的第 16 到第 20 条。

### 嵌入式 Embedded

- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：把一块 ESP32 变成房间里的动作传感器。人走过时 Wi-Fi 的传播会变，板子读信道状态信息来报有没有人动，不用摄像头、麦克风或专用雷达。README 写检测在设备本地完成，一块板覆盖一个区域；支持 ESP32-C6、C5、C3、S3、S2 和经典 ESP32。一手方代码是 GPLv3，闭源固件另有商业许可。话题含 embedded。话题 `esp-32` 不等于 esp32，搜索描述里的 ESP32 计入。
  - 领域：嵌入式 Embedded
  - 总 star：9884
- [crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)
  - 说明：给一批 ESP32 墨水屏电子书做能自己改的固件，用来读 EPUB，而不是只能用厂商锁死的阅读器。README 写它支持 ESP32-C3 的 Xteink X4 和 X3、ESP32-S3 的几款屏，以及 ESP32-C61 的 OnePage Reader，阅读引擎覆盖 EPUB 2/3。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：8992
- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的官方设备固件，用 LoRa 组一个不靠蜂窝和互联网的远距离网格。README 写支持 ESP32、nRF52、RP2040/RP2350 和 Linux。话题含 esp32、stm32 与 firmware。搜索描述没有逐项列芯片。
  - 领域：嵌入式 Embedded
  - 总 star：8646
- [FreeRTOS/FreeRTOS](https://github.com/FreeRTOS/FreeRTOS)
  - 说明：FreeRTOS 的经典发行包，把实时内核和一批示例放在一起，方便在不同板子上把任务调度跑起来。搜索描述写它从 SourceForge 的 SVN 克隆而来，内核以子模块引入。仓库名和描述里的 freertos 计入嵌入式。README 开头的发行说明是 202411.00，把内核等库对齐到 202406-LTS，并把 MbedTLS 写到 v3.5.1。
  - 领域：嵌入式 Embedded
  - 总 star：8014
- [nodemcu/nodemcu-firmware](https://github.com/nodemcu/nodemcu-firmware)
  - 说明：在乐鑫的 Wi-Fi 芯片上跑 Lua，用事件回调写联网小程序，不用从 C 固件写起。搜索描述写它面向 ESP8266、ESP8285 和 ESP32。README 写 `release` 和 `dev` 分支面向 ESP8266，`dev-esp32` 分支才面向 ESP32。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：7962
- [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library) — 见下方「自动控制 Control」完整条目。话题含 embedded 与 mcu，此处不展开。领域：嵌入式 Embedded。总 star：1181。

### AI

- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：用熟悉的 Python 写张量和神经网络，计算图按运行轨迹当场建出来，并能把计算放到 GPU 上。README 把这两点写成它的两件高层能力：像 NumPy 一样做张量运算，以及基于磁带式自动求导的动态网络。仓库名 pytorch 计入 AI。
  - 领域：AI
  - 总 star：105786
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：把大模型的推理服务做成高吞吐、省显存的引擎，让同一张卡同时接住更多请求。README 写它用 PagedAttention 管理注意力的键值缓存，并做连续批处理。搜索描述里的 LLMs 是复数，词边界不等于 llm；名称 vllm 也不等于 llm。话题含 llm、pytorch 与 transformer，因此计入 AI。
  - 领域：AI
  - 总 star：97646
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：给编程代理准备一个抓网页的入口，把页面收成干净的 Markdown 或结构化结果，也可以自己把这套爬虫架起来。搜索描述写官方提供托管 API，每月 1000 额度、不需要信用卡，本仓库是背后那套 Apache-2.0 爬虫。话题含 llm 与 ai-agents。话题里的 mcp 与 rag 不是本次 AI 关键词，不另计。
  - 领域：AI
  - 总 star：87986
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)
  - 说明：给 Claude Code 和 Codex 套一层代理编排，用来把多个代理的流程、记忆和协作放到一个入口里跑。README 的标题写它是面向这两边的 agent meta-harness。话题含 ai-agents。搜索描述里的 RAG 与话题里的 mcp 不是本次 AI 关键词，不另计。
  - 领域：AI
  - 总 star：82505
- [stereolabs/zed-sdk](https://github.com/stereolabs/zed-sdk) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：1249。

### 功率器件 Power Devices

本页剔除 Samsung Innovation Campus 课堂笔记本后为空。`total_count=29`，本页 5 条都不是碳化硅或功率器件项目。详见数据源状态。

### 电力电子电源 Power Supply

- [fl4p/batmon-ha](https://github.com/fl4p/batmon-ha)
  - 说明：在 Home Assistant 里直接读各家电池管理系统的蓝牙数据，用来核对电量计和电池状态，不用再加一块转接板。README 开头写它走主机上的蓝牙，不另加 USB、串口、RS485 或 ESP32，也能在 Linux、macOS 和 Windows 上脱离 Home Assistant 跑。后文另有可选的 RS485 和 ESPHome 蓝牙代理；搜索话题没有 esp32，不跨到嵌入式。话题含 bms，描述里的 BMS 也计入。`pushed_at` 为 `2026-11-24T09:39:10Z`。
  - 领域：电力电子电源 Power Supply
  - 总 star：537

### 自动控制 Control

- [google-deepmind/mujoco_mpc](https://github.com/google-deepmind/mujoco_mpc)
  - 说明：在 MuJoCo 里实时做预测控制，用来编写和求解机器人任务，不用每次从零写一个规划器。README 写它由 Google DeepMind 开发，导数方法包括 iLQG 和梯度下降，无导数方法包括 Predictive Sampling。话题含 mpc 与 motor-control。
  - 领域：自动控制 Control
  - 总 star：1778
- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用 MuJoCo 搭一批带肌肉的身体模型和环境，让人研究运动控制，而不是只在刚体机器人上试策略。搜索描述写这些任务包在 OpenAI gym API 里。README 写 MyoSuite 3 的同一个 env_id 可以走 Gymnasium，也能在一块 GPU 上并行训几千个环境。话题含 motor-control。
  - 领域：自动控制 Control
  - 总 star：1292
- [stereolabs/zed-sdk](https://github.com/stereolabs/zed-sdk)
  - 说明：围绕 ZED 双目相机做空间感知，让机器人或空间设备拿到深度和定位，而不是只拿到一张彩色图。搜索描述写的是快速搭建智能机器人和空间的感知框架。README 写本仓库放的是 ZED SDK 的教程和示例，并写 ZED SDK 5.6 通过 Sensors API 做多相机 SLAM：同一支架上的多台相机一起跟踪，合成一张共享地图。话题含 slam，也含 computer-vision。定位建图比通用视觉更贴近自动控制，完整条目放在这里；AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：1249
- [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library)
  - 说明：在 MCU 上跑磁场定向控制，让有感和无感的永磁同步电机都能做电流、速度和位置环，而不用从坐标变换和 SVPWM 写起。搜索描述写库内有基于 SVPWM 的多种模式，并针对嵌入式平台收过数学运算。README 徽章仍是 3.1.0，并写从有感三环到高频注入加高速无感都在真实硬件上跑过。话题含 foc、motor-control 与 pid。话题也含 embedded 与 mcu，嵌入式一节一行带过。电机控制比「跑在 MCU 上」更贴近自动控制，所以完整条目放在这里。
  - 领域：自动控制 Control
  - 总 star：1181

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。本次跨节的是 SguanFOC（自动控制完整，嵌入式一行）和 zed-sdk（自动控制完整，AI 一行）。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API，下列仓库全部 HTTP 200，默认说明文件名都是 `README.md`：`jingyaogong/minimind`、`FlashCat-Jordan/Flashduck`、`zacharyinserra/deskhub`、`tahaalakhras53-boop/dma-firmware-customization`、`andrisgauracs/bevel-os`、`jthwho/bmds`、`wangzan101/Mika`、`mdiri-ai/SoduWork`、`simplexai-labs/linger`、`jacobvm04/slam-dunk`、`ekrrems/Stereo-inertial-slam`、`inmusic-software/mpc-plugin-builder-sdk`、`EasyNavigation/StrataSLAM`、`francescopace/espectre`、`crosspoint-reader/crosspoint-reader`、`meshtastic/firmware`、`FreeRTOS/FreeRTOS`、`nodemcu/nodemcu-firmware`、`pytorch/pytorch`、`vllm-project/vllm`、`unclecode/crawl4ai`、`ruvnet/ruflo`、`sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`、`fl4p/batmon-ha`、`google-deepmind/mujoco_mpc`、`Vincentqyw/cv-arxiv-daily`、`MyoHub/myosuite`、`stereolabs/zed-sdk`、`Sguan-ZhouQing/SguanFOC_Library`、`darkfibr/artex-forensics`。`dma-firmware-customization` 的 README 没有 ESP32，身份改写的安装、配置和步骤未写入正文。`artex-forensics` 与 `Claude-BugHunter` 的漏洞或攻击步骤未写入正文。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 16 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`jingyaogong/minimind`（71604，701；描述含 LLM）。
- 核对：脚本解析出 16 条后，另一次 GET 同一 URL 仍是 HTTP 200，`<article class="Box-row">` 仍是 16 个，仓库集合和顺序相同，stars today 全部不变。总 star 有变化的是：`Claude-BugHunter` 24507→24511，`superpowers` 327457→327460，`CLI-Anything` 66333→66337，`minimind` 71604→71606，`plugins` 19776→19777，`firecrawl` 210903→210906，`diagram-design` 73820→73823，`last30days-skill` 75721→75722，`stitch-skills` 13274→13275，`AFFiNE` 78947→78949，`Ghost-Downloader-3` 19081→19082，`autoclip` 16904→16906。`nginx`（33515，150）、`openvino`（12810，176）、`app-store-compliance`（7010，561）、`opensre`（15806，325）两次总 star 一致。正文用第一次解析的数字。今日页面本身有 16 条，不是解析丢条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`elementalsouls/Claude-BugHunter`（24507，1600；技能包，描述写 85 个技能，没有 `llm`，攻击步骤不写入正文）、`firecrawl/firecrawl`（210903，1042；给代理做搜索和抓取，没有 `llm`）、`cathrynlavery/diagram-design`（73820，951；图示设计，没有 `llm`）、`XiaoYouChR/Ghost-Downloader-3`（19081，887）、`obra/superpowers`（327457，853；代理技能框架，没有 `llm`）、`zhouxiaoka/autoclip`（16904，770；本地 AI 剪辑，描述里的 MCP server 是裸 mcp，没有 `llm`）、`mvanhorn/last30days-skill`（75721，755；“AI agent skill”，没有 `llm`）、`HKUDS/CLI-Anything`（66333，744；把软件做成代理能调用的命令行，没有 `llm`）、`mjmirza/app-store-compliance`（7010，561；“skill for AI coding agents” 是空格写法，不等于 `ai-agents`）、`toeverything/AFFiNE`（78947，521）、`Tracer-Cloud/opensre`（15806，325；CI/CD 代理，没有 `llm`）、`google-labs-code/stitch-skills`（13274，308；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`cursor/plugins`（19776，268；Cursor 插件规范）、`openvinotoolkit/openvino`（12810，176；“AI inference” 是弱词，没有 `llm`）、`nginx/nginx`（33515，150）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-28 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-28 stars:>2`。HTTP 200。`total_count=429`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`FlashCat-Jordan/Flashduck`（192）、`zacharyinserra/deskhub`（161）、`tahaalakhras53-boop/dma-firmware-customization`（153）、`andrisgauracs/bevel-os`（139）、`jthwho/bmds`（130）。昨日同页是 Flashduck（190）、dma（153）、deskhub（152）、bevel-os（138）、bmds（126）。本次 `deskhub` 的总 star 是 161，排到 `dma-firmware-customization`（153）前面。这些都是搜索接口的总 star，没有 24 小时新增字段，不把与昨日的差值写成 24 小时新增。`dma-firmware-customization` 的话题含 `esp32`，README 全文没有 ESP32。`Flashduck` 的搜索描述和话题都没有 `llm`。`bmds` 的仓库名是 bmds。搜索描述里的 “Bare Metal Do Stuff” 是空格写法，不等于 bare-metal，而且 bare-metal 不在强特征描述词里。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-28 stars:>2`。HTTP 200。`total_count=2850`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（10076）、`mdiri-ai/SoduWork`（8233）、`simplexai-labs/linger`（4874）。`SoduWork` 的表标题现在写 Supported harnesses (7)，表内列出 7 个。昨日同查询的总 star 是 Mika 9992、SoduWork 8117、exact 5117、linger 4677。昨日在前 5 的 `expo/exact` 本次前 5 没有出现，不猜 star。这些都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
  - 未命中：`sarpstar/cinecode`（总 star 3069；描述是 “an AI coding agent writes the script”，空格写法不等于 `ai-agents`，也没有 `llm`）。它排在 linger（4874）后面。`DIYgod/pinky`（总 star 2809；描述是让 AI 使用手机，“any MCP agent” 里的裸 mcp 不计入，也没有 `llm`）。它是本页第 5 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-28 stars:>2`。HTTP 200。`total_count=3`，返回 3，规则保留 0，未命中 3。剩余配额 25。3 条就是全部结果，不是接口少给。返回顺序按总 star 是 `zjy2968466837/SicnuJw`（7）、`EngineerHabib/DOKKHO-E_Commerce-Porject-SICIP`（4）、`SicoKaleb/SicoAutoTerms`（3）。星数与昨日这 3 条相同。
  - 名称词边界未命中：`SicnuJw`（四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`DOKKHO-E_Commerce-Porject-SICIP`（名称 `SICIP` 不等于 `sic`，搜索描述为空）、`SicoAutoTerms`（`Sico` 不等于 `sic`，描述与碳化硅无关）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-28 stars:>2`。HTTP 200。`total_count=76`，返回 5，规则保留 1，未命中 4。剩余配额 23。规则留下的那条经人工剔除后，正文无新项目。按总 star，本页是 `acrobat-dc-desktop`（210）、`isometric-cities`（92）、`mvc2-naomi-dc`（87）、`artex-forensics`（78）、`3DCodeFactory`（37）。昨日同页前 5 是 acrobat-dc（210）、okx 网格机器人（124）、blender 套件（121）、isometric-cities（92）、naomi-dc（83）。窗口起点从昨日的 2026-10-27 移到 2026-10-28 后，okx 与 blender 不在本次前 5，不猜 star。`mvc2-naomi-dc` 昨日搜索是 83，本次是 87。这是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
  - 人工剔除：`darkfibr/artex-forensics`（总 star 78）。描述里的 LLC 是 Blackfish Security LLC，README 标题也是这个公司名，不是谐振变换器。漏洞步骤未写入正文。搜索描述和话题没有 `llm`。
  - 名称和搜索描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（210；Acrobat DC 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（92；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`gibletto/mvc2-naomi-dc`（87；NAOMI 街机的反编译移植，名称里的 dc 不等于 `dc-dc`）、`3DCodeFactory/3DCodeFactory`（37；“3D Code Agents” 不等于 `ai-agents`，名称里没有 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-28 stars:>2`。HTTP 200。`total_count=109`，返回 5，规则保留 3，未命中 2。剩余配额 21。正文保留 `jacobvm04/slam-dunk`（163）、`ekrrems/Stereo-inertial-slam`（95）。`slam-dunk` 昨日搜索是 160，本次是 163。`Stereo-inertial-slam` 昨日搜索是 91，本次是 95。昨日的 `ACCORD` 不在本次前 5，不猜 star。这些都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。按总 star，本页顺序是 `mpc-plugin-builder-sdk`（235）、`slam-dunk`（163）、`StrataSLAM`（98）、`Stereo-inertial-slam`（95）、`melodee-sample`（84）。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 235）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。README 还写 MPC Sample 要固件 v1.4.0 或更新，只做效果。描述里的 “AI coding agent” 是空格写法，不等于 `ai-agents`。
  - 名称和 topics 未命中：`EasyNavigation/StrataSLAM`（总 star 98；搜索描述为空，名称 `StrataSLAM` 里 slam 前面是字母，词边界不等于 `slam`）。README 写的是多层 ROS 2 SLAM，不参与归类，正文不收。`keremimo/melodee-sample`（总 star 84；描述里的 Akai MPC Sample 不是强特征词，名称没有 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-20 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-20 stars:>3`。HTTP 200。`total_count=1331`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=4`、`per_page=5`，本页是总结果里按总 star 排序后的第 16 到第 20 条。本查询正文：`francescopace/espectre`（9884）、`crosspoint-reader/crosspoint-reader`（8992）、`meshtastic/firmware`（8646）、`FreeRTOS/FreeRTOS`（8014）、`nodemcu/nodemcu-firmware`（7962）。另有 1 条一行来自自动控制检索：`Sguan-ZhouQing/SguanFOC_Library`（1181，话题含 embedded 与 mcu）。`espectre` 的话题是 `esp-32`，不等于 esp32，搜索描述里的 ESP32 计入。`nodemcu` 的 README 写 `release` 与 `dev` 面向 ESP8266，`dev-esp32` 才面向 ESP32。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-20 stars:>3`。HTTP 200。`total_count=9409`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 26。正文保留 `pytorch/pytorch`（105786）、`vllm-project/vllm`（97646）、`unclecode/crawl4ai`（87986）、`ruvnet/ruflo`（82505）。按总 star，本页顺序是 pytorch、vllm、crawl4ai、career-ops、ruflo。`page=4` 是总结果里的第 16 到第 20 条。`vllm` 靠话题 `llm`，名称和描述里的 LLMs 不等于 llm。`crawl4ai` 靠话题 `llm` 与 `ai-agents`。`ruflo` 靠话题 `ai-agents`。另有 1 条一行来自自动控制检索：`stereolabs/zed-sdk`（1249，话题含 computer-vision）。
  - 未命中：`career-ops-hq/career-ops`（总 star 85062；描述是 “AI job search agent”，空格写法不等于 `ai-agents`，也没有 `llm`）。它排在 crawl4ai（87986）和 ruflo（82505）之间。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-20 stars:>3`。HTTP 200。`total_count=29`，返回 5，规则保留 1，排除清单 0，未命中 4。剩余配额 24。`page=4` 是总结果里按总 star 排序后的第 16 到第 20 条。`total_count=29`，本页 5 条不是末页，也不是接口失败。本页星数是 7、7、7、7、6。规则留下的是 `sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`（7）。剔除列表里的相对顺序是 `danhyun-jeong/sickle-cite`（7）、`zjy2968466837/SicnuJw`（7）、`ufoptg/MuSicX`（7）、`rvandewater/SICdb_MEDS`（6）。脚本把保留和剔除分成两份列表，没有保存这条课堂笔记本和另外三条 7 星在接口里的先后，本次不补查、不猜测这四条 7 星的顺序。按总 star 降序，6 星在 7 星之后，所以 `SICdb_MEDS` 是本页最后一条。人工剔除后，本页没有以功率器件为最贴近的完整条目。
  - 人工剔除：`sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`（总 star 7；搜索描述为空，名称命中 `sic`）。README 标题是 Samsung Innovation Campus 2026 的 PA-C 与 PA-D 课堂材料，内容是课堂笔记本和课程资料，不是碳化硅器件。脚本的清单规则没有命中。README 项目一节仍有一处写 SIC 2025。正文不收。
  - 名称词边界未命中：`sickle-cite`（7；韩文人文引用格式工具，`sickle` 不等于 `sic`）、`SicnuJw`（7；`Sicnu` 不等于 `sic`）、`MuSicX`（7；YouTube Music 客户端，`MuSic` 不等于 `sic`）、`SICdb_MEDS`（6；萨尔茨堡重症监护数据库，`SICdb` 里 sic 后面还有字母，不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-20 stars:>3`。HTTP 200。`total_count=396`，返回 5，规则保留 1，未命中 4。剩余配额 22。`page=4` 是总结果里按总 star 排序后的第 16 到第 20 条。正文完整条目为 `fl4p/batmon-ha`（537）。按总 star，本页顺序是 batmon-ha、dcm4chee-arc-light、3dcitydb、zamba-lxc-toolbox、dcs-bios。
  - 名称、话题和搜索描述未命中电力电子：`dcm4che/dcm4chee-arc-light`（508；DICOM 归档，`dcm` 不等于 `dc-dc`）、`3dcitydb/3dcitydb`（490；CityGML 数据库，名称不等于 `dc-dc`）、`bashclub/zamba-lxc-toolbox`（452；Proxmox 容器脚本，描述里的 active directory dc 不等于 `dc-dc`）、`DCS-Skunkworks/dcs-bios`（443；DCS 飞行模拟数据导出，`dcs` 不等于 `dc-dc`）。
  - batmon 的 README 开头写不另加 ESP32，后文有可选 RS485 和 ESPHome 蓝牙代理，搜索话题没有 esp32，不跨嵌入式。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-20 stars:>3`。HTTP 200。`total_count=227`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。正文保留 `google-deepmind/mujoco_mpc`（1778）、`MyoHub/myosuite`（1292）、`stereolabs/zed-sdk`（1249）、`Sguan-ZhouQing/SguanFOC_Library`（1181）。按总 star，本页顺序是 mujoco_mpc、cv-arxiv-daily、myosuite、zed-sdk、SguanFOC。本次响应头的剩余配额是 29，前一条自动控制新项目是 21，中间没有失败重试。两次搜索间隔 7 秒，前面的请求已经跨过一分钟，配额窗口滚动，按响应头原样记录。
  - 人工剔除：`Vincentqyw/cv-arxiv-daily`（总 star 1521；话题含 slam）。搜索描述写每天自动更新计算机视觉论文，README 首行是 Updated on 2026.11.26。这是每日论文清单，脚本的清单规则没有命中，正文不收。它夹在 mujoco_mpc（1778）和 myosuite（1292）之间。
  - `zed-sdk` 的 README 写 ZED SDK 5.6 的多相机 SLAM；搜索描述把它写成感知框架，README 写本仓库是教程和示例。`SguanFOC` 徽章仍是 3.1.0。`myosuite` 的搜索描述仍写 OpenAI gym API，README 写 Gymnasium。
