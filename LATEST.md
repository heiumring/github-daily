# GitHub 领域日报 · 2026-11-21

生成时间：2026-11-21 07:32（北京时间）。数据拉取开始于 2026-11-21 07:32:52（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-22（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-14 及之后有推送、总 star > 3。轮换页 `page = (当年第 325 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 让人用自己的显卡从零训一个大约 64M 的小模型，而不是只调用现成的大模型；总 star 67670，24 小时新增 star 841。这是今日热度里唯一命中领域的仓库。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 9298，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [earendil-works/pi](https://github.com/earendil-works/pi) 给编程代理一个可以按自己流程改的最小框架，搜索描述写它带统一的 LLM 接口；总 star 123069，没有 24 小时新增数据。这是本页常青里星数最高的仓库。

## A. 今日热度

Trending 页面解析到 16 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

嵌入式、功率器件、电力电子电源、自动控制在这 16 条里都没有命中。

### AI

- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
  - 说明：把大模型的训练过程拆到个人显卡上能跑完，用来看懂预训练、微调和对齐，而不是只调一个封装好的接口。README 写主线最小版本大约 64M，并用 PyTorch 从零实现整条训练链路。同一段注明「2 小时」是监督微调阶段在单张 NVIDIA 3090 上跑完 1 个 epoch 的实测，「3 块钱」是这段时间的租卡费用。搜索描述里的 LLM 计入 AI。
  - 领域：AI
  - 总 star：67670
  - 24 小时新增 star：841

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [Kristian8606/esp32-airplay2-surround](https://github.com/Kristian8606/esp32-airplay2-surround)
  - 说明：用便宜的板子自己组一套无线环绕声。README 写明 Apple TV 只看到网关这一台 AirPlay 2 音箱，网关把 5.1 / 7.1 码流原样分给音箱板，每块 ESP32-S3 只解码自己的声道。目前写明网关加五只音箱（前左右、中置、两侧）已经能同步播放 5.1 和 7.1，iPhone 的立体声也能跟上；闪存建议买 16 MB 的 N16R8，8 MB 板仍能编译，音箱固件副本只剩大约 117 KB。搜索描述为空，话题也为空，只靠仓库名里的 esp32 归入嵌入式。
  - 领域：嵌入式 Embedded
  - 总 star：394
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。表格里 MG2500 系列的 MG2550S 标成绿，意思是已在真机验证；其余型号标成黄，预期能用但还没上真机。
  - 领域：嵌入式 Embedded
  - 总 star：343
- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑；ESP-IDF 6.0.1 起，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：186
- [tahaalakhras53-boop/dma-firmware-customization](https://github.com/tahaalakhras53-boop/dma-firmware-customization)
  - 说明：仓库自称是一份给 PCIe DMA 板改写固件身份、让主机把它认成别的设备的说明。README 标题是 “DMA Firmware Customization — Security Tool”。这是在总线上隐瞒设备身份，正文不写安装、配置和改写步骤。话题含 embedded 与 esp32，仓库名含 firmware，因此归入嵌入式；README 全文没有 ESP32，不把话题里的 esp32 写成这块板的主控。话题里同时有 adc、battery-monitor、hub75、oled 等和这份说明对不上的标签。`created_at` 为 `2026-11-15T19:45:19Z`。
  - 领域：嵌入式 Embedded
  - 总 star：153
- [andrisgauracs/bevel-os](https://github.com/andrisgauracs/bevel-os)
  - 说明：在一块 ESP32-S3 上跑一个能开窗口的小桌面，用六只电阻把 640×480、64 色的画面送到 VGA 显示器。README 写它由模型 Claude Fable 5.2 写成，人负责接线和 3D 打印；开机到桌面 0.7 秒，窗口里的 Doom（共享版 E1M1）大约 32 帧。搜索描述里的 ESP32-S3 按词边界计入 esp32。`created_at` 为 `2026-11-14T14:18:34Z`。
  - 领域：嵌入式 Embedded
  - 总 star：119

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：9298
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给作者自己即将发布的程序加一层防护，让自动做逆向的语言模型代理在受保护的产物上得不到可用结果。README 徽章写 npm 包 `bla-agents` v3.5.4，并写明在 14 个对照目标上验证过；正文限定用途是作者和安全团队保护自己的发布物。话题 `llm-security` 按词边界计入 llm。防护参数和绕过细节不写入正文。
  - 领域：AI
  - 总 star：6323
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
  - 说明：给团队自托管的一件工作引擎。提一句需求不算做完，要等提出的人签收；可以指定一个代理干活，另一个代理按验收标准复查，不过就退回。README 写它能接上 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code、Codex Harness 和 Codex。话题含 llm 与 ai-agents。`created_at` 为 `2026-10-29T02:43:14Z`。
  - 领域：AI
  - 总 star：5960
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、iOS、macOS、Android 和 Linux 上按各自的原生控件跑，编程代理可以自己建、自己跑、自己看、自己测。README 写界面用一种叫 Contract 的声明式语言，布局和属性名沿用 CSS；网页产物是大约 20 KB 的运行时加上一个 ES 模块。Android 写明已经能用，Material 3 的打磨还在进行；Windows 仍在早期。仓库仍是 pre-1.0，没有打包发布。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：4826

### 功率器件 Power Devices

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

本窗口没有以功率器件为最贴近领域的完整新项目。名称撞上 `sic` 的课堂笔记本已剔除。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。返回的 5 条里，1 条是公司后缀 LLC，不是谐振变换器；另外 4 条的名称、话题和搜索描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`。详见数据源状态。

### 自动控制 Control

- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：给第一人称、野外长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参。README 写一套常规的离线光束法平差能缩小和行业系统的差距，但会停在公开提交的水平；把这两项物理现象放进同一条流水线后，LaMAria 训练集的控制点分数从 69.1 到 82.4。它在 LaMAria 测试集上与 Aria 的 SLAM 打平，并在五个类别里的三个上第一次超过 Aria，UZH-FPV 排行榜上排第二。仓库名里的 slam 计入自动控制。`created_at` 为 `2026-11-13T01:47:26Z`。
  - 领域：自动控制 Control
  - 总 star：155
- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：给移动机器人一套 ROS 2 激光惯性定位，覆盖里程计、点云建图、先验地图定位、回环和重定位，也可以接 UWB。README 写这是 2026 年东北大学 T-DT 实验室 RoboMaster 超级对抗赛的哨兵定位开源，实机和 rosbag 回放走同一个入口，依赖徽章写 ROS 2 Humble、C++17。作者在开头写，除非有重大 bug，大概率不会再更新。话题含 ros2 与 slam。`created_at` 为 `2026-10-22T08:49:49Z`，落在本次窗口的第一天。
  - 领域：自动控制 Control
  - 总 star：131
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用一个水箱、超声测距和一台泵，把通断、P 和 PI 液位控制做成可以对照仿真的实验。README 写实验台是 15 L 罐子，由 500 L 水箱经一台约 0.5 马力、230 V 的泵补水，市电泵走 Fotek SSR-40DA，直流泵则用 MOSFET 做 PWM；MATLAB 应用的物理量来自你自己的水箱、出口和泵，徽章写 MATLAB R2023b 及以上。2026-10-26 的实测写明当天罐子还没有排水口，靠手倒空，超调是 2.8 cm（11% 到 13%）。话题含 control-systems，话题 `pid-control` 按词边界计入 pid。水位控制比 MOSFET 开关更贴近本领域，功率器件一节一行带过。这条来自功率器件新项目检索，不在自动控制本页前 5。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=2`、`per_page=5`，本页是各查询按总 star 排序后的第 6 到第 10 条。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：给 ESP32 接上可寻址灯带，用手机在局域网里改颜色、效果和分段，不用自己从驱动写起。README 写它有 200 多种内置效果，ESP32 上最多 17 路灯带输出，并列出 original、S2、S3、C3。话题含 esp32，也含 esp8266；本次 README 正文没有再写 ESP8266。默认说明文件名是 `readme.md`。
  - 领域：嵌入式 Embedded
  - 总 star：19089
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：用 Go 写能放进单片机、WebAssembly 和命令行的小程序，换一块板往往只改编译目标。README 的闪灯例子写明同一份代码可以编到 Arduino Uno、Circuit Playground Express 或 Seeed Studio XIAO-ESP32S3。话题含 esp32 与 stm32。
  - 领域：嵌入式 Embedded
  - 总 star：17924
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：让 Arduino 的写法和库能用在 ESP32 系列上，已有的草图不用先改成 ESP-IDF 工程。README 的支持表列出 ESP32、C3、C5、C6、H2、P4、S2、S3、S31；C2 和 C61 也支持，但要把 Arduino 当作 ESP-IDF 组件，或重新编译静态库。话题含 esp32，描述里的 ESP32 也计入。
  - 领域：嵌入式 Embedded
  - 总 star：17776
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：给 3D 打印机的主板一套开源固件，把切片后的运动变成步进电机和挤出机的动作。搜索描述写它同时面向 8 位和 32 位微控制器，不少商品打印机出厂就带它。README 把当前分支标成 Marlin 2.1 的 bugfix 分支，并写明不供生产使用；同一段写 2.1 同时支持 32 位 ARM 和 8 位 AVR，最多 9 个联动轴、8 个挤出机。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：17685
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：给资源紧的设备一套可伸缩的实时操作系统，从传感器和灯带到手表和物联网网关都能用同一套内核。README 写它覆盖 ARM Cortex-A、Cortex-R、Cortex-M，以及 Intel x86、ARC、Tensilica Xtensa、RISC-V、SPARC 和 MIPS。话题含 embedded、rtos、zephyr 与 mcu。默认说明文件是 `README.rst`。
  - 领域：嵌入式 Embedded
  - 总 star：17149

### AI

- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：一个可以按自己的流程改的编程代理框架，扩展、技能和主题都能装，也能做成 npm 包分给别人。搜索描述写它是统一 LLM API、代理循环、终端界面和编程代理命令行的工具包；话题为空，归类靠描述里的 LLM。README 写默认不带子代理和计划模式，要求 Node.js 22.19 或更新，包 `@earendil-works/pi-ai` 是面向多家供应商的 LLM 接口。
  - 领域：AI
  - 总 star：123069
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：让模型在真实浏览器里把一件事做完，开源库用 Python 去点页面，也可以接到托管的浏览器和代理接口。搜索描述写了隐身浏览器和托管代理 API。README 写它能跑在任意 LLM 上，并要求把版本钉在 `browser-use==1.0.8rc1`。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：121616
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
  - 说明：让编程代理下次开工时还记得上次做过什么，免得每次从零再读一遍仓库。README 写它在旁边跑第二个代理做笔记，下一会话先给一份短索引，需要时再把细节取回来；能配合 Claude Code、Codex、Cursor、OpenCode，另外还有 11 个代理。Copilot CLI、Goose、Roo Code、Warp 和 Zed 可以搜索记忆，但它们的会话不会被记下来。记忆文件在本机 `~/.claude-mem`，云同步是可选项；安装说明写选择 claude-mem observer 会进入 30 天试用，结账页要求填写付款方式。话题含 ai-agents。
  - 领域：AI
  - 总 star：118631

### 功率器件 Power Devices

本页没有命中功率器件的条目。`siconos`、`sicp`、`SICAP`、`SICK`、`SiCo` 都是词边界上的撞名。详见数据源状态。

### 电力电子电源 Power Supply

- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：在 Home Assistant 里读一块极空电池管理系统的电芯电压和状态，并做控制，走串口或蓝牙，不用厂家那一个 App。搜索描述写的是 monitor and control。README 写软件版本不低于 6.0 的 JK-BMS 用的是这套协议；蓝牙选项 `JK02_24S` 和 `JK02_32S` 选的是帧格式，不是电芯节数。话题 `jikong-bms` 按词边界计入 bms。README 的接线写了 ESP32 或 ESP8266，搜索话题没有 esp32，不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：1056

### 自动控制 Control

- [MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)
  - 说明：把不同里程计和 SLAM 输出的轨迹放到同一套工具里比误差，用来看一套算法到底比另一套好多少。README 写它支持 TUM、KITTI、EuRoC，以及 ROS 和 ROS 2 的 bag。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：4367
- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：一套同时做定位和建图的库，也可以当成独立程序跑，用来把相机或激光的观测收成一张能重访的地图。话题含 ros2 与 slam。README 写要在 ROS 里用，去另一个仓库 `rtabmap_ros`；ROS 2 的文档和示例在那个仓库的 `ros2` 分支，ROS 1 Noetic 在 `master` 分支。
  - 领域：自动控制 Control
  - 总 star：4115
- [RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)
  - 说明：把 SLAM 和光束法平差里的非线性最小二乘写成一张图来优化，新问题通常加几行就能接上。话题含 slam。README 提到 computer-vision，搜索描述和话题没有这个词，不跨到 AI。
  - 领域：自动控制 Control
  - 总 star：3479
- [luigifreda/pyslam](https://github.com/luigifreda/pyslam)
  - 说明：在一套环境里试验视觉 SLAM，单目、双目和 RGB-D 都能跑，方便换特征、回环和建图模块。README 标题写 v2.12.0，稀疏核心同时有 Python 和 C++，两边存的地图可以互读。话题含 slam。搜索描述和话题没有 computer-vision 或 pytorch，不跨到 AI。
  - 领域：自动控制 Control
  - 总 star：3438

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。本次只有水位实验跨了功率器件和自动控制。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API（定位仓库默认说明文件），下列仓库全部 HTTP 200：`jingyaogong/minimind`、`Kristian8606/esp32-airplay2-surround`、`ngxson/esp32-usb-to-airprint`、`FlashCat-Jordan/Flashduck`、`tahaalakhras53-boop/dma-firmware-customization`、`andrisgauracs/bevel-os`、`wangzan101/Mika`、`qybaihe/bla`、`mdiri-ai/SoduWork`、`expo/exact`、`Samarth030312/arduino-water-level-control-lab`、`jacobvm04/slam-dunk`、`mozihe/z-localization`、`wled/WLED`、`tinygo-org/tinygo`、`espressif/arduino-esp32`、`MarlinFirmware/Marlin`、`zephyrproject-rtos/zephyr`、`earendil-works/pi`、`browser-use/browser-use`、`thedotmack/claude-mem`、`syssi/esphome-jk-bms`、`MichaelGrupp/evo`、`introlab/rtabmap`、`RainerKuemmerle/g2o`、`luigifreda/pyslam`、`sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`、`darkfibr/artex-forensics`、`inmusic-software/mpc-plugin-builder-sdk`、`vedderb/bldc`。`WLED` 的文件名是 `readme.md`，`zephyr` 是 `README.rst`。`dma-firmware-customization` 的 README 没有 ESP32，身份改写的安装、配置和步骤未写入正文。`artex-forensics` 的 README 只用来确认公司后缀，其中的漏洞复现步骤未写入正文。`bla` 的防护参数和绕过细节未写入正文。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 16 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`jingyaogong/minimind`（67670，841；描述含 LLM）。
- 核对：脚本解析出 16 条后，另一次 GET 同一 URL 仍是 HTTP 200，`<article class="Box-row">` 仍是 16 个，仓库集合和顺序相同，stars today 全部不变。6 个仓库的总 star 有变化：`Claude-BugHunter` 14176→14178，`superpowers` 322813→322814，`CLI-Anything` 61357→61358，`firecrawl` 205226→205227，`opensre` 13585→13587，`AFFiNE` 75771→75775。`minimind`（67670，841）、`plugins`（17835，292）、`nginx`（32555，246）、`openvino`（11776，219）、`diagram-design`（69262，634）、`last30days-skill`（71419，685）、`stitch-skills`（11015，315）、`app-store-compliance`（2703，874）、`Ghost-Downloader-3`（13669，1082）、`autoclip`（12149，983）两次一致。正文用第一次解析的数字。今日页面本身有 16 条，不是解析丢条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`elementalsouls/Claude-BugHunter`（14176，1660；技能包，没有 `llm`）、`firecrawl/firecrawl`（205226，1226；给代理做搜索和抓取，没有 `llm`）、`XiaoYouChR/Ghost-Downloader-3`（13669，1082）、`zhouxiaoka/autoclip`（12149，983；AI 视频剪辑，没有 `llm`）、`obra/superpowers`（322813，888；代理技能框架，没有 `llm`）、`mjmirza/app-store-compliance`（2703，874；“AI coding agents” 是空格写法，不等于 `ai-agents`）、`HKUDS/CLI-Anything`（61357，774；把软件做成代理能调用的命令行，没有 `llm`）、`toeverything/AFFiNE`（75771，686）、`mvanhorn/last30days-skill`（71419，685；“AI agent skill”，没有 `llm`）、`cathrynlavery/diagram-design`（69262，634；图示设计，没有 `llm`）、`Tracer-Cloud/opensre`（13585，465；CI/CD 代理，没有 `llm`）、`google-labs-code/stitch-skills`（11015，315；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`cursor/plugins`（17835，292；Cursor 插件规范）、`nginx/nginx`（32555，246）、`openvinotoolkit/openvino`（11776，219；“AI inference” 是弱词，没有 `llm`）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-22 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-22 stars:>2`。HTTP 200。`total_count=445`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`Kristian8606/esp32-airplay2-surround`（394）、`ngxson/esp32-usb-to-airprint`（343）、`FlashCat-Jordan/Flashduck`（186）、`tahaalakhras53-boop/dma-firmware-customization`（153）、`andrisgauracs/bevel-os`（119）。`esp32-airplay2-surround` 的搜索描述和话题都为空，只靠仓库名 `esp32`。`Flashduck` 的 `created_at` 为 `2026-10-31T05:10:09Z`，搜索描述和话题都没有 `llm`，不跨到 AI。`dma-firmware-customization` 的 `created_at` 为 `2026-11-15T19:45:19Z`，话题含 `esp32`，README 全文没有 ESP32。`bevel-os` 的 `created_at` 为 `2026-11-14T14:18:34Z`，搜索描述里的 ESP32-S3 计入 esp32。窗口起点从昨日的 2026-10-21 移到 2026-10-22。昨日报告记录 `agharsallah/esp-labs-web` 的 `created_at` 为 `2026-10-21T13:40:04Z`，落在新窗口外，本次查询不会返回它，也不猜它现在的 star。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-22 stars:>2`。HTTP 200。`total_count=2824`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（9298）、`qybaihe/bla`（6323）、`mdiri-ai/SoduWork`（5960）、`expo/exact`（4826）。`exact` 的 `created_at` 为 `2026-11-02T01:29:01Z`。`Mika` 的 `created_at` 为 `2026-10-29T14:34:07Z`。`SoduWork` 的 `created_at` 为 `2026-10-29T02:43:14Z`。`bla` 的 npm 徽章现为 v3.5.4。昨日同查询里 `SoduWork` 的总 star 是 4168，排在 `exact`（4729）之后；本次是 5960，排到 `exact`（4826）前面。两次都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
  - 未命中：`benjitaylor/skills`（总 star 3881；描述是 “Skills for AI coding agents.”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。按总 star 它是返回的第 5 条，排在 `exact`（4826）之后。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-22 stars:>2`。HTTP 200。`total_count=5`，返回 5，规则保留 2，未命中 3。剩余配额 25。`total_count` 等于返回条数，本次没有第 6 条。规则保留的 2 条里，1 条是课堂笔记本，剔除；1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9），其次是课堂笔记本（7），然后是 `SicnuJw`（6），`SicoAutoTerms` 与 `Sicip-data-science` 都是 3。
  - `sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`（总 star 7）：名称含 SIC，搜索描述为空。README 标题写明这是 Samsung Innovation Campus 2026 的 PA-C 与 PA-D 课堂材料，含 Google Colab 笔记本，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-24T17:55:41Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（6；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`SicoKaleb/SicoAutoTerms`（3；`Sico` 不等于 `sic`，描述与碳化硅无关）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-22 stars:>2`。HTTP 200。`total_count=73`，返回 5，规则保留 1，未命中 4。剩余配额 23。规则留下的 1 条是公司后缀，剔除后本日无新项目。按总 star，本页是 `acrobat-dc-desktop`（210）、`isometric-cities`（87）、`artex-forensics`（78）、`mvc2-naomi-dc`（64）、`grid-dca-bot`（49）。
  - 撞名剔除：`darkfibr/artex-forensics`（总 star 78）。描述末尾是 “Blackfish Security LLC”，README 标题同样是 Blackfish Security LLC。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。搜索描述和话题没有 `llm`，不因 README 里出现的模型字样跨到 AI。漏洞复现步骤未写入正文。
  - 名称、话题和搜索描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（210；Acrobat DC 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（87；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`gibletto/mvc2-naomi-dc`（64；街机游戏反编译，名称里的 dc 不等于 `dc-dc`）、`leftamber/grid-dca-bot`（49；名称里的 DCA 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-22 stars:>2`。HTTP 200。`total_count=111`，返回 5，规则保留 3，未命中 2。剩余配额 21。正文保留 `jacobvm04/slam-dunk`（155）、`mozihe/z-localization`（131）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。`z-localization` 的 `created_at` 为 `2026-10-22T08:49:49Z`。按总 star，本页顺序是 `mpc-plugin-builder-sdk`（196）、`slam-dunk`（155）、`z-localization`（131）、`SampQOL-OS`（127）、`melodee-sample`（70）。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 196）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。描述里的 “AI coding agent” 是空格写法，不等于 `ai-agents`。
  - 名称和 topics 未命中：`snarebes/SampQOL-OS`（总 star 127；描述里的 Akai MPC Sample 不是强特征词，名称也不含 `mpc`）、`keremimo/melodee-sample`（总 star 70；描述里的 Akai MPC Sample 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-14 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-14 stars:>3`。HTTP 200。`total_count=1366`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=2`、`per_page=5`，本页是总结果里按总 star 排序后的第 6 到第 10 条。本查询正文：`wled/WLED`（19089）、`tinygo-org/tinygo`（17924）、`espressif/arduino-esp32`（17776）、`MarlinFirmware/Marlin`（17685）、`zephyrproject-rtos/zephyr`（17149）。`WLED` 话题含 esp8266，本次 README 正文没有写 ESP8266。`huawei_solar` 话题含 modbus，但不在本页前 5，不跨节。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-14 stars:>3`。HTTP 200。`total_count=9787`，返回 5，规则保留 3，排除清单 0，未命中 2。剩余配额 26。正文保留 `earendil-works/pi`（123069）、`browser-use/browser-use`（121616）、`thedotmack/claude-mem`（118631）。`pi` 的话题为空，靠搜索描述里的 LLM。按总 star，本页顺序是 pi、browser-use、agent-skills、claude-mem、impeccable。`page=2` 是总结果里的第 6 到第 10 条。
  - 未命中：`addyosmani/agent-skills`（总 star 119391；描述是 “AI coding agents”，空格写法不等于 `ai-agents`）。它夹在 browser-use 与 claude-mem 之间。`pbakaus/impeccable`（总 star 114035；描述是 “coding agent”，不等于 `ai-agents`）。它是本页第 5 条。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-14 stars:>3`。HTTP 200。`total_count=32`，返回 5，规则保留 0，排除清单 0，未命中 5。剩余配额 24。`page=2` 是总结果里按总 star 排序后的第 6 到第 10 条。返回的星数是 187、114、96、44、30。`total_count=32`，本页 5 条是末段之前的一页，不是接口失败。本节没有完整条目。
  - 名称词边界未命中：`siconos/siconos`（187；非光滑动力系统仿真，`siconos` 不等于 `sic`）、`hexlet-volunteers/hexlet-sicp`（114；SICP 教材的进度服务，`sicp` 不等于 `sic`）、`sicap-pro/SICAP.ai`（96；公共采购检索，`SICAP` 不等于 `sic`）、`SICKAG/sick_safetyscanners2`（44；SICK 安全激光雷达的驱动，描述里的 ROS2 不是强特征词，话题也没有 `ros2`，不跨到自动控制）、`opencad-abu/SiCo`（30；矽科，集成电路设计助手，`SiCo` 不等于 `sic`。搜索描述和话题没有 `llm`，不跨到 AI）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-14 stars:>3`。HTTP 200。`total_count=428`，返回 5，规则保留 1，未命中 4。剩余配额 22。`page=2` 是总结果里按总 star 排序后的第 6 到第 10 条。正文保留 `syssi/esphome-jk-bms`（1056）。按总 star，本页顺序是 `esphome-jk-bms`、`huawei_solar`、`dcmtk`、`rum`、`dcrd`。
  - 名称和 topics 未命中电力电子：`wlcrs/huawei_solar`（953；描述里的 solar inverters 是复数，词边界不等于 `inverter`。话题含 modbus，不在嵌入式常青前 5，不跨节）、`DCMTK/dcmtk`（919；DICOM 工具包，名称里的 dcmtk 不等于 `dc-dc`）、`postgrespro/rum`（849；描述是 inverted index，`inverted` 不等于 `inverter`）、`decred/dcrd`（777；Decred 守护进程，名称里的 dcrd 不等于 `dc-dc`）。
  - `esphome-jk-bms` 的 README 写了 ESP32 与 ESP8266 接线，搜索话题没有 esp32，不跨嵌入式。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-14 stars:>3`。HTTP 200。`total_count=252`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 29。正文保留 `MichaelGrupp/evo`（4367）、`introlab/rtabmap`（4115）、`RainerKuemmerle/g2o`（3479）、`luigifreda/pyslam`（3438）。按总 star，本页顺序是 evo、rtabmap、bldc、g2o、pyslam。`bldc` 夹在 rtabmap 与 g2o 之间。本次响应头的剩余配额是 29，前一条自动控制新项目是 21，中间没有失败重试，按响应头原样记录。
  - 名称和搜索描述未命中：`vedderb/bldc`（总 star 3583）。搜索描述是 “The VESC motor control firmware”，“motor control” 的空格写法不等于 `motor-control`。名称 `bldc` 不在领域关键词表里；`bldc` 只在强特征描述词中，不拿来扫仓库名。README 写了 “DC/BLDC/FOC controller”，其中的 FOC 若出现在搜索描述里会计入自动控制，但搜索描述和话题都没有 `foc`，正文不收。
  - `g2o` 的 README 写了 computer-vision，搜索描述和话题没有，不跨 AI。`pyslam` 的搜索描述和话题没有 computer-vision 或 pytorch，不跨 AI。
