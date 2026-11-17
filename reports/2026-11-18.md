# GitHub 领域日报 · 2026-11-18

生成时间：2026-11-18 07:39（北京时间）。数据拉取开始于 2026-11-18 07:33:10（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-19（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-11 及之后有推送、总 star > 3。轮换页 `page = (当年第 322 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [alibaba/open-code-review](https://github.com/alibaba/open-code-review) 读 Git 改动，用可配置的语言模型代理写出精确到行的审查意见，并配有不依赖模型的检查流水线；总 star 53704，24 小时新增 star 764。这是今日热度里 24 小时新增最高的领域命中。
2. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 从零训练一个约 64M 参数的小模型；页面写 2 小时，README 把这 2 小时限定为单张 3090 上监督微调 1 个 epoch。总 star 65925，24 小时新增 star 188。这是今日热度里第二条领域命中。
3. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 8964，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 15 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 2 条，都在 AI。

### AI

- [alibaba/open-code-review](https://github.com/alibaba/open-code-review)
  - 说明：做代码审查，把通用编程代理留在审查流程外面。页面描述写明它是确定性流水线加语言模型代理的混合架构，能给出精确到行的意见，并内置空指针、线程安全、XSS 和 SQL 注入规则。README 写明它读 Git diff，代理可以读全文、搜代码库、看其他改动文件；`ocr scan` 也可以在没有有意义 diff 时审整份文件。前身是阿里集团内部审查助手，过去两年服务了数万名开发者，识别了数百万个代码缺陷。基准从 50 个热门仓库里选了 200 个真实 Pull Request、覆盖 10 种语言，由 80 多位资深工程师交叉标注，共 1505 个标注缺陷。同一底层模型下，它相对通用代理的准确率和 F1 更高，token 大约是九分之一，召回率更低。依赖 Git 不低于 2.41。页面描述里的 “LLM Agent” 按强特征词计入 AI。
  - 领域：AI
  - 总 star：53704
  - 24 小时新增 star：764
- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
  - 说明：把大模型训练收成个人 GPU 上能复现的一条链路，用来看清结构而不是只做微调。页面描述写 2 小时从零训练 64M 参数的模型。README 注明「2 小时」是监督微调阶段在单张 NVIDIA 3090 上跑完 1 个 epoch 的实测，「3 块钱」是对应时段的租卡费用；主线最小版本体积大约是 GPT-3 的 1/2700。当前主线 `minimind-3` 是约 64M 的 Dense，`minimind-3-moe` 是约 198M、激活约 64M，结构对齐 Qwen3 / Qwen3-MoE，发布日期写 2026-04-01。训练链路覆盖预训练、监督微调、LoRA、DPO 以及 PPO / GRPO / CISPO。页面描述里的 “LLM” 按强特征词计入 AI。
  - 领域：AI
  - 总 star：65925
  - 24 小时新增 star：188

嵌入式、功率器件、电力电子电源、自动控制在这 15 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 的实验台收成一个网页。README 写明目前是 32 个动手实验，每课先在浏览器里跑，带实时引脚、交互模拟、逐行讲解固件的阅读器，以及一块 3D 板；数据手册部分把芯片手册收成可引用的章节。搜索描述写 11 种语言；README 徽章写 12 languages，列出英语、法语、西班牙语、意大利语、德语、波兰语、土耳其语、简体中文、繁体中文、日语，以及从右到左的阿拉伯语和波斯语。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：892
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。表格里 MG2500 系列的 MG2550S 标成绿，意思是已在真机验证；其余型号标成黄，预期能用但还没上真机。
  - 领域：嵌入式 Embedded
  - 总 star：327
- [Kristian8606/esp32-airplay2-surround](https://github.com/Kristian8606/esp32-airplay2-surround)
  - 说明：用便宜的板子自己组一套无线环绕声。README 写明 Apple TV 只看到网关这一台 AirPlay 2 音箱，网关把 5.1 / 7.1 码流原样分给音箱板，每块 ESP32-S3 只解码自己的声道。目前写明网关加五只音箱（前左右、中置、两侧）已经能同步播放 5.1 和 7.1，iPhone 的立体声也能跟上；闪存建议买 16 MB 的 N16R8，8 MB 板仍能编译，音箱固件副本只剩大约 117 KB。搜索描述为空，话题也为空，只靠仓库名里的 esp32 归入嵌入式。
  - 领域：嵌入式 Embedded
  - 总 star：300
- [andrisgauracs/whistle-esp32](https://github.com/andrisgauracs/whistle-esp32)
  - 说明：把开源语音模型 Whistle 做成一块 ESP32-S3 上的独立实现。按住按键说一句把灯闪成某种颜色，识别在板子上完成，不走网络。README 写明七种语言同时在板子上，模型约 14.5 MB，需要 16 MB 闪存和 8 MB 八线 PSRAM，并用 C99 对照官方引擎逐张量核对过。搜索描述和话题都没有 llm，不跨到 AI。`created_at` 为 `2026-10-19T04:19:26Z`，落在本次创建窗口的边界上。
  - 领域：嵌入式 Embedded
  - 总 star：243
- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑；ESP-IDF 6.0.1 起，外壳可 3D 打印，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：184

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：8964
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给作者自己即将发布的程序加一层防护，让自动做逆向的语言模型代理在受保护的产物上得不到可用结果。README 徽章写 npm 包 `bla-agents` v3.4.4，并写明在 14 个对照目标上验证过，用途限定为作者保护自己的发布物。话题 `llm-security` 按词边界计入 llm。
  - 领域：AI
  - 总 star：6056
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、macOS、iOS 和 Linux 上原生跑，编程代理可以自己建、自己跑、自己看、自己测。README 写界面用一种叫 Contract 的声明式语言，布局和属性名沿用 CSS；网页产物是大约 20 KB 的运行时加上一个 ES 模块，各平台的界面都不走 webview。Android 和 Windows 还在早期，应用能编过并跑起来，缺的部分单独列着。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：4604

### 功率器件 Power Devices

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

本窗口没有以功率器件为最贴近领域的完整新项目。名称撞上 `sic` 的课堂笔记本已剔除。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。返回的 5 条里，1 条是公司后缀 LLC，不是谐振变换器；另外 4 条的名称和描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`。详见数据源状态。

### 自动控制 Control

- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：给第一人称、野外长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参。README 写一套常规的离线光束法平差能缩小和行业系统的差距，但会停在公开提交的水平；把这两项物理现象放进同一条流水线后，LaMAria 训练集的控制点分数从 69.1 到 82.4。它在 LaMAria 测试集上与 Aria 的 SLAM 打平，并在五个类别里的三个上第一次超过 Aria，UZH-FPV 排行榜上排第二。仓库名里的 slam 计入自动控制。
  - 领域：自动控制 Control
  - 总 star：131
- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：给移动机器人一套 ROS 2 激光惯性定位，覆盖里程计、点云建图、先验地图定位、回环和重定位，也可以接 UWB。README 写这是 2026 年东北大学 T-DT 实验室 RoboMaster 超级对抗赛的哨兵定位开源，实机和 rosbag 回放走同一个入口，依赖徽章写 ROS 2 Humble、C++17。话题含 ros2 与 slam。`created_at` 为 `2026-10-22T08:49:49Z`。
  - 领域：自动控制 Control
  - 总 star：128
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用一个水箱、超声测距和一台泵，把通断、P 和 PI 液位控制做成可以对照仿真的实验。README 写实验台是 15 L 罐子，由 500 L 水箱经一台约 0.5 马力、230 V 的泵补水，市电泵走 Fotek SSR-40DA，直流泵则用 MOSFET 做 PWM；MATLAB 应用的物理量来自你自己的水箱、出口和泵，徽章写 MATLAB R2023b 及以上。话题含 control-systems，话题 `pid-control` 按词边界计入 pid。水位控制比 MOSFET 开关更贴近本领域，功率器件一节一行带过。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=3`、`per_page=5`，本页是各查询按总 star 排序后的第 11 到第 15 条。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件仓库，给这台便携设备提供可编译、可刷写的系统。话题含 stm32 与 firmware，也标了红外、NFC、RFID 和 sub-GHz。README 把用户文档和开发文档分开，并写明很多想法可以做成外部应用，不必都进固件。
  - 领域：嵌入式 Embedded
  - 总 star：16917
- [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder)
  - 说明：在一块 ESP32 上收齐 Wi-Fi 和蓝牙工具，用来在现场看无线环境。README 的原话是 offensive and defensive tools。话题含 esp32 与 firmware，也含 esp32-c5、esp32-s2，按词边界计入 esp32。这里只记它是什么，不写具体手法。
  - 领域：嵌入式 Embedded
  - 总 star：13139
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13130。
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用一份 YAML 配置 ESP32、ESP8266、BK72xx 和 RP2040，再从家庭自动化系统远程控制它们。搜索描述就是这件事。README 很短，把文档指到 esphome.io。
  - 领域：嵌入式 Embedded
  - 总 star：12118
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给小智 ESP32 语音硬件配后端，让一块板子接上就能对话和控制。README 写用 Python、Java 和 Vue 按小智通信协议实现，支持 MQTT+UDP、WebSocket、声纹识别和知识库。话题含 esp32。话题里的 mcp-server 不是本报告的 AI 关键词，搜索描述也没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：11324
- [okalachev/flix](https://github.com/okalachev/flix) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：2515。
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：720。
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：557。

### AI

- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：在终端里跑的开源编程代理，现在 README 把它收成企业版 Gemini Code Assist 的入口。重要提示写明：免费个人访问以及 Google AI Pro / Ultra 已在 2026-06-18 转到 Antigravity CLI；本仓库面向 Gemini Code Assist Standard / Enterprise，以及 Google Cloud 上的 Code Assist for GitHub，并写明没有按 Gemini 4 及以后的系列调过。话题含 ai-agents。
  - 领域：AI
  - 总 star：108902
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：用 Python 做带 GPU 加速的张量计算，并用磁带式自动求导搭神经网络。README 就写这两件事，也可以接着用 NumPy、SciPy 和 Cython。名称命中 pytorch。话题里没有 llm。
  - 领域：AI
  - 总 star：105808
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：把大模型推理服务做成高吞吐、省显存的库，让自己部署模型时不必按最坏批次预留显存。README 标题是给所有人的易用、快速、便宜的语言模型服务，并写用 PagedAttention 管理注意力的键值缓存。名称 `vllm` 不等于 llm，靠话题 llm；话题同时有 pytorch 与 transformer。描述里的 LLMs 是复数，词边界本身不等于 llm。
  - 领域：AI
  - 总 star：97114
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：把网页收成给代理和数据管道用的干净 Markdown 或结构化 JSON。README 写云服务每月 1000 额度、不需要信用卡，浏览器和代理由它来管；这个仓库是驱动云服务的 Apache-2.0 爬虫，可以用 Python 或 Docker 自己跑。徽章写最新版 v0.9.5，日期 2026-10-14。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：87482
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2175。

### 功率器件 Power Devices

- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：17。

本页没有以功率器件为最贴近领域的完整条目。`libresidfp` 是 C64 的 SID 芯片仿真，话题里的 mosfet 不是功率器件，已剔除。详见数据源状态。

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：把阳光电源逆变器的 Modbus 数据接进 Home Assistant，用 YAML 就能看发电和电池。搜索描述列出 SH*RT（如 SH10RT）、SHx.RS（如 SH3.RS）、SH*K（如 SH4K6）和 SxT（如 S20T）。README 在 2026-11-07 写明，一个真正的集成正在 `proper-ha-integration` 分支上做，目标是 2026 年 12 月，实体 ID 保持不变，现有 YAML 包会继续维护到新集成对齐功能。话题含 inverter。话题也含 modbus，嵌入式一节一行带过。`pushed_at` 为 `2026-11-17T13:22:18Z`。
  - 领域：电力电子电源 Power Supply
  - 总 star：720
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman)
  - 说明：把 Solarman 采集棒上的逆变器数据接进 Home Assistant。README 写它基于异步的 pysolarmanv5，并支持 Modbus TCP，例子包括 ESP 桥、Waveshare 和以太网记录仪。话题含 inverter，也标了德业、首航、锦浪等品牌。话题含 modbus，嵌入式一节一行带过。`pushed_at` 为 `2026-11-11T09:35:09Z`，落在本次推送窗口的边界上。
  - 领域：电力电子电源 Power Supply
  - 总 star：557
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 主机和一台有线调制解调器做一套 12 V 磷酸铁锂直流不间断电源，停电时先撑住，电量见底前把主机关干净。README 写明威电源经 MOSFET 理想二极管浮充 10 Ah 电池，Victron BatteryProtect 做硬件低压断开，18 V 升压给现在的 N100DC 主机；这台主机从 2026-08-29 起改由本电源供电。监测固件是 ESPHome V1.20。2026-09-15 从起始到低压断开测得 2.5331 Ah / 31.821 Wh，并写明 2026 年 9 月以前包括约 4.18 Ah 在内的续航数字描述的是已经换掉的电池包和负载。话题含 power-supply，所以完整条目放在电力电子；话题里的 mosfet 是理想二极管，功率器件一节一行带过。README 的监测板是 XIAO ESP32-C3，搜索话题没有 esp32，不跨到嵌入式。这条来自功率器件常青检索，不在电力电子本页前 5。
  - 领域：电力电子电源 Power Supply
  - 总 star：17

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：一台自己做的开源扫地机器人，用二维激光雷达在本地建图和导航，常规功能不依赖云。README 仍写明现在还不能按物料单造出来，今天只能在仿真里跑，物料单要等第一版在真机上核对过。话题含 ros2 与 slam，也含 esp32。扫地的定位导航比板子更贴近本领域，嵌入式一节一行带过。这条来自嵌入式常青检索，不在自动控制本页前 5。总 star 高于本页四条。
  - 领域：自动控制 Control
  - 总 star：13130
- [okalachev/flix](https://github.com/okalachev/flix)
  - 说明：用通用零件从零做一台 ESP32 四旋翼。README 写固件大约两千行 Arduino，通信用 MAVLink，Gazebo 里能仿真；1.1 版是 3D 打印的机架，并且真的能飞。话题含 flight-controller 与 esp32。飞控比板子更贴近本领域，嵌入式一节一行带过。物料表里的 MOSFET 不在搜索描述和话题里，不跨到功率器件。
  - 领域：自动控制 Control
  - 总 star：2515
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：移动机器人的 C++ 工具箱，把定位、建图和运动估计放在同一套库里。README 写它从 2005 年在马拉加大学起步，MRPT 3.0 改成按 colcon 分包、公开接口对齐 C++17。话题含 slam 与 computer-vision。定位建图比视觉话题更贴近本领域，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：2175
- [ROBOTIS-GIT/turtlebot3](https://github.com/ROBOTIS-GIT/turtlebot3)
  - 说明：TurtleBot3 这台小型移动机器人的 ROS 软件包，用来在同一套车上做建图和导航。搜索描述写的是 ROS packages。README 主要是相关仓库和官方手册的链接，没有把发行版写成 ROS 2，这里也不写成 ROS 2。话题含 slam。
  - 领域：自动控制 Control
  - 总 star：2107
- [ShisatoYano/AutonomousVehicleControlBeginnersGuide](https://github.com/ShisatoYano/AutonomousVehicleControlBeginnersGuide)
  - 说明：用 Python 仿真和一本开放教材，把定位、建图、规划、跟踪、感知和控制接到同一套自动驾驶系统里，算法可以换着比较。README 的例子包括 EKF、UKF 和粒子滤波的对照，以及 MPPI 路径跟踪、Hybrid A* 和 NDT 建图。话题含 slam 与 kalman-filter，也含 education 和 textbook。这是可运行的仿真加教材，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：1961

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API（定位仓库默认说明文件），下列仓库全部 HTTP 200：`alibaba/open-code-review`、`jingyaogong/minimind`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Kristian8606/esp32-airplay2-surround`、`andrisgauracs/whistle-esp32`、`FlashCat-Jordan/Flashduck`、`wangzan101/Mika`、`qybaihe/bla`、`expo/exact`、`Samarth030312/arduino-water-level-control-lab`、`sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`、`jacobvm04/slam-dunk`、`mozihe/z-localization`、`inmusic-software/mpc-plugin-builder-sdk`、`darkfibr/artex-forensics`、`flipperdevices/flipperzero-firmware`、`justcallmekoko/ESP32Marauder`、`makerspet/oomwoo`、`esphome/esphome`、`xinnan-tech/xiaozhi-esp32-server`、`google-gemini/gemini-cli`、`pytorch/pytorch`、`vllm-project/vllm`、`unclecode/crawl4ai`、`wkcollis1-eng/DIY-LiFePO4-UPS`、`libsidplayfp/libresidfp`、`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`、`davidrapan/ha-solarman`、`okalachev/flix`、`MRPT/mrpt`、`ROBOTIS-GIT/turtlebot3`、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`。`xiaozhi-esp32-server` 的 README 正文里出现把说话人身份传给 LLM 的句子，搜索描述和话题没有 llm。`DIY-LiFePO4-UPS` 的 README 写了 XIAO ESP32-C3，搜索话题没有 esp32。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 15 条，规则命中 2 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 核对：脚本解析出 15 条后，另一次 GET 同一 URL 仍是 HTTP 200，仓库集合和顺序相同，stars today 全部不变。11 个仓库的总 star 有增加：`Claude-BugHunter` 9192→9197，`last30days-skill` 69007→69008，`open-code-review` 53704→53705，`univer` 28881→28882，`arcane` 9303→9305，`stitch-skills` 10082→10083，`superpowers` 319302→319304，`plannotator` 13053→13054，`svelte` 89575→89578，`ECC` 305470→305471，`paper-orchestra` 2936→2938。`LoopForge`（3097，590）、`cursor/plugins`（16886，196）、`ag-ui`（19976，1444）、`minimind`（65925，188）两次一致。正文用第一次解析的数字。今日页面本身只有 15 条，不是解析漏条。
- 命中：`alibaba/open-code-review`（53704，764；描述含 “LLM Agent”）、`jingyaogong/minimind`（65925，188；描述含 “LLM”）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`dream-num/univer`（28881，1776；“AI agents” 是空格写法，不等于 `ai-agents`）、`ag-ui-protocol/ag-ui`（19976，1444；Agent-User Interaction Protocol，不等于 `ai-agents`）、`google-research/paper-orchestra`（2936，1175；多智能体写论文，没有 `llm`）、`elementalsouls/Claude-BugHunter`（9192，1007；Claude Code 技能包，没有 `llm`）、`affaan-m/ECC`（305470，902；代理性能框架，没有 `llm`）、`mvanhorn/last30days-skill`（69007，772；“AI agent skill”，没有 `llm`）、`backnotprop/plannotator`（13053，691；围绕代理的工作区，没有 `llm`）、`getarcaneapp/arcane`（9303，654；Docker 管理）、`obra/superpowers`（319302，598；代理技能框架，没有 `llm`）、`Tencent/LoopForge`（3097，590；coding-agent 工作流，没有 `llm`）、`sveltejs/svelte`（89575，533）、`google-labs-code/stitch-skills`（10082，350；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`cursor/plugins`（16886，196；Cursor 插件规范）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-19 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-19 stars:>2`。HTTP 200。`total_count=453`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`agharsallah/esp-labs-web`（892）、`ngxson/esp32-usb-to-airprint`（327）、`Kristian8606/esp32-airplay2-surround`（300）、`andrisgauracs/whistle-esp32`（243）、`FlashCat-Jordan/Flashduck`（184）。`whistle-esp32` 的 `created_at` 为 `2026-10-19T04:19:26Z`。`Flashduck` 的 `created_at` 为 `2026-10-31T05:10:09Z`。`whistle-esp32` 与 `Flashduck` 的搜索描述和话题都没有 `llm`，不跨到 AI。`esp32-airplay2-surround` 的搜索描述和话题都为空，只靠仓库名 `esp32`。`esp-labs-web` 话题含 `education`，是带模拟器的实验台，不是公开课清单，正文保留。窗口起点从昨日的 2026-10-18 移到 2026-10-19。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-19 stars:>2`。HTTP 200。`total_count=2877`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（8964）、`qybaihe/bla`（6056）、`expo/exact`（4604）。这 3 条是本页星数最高的连续 3 条。`exact` 的 `created_at` 为 `2026-11-02T01:29:01Z`。`Mika` 的 `created_at` 为 `2026-10-29T14:34:07Z`。`bla` 的 npm 徽章现为 v3.4.4。
  - 未命中：`benjitaylor/skills`（总 star 3633；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）、`sarpstar/cinecode`（总 star 2665；描述是 “an AI coding agent writes the script”，不等于 `ai-agents`）。名称和 topics 都没有领域关键词。二者排在 `exact` 之后，是返回的第 4、第 5 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-19 stars:>2`。HTTP 200。`total_count=5`，返回 5，规则保留 2，未命中 3。剩余配额 25。`total_count` 等于返回条数，本次没有第 6 条。规则保留的 2 条里，1 条是课堂笔记本，剔除；1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9），其次是 `SicnuJw`（5），其余 3 条总 star 都是 3。
  - `sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`（总 star 3）：名称含 SIC，搜索描述为空。README 标题写明这是 Samsung Innovation Campus 2026 的 PA-C 与 PA-D 课堂材料，含 Google Colab 笔记本，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-24T17:55:41Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（5；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3；`First-Sick` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-19 stars:>2`。HTTP 200。`total_count=73`，返回 5，规则保留 1，未命中 4。剩余配额 23。规则留下的 1 条是公司后缀，剔除后本日无新项目。按总 star，本页顺序是 `acrobat-dc-desktop`、`isometric-cities`、`artex-forensics`、`mvc2-naomi-dc`、`grid-dca-bot`。
  - 撞名剔除：`darkfibr/artex-forensics`（总 star 77）。描述末尾是 “Blackfish Security LLC”，README 标题同样是 Blackfish Security LLC。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（247；Acrobat DC 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（84；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`gibletto/mvc2-naomi-dc`（50；街机游戏反编译，名称里的 dc 不等于 `dc-dc`）、`leftamber/grid-dca-bot`（49；描述里的 DCA 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-19 stars:>2`。HTTP 200。`total_count=101`，返回 5，规则保留 3，未命中 2。剩余配额 29。正文保留 `jacobvm04/slam-dunk`（131）、`mozihe/z-localization`（128）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。按总 star，本页顺序是 `mpc-plugin-builder-sdk`、`FrankyRenderer`、`slam-dunk`、`z-localization`、`SampQOL-OS`。本次响应头的剩余配额是 29，前一条电力电子新项目是 23，中间没有失败重试，按响应头原样记录。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 175）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 136；描述里的 MPC-BE 与 MPC-HC 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 120；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-11 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-11 stars:>3`。HTTP 200。`total_count=1368`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=3`、`per_page=5`，本页是总结果里按总 star 排序后的第 11 到第 15 条。本查询正文：`flipperdevices/flipperzero-firmware`（16917）、`justcallmekoko/ESP32Marauder`（13139）、`esphome/esphome`（12118）、`xinnan-tech/xiaozhi-esp32-server`（11324）。另有 1 条完整条目不在本页前 5、但写在自动控制：`makerspet/oomwoo`（13130，话题含 ros2 与 slam，也含 esp32）。另有 3 条一行不在本页前 5：`okalachev/flix`（2515，话题含 esp32，完整条目在自动控制）、`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（720，话题含 modbus，完整条目在电力电子）、`davidrapan/ha-solarman`（557，话题含 modbus，完整条目在电力电子）。`xiaozhi-esp32-server` 话题含 mcp-server，不是 AI 关键词。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-11 stars:>3`。HTTP 200。`total_count=9747`，返回 5，规则保留 4，排除清单 0，未命中 1。剩余配额 26。正文保留 `google-gemini/gemini-cli`（108902）、`pytorch/pytorch`（105808）、`vllm-project/vllm`（97114）、`unclecode/crawl4ai`（87482）。另有 1 条一行不在本页前 5：`MRPT/mrpt`（2175，话题含 computer-vision，完整条目在自动控制）。按总 star，本页顺序是 gemini-cli、open-design、pytorch、vllm、crawl4ai。
  - 未命中：`nexu-io/open-design`（总 star 108101；描述是 “with your team and AI agents”，空格写法不等于 `ai-agents`）。它夹在 gemini-cli 与 pytorch 之间。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-11 stars:>3`。HTTP 200。`total_count=31`，返回 5，规则保留 2，排除清单 0，未命中 3。剩余配额 24。`page=3` 是总结果里按总 star 排序后的第 11 到第 15 条。返回的星数是 25、20、18、17、16。规则留下的 2 条里，1 条是 SID 仿真，剔除；1 条是 UPS，更贴近电力电子，本节只留一行。本节没有完整条目。
  - 撞名剔除：`libsidplayfp/libresidfp`（总 star 16）。话题含 mosfet。README 写明这是周期精确的 SID 仿真，覆盖 6581 和 8580，给 Commodore 64 用，不是功率器件，正文不收。
  - 名称词边界未命中：`Zmy0312bry/BUPT_SICE_ARCHIVE`（25；北京邮电大学信息与通信工程学院作业资料，`SICE` 不等于 `sic`）、`SICKAG/sick_safetyscanners_base`（20；SICK 安全激光雷达驱动，`SICK` 不等于 `sic`）、`sicopolis/sicopolis`（18；冰盖演化仿真，`sicopolis` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-11 stars:>3`。HTTP 200。`total_count=419`，返回 5，规则保留 2，未命中 3。剩余配额 22。`page=3` 是总结果里按总 star 排序后的第 11 到第 15 条。正文完整条目为 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（720）、`davidrapan/ha-solarman`（557）。另有 1 条完整条目来自功率器件检索：`wkcollis1-eng/DIY-LiFePO4-UPS`（17，话题含 power-supply 与 mosfet）。按总 star，本页顺序是 `DCGM`、`dcs_liberation`、`Sungrow`、`dcts-shipping`、`ha-solarman`。
  - 名称和 topics 未命中电力电子：`NVIDIA/DCGM`（817；数据中心 GPU 管理，名称里的 DCGM 不等于 `dc-dc`）、`dcs-liberation/dcs_liberation`（802；DCS World 动态战役，不等于 `dc-dc`）、`hackthedev/dcts-shipping`（645；名称里的 dcts 不等于 `dc-dc`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-11 stars:>3`。HTTP 200。`total_count=245`，返回 5，规则保留 4，未命中 0，排除清单 1。剩余配额 28。正文保留 `okalachev/flix`（2515）、`MRPT/mrpt`（2175）、`ROBOTIS-GIT/turtlebot3`（2107）、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`（1961）。`flix` 在嵌入式一行，`mrpt` 在 AI 一行。另有 1 条完整条目来自嵌入式常青检索：`makerspet/oomwoo`（13130）。按总 star，本页顺序是 flix、mrpt、awesome-NeRF-and-3DGS-SLAM、turtlebot3、AutonomousVehicleControlBeginnersGuide。本次响应头的剩余配额是 28。
  - 清单类排除：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2164；名称命中 awesome，话题含 slam，脚本已按合集排除）。
