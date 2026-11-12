# GitHub 领域日报 · 2026-11-13

生成时间：2026-11-13 07:39（北京时间）。数据拉取开始于 2026-11-13 07:34:33（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-14（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-06 及之后有推送、总 star > 3。轮换页 `page = (当年第 317 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) 用 C/C++ 在本机做大模型推理，不必先搭一套 Python 推理栈；总 star 134528，24 小时新增 star 287。这是今日热度里新增最多的领域命中。
2. [ashhart/TensorFold](https://github.com/ashhart/TensorFold) 用一个 Zig 程序在 Apple Silicon 和 NVIDIA GPU 上提供语言模型服务，读检查点并直接跑内核，不用先装 Python 或 MLX；总 star 1926，24 小时新增 star 94。
3. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 8397，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 13 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 2 条，都在 AI。

### AI

- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
  - 说明：在本机用 C/C++ 跑大模型推理。README 的安装之后就是从 Hugging Face 拉一个模型直接运行。页面描述是 “LLM inference in C/C++”，按强特征词计入 AI。
  - 领域：AI
  - 总 star：134528
  - 24 小时新增 star：287
- [ashhart/TensorFold](https://github.com/ashhart/TensorFold)
  - 说明：给本机提供一个不依赖 Python 或 MLX 的语言模型服务。README 写明它是一个 Zig 二进制，面向 Apple Silicon 和 NVIDIA GPU，读检查点、做分词，并直接跑 Metal 或 CUDA 内核。页面描述还写了 Vulkan。描述以 LLM 开头，按强特征词计入 AI。
  - 领域：AI
  - 总 star：1926
  - 24 小时新增 star：94

嵌入式、功率器件、电力电子电源、自动控制在这 13 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 的实验台收成一个网页。能看实时引脚、在浏览器里跑交互模拟、逐行读固件，并记实验日志。README 写明目前是 32 个动手实验，还有一块可点亮零件的 3D 板。搜索描述写 11 种语言；README 徽章写 12 languages，正文列出英语、法语、西班牙语、意大利语、德语、波兰语、土耳其语、简体中文、繁体中文、日语、阿拉伯语和波斯语，后两种整页从右到左。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：841
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：296
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32-S3 上做语音终端。板子负责听和说，电脑上的后端决定这句话交给 Grok，还是在本机放歌、暂停和调音量；刷过补丁固件的小米智能音箱 Pro 也能接进来。README 写明这是社区项目，不是小智、Grok 或 xAI 的官方产品。话题含 grok，没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：263
- [andrisgauracs/whistle-esp32](https://github.com/andrisgauracs/whistle-esp32)
  - 说明：把开源语音模型 Whistle 做成一块 ESP32-S3 上的独立实现。按住按键说一句把灯闪成某种颜色，识别在板子上完成，不走网络。README 写明七种语言同时在板子上，模型约 14.5 MB，需要 16 MB 闪存和 8 MB 八线 PSRAM，并用 C99 对照官方引擎逐张量核对过。
  - 领域：嵌入式 Embedded
  - 总 star：227
- [Syfyivan/douli-esp32](https://github.com/Syfyivan/douli-esp32)
  - 说明：一只放在身边的实体电子宠物。喊「你好豆梨」，微雪 ESP32-S3 音频板负责唤醒、收音和播放，说到一半可以打断；电脑或支持的 Android 手机跑配套后台，调用使用者自己配置的模型，并把聊天和记忆存在本地。README 写明本仓库不包含自研基础大模型。搜索描述和话题都没有 llm，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：200
- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming)
  - 说明：给编程代理一套 STM32 技能。README 写明按标准库或 HAL、裸机或 FreeRTOS 四条轨生成工程，带引脚表和烧录说明。检索描述列出 CAN、Modbus、BMS、FOC，以及 85 条实测坑和 29 份领域文档。仓库本身是嵌入式开发技能，所以完整条目放在这里。描述里的 BMS 让它出现在电力电子检索里，FOC 也命中控制，但同一仓库只进两个领域节，控制不单列。这是代码生成技能，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：41

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 写明没有 Mika 自己的服务器，模型用自己的 API 密钥，或登录 ChatGPT、xAI、OpenRouter；安装包要求 Android 11 及以上。话题含 llm。
  - 领域：AI
  - 总 star：8397
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上投毒、资源耗尽和幻觉，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。README 写明只给软件作者保护自己的发布物，并在 14 个对照目标上验证过。
  - 领域：AI
  - 总 star：5455
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵。代理已经能写出影片、演示和游戏的声音，却听不出按键廉价、撞击晚了 80 毫秒或配乐鼓错了地方。README 写明它把声音变成代理可以判断的证据，并且只在 CPU 上跑，也能让代理自己写声音再听一遍改。话题含 ai-agents。
  - 领域：AI
  - 总 star：4658
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，就在网页、macOS、iOS 和 Linux 上以原生方式运行。编程代理不只要能生成代码，还要能把应用建出来、跑起来、看见界面并在这些平台上测完。话题含 ai-agents。接口 `created_at` 为 `2026-11-02T01:29:01Z`，北京时间是 2026-11-02 09:29。
  - 领域：AI
  - 总 star：3352

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 做直流泵 PWM 的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

### 电力电子电源 Power Supply

- [wdcjx/Embedded-programming](https://github.com/wdcjx/Embedded-programming) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS，此处不展开。领域：电力电子电源 Power Supply。总 star：41。
- [invisiblelevel/canifol](https://github.com/invisiblelevel/canifol)
  - 说明：给修电路的人一套工具。计算器覆盖电阻、电容、电感，其中 BMS 一节算均衡电阻、串并联电池组、电流分流器和 MOSFET 保护，旁边还有数据手册、引脚图、SMD 代码和 BoardView。README 写明 1.5.1 版带 6000 多个笔记本、显卡和游戏机图纸，超过 10 GB，SMD 代码库有 270974 条，安装包覆盖 Windows、Android 和 Linux。搜索描述里的 BMS 是强特征词，所以归入本领域。
  - 领域：电力电子电源 Power Supply
  - 总 star：26

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室 2026 年 RoboMaster 哨兵的定位栈。README 写明它跑在 Ubuntu 22.04 和 ROS 2 Humble 上，用激光和惯性做里程计、点云建图、先验地图定位、回环和重定位，也可以接入 UWB；实机和 rosbag 回放走同一套入口。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：125
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵用 MOSFET 做 PWM；固件里有通断、P 和 PI，并带溢流、干转和传感器保护。README 写明实验台是 15 升罐，水来自 500 升水箱，用 0.5 马力级 230 伏泵和 Fotek SSR-40DA，并有按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 2`，每页 5 条，本页是各查询按总 star 排序后的第 6 到第 10 条。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：用 ESP32 经 Wi-Fi 控制可寻址灯带。README 写明从普通灯带到二维矩阵和 HUB75 屏。话题含 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：19034
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：把 Go 编译到单片机、WebAssembly 和命令行小工具上，后端用 LLVM。话题含 esp32 与 stm32。
  - 领域：嵌入式 Embedded
  - 总 star：17908
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：让 Arduino 的写法能用在 ESP32 系列芯片上的核心库。话题含 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：17719
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：给熔融沉积 3D 打印机用的固件，8 位和 32 位都能跑，很多商品机出厂就带它。话题含 esp32 与 firmware。README 写 AVR 和 STM32 是最常见的硬件层，ESP32 也有一层；搜索话题是 `esp32` 和 `stmicro`，没有单独的 `stm32`，不因此再开一节。
  - 领域：嵌入式 Embedded
  - 总 star：17659
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：面向多种硬件架构的实时操作系统，按资源受限设备来做，并把安全放进设计。话题含 embedded、rtos 与 zephyr。
  - 领域：嵌入式 Embedded
  - 总 star：17071
- [okalachev/flix](https://github.com/okalachev/flix) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：2496。

### AI

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图在本机跑扩散模型，同时提供界面、API 和后端。话题 `stable-diffusion` 按词边界计入 diffusion，话题也含 pytorch。
  - 领域：AI
  - 总 star：146520
- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：一套可以按自己的流程改的编程代理外壳，自带统一的多供应商 LLM 接口、代理循环、终端界面和命令行。搜索描述里的 LLM 是强特征词。话题为空。
  - 领域：AI
  - 总 star：121665
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：让模型在真实浏览器里办事。README 写明代理用 Python 对 Chrome DevTools Protocol 写操作，可以跑在本机，也有托管的浏览器和代理接口。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：120849
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
  - 说明：让编程代理换一次会话还记得上次做过什么。旁边有一个记笔记的代理，下次只把用得上的上下文送回去。README 写明记忆放在本机的 `~/.claude-mem`，云同步要自己打开。话题含 ai-agents。
  - 领域：AI
  - 总 star：116557
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2175。

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。名称命中 `sic` 的 `epilys/sic` 是标签链接聚合，与碳化硅器件无关。磷酸铁锂 UPS 的完整说明写在下方「电力电子电源」，这里只因话题含 mosfet 留一行。

- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：17。

### 电力电子电源 Power Supply

- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：在 Home Assistant 里读写极空电池管理系统。用 UART-TTL 或蓝牙连接，软件版本不低于 6.0 的机型走这套协议。话题 `jikong-bms` 按词边界计入 bms。README 写了 ESP32 和 ESP8266 的接线，搜索话题没有 esp32，不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：1053
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 主机和网络设备做的 12 伏磷酸铁锂直流不间断电源。断电后继续供电，电池见底前把主机关掉，来电后再自己恢复。搜索描述写明 2026-05-06 那次整段断电验证为交流断开 217 分钟，放出 4.18 Ah / 53.3 Wh，并靠斜率判断悬崖来临后正常关机。README 写明现在的主机是 ASRock N100DC-ITX，从 2026-08-29 起由这套电源供电，原来的 Home Assistant Green 已停用；徽章写最近一次放到低压断开是 2026-09-15、1 小时 30 分。话题含 power-supply 与 mosfet。它是一台电源，所以完整条目放在这里，功率器件一节一行带过。README 写监控板用的是 XIAO ESP32-C3，搜索话题没有 esp32，不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：17

### 自动控制 Control

- [RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)
  - 说明：用图来优化非线性误差，现成解覆盖多种 SLAM 和光束法平差。新问题通常只要补几行就能接上。话题含 slam。
  - 领域：自动控制 Control
  - 总 star：3479
- [okalachev/flix](https://github.com/okalachev/flix)
  - 说明：用通用零件从零做一架基于 ESP32 的四旋翼，固件大约两千行，能飞。README 写明用 MAVLink 走 Wi-Fi 或 ESP-NOW，可以用手柄、遥控或手机控制，并用 Gazebo 做仿真。飞控比板上的 ESP32 更贴近本领域，嵌入式一节一行带过。物料里有驱动电机的 MOSFET，搜索描述和话题没有 mosfet，不跨到功率器件。
  - 领域：自动控制 Control
  - 总 star：2496
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：移动机器人的 C++ 工具箱，从 2005 年做到现在，里面有定位、建图和 SLAM。话题含 slam 与 computer-vision。机器人算法比视觉话题更贴近本领域，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：2175

## 数据源状态

11 次逻辑请求全部最终成功。功率器件常青第一次遇到限流，脚本不保存第一次状态码，等 30 秒重试后 HTTP 200。其余 10 次第一次即 HTTP 200。实际 HTTP 12 次，逻辑请求 11 次。相邻逻辑请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面；这个数字随每分钟窗口回升，中间出现过从 5 回到 9，不是失败。成功的搜索里 `incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取里，下列仓库的 `HEAD/README.md` 为 HTTP 200：`ggml-org/llama.cpp`、`ashhart/TensorFold`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Liu-zhongxian/zongzhu-bot`、`andrisgauracs/whistle-esp32`、`Syfyivan/douli-esp32`、`wdcjx/Embedded-programming`、`invisiblelevel/canifol`、`Samarth030312/arduino-water-level-control-lab`、`profesor003-fundesteam/SIC-2026`、`epilys/sic`、`wkcollis1-eng/DIY-LiFePO4-UPS`、`syssi/esphome-jk-bms`、`mozihe/z-localization`、`woolimi/robotics-roadmap`、`wangzan101/Mika`、`qybaihe/bla`、`Leonxlnx/earshot`、`expo/exact`、`tinygo-org/tinygo`、`espressif/arduino-esp32`、`MarlinFirmware/Marlin`、`Comfy-Org/ComfyUI`、`earendil-works/pi`、`browser-use/browser-use`、`thedotmack/claude-mem`、`RainerKuemmerle/g2o`、`okalachev/flix`、`MRPT/mrpt`。`wled/WLED` 的 `HEAD/README.md` 为 404，文件名是 `readme.md`，该地址 HTTP 200。`zephyrproject-rtos/zephyr` 的 `HEAD/README.md`、`readme.md`、`ReadMe.md` 为 404，文件名是 `README.rst`，该地址 HTTP 200。`espressif/arduino-esp32`、`tinygo-org/tinygo` 的说明没有超出搜索描述，README 只用来核对。这 32 个仓库的 README 请求和下面 1 次 Trending 核对，不计入上面 11 次配额。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 13 条，规则命中 2 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 核对：脚本解析出 13 条后，另一次 GET 同一 URL 仍是 HTTP 200，页面上有 13 个 `article.Box-row`、13 处 “stars today”，仓库名与第一次相同。这次核对不计入 11 次配额。stars today 与第一次一致；部分总 star 多了 1 或 2。正文用第一次解析的数字。今日页面本身只有 13 条，不是解析漏条。
- 命中：`ggml-org/llama.cpp`（134528，287；描述是 “LLM inference in C/C++”）、`ashhart/TensorFold`（1926，94；描述以 LLM 开头）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`meta/astryx`（26471，1789；描述是 agent ready，不等于 `ai-agents`）、`we-promise/sure`（13874，974；个人理财）、`addyosmani/agent-skills`（116646，812；描述是 “skills for AI coding agents”，空格写法不等于 `ai-agents`）、`GoogleChrome/modern-web-guidance-src`（2844，799；描述是 “coding agent”，不等于 `ai-agents`）、`openai/codex-security`（12382，663）、`Alishahryar1/free-claude-code`（69256，461；描述点名 Claude Code 等套件，没有 `llm`）、`pookjw/HermesEnabler`（1516，300）、`CopilotKit/OpenBot`（11569，291；描述是 “AI coworkers” 和 “AG-UI agent”，不等于 `ai-agents`）、`QwenLM/qwen-code`（29781，151；描述是 “AI coding agent”，空格写法不等于 `ai-agents`）、`nodejs/node`（123588，133）、`nvm-sh/nvm`（96000，107）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-14 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-14 stars:>2`。HTTP 200。`total_count=464`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 9。这 5 条都写入正文：`agharsallah/esp-labs-web`（841）、`ngxson/esp32-usb-to-airprint`（296）、`Liu-zhongxian/zongzhu-bot`（263）、`andrisgauracs/whistle-esp32`（227）、`Syfyivan/douli-esp32`（200）。`zongzhu-bot` 话题含 `grok`，没有 `llm`，不跨到 AI。`whistle-esp32` 与 `douli-esp32` 的搜索描述和话题都没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，是带模拟器的实验台，不是公开课清单，正文保留。另有 1 条完整条目来自电力电子检索：`wdcjx/Embedded-programming`（41），因为 STM32 技能比描述里的 BMS 更贴近本领域。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-14 stars:>2`。HTTP 200。`total_count=2487`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 8。正文保留 `wangzan101/Mika`（8397）、`qybaihe/bla`（5455）、`Leonxlnx/earshot`（4658）、`expo/exact`（3352）。这 4 条是本页星数最高的连续 4 条。
  - 未命中：`benjitaylor/skills`（总 star 3196；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。它排在 `exact` 之后，是返回的第 5 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-14 stars:>2`。HTTP 200。`total_count=7`，返回 5，规则保留 2，未命中 3。剩余配额 5。`per_page=5`，第 6、第 7 条不在本次返回里，正文不猜测它们是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9），其次是 `SicnuJw`（4），其余 3 条总 star 都是 3。
  - `profesor003-fundesteam/SIC-2026`（总 star 3）：名称和描述含 SIC。README 标题写明这是 Samsung Innovation Campus 2026 的数据分析、数据科学与人工智能课堂材料，含笔记本和数据集，讲师是 Danny Jose Delgado De Sousa，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-18T15:03:12Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（4；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3；`First-Sick` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-14 stars:>2`。HTTP 200。`total_count=57`，返回 5，规则保留 2，未命中 3。剩余配额 9。正文保留 `invisiblelevel/canifol`（26）。`wdcjx/Embedded-programming`（41）更贴近嵌入式，本节一行带过。按总 star，本页顺序是 `grid-dca-bot`、`DCore`、`Embedded-programming`、`canifol`、`DCR-SAM`。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`leftamber/grid-dca-bot`（49；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（48；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）、`set-path/DCR-SAM`（23；名称里的 DCR 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-14 stars:>2`。HTTP 200。`total_count=80`，返回 5，规则保留 2，未命中 3。剩余配额 7。正文保留 `mozihe/z-localization`（125）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`FrankyRenderer`、`robotics-roadmap` 与 `SampQOL-OS` 夹在 `z-localization` 和更低的未命中项之间，剔除课程清单后，本查询自己留下的命中只有 `z-localization`。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 99）。话题含 `ros2` 与 `slam`。README 徽章写 57 讲、120 小时，正文是 57 讲自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 111；描述里的 MPC-BE 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 98；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）、`night-watchman401/hdbot-navigation`（总 star 61；描述里的 “ROS 2” 与 “LiDAR SLAM” 是空格写法，不等于 `ros2` / `slam`，而 `slam` 也不是强特征描述词）。

### C. 领域常青（`pushed:>=2026-11-06 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-06 stars:>3`。HTTP 200。`total_count=1323`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 7。`page=2`、`per_page=5`，本页是总结果里按总 star 排序后的第 6 到第 10 条。本查询正文：`wled/WLED`（19034）、`tinygo-org/tinygo`（17908）、`espressif/arduino-esp32`（17719）、`MarlinFirmware/Marlin`（17659）、`zephyrproject-rtos/zephyr`（17071）。另有 1 条一行不在本页前 5：`okalachev/flix`（2496，话题含 esp32，完整条目在自动控制）。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-06 stars:>3`。HTTP 200。`total_count=9171`，返回 5，规则保留 4，排除清单 1，未命中 0。剩余配额 9。正文保留 `Comfy-Org/ComfyUI`（146520）、`earendil-works/pi`（121665）、`browser-use/browser-use`（120849）、`thedotmack/claude-mem`（116557）。按总 star，本页顺序是 ComfyUI、awesome-llm-apps、pi、browser-use、claude-mem。`pi` 话题为空，靠描述里的 LLM 计入。另有 1 条一行不在本页前 5：`MRPT/mrpt`（2175，话题含 computer-vision，完整条目在自动控制）。
  - 清单类剔除：`Shubhamsaboo/awesome-llm-apps`（总 star 144514）。名称含 awesome，描述是代理应用合集，脚本已排除，不进正文。它夹在 ComfyUI 与 pi 之间。
- 功率器件：成功，经过一次重试。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-06 stars:>3`。第一次为 403 或 429（脚本不保存第一次状态码），等 30 秒重试后 HTTP 200。`total_count=26`，返回 5，规则保留 2，未命中 3。剩余配额 9。`page=2` 是总结果里按总 star 排序后的第 6 到第 10 条。规则保留的 2 条里，1 条撞名剔除，1 条更贴近电力电子，本节只留一行。本页按总 star 的顺序是 `sicp-racket`、`hexlet-sicp`、`epilys/sic`、`BUPT_SICE_ARCHIVE`、`DIY-LiFePO4-UPS`。
  - `epilys/sic`（总 star 27）：名称命中 `sic`。README 写明这是按标签组织的链接聚合，公开站点是 sic.pm，与碳化硅器件无关，正文不收。
  - `wkcollis1-eng/DIY-LiFePO4-UPS`（总 star 17）：话题含 mosfet 与 power-supply。完整条目在电力电子，本节一行带过。
  - 名称词边界未命中：`hexlet-boilerplates/sicp-racket`（136；空描述，`sicp` 不等于 `sic`）、`hexlet-volunteers/hexlet-sicp`（114；SICP 读书进度服务，`sicp` 不等于 `sic`）、`Zmy0312bry/BUPT_SICE_ARCHIVE`（25；北京邮电大学信息与通信工程学院作业资料，`SICE` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-06 stars:>3`。HTTP 200。`total_count=391`，返回 5，规则保留 1，未命中 2，另有 2 条只命中其他领域。剩余配额 7。`page=2` 是总结果里按总 star 排序后的第 6 到第 10 条。本查询正文：`syssi/esphome-jk-bms`（1053）。另有 1 条完整条目来自功率器件检索：`DIY-LiFePO4-UPS`（17）。按总 star，本页顺序是 `Evalle/DCA`、`moteus`、`iot-dc3`、`esphome-jk-bms`、`huawei_solar`。
  - 名称和 topics 未命中：`Evalle/DCA`（1413；Docker Certified Associate 备考，`DCA` 不等于 `dc-dc`）、`mjbots/moteus`（1378；描述是 “motor controller”，空格写法不等于 `motor-control`，名称里的 DC 也不等于 `dc-dc`）。
  - 只命中其他领域：`pnoker/iot-dc3`（1270）。话题含 modbus 与 ai-agents，名称 `dc3` 不等于 `dc-dc`。它不在嵌入式或 AI 常青本页前 5，不跨节。`wlcrs/huawei_solar`（947）。描述是 solar inverters，复数不等于 `inverter`，话题含 modbus。它不在嵌入式常青本页前 5，不跨节。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-06 stars:>3`。HTTP 200。`total_count=245`，返回 5，规则保留 3，未命中 1，排除清单 1。剩余配额 9。正文保留 `RainerKuemmerle/g2o`（3479）、`okalachev/flix`（2496）、`MRPT/mrpt`（2175）。按总 star，本页顺序是 `vedderb/bldc`、`g2o`、`awesome-robotics-libraries`、`flix`、`mrpt`。`flix` 话题含 esp32，嵌入式一节一行带过。`mrpt` 话题含 computer-vision，AI 一节一行带过。
  - 清单类剔除：`jslee02/awesome-robotics-libraries`（总 star 3111）。名称含 awesome，脚本已排除，不进正文。
  - 名称和 topics 未命中：`vedderb/bldc`（总 star 3572）。描述是 “motor control”，空格写法不等于 `motor-control`，名称 `bldc` 不在控制关键词表，正文不收。
