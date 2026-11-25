# GitHub 领域日报 · 2026-11-26

生成时间：2026-11-26 07:38（北京时间）。数据拉取开始于 2026-11-26 07:34:45（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-27（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-19 及之后有推送、总 star > 3。轮换页 `page = (当年第 330 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 让人用自己的显卡从零训一个大约 64M 的小模型，而不是只调用现成的大模型；总 star 70918，24 小时新增 star 828。这是今日热度里唯一命中领域的仓库。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 9992，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) 给编程代理补上它自己搜不到的站点，一条命令读 X、Reddit、YouTube、B 站和小红书；总 star 114720，没有 24 小时新增数据。这是本页常青里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 16 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

嵌入式、功率器件、电力电子电源、自动控制在这 16 条里都没有命中。

### AI

- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
  - 说明：把大模型的训练过程拆到个人显卡上能跑完，用来看懂预训练、微调和对齐，而不是只调一个封装好的接口。README 写主线最小版本大约 64M，并用 PyTorch 从零实现整条训练链路。同一段注明「2 小时」是监督微调阶段在单张 NVIDIA 3090 上跑完 1 个 epoch 的实测，「3 块钱」是这段时间的租卡费用。搜索描述里的 LLM 计入 AI。
  - 领域：AI
  - 总 star：70918
  - 24 小时新增 star：828

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑，刷一套会覆盖另一套；ESP-IDF 6.0.1 起，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：190
- [tahaalakhras53-boop/dma-firmware-customization](https://github.com/tahaalakhras53-boop/dma-firmware-customization)
  - 说明：仓库自称是一份给 PCIe DMA 板改写固件身份、让主机把它认成别的设备的说明。README 标题是 “DMA Firmware Customization — Security Tool”，搜索描述写成针对 PCIe Screamer Squirrel 的硬件混淆指南。这是在总线上隐瞒设备身份，正文不写安装、配置和改写步骤。话题含 embedded 与 esp32，仓库名含 firmware，因此归入嵌入式；README 全文没有 ESP32，不把话题里的 esp32 写成这块板的主控。话题里同时有 adc、battery-monitor、hub75、oled 等和这份说明对不上的标签。`created_at` 为 `2026-11-15T19:45:19Z`。
  - 领域：嵌入式 Embedded
  - 总 star：153
- [zacharyinserra/deskhub](https://github.com/zacharyinserra/deskhub)
  - 说明：把一块 Waveshare ESP32-S3 触控屏放在桌上，看电脑的占用、日历、正在播放的媒体，以及 Claude Code 的用量，也能按屏幕上的按钮去操作这台电脑。搜索描述已经写了 Steam 和 3D 打印机。README 写固件是 ESP-IDF v5.5 加 LVGL，屏是 4.3 英寸 B 款、800×480 电容触摸，只连 2.4 GHz Wi-Fi；Windows 上的配套程序负责把电脑数据送过来，时钟和天气在电脑关机后仍由板子自己显示，另有 Codex 用量页。天气和 Codex 来自 README，不在搜索描述里。描述里的 Claude Code 不是 llm，不跨到 AI。`created_at` 为 `2026-11-17T16:57:49Z`。
  - 领域：嵌入式 Embedded
  - 总 star：152
- [andrisgauracs/bevel-os](https://github.com/andrisgauracs/bevel-os)
  - 说明：在一块 ESP32-S3 上跑一个能开窗口的小桌面，用六只电阻把 640×480、64 色的画面送到 VGA 显示器。搜索描述写它由模型 Claude Fable 5.2 写成。README 写人负责接线和 3D 打印；开机到桌面 0.7 秒，窗口里的 Doom（共享版 E1M1）大约 32 帧。硬件写明 16 MB 闪存、8 MB 八线 PSRAM 的 N16R8，系统跑在 ESP-IDF 5.5.3 和 FreeRTOS 上。搜索描述里的 ESP32-S3 按词边界计入 esp32。`created_at` 为 `2026-11-14T14:18:34Z`。
  - 领域：嵌入式 Embedded
  - 总 star：138
- [jthwho/bmds](https://github.com/jthwho/bmds)
  - 说明：把一块没有无线的 ESP32-P4 板做成一台自己能用的小电脑。插上显示器、键盘和网线，就有窗口、命令行，以及能在机器上写脚本的编辑器。搜索描述写的是给 Olimex ESP32-P4-PC 做的一个像 DOS 的小操作系统。README 写芯片是 360 MHz 双核 RISC-V、没有射频，内核用 ESP-IDF 里的 FreeRTOS，画面写的是 1280×720，并写程序之间没有内存保护。搜索描述里的 ESP32-P4 按词边界计入 esp32。`created_at` 为 `2026-11-02T03:03:38Z`。
  - 领域：嵌入式 Embedded
  - 总 star：126

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：9992
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
  - 说明：给团队自托管的一件工作引擎。提一句需求不算做完，要等提出的人签收；可以指定一个代理干活，另一个代理按验收标准复查，不过就退回。README 首页列出 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code、Codex Harness 和 Codex。展开的表标题现在写 Supported harnesses (7)，表里就是这 7 个。话题含 llm 与 ai-agents。话题里的 mcp 不是本次 AI 关键词，不另计。`created_at` 为 `2026-10-29T02:43:14Z`。
  - 领域：AI
  - 总 star：8117
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、iOS、macOS、Android 和 Linux 上按各自的原生控件跑，编程代理可以自己建、自己跑、自己看、自己测。README 写界面用一种叫 Contract 的声明式语言，布局和属性名沿用 CSS；网页产物是大约 20 KB 的运行时。Android 写明已经能用，Material 3 的打磨还在进行；Windows 仍在早期。仓库仍是 pre-1.0，没有打包发布，并写 Bun 钉在 1.4.2。搜索描述只写了网页、macOS、iOS 和 Linux，Android 的状态来自 README。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：5117
- [simplexai-labs/linger](https://github.com/simplexai-labs/linger)
  - 说明：在自己的电脑上跑一个私人代理，模型和记忆留在本机，而不是按次把对话送到别人的服务器。README 写 MoE 推理把常用专家留在显卡上，其余放在内存或固态硬盘，并写 125B 的 Qwen3.8-Flash-Next 能在 12 GB 显卡加 64 GB 内存上跑。图注写这个模型的 2-bit 文件是 39 GB；速度表里 RTX 3060（12 GB）那一格是 45.5 token/s。这些数字是 README 的说法，不是本次实测。话题 `local-llm` 按词边界计入 llm。`created_at` 为 `2026-11-10T03:50:38Z`。
  - 领域：AI
  - 总 star：4677

### 功率器件 Power Devices

本日无新项目。`total_count=3`，3 条全部返回，名称都没落到 `sic` 的词边界上。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。返回的 5 条里，名称和搜索描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`。详见数据源状态。

### 自动控制 Control

- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：给第一人称、野外长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参。README 写一套常规的离线光束法平差能缩小和行业系统的差距，但会停在公开提交的水平；把这两项物理现象放进同一条流水线后，LaMAria 训练集的控制点分数从 69.1 到 82.4。它在 LaMAria 测试集上与 Aria 的 SLAM 打平，并在五个类别里的三个上第一次超过 Aria，UZH-FPV 排行榜上排第二。仓库名里的 slam 计入自动控制。`created_at` 为 `2026-11-13T01:47:26Z`。
  - 领域：自动控制 Control
  - 总 star：160
- [ekrrems/Stereo-inertial-slam](https://github.com/ekrrems/Stereo-inertial-slam)
  - 说明：用双目相机和 IMU 从零写一套视觉惯性 SLAM，同时出稀疏地图和稠密地图，并拿公开路测轨迹对一下误差。README 标题是 RigVis，实现是 C++17（Eigen、OpenCV、Ceres），IMU 融合用误差状态卡尔曼滤波。它在 KITTI 里程计序列 00（4544 帧，3.7 km）上写的相对平移误差是 1.20%，相对旋转是 0.50°/100 m，绝对轨迹误差均方根 2.81 m；同一张表引用的 ORB-SLAM2 双目论文数字是 0.70%、0.25°/100 m 和 1.3 m。仓库名里的 slam 计入自动控制。搜索描述没有这些数字。`created_at` 为 `2026-11-01T17:38:10Z`。
  - 领域：自动控制 Control
  - 总 star：91
- [be2rlab/ACCORD](https://github.com/be2rlab/ACCORD)
  - 说明：只用一台相机和一只 IMU，在线做出带闭环的度量稠密地图。README 写 OpenVINS 负责跟踪相机，Depth Anything 3 给关键帧窗口出深度，再放进位姿图里用回环修正。默认深度模型是 DA3-Giant，README 写显存大约 24 GB；换成 DA3-Base 大约 6 GB。话题含 slam。`created_at` 为 `2026-11-04T15:37:22Z`。
  - 领域：自动控制 Control
  - 总 star：82

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=3`、`per_page=5`，本页是各查询按总 star 排序后的第 11 到第 15 条。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件源码。话题含 stm32 与 firmware。README 把功能说明指到官网和用户文档，本仓库主要放固件源码和贡献规则。默认说明文件名是 `ReadMe.md`。
  - 领域：嵌入式 Embedded
  - 总 star：16996
- [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder)
  - 说明：给 ESP32 准备一套 Wi-Fi 和蓝牙工具固件。搜索描述和 README 标题都把它写成进攻和防护两类工具。话题含 esp32 与 firmware，话题 `esp32-c5`、`esp32-s2` 按词边界计入 esp32。具体功能、安装和操作步骤不写入正文。
  - 领域：嵌入式 Embedded
  - 总 star：13236
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13221。
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用一份配置文件驱动 ESP32、ESP8266、BK72xx 和 RP2040，再交给家庭自动化系统远程控制，不用从每种板子的固件写起。搜索描述写明这一点。README 本身主要是标志和文档链接。话题含 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：12172
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给小智 ESP32 语音硬件提供后端，把设备接到语音识别和对话服务上。搜索描述写的是快速搭建 ESP32 设备控制服务器。话题含 esp32。README 里出现大模型字样，搜索描述和话题没有 `llm`；话题 `mcp-server` 不是 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：11413
- [okalachev/flix](https://github.com/okalachev/flix) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：2556。
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：726。
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：561。

### AI

- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
  - 说明：给已经会上网的编程代理补上它自己够不着的站点，让它搜索和阅读 X、Reddit、YouTube、B 站、小红书和 GitHub，而不是只靠通用网页搜索。搜索描述写一条命令行、不另付 API 费用。话题 `llm-tools` 按词边界计入 llm。话题里的 mcp 不是本次 AI 关键词，不另计。README 里关于登录会话的做法不写入正文。
  - 领域：AI
  - 总 star：114720
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：在终端里跑一个开源的 Gemini 编程代理。README 写明它现在面向 Gemini Code Assist 的标准版、企业版，以及 Google Cloud 上的 Code Assist for GitHub；个人免费访问和 Google AI Pro / Ultra 已在 2026-06-18 转到 Antigravity CLI。同一段写它没有针对 Gemini 4 系列调过，例子点了 Gemini 4 Argon。话题含 ai-agents。搜索描述没有 `llm`。话题里的 mcp-client、mcp-server 不是本次 AI 关键词，不另计。
  - 领域：AI
  - 总 star：109114
- [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
  - 说明：把一本从零实现类 GPT 模型的书配上可运行的代码，用来自己走完预训练和微调，而不是只调现成接口。README 写这是 *Build a Large Language Model (From Scratch)* 的官方代码仓库，ISBN 9781633437166，并用 PyTorch 实现。话题含 llm 与 pytorch。这是一本书的配套代码，不是外部公开课清单，正文保留。
  - 领域：AI
  - 总 star：109051
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2177。

### 功率器件 Power Devices

- [SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark)
  - 说明：给半导体器件的 SPICE 模型做自动核对，看模型放进电路里是否还站得住，而不是只比一条电流电压曲线。README 写重点是 MOSFET，并能把 HSPICE、Spectre 转成 ngspice 再跑。归类靠仓库名 `spice`。搜索描述里的 MOSFETs 是复数，词边界不等于 mosfet，不另计。安装示例仍写着 `yourusername/spice_model_benchmark`，不是本仓库的组织名。`pushed_at` 为 `2026-11-25T23:34:09Z`。
  - 领域：功率器件 Power Devices
  - 总 star：10
- [fl4p/fetlib](https://github.com/fl4p/fetlib)
  - 说明：帮人给一台直流变换器挑开关管。它从资料里抽出 MOSFET 参数，再按给定的负载点估算损耗并排名，而不是只拿导通电阻乘栅极电荷当指标。README 标题写的是面向 DC-DC 变换器的 MOSFET 参数搜索，目前损耗模型只覆盖同步降压；文中写这套模型用在一台 1 kW 的 MPPT 跟踪器设计里，并写明还没有用实测栅极驱动波形做核对。搜索描述是 “Find the right switch”，并写按直流变换器里的损耗给 FET 排名。话题含 mosfet，所以完整条目放在功率器件；话题含 power-supply，电力电子一节一行带过。搜索描述里的 DCDC 没有连字符，不另计 `dc-dc`。
  - 领域：功率器件 Power Devices
  - 总 star：9

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：把阳光电源逆变器的 Modbus 数据接进 Home Assistant，用 YAML 就能看发电和电池。搜索描述列出 SH*RT（如 SH10RT）、SHx.RS（如 SH3.RS）、SH*K（如 SH4K6）和 SxT（如 S20T）。README 在 2026-11-07 写明，一个真正的集成正在 `proper-ha-integration` 分支上做，目标是 2026 年 12 月，实体 ID 保持不变，现有 YAML 包会继续维护到新集成对齐功能。话题含 inverter。话题也含 modbus，嵌入式一节一行带过。`pushed_at` 为 `2026-11-25T14:58:10Z`。
  - 领域：电力电子电源 Power Supply
  - 总 star：726
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman)
  - 说明：把 Solarman 采集棒上的逆变器数据接进 Home Assistant。README 写它基于异步的 pysolarmanv5，并支持 Modbus TCP，例子包括 ESP 桥、Waveshare 和以太网记录仪。话题含 inverter，也标了德业、首航、锦浪等品牌。话题含 modbus，嵌入式一节一行带过。默认说明文件名是 `readme.md`。`pushed_at` 为 `2026-11-20T11:39:13Z`。
  - 领域：电力电子电源 Power Supply
  - 总 star：561
- [fl4p/fetlib](https://github.com/fl4p/fetlib) — 见上方「功率器件 Power Devices」完整条目。话题含 power-supply，此处不展开。领域：电力电子电源 Power Supply。总 star：9。

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：一台自己能改的家用扫地机，用二维激光建图并自己走，常规功能不依赖云端。搜索描述写的是开源吸尘机器人。README 写它用树莓派、3D 打印、Home Assistant、Arduino 和 ROS 2。同一段写明现在还不能按物料单组装，今天只能在仿真里跑，等第一份物料单在真机上验证过才会跟上组装说明。话题含 ros2 与 slam，也含 esp32。扫地和定位比单块 ESP32 更贴近自动控制，所以完整条目放在这里；嵌入式一节一行带过。这条来自嵌入式常青检索，不在自动控制本页前 5。`pushed_at` 为 `2026-11-25T22:23:09Z`。
  - 领域：自动控制 Control
  - 总 star：13221
- [okalachev/flix](https://github.com/okalachev/flix)
  - 说明：用一块 ESP32 从零做一架四旋翼，而不是改现成的飞控固件。搜索描述就是这句话。话题含 flight-controller 与 esp32。README 的物料表写了 MOSFET，搜索描述和话题没有 mosfet，不跨到功率器件。完整条目在自动控制，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：2556
- [nv-tlabs/vipe](https://github.com/nv-tlabs/vipe)
  - 说明：从一段没有标定的原始视频里估出相机内参、运动和接近真实尺度的稠密深度，用来给视频标几何，而不是只做在线机器人定位。README 写支持针孔、广角和 360 度全景。2026 年 11 月的更新写加入了 Depth Pro 2，并写推理速度大约是 Depth Pro L 16 FPS、Depth Pro H+ 14 FPS，对照的 MoGe-2 是 12 FPS；同一段写 ViPE-Long（metrictrail）用来流式重建长视频。这些速度是 README 的说法，不是本次实测。话题含 slam。
  - 领域：自动控制 Control
  - 总 star：2222
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：给移动机器人提供一套从 2005 年做到现在的 C++ 库，定位、建图和导航都能从这里搭，而不是每个实验重写滤波和图优化。搜索描述写的是移动机器人编程工具包。README 写 MRPT 3 拆成独立的 colcon 包并改用 C++17。MOLA 那一行写了 ROS 2，那是另一个仓库；本仓库搜索话题没有 ros2，不把 MRPT 本身写成 ROS 2 包。话题含 slam 与 computer-vision。完整条目在自动控制，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：2177
- [ShisatoYano/AutonomousVehicleControlBeginnersGuide](https://github.com/ShisatoYano/AutonomousVehicleControlBeginnersGuide)
  - 说明：用同一套 Python 仿真把自动驾驶拆开学：定位、建图、规划和跟踪可以换算法对照，而不是只看一篇综述。搜索描述写它是仿真加一本开放教材，系统一块一块长出来。README 写示例要求 Python 3.14.x。话题含 slam 与 kalman-filter。这是教材和可运行示例，不是外部公开课清单，正文保留。
  - 领域：自动控制 Control
  - 总 star：1962

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。本次跨节的是 oomwoo（自动控制完整，嵌入式一行）、flix（自动控制完整，嵌入式一行）、Sungrow 与 ha-solarman（电力电子完整，嵌入式各一行）、MRPT（自动控制完整，AI 一行）、fetlib（功率器件完整，电力电子一行）。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API，下列仓库全部 HTTP 200。默认说明文件名是 `README.md` 的有：`jingyaogong/minimind`、`FlashCat-Jordan/Flashduck`、`tahaalakhras53-boop/dma-firmware-customization`、`zacharyinserra/deskhub`、`andrisgauracs/bevel-os`、`jthwho/bmds`、`wangzan101/Mika`、`mdiri-ai/SoduWork`、`expo/exact`、`simplexai-labs/linger`、`jacobvm04/slam-dunk`、`ekrrems/Stereo-inertial-slam`、`be2rlab/ACCORD`、`justcallmekoko/ESP32Marauder`、`makerspet/oomwoo`、`esphome/esphome`、`xinnan-tech/xiaozhi-esp32-server`、`Panniantong/Agent-Reach`、`google-gemini/gemini-cli`、`rasbt/LLMs-from-scratch`、`SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark`、`fl4p/fetlib`、`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`、`okalachev/flix`、`nv-tlabs/vipe`、`MRPT/mrpt`、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`、`inmusic-software/mpc-plugin-builder-sdk`、`EasyNavigation/StrataSLAM`、`sarpstar/cinecode`。`flipperdevices/flipperzero-firmware` 的文件名是 `ReadMe.md`。`davidrapan/ha-solarman` 的文件名是 `readme.md`。`dma-firmware-customization` 的 README 没有 ESP32，身份改写的安装、配置和步骤未写入正文。`ESP32Marauder` 的具体功能和操作步骤未写入正文。`Claude-BugHunter` 的攻击步骤未写入正文。`Agent-Reach` 的登录会话做法未写入正文。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 16 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`jingyaogong/minimind`（70918，828；描述含 LLM）。
- 核对：脚本解析出 16 条后，另一次 GET 同一 URL 仍是 HTTP 200，`<article class="Box-row">` 仍是 16 个，仓库集合和顺序相同，stars today 全部不变。总 star 有变化的是：`Claude-BugHunter` 22945→22946，`superpowers` 326587→326588，`CLI-Anything` 65645→65646，`firecrawl` 210000→210001，`last30days-skill` 75074→75076，`app-store-compliance` 6457→6458，`AFFiNE` 78469→78470，`autoclip` 16126→16128。`minimind`（70918，828）、`plugins`（19522，408）、`nginx`（33363，174）、`openvino`（12648，188）、`diagram-design`（72995，1133）、`stitch-skills`（12965，352）、`opensre`（15504，343）、`Ghost-Downloader-3`（18207，950）两次总 star 一致。正文用第一次解析的数字。今日页面本身有 16 条，不是解析丢条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`elementalsouls/Claude-BugHunter`（22945，1644；技能包，没有 `llm`，攻击步骤不写入正文）、`cathrynlavery/diagram-design`（72995，1133；图示设计，没有 `llm`）、`firecrawl/firecrawl`（210000，1131；给代理做搜索和抓取，没有 `llm`）、`HKUDS/CLI-Anything`（65645，1094；把软件做成代理能调用的命令行，没有 `llm`）、`mvanhorn/last30days-skill`（75074，950；“AI agent skill”，没有 `llm`）、`XiaoYouChR/Ghost-Downloader-3`（18207，950）、`obra/superpowers`（326587，902；代理技能框架，没有 `llm`）、`zhouxiaoka/autoclip`（16126，868；AI 视频剪辑，没有 `llm`）、`mjmirza/app-store-compliance`（6457，853；“skill for AI coding agents” 是空格写法，不等于 `ai-agents`）、`toeverything/AFFiNE`（78469，578）、`cursor/plugins`（19522，408；Cursor 插件规范）、`google-labs-code/stitch-skills`（12965，352；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`Tracer-Cloud/opensre`（15504，343；CI/CD 代理，没有 `llm`）、`openvinotoolkit/openvino`（12648，188；“AI inference” 是弱词，没有 `llm`）、`nginx/nginx`（33363，174）。两条 950 的先后按页面顺序，`last30days-skill` 在 `Ghost-Downloader-3` 前面。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-27 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-27 stars:>2`。HTTP 200。`total_count=430`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`FlashCat-Jordan/Flashduck`（190）、`tahaalakhras53-boop/dma-firmware-customization`（153）、`zacharyinserra/deskhub`（152）、`andrisgauracs/bevel-os`（138）、`jthwho/bmds`（126）。昨日同页是 airprint（348）、Flashduck（189）、dma（153）、deskhub（146）、bevel-os（134）。窗口起点从昨日的 2026-10-26 移到 2026-10-27 后，`ngxson/esp32-usb-to-airprint`（`created_at` 为 `2026-10-26T16:18:54Z`）落在窗口外，本次前 5 没有它，不猜 star。`deskhub` 的总 star 从昨日搜索的 146 到本次 152，仍排在 `bevel-os`（138）前面。`Flashduck` 从 189 到 190，`dma-firmware-customization` 仍是 153。`bmds` 是本次新进入前 5 的一条。这些都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。`dma-firmware-customization` 的话题含 `esp32`，README 全文没有 ESP32。`Flashduck` 的搜索描述和话题都没有 `llm`。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-27 stars:>2`。HTTP 200。`total_count=2836`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（9992）、`mdiri-ai/SoduWork`（8117）、`expo/exact`（5117）、`simplexai-labs/linger`（4677）。`SoduWork` 的表标题现在写 Supported harnesses (7)，表内列出 7 个。`exact` 的 Bun 仍钉在 1.4.2。昨日同查询的总 star 是 Mika 9865、SoduWork 7608、exact 5056、linger 4354。这些都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
  - 未命中：`sarpstar/cinecode`（总 star 2959；描述是 “an AI coding agent writes the script”，空格写法不等于 `ai-agents`，也没有 `llm`）。它排在 linger（4677）后面。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-27 stars:>2`。HTTP 200。`total_count=3`，返回 3，规则保留 0，未命中 3。剩余配额 25。3 条就是全部结果，不是接口少给。返回顺序按总 star 是 `zjy2968466837/SicnuJw`（7）、`EngineerHabib/DOKKHO-E_Commerce-Porject-SICIP`（4）、`SicoKaleb/SicoAutoTerms`（3）。星数与昨日这 3 条相同。昨日窗口里还有第 4 条，本次 `total_count=3` 的全部结果里没有它，不猜 star。
  - 名称词边界未命中：`SicnuJw`（四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`DOKKHO-E_Commerce-Porject-SICIP`（名称 `SICIP` 不等于 `sic`，搜索描述为空）、`SicoAutoTerms`（`Sico` 不等于 `sic`，描述与碳化硅无关）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-27 stars:>2`。HTTP 200。`total_count=79`，返回 5，规则保留 0，未命中 5。剩余配额 23。按总 star，本页是 `acrobat-dc-desktop`（210）、`okx-agent-trade-kit-mcp-grid-dca-bot`（124）、`blender-5-3-zbrush-2027-3dcg-modeling-suite-ja`（121）、`isometric-cities`（92）、`mvc2-naomi-dc`（83）。
  - 名称和搜索描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（210；Acrobat DC 不等于 `dc-dc`）、`bettysuzuki/okx-agent-trade-kit-mcp-grid-dca-bot`（124；名称里的 DCA 不等于 `dc-dc`，裸 mcp 不计入）、`mywilliam211/blender-5-3-zbrush-2027-3dcg-modeling-suite-ja`（121；名称里的 3dcg 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（92；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`gibletto/mvc2-naomi-dc`（83；NAOMI 街机的反编译移植，名称里的 dc 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-27 stars:>2`。HTTP 200。`total_count=105`，返回 5，规则保留 4，未命中 1。剩余配额 21。正文保留 `jacobvm04/slam-dunk`（160）、`ekrrems/Stereo-inertial-slam`（91）、`be2rlab/ACCORD`（82）。`slam-dunk` 的总 star 与昨日搜索相同，仍是 160。`Stereo-inertial-slam` 昨日搜索是 89，本次是 91。昨日的 `ACCORD` 不在前 5，本次回到前 5，总 star 82；2026-11-24 那次搜索是 76。这些都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。按总 star，本页顺序是 `mpc-plugin-builder-sdk`（229）、`slam-dunk`（160）、`StrataSLAM`（96）、`Stereo-inertial-slam`（91）、`ACCORD`（82）。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 229）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。README 还写 MPC Sample 要固件 v1.4.0 或更新，只做效果。描述里的 “AI coding agent” 是空格写法，不等于 `ai-agents`。
  - 名称和 topics 未命中：`EasyNavigation/StrataSLAM`（总 star 96；搜索描述为空，名称 `StrataSLAM` 里 slam 前面是字母，词边界不等于 `slam`）。README 写的是多层 ROS 2 SLAM，不参与归类，正文不收。

### C. 领域常青（`pushed:>=2026-11-19 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-19 stars:>3`。HTTP 200。`total_count=1339`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=3`、`per_page=5`，本页是总结果里按总 star 排序后的第 11 到第 15 条。本查询正文：`flipperdevices/flipperzero-firmware`（16996）、`justcallmekoko/ESP32Marauder`（13236）、`esphome/esphome`（12172）、`xinnan-tech/xiaozhi-esp32-server`（11413）。另有 1 条完整条目不在本页前 5、但写在自动控制：`makerspet/oomwoo`（13221，话题含 ros2 与 slam，也含 esp32）。另有 3 条一行不在本页前 5：`okalachev/flix`（2556，话题含 esp32，完整条目在自动控制）、`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（726，话题含 modbus，完整条目在电力电子）、`davidrapan/ha-solarman`（561，话题含 modbus，完整条目在电力电子）。`xiaozhi-esp32-server` 话题含 mcp-server，不是 AI 关键词；README 出现大模型，搜索描述和话题没有 `llm`，不跨 AI。`flipperzero-firmware` 的文件名是 `ReadMe.md`。`oomwoo` 的 README 仍写明现在不能按物料单组装，只能仿真。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-19 stars:>3`。HTTP 200。`total_count=9418`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 26。正文保留 `Panniantong/Agent-Reach`（114720）、`google-gemini/gemini-cli`（109114）、`rasbt/LLMs-from-scratch`（109051）。按总 star，本页顺序是 impeccable、Agent-Reach、open-design、gemini-cli、LLMs-from-scratch。`page=3` 是总结果里的第 11 到第 15 条。`Agent-Reach` 靠话题 `llm-tools` 计入 llm。`gemini-cli` 靠话题 `ai-agents`；README 仍写免费个人访问已于 2026-06-18 转到 Antigravity CLI。`LLMs-from-scratch` 靠话题 `llm` 与 `pytorch`，ISBN 仍是 9781633437166。另有 1 条一行来自自动控制检索：`MRPT/mrpt`（2177，话题含 computer-vision）。
  - 未命中：`pbakaus/impeccable`（总 star 116878；描述是 “your coding agent”，空格写法不等于 `ai-agents`，也没有 `llm`）。它排在本页第 1。`nexu-io/open-design`（总 star 109488；描述是 “with your team and AI agents”，空格写法不等于 `ai-agents`，也没有 `llm`）。它排在 Agent-Reach 和 gemini-cli 之间。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-19 stars:>3`。HTTP 200。`total_count=29`，返回 5，规则保留 2，排除清单 1，未命中 2。剩余配额 24。`page=3` 是总结果里按总 star 排序后的第 11 到第 15 条。`total_count=29`，本页 5 条不是末页，也不是接口失败。本页星数是 12、10、10、9、8。两条 10 星分别是 `spice_model_benchmark` 和下面的 awesome 镜像。脚本把保留和剔除分成两份列表，没有保存这两条在接口里的先后，本次不补查、不猜测顺序。正文保留 `SJTU-YONGFU-RESEARCH-GRP/spice_model_benchmark`（10）和 `fl4p/fetlib`（9）。
  - 清单类排除：`satnamrsm/https-github.com-sickn33-antigravity-awesome-skills`（总 star 10；仓库名命中 awesome，搜索描述为空）。正文不收。
  - 名称词边界未命中：`linuxserver/docker-sickgear`（12；搜索描述为空，`SickGear` 不等于 `sic`）、`danhyun-jeong/sickle-cite`（8；韩文人文引用格式工具，`sickle` 不等于 `sic`）。
  - `fl4p/fetlib`（总 star 9）：话题含 mosfet 与 power-supply。完整条目在功率器件，电力电子一行带过。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-19 stars:>3`。HTTP 200。`total_count=422`，返回 5，规则保留 2，未命中 3。剩余配额 22。`page=3` 是总结果里按总 star 排序后的第 11 到第 15 条。正文完整条目为 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（726）、`davidrapan/ha-solarman`（561）。另有 1 条一行来自功率器件检索：`fl4p/fetlib`（9，话题含 power-supply 与 mosfet）。按总 star，本页顺序是 `DCGM`、`dcs_liberation`、`dcrd`、`Sungrow`、`ha-solarman`。
  - 名称、话题和搜索描述未命中电力电子：`NVIDIA/DCGM`（821；NVIDIA 数据中心 GPU 管理，`DCGM` 不等于 `dc-dc`）、`dcs-liberation/dcs_liberation`（804；DCS World 动态战役，`dcs` 不等于 `dc-dc`）、`decred/dcrd`（777；Decred 守护进程，`dcrd` 不等于 `dc-dc`）。
  - Sungrow 的正式集成目标仍是 2026 年 12 月。`ha-solarman` 的文件名是 `readme.md`。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-19 stars:>3`。HTTP 200。`total_count=229`，返回 5，规则保留 4，排除清单 1，未命中 0。剩余配额 29。正文保留 `okalachev/flix`（2556）、`nv-tlabs/vipe`（2222）、`MRPT/mrpt`（2177）、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`（1962）。另有 1 条完整条目来自嵌入式检索：`makerspet/oomwoo`（13221）。按总 star，本页顺序是 flix、vipe、mrpt、awesome-NeRF-and-3DGS-SLAM、AutonomousVehicleControlBeginnersGuide。本次响应头的剩余配额是 29，前一条自动控制新项目是 21，中间没有失败重试。两次搜索间隔 7 秒，前面的请求已经跨过一分钟，配额窗口滚动，按响应头原样记录。
  - 清单类排除：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2164；仓库名命中 awesome，话题含 slam）。正文不收。它夹在 mrpt（2177）和 AutonomousVehicleControlBeginnersGuide（1962）之间。
  - `flix` 的 README 物料表有 MOSFET，搜索描述和话题没有，不跨功率器件。`mrpt` 的 README 写 MRPT 3 与 C++17；MOLA 行里的 ROS 2 不把本仓库算成 ros2。`vipe` 的 16 FPS、14 FPS、12 FPS 是 README 数字，不是本次实测。
