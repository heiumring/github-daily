# GitHub 领域日报 · 2026-11-22

生成时间：2026-11-22 07:40（北京时间）。数据拉取开始于 2026-11-22 07:35:34（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-23（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-15 及之后有推送、总 star > 3。轮换页 `page = (当年第 326 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 让人用自己的显卡从零训一个大约 64M 的小模型，而不是只调用现成的大模型；总 star 68133，24 小时新增 star 488。这是今日热度里唯一命中领域的仓库。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 9448，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) 把 Gemini 放进终端里当编程代理；README 写明本仓库现在面向企业版 Code Assist，个人免费访问已在 2026-06-18 转到 Antigravity CLI。总 star 108975，没有 24 小时新增数据。这是本页常青里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 16 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

嵌入式、功率器件、电力电子电源、自动控制在这 16 条里都没有命中。

### AI

- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
  - 说明：把大模型的训练过程拆到个人显卡上能跑完，用来看懂预训练、微调和对齐，而不是只调一个封装好的接口。README 写主线最小版本大约 64M，并用 PyTorch 从零实现整条训练链路。同一段注明「2 小时」是监督微调阶段在单张 NVIDIA 3090 上跑完 1 个 epoch 的实测，「3 块钱」是这段时间的租卡费用。搜索描述里的 LLM 计入 AI。
  - 领域：AI
  - 总 star：68133
  - 24 小时新增 star：488

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [Kristian8606/esp32-airplay2-surround](https://github.com/Kristian8606/esp32-airplay2-surround)
  - 说明：用便宜的板子自己组一套无线环绕声。README 写明 Apple TV 只看到网关这一台 AirPlay 2 音箱，网关把 5.1 / 7.1 码流原样分给音箱板，每块 ESP32-S3 只解码自己的声道。目前写明网关加五只音箱（前左右、中置、两侧）已经能同步播放 5.1 和 7.1，iPhone 的立体声也能跟上；闪存建议买 16 MB 的 N16R8，8 MB 板仍能编译，音箱固件副本只剩大约 117 KB。搜索描述为空，话题也为空，只靠仓库名里的 esp32 归入嵌入式。`created_at` 为 `2026-10-24T16:13:06Z`。
  - 领域：嵌入式 Embedded
  - 总 star：403
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。表格里 MG2500 系列的 MG2550S 标成绿，意思是已在真机验证；其余型号标成黄，预期能用但还没上真机。
  - 领域：嵌入式 Embedded
  - 总 star：345
- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑；ESP-IDF 6.0.1 起，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：186
- [tahaalakhras53-boop/dma-firmware-customization](https://github.com/tahaalakhras53-boop/dma-firmware-customization)
  - 说明：仓库自称是一份给 PCIe DMA 板改写固件身份、让主机把它认成别的设备的说明。README 标题是 “DMA Firmware Customization — Security Tool”，搜索描述写成针对 PCIe Screamer Squirrel 的硬件混淆指南。这是在总线上隐瞒设备身份，正文不写安装、配置和改写步骤。话题含 embedded 与 esp32，仓库名含 firmware，因此归入嵌入式；README 全文没有 ESP32，不把话题里的 esp32 写成这块板的主控。话题里同时有 adc、battery-monitor、hub75、oled 等和这份说明对不上的标签。`created_at` 为 `2026-11-15T19:45:19Z`。
  - 领域：嵌入式 Embedded
  - 总 star：153
- [andrisgauracs/bevel-os](https://github.com/andrisgauracs/bevel-os)
  - 说明：在一块 ESP32-S3 上跑一个能开窗口的小桌面，用六只电阻把 640×480、64 色的画面送到 VGA 显示器。README 写它由模型 Claude Fable 5.2 写成，人负责接线和 3D 打印；开机到桌面 0.7 秒，窗口里的 Doom（共享版 E1M1）大约 32 帧。搜索描述里的 ESP32-S3 按词边界计入 esp32。`created_at` 为 `2026-11-14T14:18:34Z`。
  - 领域：嵌入式 Embedded
  - 总 star：127

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：9448
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
  - 说明：给团队自托管的一件工作引擎。提一句需求不算做完，要等提出的人签收；可以指定一个代理干活，另一个代理按验收标准复查，不过就退回。README 首页列出 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code、Codex Harness 和 Codex。展开的表标题写支持 9 个 harness，表里实际列出这 7 个，没有写出的两个不计入。话题含 llm 与 ai-agents。`created_at` 为 `2026-10-29T02:43:14Z`。
  - 领域：AI
  - 总 star：6439
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给作者和安全团队保护自己即将发布的程序，让自动做逆向的语言模型代理在受保护的产物上得不到可用结果。README 徽章写 npm 包 `bla-agents` v3.5.7，并写明在 14 个对照目标上验证过；开头声明用途只限于保护自己的知识产权和发布物。话题 `llm-security` 按词边界计入 llm。防护参数和绕过细节不写入正文。
  - 领域：AI
  - 总 star：6378
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、iOS、macOS、Android 和 Linux 上按各自的原生控件跑，编程代理可以自己建、自己跑、自己看、自己测。README 写界面用一种叫 Contract 的声明式语言，布局和属性名沿用 CSS；网页产物是大约 20 KB 的运行时加上一个 ES 模块。Android 写明已经能用，Material 3 的打磨还在进行；Windows 仍在早期。仓库仍是 pre-1.0，没有打包发布。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：4874

### 功率器件 Power Devices

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

本窗口没有以功率器件为最贴近领域的完整新项目。名称撞上 `sic` 的课堂笔记本已剔除。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。返回的 5 条里，1 条是公司后缀 LLC，不是谐振变换器；另外 4 条的名称、话题和搜索描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`。详见数据源状态。

### 自动控制 Control

- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：给第一人称、野外长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参。README 写一套常规的离线光束法平差能缩小和行业系统的差距，但会停在公开提交的水平；把这两项物理现象放进同一条流水线后，LaMAria 训练集的控制点分数从 69.1 到 82.4。它在 LaMAria 测试集上与 Aria 的 SLAM 打平，并在五个类别里的三个上第一次超过 Aria，UZH-FPV 排行榜上排第二。仓库名里的 slam 计入自动控制。`created_at` 为 `2026-11-13T01:47:26Z`。
  - 领域：自动控制 Control
  - 总 star：156
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用递归的非均匀 B 样条做多传感器里程计，同一套估计能接激光惯性、激光视觉惯性和腿式运动学，并可选全局样条修正。README 写这些组合都能在实时约束里跑完，支持 ROS 2 Humble（Ubuntu 22.04）和 Jazzy（Ubuntu 24.04）。话题含 ros2 与 slam。`created_at` 为 `2026-10-27T16:44:13Z`。
  - 领域：自动控制 Control
  - 总 star：63
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用一个水箱、超声测距和一台泵，把通断、P 和 PI 液位控制做成可以对照仿真的实验。README 写实验台是 15 L 罐子，由 500 L 水箱经一台约 0.5 马力、230 V 的泵补水，市电泵走 Fotek SSR-40DA，直流泵则用 MOSFET 做 PWM；MATLAB 应用的物理量来自你自己的水箱、出口和泵，徽章写 MATLAB R2023b 及以上。2026-10-26 的实测写明当天罐子还没有排水口，靠手倒空，超调是 2.8 cm（11% 到 13%）。话题含 control-systems，话题 `pid-control` 按词边界计入 pid。水位控制比 MOSFET 开关更贴近本领域，功率器件一节一行带过。这条来自功率器件新项目检索，不在自动控制本页前 5。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=3`、`per_page=5`，本页是各查询按总 star 排序后的第 11 到第 15 条。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件源码。话题含 stm32 与 firmware。README 把功能说明指到官网和用户文档，本仓库主要放固件源码和贡献规则。默认说明文件名是 `ReadMe.md`。
  - 领域：嵌入式 Embedded
  - 总 star：16952
- [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder)
  - 说明：给 ESP32 准备一套 Wi-Fi 和蓝牙工具固件。搜索描述和 README 标题都把它写成进攻和防护两类工具。话题含 esp32 与 firmware，也含 esp32-c5 与 esp32-s2。具体功能、安装和操作步骤不写入正文。
  - 领域：嵌入式 Embedded
  - 总 star：13186
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13175。
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用一份配置文件驱动 ESP32、ESP8266、BK72xx 和 RP2040，再交给家庭自动化系统远程控制，不用从每种板子的固件写起。搜索描述写明这一点。README 本身主要是标志和文档链接。话题含 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：12146
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给小智 ESP32 语音硬件提供后端，把设备接到语音识别和对话服务上。搜索描述写的是快速搭建 ESP32 设备控制服务器。话题含 esp32。README 里出现大模型字样，搜索描述和话题没有 `llm`；话题 `mcp-server` 不是 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：11362
- [okalachev/flix](https://github.com/okalachev/flix) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：2531。
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：722。
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：558。

### AI

- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：在终端里跑一个开源的 Gemini 编程代理。README 写明它现在面向 Gemini Code Assist 的标准版、企业版，以及 Google Cloud 上的 Code Assist for GitHub；个人免费访问和 Google AI Pro / Ultra 已在 2026-06-18 转到 Antigravity CLI。同一段写它没有针对 Gemini 4 系列调过。话题含 ai-agents。搜索描述没有 `llm`。
  - 领域：AI
  - 总 star：108975
- [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
  - 说明：把一本从零实现类 GPT 模型的书配上可运行的代码，用来自己走完预训练和微调，而不是只调现成接口。README 写这是 *Build a Large Language Model (From Scratch)* 的官方代码仓库，ISBN 9781633437166，并用 PyTorch 实现。话题含 llm 与 pytorch。这是一本书的配套代码，不是外部公开课清单，正文保留。
  - 领域：AI
  - 总 star：108772
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：给 Python 一套带 GPU 加速的张量计算和动态神经网络，训练和推理都从这里搭。README 写它提供类似 NumPy 的张量运算，以及基于磁带的自动求导。仓库名 `pytorch` 计入 AI。话题里没有再单独标 `pytorch`。
  - 领域：AI
  - 总 star：105780
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2175。

### 功率器件 Power Devices

- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：17。

本页没有以功率器件为最贴近领域的完整条目。`epilys/sic` 是链接聚合，已剔除。详见数据源状态。

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：把阳光电源逆变器的 Modbus 数据接进 Home Assistant，用 YAML 就能看发电和电池。搜索描述列出 SH*RT（如 SH10RT）、SHx.RS（如 SH3.RS）、SH*K（如 SH4K6）和 SxT（如 S20T）。README 在 2026-11-07 写明，一个真正的集成正在 `proper-ha-integration` 分支上做，目标是 2026 年 12 月，实体 ID 保持不变，现有 YAML 包会继续维护到新集成对齐功能。话题含 inverter。话题也含 modbus，嵌入式一节一行带过。`pushed_at` 为 `2026-11-21T22:15:36Z`。
  - 领域：电力电子电源 Power Supply
  - 总 star：722
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman)
  - 说明：把 Solarman 采集棒上的逆变器数据接进 Home Assistant。README 写它基于异步的 pysolarmanv5，并支持 Modbus TCP，例子包括 ESP 桥、Waveshare 和以太网记录仪。话题含 inverter，也标了德业、首航、锦浪等品牌。话题含 modbus，嵌入式一节一行带过。默认说明文件名是 `readme.md`。`pushed_at` 为 `2026-11-20T11:39:13Z`。
  - 领域：电力电子电源 Power Supply
  - 总 star：558
- [fl4p/batmon-ha](https://github.com/fl4p/batmon-ha)
  - 说明：在 Home Assistant 里用蓝牙读多块电池管理系统的电芯电压和电流，不用再接一块专门的板。搜索描述列出 JK、JBD、Daly、ANT、SOK、Supervolt 等。README 开头写用主机自带蓝牙，不另加 USB、串口、RS485 或 ESP32；后文另有可选的串口和 RS485。话题 `jikong-bms` 按词边界计入 bms。搜索话题没有 esp32，不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：536
- [AndyShaman/BYDMate](https://github.com/AndyShaman/BYDMate)
  - 说明：给比亚迪 DiLink 车机记行程和真实电耗。README 写车机自带电脑会把电耗报低，这个应用直接读 BMS 的 energydata，并写这个差距是 10% 到 30%。搜索描述列出 DiLink 3.0 / 5.0 / 5.1 和 UI7，以及豹 3、豹 5、海狮 07、宋、宋 Pro DM-i、Atto 3；README 徽章是 Android 10 及以上，并多写了 DiLink 4.0。描述里的 “voice AI agent” 是空格写法，不等于 `ai-agents`，不跨到 AI。归类靠描述里的 BMS。
  - 领域：电力电子电源 Power Supply
  - 总 star：531
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 主机和一台有线调制解调器做一套 12 V 磷酸铁锂直流不间断电源，停电时先撑住，电量见底前把主机关干净。README 写明威电源经 MOSFET 理想二极管浮充 10 Ah 电池，Victron BatteryProtect 做硬件低压断开，18 V 升压给现在的 N100DC 主机。监测固件是 ESPHome V1.20。2026-09-15 从起始到低压断开测得 2.5331 Ah / 31.821 Wh。搜索描述仍写 2026-05-06 的 4.18 Ah / 53.3 Wh；README 写明 2026 年 9 月以前包括约 4.18 Ah 在内的续航数字，描述的是已经换掉的电池包和负载。话题含 power-supply，所以完整条目放在电力电子；话题里的 mosfet 是理想二极管，功率器件一节一行带过。README 的监测板是 XIAO ESP32-C3，搜索话题没有 esp32，不跨到嵌入式。这条来自功率器件常青检索，不在电力电子本页前 5。
  - 领域：电力电子电源 Power Supply
  - 总 star：17

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：一台自己做的开源扫地机器人，用二维激光雷达在本地建图和导航，常规功能不依赖云。README 仍写明现在还不能按物料单造出来，今天只能在仿真里跑，物料单要等第一版在真机上核对过。话题含 ros2 与 slam，也含 esp32。扫地的定位导航比板子更贴近本领域，嵌入式一节一行带过。这条来自嵌入式常青检索，不在自动控制本页前 5。总 star 高于本页三条。
  - 领域：自动控制 Control
  - 总 star：13175
- [okalachev/flix](https://github.com/okalachev/flix)
  - 说明：用通用零件从零做一台 ESP32 四旋翼。README 写固件大约两千行 Arduino，通信用 MAVLink，Gazebo 里能仿真；1.1 版是 3D 打印的机架，并且真的能飞。话题含 flight-controller 与 esp32。飞控比板子更贴近本领域，嵌入式一节一行带过。物料表里的 MOSFET 不在搜索描述和话题里，不跨到功率器件。
  - 领域：自动控制 Control
  - 总 star：2531
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：移动机器人的 C++ 工具箱，把定位、建图和运动估计放在同一套库里。README 写它从 2005 年在马拉加大学起步，MRPT 3.0 改成按 colcon 分包、公开接口对齐 C++17。话题含 slam 与 computer-vision。定位建图比视觉话题更贴近本领域，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：2175
- [ShisatoYano/AutonomousVehicleControlBeginnersGuide](https://github.com/ShisatoYano/AutonomousVehicleControlBeginnersGuide)
  - 说明：用同一套 Python 仿真把自动驾驶拆成定位、建图、规划和跟踪，换一个算法就能在同一条链路里对比。README 写每个算法是一段带动画的小仿真，并配有一本放在本仓库里的开放教材。话题含 slam 与 kalman-filter。这是仓库自带的仿真和教材，不是外部公开课清单，正文保留。
  - 领域：自动控制 Control
  - 总 star：1963

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。本次跨节的是水位实验（功率器件一行，自动控制完整）、oomwoo 与 flix（嵌入式一行，自动控制完整）、Sungrow 与 ha-solarman（嵌入式一行，电力电子完整）、DIY-LiFePO4-UPS（功率器件一行，电力电子完整）、MRPT（AI 一行，自动控制完整）。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API（定位仓库默认说明文件），下列仓库全部 HTTP 200：`jingyaogong/minimind`、`Kristian8606/esp32-airplay2-surround`、`ngxson/esp32-usb-to-airprint`、`FlashCat-Jordan/Flashduck`、`tahaalakhras53-boop/dma-firmware-customization`、`andrisgauracs/bevel-os`、`wangzan101/Mika`、`mdiri-ai/SoduWork`、`qybaihe/bla`、`expo/exact`、`Samarth030312/arduino-water-level-control-lab`、`sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`、`epilys/sic`、`wkcollis1-eng/DIY-LiFePO4-UPS`、`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`、`davidrapan/ha-solarman`、`fl4p/batmon-ha`、`AndyShaman/BYDMate`、`darkfibr/artex-forensics`、`jacobvm04/slam-dunk`、`ASIG-X/RESPLE2`、`inmusic-software/mpc-plugin-builder-sdk`、`okalachev/flix`、`MRPT/mrpt`、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`、`flipperdevices/flipperzero-firmware`、`justcallmekoko/ESP32Marauder`、`makerspet/oomwoo`、`esphome/esphome`、`xinnan-tech/xiaozhi-esp32-server`、`google-gemini/gemini-cli`、`rasbt/LLMs-from-scratch`、`pytorch/pytorch`。`flipperzero-firmware` 的文件名是 `ReadMe.md`，`ha-solarman` 是 `readme.md`。`dma-firmware-customization` 的 README 没有 ESP32，身份改写的安装、配置和步骤未写入正文。`artex-forensics` 的 README 只用来确认公司后缀，其中的漏洞复现步骤未写入正文。`bla` 的防护参数和绕过细节未写入正文。`ESP32Marauder` 的功能、安装和操作步骤未写入正文。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 16 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`jingyaogong/minimind`（68133，488；描述含 LLM）。
- 核对：脚本解析出 16 条后，另一次 GET 同一 URL 仍是 HTTP 200，`<article class="Box-row">` 仍是 16 个，仓库集合和顺序相同，stars today 全部不变。总 star 有变化的是：`Claude-BugHunter` 15991→15994，`superpowers` 323702→323704，`CLI-Anything` 62053→62056，`plugins` 18096→18097，`firecrawl` 206153→206156，`openvino` 11925→11926，`diagram-design` 69778→69779，`last30days-skill` 71971→71973，`stitch-skills` 11404→11407，`app-store-compliance` 3376→3379，`opensre` 13975→13976，`AFFiNE` 76268→76271，`Ghost-Downloader-3` 14420→14419，`autoclip` 12824→12825。`minimind`（68133，488）与 `nginx`（32723，195）两次一致。正文用第一次解析的数字。今日页面本身有 16 条，不是解析丢条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`elementalsouls/Claude-BugHunter`（15991，1794；技能包，没有 `llm`，攻击步骤不写入正文）、`firecrawl/firecrawl`（206153，999；给代理做搜索和抓取，没有 `llm`）、`obra/superpowers`（323702，884；代理技能框架，没有 `llm`）、`XiaoYouChR/Ghost-Downloader-3`（14420，774）、`HKUDS/CLI-Anything`（62053，767；把软件做成代理能调用的命令行，没有 `llm`）、`mjmirza/app-store-compliance`（3376，724；“AI coding agents” 是空格写法，不等于 `ai-agents`）、`zhouxiaoka/autoclip`（12824，689；AI 视频剪辑，没有 `llm`）、`cathrynlavery/diagram-design`（69778，582；图示设计，没有 `llm`）、`toeverything/AFFiNE`（76268，577）、`mvanhorn/last30days-skill`（71971，566；“AI agent skill”，没有 `llm`）、`Tracer-Cloud/opensre`（13975，450；CI/CD 代理，没有 `llm`）、`google-labs-code/stitch-skills`（11404，324；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`cursor/plugins`（18096，261；Cursor 插件规范）、`openvinotoolkit/openvino`（11925，202；“AI inference” 是弱词，没有 `llm`）、`nginx/nginx`（32723，195）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-23 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-23 stars:>2`。HTTP 200。`total_count=447`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`Kristian8606/esp32-airplay2-surround`（403）、`ngxson/esp32-usb-to-airprint`（345）、`FlashCat-Jordan/Flashduck`（186）、`tahaalakhras53-boop/dma-firmware-customization`（153）、`andrisgauracs/bevel-os`（127）。`esp32-airplay2-surround` 的搜索描述和话题都为空，只靠仓库名 `esp32`。`Flashduck` 的 `created_at` 为 `2026-10-31T05:10:09Z`，搜索描述和话题都没有 `llm`，不跨到 AI。`dma-firmware-customization` 的 `created_at` 为 `2026-11-15T19:45:19Z`，话题含 `esp32`，README 全文没有 ESP32。`bevel-os` 的 `created_at` 为 `2026-11-14T14:18:34Z`，搜索描述里的 ESP32-S3 计入 esp32。窗口起点从昨日的 2026-10-22 移到 2026-10-23。这 5 条的 `created_at` 都晚于 2026-10-23，仍在窗口内。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-23 stars:>2`。HTTP 200。`total_count=2813`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（9448）、`mdiri-ai/SoduWork`（6439）、`qybaihe/bla`（6378）、`expo/exact`（4874）。`exact` 的 `created_at` 为 `2026-11-02T01:29:01Z`。`Mika` 的 `created_at` 为 `2026-10-29T14:34:07Z`。`SoduWork` 的 `created_at` 为 `2026-10-29T02:43:14Z`。`bla` 的 npm 徽章现为 v3.5.7。`SoduWork` 的表标题写 9 个 harness，表内列出 7 个。昨日同查询里 `SoduWork` 的总 star 是 5960，排在 `bla`（6323）之后；本次是 6439，排到 `bla`（6378）前面。两次都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
  - 未命中：`benjitaylor/skills`（总 star 3952；描述是 “Skills for AI coding agents.”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。按总 star 它是返回的第 5 条，排在 `exact`（4874）之后。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-23 stars:>2`。HTTP 200。`total_count=5`，返回 5，规则保留 2，未命中 3。剩余配额 25。`total_count` 等于返回条数，本次没有第 6 条。规则保留的 2 条里，1 条是课堂笔记本，剔除；1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9），其次是课堂笔记本（7），然后是 `SicnuJw`（6），`SicoAutoTerms` 与 `Sicip-data-science` 都是 3。
  - `sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`（总 star 7）：名称含 SIC，搜索描述为空。README 标题写明这是 Samsung Innovation Campus 2026 的 PA-C 与 PA-D 课堂材料，含 Google Colab 笔记本，没有讲师姓名，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-24T17:55:41Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（6；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`SicoKaleb/SicoAutoTerms`（3；`Sico` 不等于 `sic`，描述与碳化硅无关）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-23 stars:>2`。HTTP 200。`total_count=78`，返回 5，规则保留 1，未命中 4。剩余配额 23。规则留下的 1 条是公司后缀，剔除后本日无新项目。按总 star，本页是 `acrobat-dc-desktop`（210）、`isometric-cities`（90）、`artex-forensics`（78）、`mvc2-naomi-dc`（68）、`grid-dca-bot`（49）。
  - 撞名剔除：`darkfibr/artex-forensics`（总 star 78）。README 标题是 “ARTEX Forensics — Blackfish Security LLC”，搜索描述末尾也是 Blackfish Security LLC。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。搜索描述和话题没有 `llm`，不因 README 里出现的模型字样跨到 AI。漏洞复现步骤未写入正文。
  - 名称、话题和搜索描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（210；Acrobat DC 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（90；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`gibletto/mvc2-naomi-dc`（68；街机游戏反编译，名称里的 dc 不等于 `dc-dc`）、`leftamber/grid-dca-bot`（49；名称里的 DCA 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-23 stars:>2`。HTTP 200。`total_count=111`，返回 5，规则保留 3，未命中 2。剩余配额 21。正文保留 `jacobvm04/slam-dunk`（156）、`ASIG-X/RESPLE2`（63）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`RESPLE2` 的 `created_at` 为 `2026-10-27T16:44:13Z`。按总 star，本页顺序是 `mpc-plugin-builder-sdk`（200）、`slam-dunk`（156）、`SampQOL-OS`（127）、`melodee-sample`（72）、`RESPLE2`（63）。窗口起点移到 2026-10-23 之后，昨日报告里的 `mozihe/z-localization`（当时总 star 131，`created_at` 为 `2026-10-22T08:49:49Z`）落在新窗口外，本次查询不会返回它，也不猜它现在的 star。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 200）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。描述里的 “AI coding agent” 是空格写法，不等于 `ai-agents`。
  - 名称和 topics 未命中：`snarebes/SampQOL-OS`（总 star 127；描述里的 Akai MPC Sample 不是强特征词，名称也不含 `mpc`）、`keremimo/melodee-sample`（总 star 72；描述里的 Akai MPC Sample 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-15 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-15 stars:>3`。HTTP 200。`total_count=1346`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=3`、`per_page=5`，本页是总结果里按总 star 排序后的第 11 到第 15 条。本查询正文：`flipperdevices/flipperzero-firmware`（16952）、`justcallmekoko/ESP32Marauder`（13186）、`esphome/esphome`（12146）、`xinnan-tech/xiaozhi-esp32-server`（11362）。另有 1 条完整条目不在本页前 5、但写在自动控制：`makerspet/oomwoo`（13175，话题含 ros2 与 slam，也含 esp32）。另有 3 条一行不在本页前 5：`okalachev/flix`（2531，话题含 esp32，完整条目在自动控制）、`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（722，话题含 modbus，完整条目在电力电子）、`davidrapan/ha-solarman`（558，话题含 modbus，完整条目在电力电子）。`xiaozhi-esp32-server` 话题含 mcp-server，不是 AI 关键词；README 出现大模型，搜索描述和话题没有 `llm`，不跨 AI。`flipperzero-firmware` 的文件名是 `ReadMe.md`。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-15 stars:>3`。HTTP 200。`total_count=9785`，返回 5，规则保留 3，排除清单 0，未命中 2。剩余配额 26。正文保留 `google-gemini/gemini-cli`（108975）、`rasbt/LLMs-from-scratch`（108772）、`pytorch/pytorch`（105780）。另有 1 条一行不在本页前 5：`MRPT/mrpt`（2175，话题含 computer-vision，完整条目在自动控制）。按总 star，本页顺序是 impeccable、gemini-cli、open-design、LLMs-from-scratch、pytorch。`page=3` 是总结果里的第 11 到第 15 条。`gemini-cli` 靠话题 `ai-agents`，搜索描述没有 `llm`。`pytorch` 靠仓库名。
  - 未命中：`pbakaus/impeccable`（总 star 114523；描述是 “coding agent”，不等于 `ai-agents`）。它是本页第 1 条。`nexu-io/open-design`（总 star 108840；描述是 “AI agents”，空格写法不等于 `ai-agents`）。它夹在 gemini-cli 与 LLMs-from-scratch 之间。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-15 stars:>3`。HTTP 200。`total_count=30`，返回 5，规则保留 2，排除清单 0，未命中 3。剩余配额 24。`page=3` 是总结果里按总 star 排序后的第 11 到第 15 条。返回的星数是 27、20、18、17、14。`total_count=30`，本页 5 条是末段之前的一页，不是接口失败。规则留下的 2 条里，1 条是链接聚合，剔除；1 条是 UPS，更贴近电力电子，本节只留一行。本节没有完整条目。
  - 撞名剔除：`epilys/sic`（总 star 27）。名称是 sic，搜索描述和 README 写明这是按标签组织的链接聚合，公开实例在 sic.pm，与碳化硅器件无关，正文不收。
  - 名称词边界未命中：`SICKAG/sick_safetyscanners_base`（20；SICK 安全激光雷达的 C++ 驱动，`SICK` 不等于 `sic`。描述没有 `ros2`，不跨到自动控制）、`sicopolis/sicopolis`（18；冰盖演化仿真，`sicopolis` 不等于 `sic`）、`ducroo/SICTIC-AI`（14；瑞士商业天使俱乐部 SICTIC 的引擎，`SICTIC` 不等于 `sic`。描述里的 AI 是弱词，搜索描述和话题没有 `llm`，不跨到 AI）。
  - `DIY-LiFePO4-UPS`（17）话题含 mosfet 与 power-supply。完整条目在电力电子，本节一行带过。README 写了 XIAO ESP32-C3，搜索话题没有 esp32，不跨嵌入式。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-15 stars:>3`。HTTP 200。`total_count=420`，返回 5，规则保留 4，未命中 1。剩余配额 22。`page=3` 是总结果里按总 star 排序后的第 11 到第 15 条。正文保留 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（722）、`davidrapan/ha-solarman`（558）、`fl4p/batmon-ha`（536）、`AndyShaman/BYDMate`（531）。另有 1 条完整条目来自功率器件常青检索：`wkcollis1-eng/DIY-LiFePO4-UPS`（17）。按总 star，本页顺序是 `dcrd`、Sungrow、ha-solarman、batmon-ha、BYDMate。
  - 名称和 topics 未命中电力电子：`decred/dcrd`（777；Decred 守护进程，名称里的 dcrd 不等于 `dc-dc`）。它是本页第 1 条。
  - `Sungrow` 与 `ha-solarman` 话题含 modbus，嵌入式各一行。`batmon-ha` 的 README 开头写不另加 ESP32，搜索话题没有 esp32，不跨嵌入式。`BYDMate` 靠描述里的 BMS 计入；“voice AI agent” 不等于 `ai-agents`。`ha-solarman` 的文件名是 `readme.md`。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-15 stars:>3`。HTTP 200。`total_count=255`，返回 5，规则保留 3，未命中 0，排除清单 2。剩余配额 29。正文保留 `okalachev/flix`（2531）、`MRPT/mrpt`（2175）、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`（1963）。`flix` 在嵌入式一行，`mrpt` 在 AI 一行。另有 1 条完整条目来自嵌入式常青检索：`makerspet/oomwoo`（13175）。按总 star，本页顺序是 awesome-robotics-libraries、flix、mrpt、awesome-NeRF-and-3DGS-SLAM、AutonomousVehicleControlBeginnersGuide。本次响应头的剩余配额是 29，前一条自动控制新项目是 21，中间没有失败重试，按响应头原样记录。
  - 清单类排除：`jslee02/awesome-robotics-libraries`（总 star 3114；描述是 curated list，话题含 slam，脚本已按 awesome 排除）。它是本页第 1 条。`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2163；描述是 comprehensive list，话题含 slam，脚本已按 awesome 排除）。它夹在 mrpt 与 AutonomousVehicleControlBeginnersGuide 之间。
  - `flix` 的 README 物料表有 MOSFET，搜索描述和话题没有，不跨功率器件。`mrpt` 话题含 computer-vision，AI 一节一行带过。
