# GitHub 领域日报 · 2026-11-15

生成时间：2026-11-15 07:39（北京时间）。数据拉取开始于 2026-11-15 07:33:11（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-16（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-08 及之后有推送、总 star > 3。轮换页 `page = (当年第 319 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [alibaba/open-code-review](https://github.com/alibaba/open-code-review) 读 Git 改动，用可配置的语言模型代理写出精确到行的审查意见，并配有不依赖模型的检查流水线；总 star 51404，24 小时新增 star 897。这是今日热度里新增最多的领域命中。
2. [ashhart/TensorFold](https://github.com/ashhart/TensorFold) 用一个 Zig 二进制在 Apple Silicon 和 NVIDIA GPU 上跑语言模型推理，服务时不装 Python 或 MLX；总 star 2154，24 小时新增 star 53。
3. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 8613，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 15 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 2 条，都在 AI。

### AI

- [alibaba/open-code-review](https://github.com/alibaba/open-code-review)
  - 说明：做代码审查，而不是再包一个通用编程代理。页面描述写明它是确定性流水线加语言模型代理的混合架构，能给出精确到行的意见，并内置空指针、线程安全、XSS 和 SQL 注入规则。README 写明它读 Git diff，代理可以读全文、搜代码库、看其他改动文件；`ocr scan` 也可以在没有有意义 diff 时审整份文件。中文 README 写明前身是阿里集团内部审查助手，过去两年服务了数万名开发者；基准从 50 个热门仓库里选了 200 个真实 Pull Request、覆盖 10 种语言，由 80 多位资深工程师交叉标注。同一底层模型下，它相对通用代理的准确率和 F1 更高，token 大约是九分之一，召回率更低。页面描述里的 “LLM Agent” 按强特征词计入 AI。
  - 领域：AI
  - 总 star：51404
  - 24 小时新增 star：897
- [ashhart/TensorFold](https://github.com/ashhart/TensorFold)
  - 说明：在本机提供语言模型推理，不靠 Python 运行时。README 写明一个 Zig 二进制读取检查点、做分词，并在 Apple Silicon 和 NVIDIA GPU 上直接跑 Metal 或 CUDA 内核，不需要安装 Python 或 MLX。页面描述还写了 Vulkan；本次读到的 README 前段没有出现 Vulkan，这一项只来自 Trending 页面。页面描述 “LLM Inference Engine” 按强特征词计入 AI。
  - 领域：AI
  - 总 star：2154
  - 24 小时新增 star：53

嵌入式、功率器件、电力电子电源、自动控制在这 15 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 的实验台收成一个网页。README 写明目前是 32 个动手实验，每课先在浏览器里跑，带实时引脚、交互模拟、逐行讲解固件的阅读器，以及一块 3D 板。搜索描述写 11 种语言；README 徽章写 12 languages，含从右到左。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：858
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：314
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32-S3 上做语音终端。板子负责听和说，电脑上的后端决定这句话交给 Grok，还是在本机放歌、暂停和调音量；刷过补丁固件的小米智能音箱 Pro 也能接进来。README 写明这是社区项目，不是小智、Grok 或 xAI 的官方产品。搜索描述写明版本 2.5.2.9。`created_at` 为 `2026-10-16T15:37:18Z`，正好落在本次 30 天窗口的边界上。话题含 grok，没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：267
- [andrisgauracs/whistle-esp32](https://github.com/andrisgauracs/whistle-esp32)
  - 说明：把开源语音模型 Whistle 做成一块 ESP32-S3 上的独立实现。按住按键说一句把灯闪成某种颜色，识别在板子上完成，不走网络。README 写明七种语言同时在板子上，模型约 14.5 MB，需要 16 MB 闪存和 8 MB 八线 PSRAM，并用 C99 对照官方引擎逐张量核对过。
  - 领域：嵌入式 Embedded
  - 总 star：233
- [Syfyivan/douli-esp32](https://github.com/Syfyivan/douli-esp32)
  - 说明：一只放在身边的实体电子宠物。喊「你好豆梨」，微雪 ESP32-S3 音频板负责唤醒、收音和播放，说到一半可以打断；电脑或支持的 Android 手机跑配套后台，调用使用者自己配置的模型，并把聊天和记忆存在本地。README 写明本仓库不包含自研基础大模型。搜索描述和话题都没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：200
- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming)
  - 说明：给编程代理一套 STM32 技能。README 写明按标准库或 HAL、裸机或 FreeRTOS 四条轨生成工程，带引脚表和烧录说明。检索描述列出 CAN、Modbus、BMS、FOC，以及 85 条实测坑和 29 份领域文档。仓库本身是嵌入式开发技能，所以完整条目放在这里。描述里的 BMS 让它出现在电力电子检索里，FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。这是代码生成技能，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：42

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上。话题含 llm。
  - 领域：AI
  - 总 star：8613
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上投毒、资源耗尽和幻觉。话题 `llm-security` 按词边界计入 llm。README 写明在 14 个对照目标上验证过。
  - 领域：AI
  - 总 star：5684
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、macOS、iOS 和 Linux 上原生跑，编程代理可以自己建、自己跑、自己看、自己测。README 写明 Android 和 Windows 还在早期，应用能编过并跑起来，缺的部分单独列着。话题含 ai-agents。创建日是 2026-11-02。
  - 领域：AI
  - 总 star：4178

### 功率器件 Power Devices

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

本窗口没有以功率器件为最贴近领域的完整新项目。名称撞上 `sic` 的课堂笔记本已剔除。详见数据源状态。

### 电力电子电源 Power Supply

- [invisiblelevel/canifol](https://github.com/invisiblelevel/canifol)
  - 说明：给修板的人算电阻、电容、电感和 BMS，并查数据手册和引脚。README 的 1.6.0 更新写了草图板，可以在电路板照片上描线，并带 BoardView。描述里的 BMS 计入电力电子。有 Windows、Android 和 Linux 构建。
  - 领域：电力电子电源 Power Supply
  - 总 star：26
- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS，此处不展开。领域：电力电子电源 Power Supply。总 star：42。

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

`page = 4`，每页 5 条，本页是各查询按总 star 排序后的第 16 到第 20 条。

### 嵌入式 Embedded

- [platformio/platformio-core](https://github.com/platformio/platformio-core)
  - 说明：PlatformIO Core。README 写明它用声明式、可测试的现代工具链来做嵌入式软件。话题含 build-system、libraries、debugging、embedded、esp32、firmware、risc-v、rtos，以及 zephyr-rtos。
  - 领域：嵌入式 Embedded
  - 总 star：9603
- [crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)
  - 说明：给墨水屏做开源电子书固件。README 写明现在跑在 ESP32-C3 的 Xteink X4、X3，以及 ESP32-S3 的 Xteink X4Pro、X4Classic、Seeed reTerminal Sticky、M5PaperMono、Metalio E-Ink 4、EEGOREAD A4 和 Boox Picco 上，能读 EPUB、xtc、txt 和 bmp。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：8781
- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的设备固件，用 LoRa 组一张不靠蜂窝和互联网的网，传文字、位置和遥测。README 写明支持 ESP32、nRF52、RP2040/RP2350 和 Linux。话题另含 stm32，仓库名含 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：8578
- [FastLED/FastLED](https://github.com/FastLED/FastLED)
  - 说明：驱动可寻址彩灯。README 写明高端设备可以带动 3 万颗以上，小芯片上也能跑，并写明支持 Arduino、ESP32、Teensy、树莓派，以及另外 50 多个平台。话题含 embedded 与 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：7534
- [bblanchon/ArduinoJson](https://github.com/bblanchon/ArduinoJson)
  - 说明：在 Arduino 和嵌入式 C++ 里解析、生成 JSON，也处理 MessagePack。话题含 embedded 与 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：7245
- [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library) — 见下方「自动控制 Control」完整条目。话题含 embedded 与 mcu，此处不展开。领域：嵌入式 Embedded。总 star：1164。
- [rtlopez/esp-fc](https://github.com/rtlopez/esp-fc) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：894。
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：553。

### AI

- [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
  - 说明：一本书的官方代码，用 PyTorch 从零搭一个 GPT 式模型，含预训练和微调。话题含 llm 与 pytorch。它是这一本书的代码，不是多门课的清单，正文保留。
  - 领域：AI
  - 总 star：108414
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：提供带 GPU 加速的张量计算，以及基于磁带式自动微分的动态神经网络。名称命中 pytorch。
  - 领域：AI
  - 总 star：105496
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：做高吞吐的语言模型推理和服务。README 写明用 PagedAttention 管理注意力的键值缓存，并连续批处理请求。话题含 llm、pytorch 和 transformer。名称 `vllm` 按词边界不等于 `llm`。
  - 领域：AI
  - 总 star：96938
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：给代理抓网页。README 写明云端接口把页面收成 Markdown 或结构化 JSON，每月 1000 个免费额度、不要信用卡；本仓库是支撑它的 Apache-2.0 爬虫，可以用 Python 或 Docker 自己托管。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：87359
- [MOLAorg/mola](https://github.com/MOLAorg/mola) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：1059。

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。名称撞上 `sic` 的图片转换器已剔除，其余返回项的词边界不等于 `sic`。详见数据源状态。

### 电力电子电源 Power Supply

- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman)
  - 说明：把 Solarman 采集棒接进 Home Assistant，用来看这些品牌的逆变器。README 写明基于异步 pysolarmanv5，并支持 Modbus TCP，包括 ESP 桥、Waveshare 和以太网采集棒。话题含 inverter，也含 modbus。逆变器集成比总线话题更贴近本领域，嵌入式一节一行带过。
  - 领域：电力电子电源 Power Supply
  - 总 star：553
- [fl4p/batmon-ha](https://github.com/fl4p/batmon-ha)
  - 说明：用电脑自己的蓝牙读电池管理系统，把电量、电流、功率和单体电压经 MQTT 送进 Home Assistant。README 写明不需要再加 USB、串口、RS485 或 ESP32，也可以不装 Home Assistant，在 Linux、macOS 和 Windows 上单独跑。话题含 bms。搜索话题没有 esp32，不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：534
- [AndyShaman/BYDMate](https://github.com/AndyShaman/BYDMate)
  - 说明：比亚迪 DiLink 车机上的行程和能耗记录。README 写明原车电脑会把能耗报低 10% 到 30%，这个应用直接读 BMS 的 energydata 来显示实际消耗，并记下停车消耗和电芯平衡；行程、充电、自动化和本地洞察在车机上运行，不依赖上网。README 把 4.1.0 标成当前要点，支持 DiLink 3.0、4.0、5.0、5.1 和 UI7。描述里的 “voice AI agent” 不是 `ai-agents`，话题里的 `ai` 也不是本报告的 AI 关键词，不跨到 AI。
  - 领域：电力电子电源 Power Supply
  - 总 star：512

### 自动控制 Control

- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用 MuJoCo 模拟肌肉骨骼模型，让学习算法去完成这些动作任务。README 写明 MyoSuite 3 可以在一块 GPU 上并行大量环境，同一任务也能走 CPU 上的 Gymnasium。话题含 motor-control。这是仿真任务集，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：1287
- [Sguan-ZhouQing/SguanFOC_Library](https://github.com/Sguan-ZhouQing/SguanFOC_Library)
  - 说明：在 MCU 上跑永磁同步电机的磁场定向控制。README 写明纯 C，覆盖有感、无感和霍尔，从坐标变换到 SVPWM，位置环、速度环和电流环可以单环或串级。话题含 foc 与 motor-control，也含 embedded 与 mcu。电机控制比「跑在 MCU 上」更贴近本领域，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：1164
- [MOLAorg/mola](https://github.com/MOLAorg/mola)
  - 说明：把定位和建图拆成可替换的模块。README 写明这是 C++ 和 ROS 2 框架，能配激光里程计和激光惯性里程计。话题含 slam，也含 computer-vision。定位建图比视觉话题更贴近本领域，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：1059
- [rsasaki0109/lidar_slam_ros2](https://github.com/rsasaki0109/lidar_slam_ros2)
  - 说明：把 rosbag 收成能拿去导航的点云地图。README 写明默认流程用 RKO-LIO 和 graph_based_slam，输出 Autoware 兼容的点云地图、投影信息和 lanelet2，当前说明指向 v0.11.0。README 举例给出户外步行 APE 0.55 米、楼梯开发数据 ATE 0.24 米、地铁隧道 0.38 米。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：941
- [rtlopez/esp-fc](https://github.com/rtlopez/esp-fc)
  - 说明：用便宜的板子自己做飞控。README 写明支持 ESP32 和 ESP32-S3，能用 Betaflight 10.10 配置器，SPI 陀螺仪时环路最高 4 kHz，并有 DShot 和 CRSF。话题含 flight-controller、pid、esp32 和 rp2350；功能列表里写的是 ESP32 与 ESP32-S3，rp2350 只出现在话题。飞控比板子更贴近本领域，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：894

## 数据源状态

11 次逻辑请求全部第一次成功，没有重试。实际 HTTP 11 次。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面；这个数字随每分钟窗口回升，控制新项目之后剩 21，控制常青回到 29，不是失败。成功的搜索里 `incomplete_results` 均为 false。本次通过环境变量 `GH_TOKEN` 使用本机 `gh` 登录令牌，令牌没有写入脚本、报告或提交。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取按 `README.md`、`readme.md`、`ReadMe.md`、`README.rst` 的顺序，命中即停。`davidrapan/ha-solarman` 的 `README.md` 为 HTTP 404，命中 `readme.md`。`platformio/platformio-core` 的 `README.md`、`readme.md`、`ReadMe.md` 为 HTTP 404，命中 `README.rst`。其余仓库的 `README.md` 为 HTTP 200：`alibaba/open-code-review`、`ashhart/TensorFold`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Liu-zhongxian/zongzhu-bot`、`andrisgauracs/whistle-esp32`、`Syfyivan/douli-esp32`、`wdcjx/Embedded-programming`、`wangzan101/Mika`、`qybaihe/bla`、`expo/exact`、`Samarth030312/arduino-water-level-control-lab`、`profesor003-fundesteam/SIC-2026`、`Oire/sic`、`invisiblelevel/canifol`、`fl4p/batmon-ha`、`AndyShaman/BYDMate`、`inmusic-software/mpc-plugin-builder-sdk`、`mozihe/z-localization`、`woolimi/robotics-roadmap`、`MyoHub/myosuite`、`Sguan-ZhouQing/SguanFOC_Library`、`MOLAorg/mola`、`rsasaki0109/lidar_slam_ros2`、`rtlopez/esp-fc`、`crosspoint-reader/crosspoint-reader`、`meshtastic/firmware`、`FastLED/FastLED`、`bblanchon/ArduinoJson`、`rasbt/LLMs-from-scratch`、`pytorch/pytorch`、`vllm-project/vllm`、`unclecode/crawl4ai`。另读 `alibaba/open-code-review` 的 `docs/i18n/README.zh-CN.md`，HTTP 200。上述 README 读取（含命中前的 404）和下面 2 次 Trending 核对，不计入上面 11 次配额。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 15 条，规则命中 2 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 核对：脚本解析出 15 条后，另两次 GET 同一 URL 仍是 HTTP 200。第一次只核对 article 数量和 “stars today” 出现次数，都是 15，stars today 与第一次一致。第二次用脚本解析器比较，仓库集合相同，stars today 不变；8 个未命中仓库的总 star 多了 1 到 4：`plannotator` 11094→11097，`modern-web-guidance-src` 5988→5991，`claude-trading-skills` 4777→4780，`qwen-code` 30316→30317，`univer` 24462→24464，`caveman` 120048→120050，`LoopForge` 884→886，`Veyra-NRVideo` 2212→2216。两条命中的总 star 和 stars today 都没变。正文用第一次解析的数字。今日页面本身只有 15 条，不是解析漏条。
- 命中：`alibaba/open-code-review`（51404，897；描述含 “LLM Agent”）、`ashhart/TensorFold`（2154，53；描述是 “LLM Inference Engine”）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`GoogleChrome/modern-web-guidance-src`（5988，1225；描述是 “coding agent”，不等于 `ai-agents`）、`ChromeDevTools/chrome-devtools-mcp`（56272，673；名称里的裸 mcp 不是本报告的 AI 关键词）、`we-promise/sure`（15277，659；个人理财）、`tradermonty/claude-trading-skills`（4777，556；描述点名 Claude Code，没有 `llm`）、`dream-num/univer`（24462，495；“AI agents” 是空格写法，不等于 `ai-agents`）、`louislam/uptime-kuma`（94219，432）、`Likely7/Veyra-NRVideo`（2212，423；视频播放与采集增强）、`backnotprop/plannotator`（11094，412）、`martin-olivier/airgorah`（5832，269；Wi-Fi 安全审计）、`JuliusBrussee/caveman`（120048，227；给编程代理省 token，没有 `llm`）、`QwenLM/qwen-code`（30316，116；“AI coding agent” 不等于 `ai-agents`）、`Tencent/LoopForge`（884，101；coding-agent 工作流）、`ag-ui-protocol/ag-ui`（17346，9；Agent-User Interaction Protocol，不等于 `ai-agents`）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-16 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-16 stars:>2`。HTTP 200。`total_count=466`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`agharsallah/esp-labs-web`（858）、`ngxson/esp32-usb-to-airprint`（314）、`Liu-zhongxian/zongzhu-bot`（267）、`andrisgauracs/whistle-esp32`（233）、`Syfyivan/douli-esp32`（200）。`zongzhu-bot` 的 `created_at` 为 `2026-10-16T15:37:18Z`，话题含 `grok`，没有 `llm`，不跨到 AI。`whistle-esp32` 与 `douli-esp32` 的搜索描述和话题都没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，是带模拟器的实验台，不是公开课清单，正文保留。另有 1 条完整条目来自电力电子检索：`wdcjx/Embedded-programming`（42），因为 STM32 技能比描述里的 BMS 更贴近本领域。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-16 stars:>2`。HTTP 200。`total_count=3135`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（8613）、`qybaihe/bla`（5684）、`expo/exact`（4178）。这 3 条是本页星数最高的连续 3 条。`exact` 的 `created_at` 为 `2026-11-02T01:29:01Z`。
  - 未命中：`benjitaylor/skills`（总 star 3316；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）、`sarpstar/cinecode`（总 star 2500；描述是 “an AI coding agent writes the script”，不等于 `ai-agents`）。名称和 topics 都没有领域关键词。二者排在 `exact` 之后，是返回的第 4、第 5 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-16 stars:>2`。HTTP 200。`total_count=6`，返回 5，规则保留 2，未命中 3。剩余配额 25。`per_page=5`，第 6 条不在本次返回里，正文不猜测它是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9），其次是 `SicnuJw`（4），其余 3 条总 star 都是 3。
  - `profesor003-fundesteam/SIC-2026`（总 star 3）：名称和描述含 SIC。README 标题写明这是 Samsung Innovation Campus 2026 的数据分析、数据科学与人工智能课堂材料，含笔记本和数据集，讲师是 Danny Jose Delgado De Sousa，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-18T15:03:12Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（4；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3；`First-Sick` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-16 stars:>2`。HTTP 200。`total_count=70`，返回 5，规则保留 2，未命中 3。剩余配额 23。正文保留 `invisiblelevel/canifol`（26）。`wdcjx/Embedded-programming`（42）更贴近嵌入式，本节一行带过。按总 star，本页顺序是 `isometric-cities`、`grid-dca-bot`、`DCore`、`Embedded-programming`、`canifol`。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`Statecraft-Labs/isometric-cities`（80；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`leftamber/grid-dca-bot`（49；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-16 stars:>2`。HTTP 200。`total_count=87`，返回 5，规则保留 3，未命中 2。剩余配额 21。正文保留 `mozihe/z-localization`（126）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`mpc-plugin-builder-sdk`、`FrankyRenderer`、`SampQOL-OS` 与 `robotics-roadmap` 夹在返回结果里，剔除 Akai MPC 和课程清单后，本查询自己留下的命中只有 `z-localization`。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 140）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 101）。话题含 `ros2` 与 `slam`。README 徽章写 57 讲、120 小时，正文是 57 讲自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 127；描述里的 MPC-BE 与 MPC-HC 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 108；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-08 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-08 stars:>3`。HTTP 200。`total_count=1329`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=4`、`per_page=5`，本页是总结果里按总 star 排序后的第 16 到第 20 条。本查询正文：`platformio/platformio-core`（9603）、`crosspoint-reader/crosspoint-reader`（8781）、`meshtastic/firmware`（8578）、`FastLED/FastLED`（7534）、`bblanchon/ArduinoJson`（7245）。另有 3 条一行不在本页前 5：`Sguan-ZhouQing/SguanFOC_Library`（1164，话题含 embedded 与 mcu，完整条目在自动控制）、`rtlopez/esp-fc`（894，话题含 esp32，完整条目在自动控制）、`davidrapan/ha-solarman`（553，话题含 modbus，完整条目在电力电子）。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-08 stars:>3`。HTTP 200。`total_count=9971`，返回 5，规则保留 4，排除清单 0，未命中 1。剩余配额 26。正文保留 `rasbt/LLMs-from-scratch`（108414）、`pytorch/pytorch`（105496）、`vllm-project/vllm`（96938）、`unclecode/crawl4ai`（87359）。按总 star，本页顺序是 LLMs-from-scratch、open-design、pytorch、vllm、crawl4ai。另有 1 条一行不在本页：`MOLAorg/mola`（1059，话题含 computer-vision，完整条目在自动控制）。
  - 未命中：`nexu-io/open-design`（总 star 107651；描述是 “AI agents”，空格写法不等于 `ai-agents`）。它夹在 LLMs-from-scratch 与 pytorch 之间。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-08 stars:>3`。HTTP 200。`total_count=28`，返回 5，规则保留 1，排除清单 0，未命中 4。剩余配额 24。`page=4` 是总结果里按总 star 排序后的第 16 到第 20 条。规则保留的 1 条撞名剔除后，本节没有完整条目。返回的星数是 6、6、5、5、5。
  - `Oire/sic`（总 star 5）：名称和描述含 SIC。README 写明这是 Windows 上的图片格式转换器，正文不收。
  - 名称词边界未命中：`rvandewater/SICdb_MEDS`（6；萨尔茨堡重症监护数据库，`SICdb` 不等于 `sic`）、`Sizerta/SiCell.jl`（6；单细胞 RNA 工具，`SiCell` 不等于 `sic`）、`postboy/sicp-homework`（5；wizard book 习题解答，`sicp` 不等于 `sic`）、`anzeabram/SiCS`（5；斯洛文尼亚洞穴测量，`SiCS` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-08 stars:>3`。HTTP 200。`total_count=391`，返回 5，规则保留 3，未命中 2。剩余配额 22。`page=4` 是总结果里按总 star 排序后的第 16 到第 20 条。本查询正文：`davidrapan/ha-solarman`（553）、`fl4p/batmon-ha`（534）、`AndyShaman/BYDMate`（512）。按总 star，本页顺序是 `ha-solarman`、`batmon-ha`、`consul-replicate`、`BYDMate`、`dcm4chee-arc-light`。
  - 名称和 topics 未命中：`hashicorp/consul-replicate`（525；Consul 跨数据中心的 KV 复制，描述里的 DC 不等于 `dc-dc`）、`dcm4che/dcm4chee-arc-light`（508；DICOM 归档，名称里的 dcm 不等于 `dc-dc`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-08 stars:>3`。HTTP 200。`total_count=230`，返回 5，规则保留 5，未命中 0，排除清单 0。剩余配额 29。正文保留 `MyoHub/myosuite`（1287）、`Sguan-ZhouQing/SguanFOC_Library`（1164）、`MOLAorg/mola`（1059）、`rsasaki0109/lidar_slam_ros2`（941）、`rtlopez/esp-fc`（894）。`SguanFOC_Library` 与 `esp-fc` 在嵌入式各一行，`mola` 在 AI 一行。按总 star，本页顺序就是这 5 条。
