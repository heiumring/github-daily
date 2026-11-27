# GitHub 领域日报 · 2026-11-28

生成时间：2026-11-28 07:37（北京时间）。数据拉取开始于 2026-11-28 07:33:23（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-29（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-21 及之后有推送、总 star > 3。轮换页 `page = (当年第 332 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 让人用自己的显卡从零训一个大约 64M 的小模型，而不是只调用现成的大模型；总 star 72199，24 小时新增 star 667。这是今日热度里唯一命中领域的仓库。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 10136，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) 让编程代理先问这段代码有没有必要写，能复用就不新写；总 star 200108，没有 24 小时新增数据。这是本页常青里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 16 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

嵌入式、功率器件、电力电子电源、自动控制在这 16 条里都没有命中。

### AI

- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
  - 说明：把大模型的训练过程拆到个人显卡上能跑完，用来看懂预训练、微调和对齐，而不是只调一个封装好的接口。README 写主线最小版本大约 64M，并用 PyTorch 从零实现整条训练链路。同一段注明「2 小时」是监督微调阶段在单张 NVIDIA 3090 上跑完 1 个 epoch 的实测，「3 块钱」是这段时间的租卡费用。搜索描述里的 LLM 计入 AI。
  - 领域：AI
  - 总 star：72199
  - 24 小时新增 star：667

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
  - 总 star：171
- [tahaalakhras53-boop/dma-firmware-customization](https://github.com/tahaalakhras53-boop/dma-firmware-customization)
  - 说明：仓库自称是一份给 PCIe DMA 板改写固件身份、让主机把它认成别的设备的说明。README 标题是 “DMA Firmware Customization — Security Tool”，搜索描述写成针对 PCIe Screamer Squirrel 的硬件混淆指南。这是在总线上隐瞒设备身份，正文不写配置、构建和改写步骤。话题含 embedded 与 esp32，仓库名含 firmware，因此归入嵌入式；README 全文没有 ESP32，不把话题里的 esp32 写成这块板的主控。话题里同时有 adc、battery-monitor、hub75、oled 等和这份说明对不上的标签，也有 xilinx-vivado。`created_at` 为 `2026-11-15T19:45:19Z`。
  - 领域：嵌入式 Embedded
  - 总 star：153
- [andrisgauracs/bevel-os](https://github.com/andrisgauracs/bevel-os)
  - 说明：在一块 ESP32-S3 上跑一个能开窗口的小桌面，用六只电阻把 640×480、64 色的画面送到 VGA 显示器。搜索描述写它由模型 Claude Fable 5.2 写成。README 写人负责接线、插线和 3D 打印，具体改线不写入正文；开机到桌面 0.7 秒，窗口里的 Doom（共享版 E1M1）大约 32 帧。硬件写明 16 MB 闪存、8 MB 八线 PSRAM 的 N16R8，系统跑在 ESP-IDF 5.5.3 和 FreeRTOS 上。搜索描述里的 ESP32-S3 按词边界计入 esp32。`created_at` 为 `2026-11-14T14:18:34Z`。
  - 领域：嵌入式 Embedded
  - 总 star：141
- [jthwho/bmds](https://github.com/jthwho/bmds)
  - 说明：把一块没有无线的 ESP32-P4 板做成一台自己能用的小电脑。插上显示器、键盘和网线，就有窗口、命令行，以及能在机器上写脚本的编辑器。搜索描述写的是给 Olimex ESP32-P4-PC 做的一个像 DOS 的小操作系统。README 写芯片是 360 MHz 双核 RISC-V、没有射频，内核用 ESP-IDF 里的 FreeRTOS，画面写的是 1280×720，并写程序之间没有内存保护；作者手头的芯片是 v1.3，v3 的单独构建还没试过。搜索描述里的 ESP32-P4 按词边界计入 esp32。搜索描述里的 “Bare Metal Do Stuff” 是空格写法，不等于 bare-metal，而且 bare-metal 不在强特征描述词里。仓库名是 bmds。`created_at` 为 `2026-11-02T03:03:38Z`。
  - 领域：嵌入式 Embedded
  - 总 star：130

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：10136
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
  - 说明：给团队自托管的一件工作引擎。提一句需求不算做完，要等提出的人签收；可以指定一个代理干活，另一个代理按验收标准复查，不过就退回。README 首页列出 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code、Codex Harness 和 Codex。展开的表标题现在写 Supported harnesses (7)，表里就是这 7 个。话题含 llm 与 ai-agents。话题里的 mcp 不是本次 AI 关键词，不另计。`created_at` 为 `2026-10-29T02:43:14Z`。
  - 领域：AI
  - 总 star：8756
- [simplexai-labs/linger](https://github.com/simplexai-labs/linger)
  - 说明：在自己的电脑上跑一个私人代理，模型和记忆留在本机，而不是按次把对话送到别人的服务器。README 写 MoE 推理把常用专家留在显卡上，其余放在内存或固态硬盘，并写 125B 的 Qwen3.8-Flash-Next 能在 12 GB 显卡加 64 GB 内存上跑。图注写这个模型的 2-bit 文件是 39 GB；速度表里 RTX 3060（12 GB）那一格是 45.5 token/s。这些数字是 README 的说法，不是本次实测。话题 `local-llm` 按词边界计入 llm。`created_at` 为 `2026-11-10T03:50:38Z`。
  - 领域：AI
  - 总 star：5102

### 功率器件 Power Devices

本日无新项目。`total_count=4`，4 条全部返回。规则留下的那条是文献工具，话题 `sic` 不是碳化硅。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。返回的 5 条里，规则留下的两条分别是域名 `bad.llc` 和公司名后缀 LLC，都不是谐振变换器。详见数据源状态。

### 自动控制 Control

- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：给第一人称、野外长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参。README 写一套常规的离线光束法平差能缩小和行业系统的差距，但会停在公开提交的水平；把这两项物理现象放进同一条流水线后，LaMAria 训练集的控制点分数从 69.1 到 82.4。它在 LaMAria 测试集上与 Aria 的 SLAM 打平，并在五个类别里的三个上第一次超过 Aria，UZH-FPV 排行榜上排第二。仓库名里的 slam 计入自动控制。`created_at` 为 `2026-11-13T01:47:26Z`。
  - 领域：自动控制 Control
  - 总 star：167
- [ekrrems/Stereo-inertial-slam](https://github.com/ekrrems/Stereo-inertial-slam)
  - 说明：用双目相机和 IMU 从零写一套视觉惯性 SLAM，同时出稀疏地图和稠密地图，并拿公开路测轨迹对一下误差。README 标题是 RigVis，实现是 C++17（Eigen、OpenCV、Ceres），IMU 融合用误差状态卡尔曼滤波。它在 KITTI 里程计序列 00（4544 帧，3.7 km）上写的相对平移误差是 1.20%，相对旋转是 0.50°/100 m，绝对轨迹误差均方根 2.81 m；同一张表引用的 ORB-SLAM2 双目论文数字是 0.70%、0.25°/100 m 和 1.3 m。仓库名里的 slam 计入自动控制。搜索描述没有这些数字。`created_at` 为 `2026-11-01T17:38:10Z`。
  - 领域：自动控制 Control
  - 总 star：97
- [be2rlab/ACCORD](https://github.com/be2rlab/ACCORD)
  - 说明：用一只相机和一只 IMU 在线做出带尺度的稠密地图，并在回到旧地方时把地图闭合起来。README 写跟踪用 OpenVINS 滤波，深度来自 Depth Anything 3，再把一段段子地图放进位姿图。仓库里有一份 ROS 2 Humble 的包装，搜索话题只有 slam，没有 ros2，正文不把本仓库算成 ros2 项目。话题 slam 计入自动控制。`created_at` 为 `2026-11-04T15:37:22Z`。
  - 领域：自动控制 Control
  - 总 star：86

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=1`、`per_page=5`，本页是各查询按总 star 排序后的第 1 到第 5 条。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：用房间里已有的 Wi-Fi 看有没有人、人怎么动，不靠摄像头。README 写人的走动和呼吸会扰动无线电，一块 ESP32 读信道状态信息，再交给小模型判断在场和姿态。它还写旧的「100% 在场」数字来自单一类别的录音，已经撤回；v2 编码器在无标签留出集上的时间三元组准确率是 82.3%。这些数字是 README 的说法，不是本次实测。话题含 esp32 与 firmware。话题里的 mcp 不是本次 AI 关键词，不另计。本次话题没有 awesome。
  - 领域：嵌入式 Embedded
  - 总 star：105359
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：用纯 C 写小游戏和图形原型，不带现成的可视化编辑器，依赖都收在仓库里，也适合嵌到小设备上。README 写它受 Borland BGI 和 XNA 影响，平台包括 Windows、Linux、macOS、树莓派、安卓和 HTML5。话题含 embedded 与 esp32。话题 `riscv` 不等于 risc-v。提交统计徽章链到的版本标签是 6.2。
  - 领域：嵌入式 Embedded
  - 总 star：35816
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：给 ESP32 做一套能对话的聊天机器人固件，用来把语音助手放进自己的板子，而不是只在手机 App 里聊天。README 点名 Qwen 和 DeepSeek，并写现在要求 ESP-IDF v6.0.1 或更新，推荐 `release/v6.1`，5.x 不再支持；当前矩阵有 171 个变体，ESP32-S31 要 IDF 6.1。默认连官方 xiaozhi.me。搜索描述和话题没有 llm，话题 mcp 不是本次 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：33920
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：给小屏幕做图形界面的库，让单片机上的按钮、图表和动画不用从画点写起。README 写它没有外部依赖，一块典型界面大约要 100 kB 内存和 200 到 300 kB 闪存。搜索描述还写它覆盖小型 MCU 和带 3D 能力的 MPU，并配有 LVGL Pro 编辑器。话题含 embedded-ui、esp32、stm32 与 zephyr。`embedded-ui` 按词边界计入 embedded。
  - 领域：嵌入式 Embedded
  - 总 star：25267
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：给乐鑫的 Wi-Fi 插座和开关换一套固件，让开关、定时和传感器留在本地，用网页或 MQTT 控制，不把日常操作交给厂商云。搜索描述写它面向 ESP8266 和 ESP32。README 把芯片名单写到 ESP32-S2、S3、C2、C3、C5、C6、C61、P4 和 S31。README 也写了电表的 Modbus 和 Modbus 桥，搜索话题没有 modbus，不另开节。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：25039
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13239。
- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd)
  - 说明：在 Flipper Zero 或一块 ESP32 上跟车辆的 CAN 总线通信，用来看电池管理系统的实时数据，搜索描述还列了其他车身功能。区域解锁、报文改写和接线不写入正文。README 标题是 “Tesla Mod for Flipper Zero”，徽章写 Flipper target 7 / API 87.1。话题含 can-bus，描述里的 ESP32 计入嵌入式，描述里的 BMS 计入电力电子电源。跟总线通信比一块仪表更贴近嵌入式，完整条目放在这里；电力电子一节一行带过。
  - 领域：嵌入式 Embedded
  - 总 star：1479

### AI

- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
  - 说明：给编程代理加一条规矩，让它先问这段代码有没有必要存在，仓库里、标准库或现成依赖能做的就不新写。README 写它的本体是一份技能提示词，其余文件只是把这份提示词装进不同代理。徽章写兼容 20 个代理。图注写对照发生在 Claude Code、同一代理、39 个任务、Opus 5.5、各跑 5 次。百分比是 README 的说法，不是本次实测。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：200108
- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：把一种模型的结构定义写一次，同一份定义既能推理也能训练，免得每个项目各包一层。README 写定义用 PyTorch，覆盖文本、计算机视觉、音频、视频和多模态。话题含 llm、pytorch 与 transformer。
  - 领域：AI
  - 总 star：169382
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：把接模型和上线应用放在同一处，用界面搭工作流、检索和代理，而不是每个产品从零接一套接口。README 写它是开源的大模型应用开发平台，并带模型管理和可观测性。话题含 llm。话题里的 mcp 不是本次 AI 关键词；描述里的 RAG 也不是本次 AI 关键词，不另计。
  - 领域：AI
  - 总 star：162029
- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图在自己的电脑上跑扩散模型，把出图、出视频的每一步参数留在图上，而不是只交一个提示词。README 写它把重点放在本地消费级硬件，并写最大的开源模型也可以在 4 GB 显存加 8 GB 内存上跑。这是 README 的说法，不是本次实测。话题含 pytorch。话题 `stable-diffusion` 按词边界计入 diffusion。
  - 领域：AI
  - 总 star：148925

### 功率器件 Power Devices

本页没有命中功率器件。`total_count=31`，本页 5 条都不是碳化硅或功率器件项目。详见数据源状态。

### 电力电子电源 Power Supply

- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd) — 见上方「嵌入式 Embedded」完整条目。描述里的 BMS 计入电力电子电源，此处不展开。领域：电力电子电源 Power Supply。总 star：1479。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：用 Python 把定位、建图、SLAM 和路径规划的算法写成能跑的示例，并配一份在线教材，用来对照公式看代码。搜索描述写的是 robotics algorithms 的示例代码和教材。这是仓库自己的算法示例，不是外部公开课清单，正文保留。话题含 slam。
  - 领域：自动控制 Control
  - 总 star：30988
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：做一台可以自己改的扫地机器人，用二维激光雷达在家里建图和导航，日常不把地图送到云上。README 仍写明现在不能按物料单组装，今天只能在仿真里跑，等第一版物料在真机上核对之后才给组装说明。话题含 ros2 与 slam，也含 esp32。扫地和定位比「板上有 ESP32」更贴近自动控制，完整条目放在这里；嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：13239
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：穿越机飞控上跑的开源固件，用来把遥控器、陀螺仪和电机闭环接起来，而不是用飞控厂商锁死的软件。README 写支持 STM32 的 F4、F7、G4、H5、H7（C5 和 N6 是开发者预览），以及 AT32F435、APM32、RP2350，并写 ESP32 和 X32 仍是实验性支持。搜索话题只有 flight-controller，没有 stm32 或 esp32，不跨到嵌入式。
  - 领域：自动控制 Control
  - 总 star：11842
- [MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)
  - 说明：把不同里程计和 SLAM 吐出的轨迹放到同一把尺子上比误差，免得每个算法各写一套评测脚本。README 写支持 TUM、KITTI、EuRoC，以及 ROS 和 ROS 2 的 bag。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：4373

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。本次跨节的是 oomwoo（自动控制完整，嵌入式一行）和 flipper-tesla-fsd（嵌入式完整，电力电子一行）。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API，下列仓库全部 HTTP 200。默认说明文件名是 `README.md` 的有：`jingyaogong/minimind`、`FlashCat-Jordan/Flashduck`、`zacharyinserra/deskhub`、`tahaalakhras53-boop/dma-firmware-customization`、`andrisgauracs/bevel-os`、`jthwho/bmds`、`wangzan101/Mika`、`mdiri-ai/SoduWork`、`simplexai-labs/linger`、`jacobvm04/slam-dunk`、`ekrrems/Stereo-inertial-slam`、`be2rlab/ACCORD`、`ruvnet/RuView`、`raysan5/raylib`、`78/xiaozhi-esp32`、`lvgl/lvgl`、`arendst/Tasmota`、`hypery11/flipper-tesla-fsd`、`DietrichGebert/ponytail`、`huggingface/transformers`、`langgenius/dify`、`Comfy-Org/ComfyUI`、`AtsushiSakai/PythonRobotics`、`makerspet/oomwoo`、`betaflight/betaflight`、`MichaelGrupp/evo`、`SlashSci/slashsci`、`saltyfireball/bad-llc`、`darkfibr/artex-forensics`、`Finbuckle/Finbuckle.MultiTenant`、`inmusic-software/mpc-plugin-builder-sdk`、`EasyNavigation/StrataSLAM`、`microsoft/Sico`。`Aleksoid1978/MPC-BE` 的说明文件是 `docs/README.md`。`dma-firmware-customization` 的 README 没有 ESP32，身份改写的配置、构建和步骤未写入正文。`artex-forensics` 与 `Claude-BugHunter` 的漏洞或攻击步骤未写入正文。`flipper-tesla-fsd` 的区域解锁、报文改写和接线未写入正文。`bevel-os` 的具体改线未写入正文。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 16 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`jingyaogong/minimind`（72199，667；描述含 LLM）。
- 核对：脚本解析出 16 条后，另一次 GET 同一 URL 仍是 HTTP 200，`<article class="Box-row">` 仍是 16 个，仓库集合和顺序相同，stars today 全部不变。总 star 有变化的是：`Claude-BugHunter` 26033→26035，`firecrawl` 211661→211662，`diagram-design` 74437→74442，`app-store-compliance` 7876→7877，`AFFiNE` 79435→79436，`Ghost-Downloader-3` 19825→19827。`superpowers`（328286，916）、`CLI-Anything`（66981，668）、`minimind`（72199，667）、`plugins`（20010，242）、`nginx`（33661，148）、`openvino`（12945，152）、`last30days-skill`（76345，664）、`stitch-skills`（13583，311）、`opensre`（16117，326）、`autoclip`（17572，733）两次总 star 一致。正文用第一次解析的数字。今日页面本身有 16 条，不是解析丢条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`elementalsouls/Claude-BugHunter`（26033，1615；技能包，描述写 85 个技能，没有 `llm`，攻击步骤不写入正文）、`obra/superpowers`（328286，916；代理技能框架，没有 `llm`）、`XiaoYouChR/Ghost-Downloader-3`（19825，843）、`firecrawl/firecrawl`（211661，833；给代理做搜索和抓取，没有 `llm`）、`zhouxiaoka/autoclip`（17572，733；本地 AI 剪辑，描述里的 MCP server 是裸 mcp，没有 `llm`）、`cathrynlavery/diagram-design`（74437，731；图示设计，没有 `llm`）、`HKUDS/CLI-Anything`（66981，668；把软件做成代理能调用的命令行，没有 `llm`）、`mvanhorn/last30days-skill`（76345，664；“AI agent skill”，没有 `llm`）、`mjmirza/app-store-compliance`（7876，531；“skill for AI coding agents” 是空格写法，不等于 `ai-agents`）、`toeverything/AFFiNE`（79435，469）、`Tracer-Cloud/opensre`（16117，326；CI/CD 代理，没有 `llm`）、`google-labs-code/stitch-skills`（13583，311；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`cursor/plugins`（20010，242；Cursor 插件规范）、`openvinotoolkit/openvino`（12945，152；“AI inference” 是弱词，没有 `llm`）、`nginx/nginx`（33661，148）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-29 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-29 stars:>2`。HTTP 200。`total_count=431`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`FlashCat-Jordan/Flashduck`（192）、`zacharyinserra/deskhub`（171）、`tahaalakhras53-boop/dma-firmware-customization`（153）、`andrisgauracs/bevel-os`（141）、`jthwho/bmds`（130）。昨日窗口起点是 2026-10-28，同页是 Flashduck（192）、deskhub（161）、dma（153）、bevel-os（139）、bmds（130）。窗口起点移到 2026-10-29 后，这 5 条仍是前 5。本次 `deskhub` 的总 star 是 171，`bevel-os` 是 141。这些都是搜索接口的总 star，没有 24 小时新增字段，不把与昨日的差值写成 24 小时新增。`dma-firmware-customization` 的话题含 `esp32`，README 全文没有 ESP32。`Flashduck` 的搜索描述和话题都没有 `llm`。`bmds` 的仓库名是 bmds。搜索描述里的 “Bare Metal Do Stuff” 是空格写法，不等于 bare-metal，而且 bare-metal 不在强特征描述词里。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-29 stars:>2`。HTTP 200。`total_count=2833`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（10136）、`mdiri-ai/SoduWork`（8756）、`simplexai-labs/linger`（5102）。`SoduWork` 的表标题现在写 Supported harnesses (7)，表内列出 7 个。昨日同查询的总 star 是 Mika 10076、SoduWork 8233、linger 4874。这些都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
  - 未命中：`sarpstar/cinecode`（总 star 3129；描述是 “an AI coding agent writes the script”，空格写法不等于 `ai-agents`，也没有 `llm`）。它排在 linger（5102）后面。`DIYgod/pinky`（总 star 2838；描述是让 AI 使用手机，“any MCP agent” 里的裸 mcp 不计入，也没有 `llm`）。它是本页第 5 条。昨日搜索这两条是 3069 和 2809。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-29 stars:>2`。HTTP 200。`total_count=4`，返回 4，规则保留 1，未命中 3。剩余配额 25。4 条就是全部结果，不是接口少给。规则留下的 `SlashSci/slashsci`（4）经人工剔除后，正文无新项目。未命中按总 star 是 `chenlejuncker/fake-sick-trainer-mod-menu`（74）、`EngineerHabib/DOKKHO-E_Commerce-Porject-SICIP`（4）、`SicoKaleb/SicoAutoTerms`（3）。`slashsci` 与 `SICIP` 同为 4 星，脚本把命中和未命中分成两份列表，没有保存这两条 4 星在接口里的先后，本次不补查、不猜测。
  - 人工剔除：`SlashSci/slashsci`（总 star 4；话题含 `sic`，搜索描述是 “More Sides of Science.”）。README 标题是 SlashSci Library，写的是文献管理和译读，不是碳化硅器件。话题里的 `sic` 是撞名。徽章里的 MCP 是裸 mcp，话题没有 llm，不跨到 AI。正文不收。
  - 名称词边界未命中：`fake-sick-trainer-mod-menu`（74；Roblox 相关菜单，`sick` 不等于 `sic`）、`DOKKHO-E_Commerce-Porject-SICIP`（4；名称 `SICIP` 不等于 `sic`，搜索描述为空）、`SicoAutoTerms`（3；`Sico` 不等于 `sic`，描述与碳化硅无关）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-29 stars:>2`。HTTP 200。`total_count=75`，返回 5，规则保留 2，未命中 3。剩余配额 23。规则留下的两条经人工剔除后，正文无新项目。按总 star，本页是 `acrobat-dc-desktop`（197）、`mvc2-naomi-dc`（93）、`isometric-cities`（92）、`bad-llc`（89）、`artex-forensics`（79）。昨日窗口起点是 2026-10-28，同页前 5 是 acrobat-dc（210）、isometric-cities（92）、naomi-dc（87）、artex-forensics（78）、3DCodeFactory（37）。`3DCodeFactory` 不在本次前 5，不猜 star。`acrobat-dc-desktop` 昨日搜索是 210，本次是 197；`mvc2-naomi-dc` 昨日是 87，本次是 93。这是两次搜索的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
  - 人工剔除：`saltyfireball/bad-llc`（总 star 89）。仓库名里的 `llc` 和描述里的 `bad.llc` 是网站域名，README 写这是 Bad Omen 的落地页，托管在 Cloudflare Pages，不是谐振变换器 LLC。`darkfibr/artex-forensics`（总 star 79）。描述里的 LLC 是 Blackfish Security LLC，不是谐振变换器。漏洞步骤未写入正文。搜索描述和话题没有 `llm`。
  - 名称和搜索描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（197；Acrobat DC 不等于 `dc-dc`）、`gibletto/mvc2-naomi-dc`（93；NAOMI 街机的反编译移植，名称里的 dc 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（92；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-29 stars:>2`。HTTP 200。`total_count=112`，返回 5，规则保留 4，未命中 1。剩余配额 21。正文保留 `jacobvm04/slam-dunk`（167）、`ekrrems/Stereo-inertial-slam`（97）、`be2rlab/ACCORD`（86）。`slam-dunk` 昨日搜索是 163，本次是 167。`Stereo-inertial-slam` 昨日搜索是 95，本次是 97。昨日的 `ACCORD` 不在前 5，本次是 86。这些都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。按总 star，本页顺序是 `mpc-plugin-builder-sdk`（238）、`slam-dunk`（167）、`StrataSLAM`（102）、`Stereo-inertial-slam`（97）、`ACCORD`（86）。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 238）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。README 还写 MPC Sample 要固件 v1.4.0 或更新，只做效果。描述里的 “AI coding agent” 是空格写法，不等于 `ai-agents`。昨日搜索是 235。
  - 名称和 topics 未命中：`EasyNavigation/StrataSLAM`（总 star 102；搜索描述为空，名称 `StrataSLAM` 里 slam 前面是字母，词边界不等于 `slam`）。README 写的是多层 ROS 2 SLAM，不参与归类，正文不收。昨日搜索是 98。

### C. 领域常青（`pushed:>=2026-11-21 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-21 stars:>3`。HTTP 200。`total_count=1330`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=1`、`per_page=5`，本页是总结果里按总 star 排序后的第 1 到第 5 条。本查询正文：`ruvnet/RuView`（105359）、`raysan5/raylib`（35816）、`78/xiaozhi-esp32`（33920）、`lvgl/lvgl`（25267）、`arendst/Tasmota`（25039）。另有 1 条一行来自自动控制检索：`makerspet/oomwoo`（13239，话题含 esp32）。另有 1 条完整条目来自电力电子检索：`hypery11/flipper-tesla-fsd`（1479，话题含 can-bus，描述含 ESP32）。按总 star，这一行和这一条排在本查询 5 条之后。`raylib` 的话题是 `riscv`，不等于 risc-v。`xiaozhi-esp32` 的 README 点名 Qwen 和 DeepSeek，搜索描述和话题没有 llm。`Tasmota` 的 README 写了 Modbus，搜索话题没有 modbus，不另开节。`RuView` 本次话题没有 awesome，话题里的 mcp 不计入 AI。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-21 stars:>3`。HTTP 200。`total_count=9451`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 26。正文保留 `DietrichGebert/ponytail`（200108）、`huggingface/transformers`（169382）、`langgenius/dify`（162029）、`Comfy-Org/ComfyUI`（148925）。按总 star，本页顺序是 ponytail、transformers、dify、langflow、ComfyUI。`page=1` 是总结果里的第 1 到第 5 条。`ponytail` 靠话题 `llm` 与 `ai-agents`。`transformers` 靠话题 `llm`、`pytorch` 与 `transformer`。`dify` 靠话题 `llm`。`ComfyUI` 靠话题 `pytorch` 与 `stable-diffusion`。
  - 未命中：`langflow-ai/langflow`（总 star 156991；描述是 “AI-powered agents and workflows”，不等于 `ai-agents`，也没有 `llm`）。它排在 dify（162029）和 ComfyUI（148925）之间。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-21 stars:>3`。HTTP 200。`total_count=31`，返回 5，规则保留 0，排除清单 0，未命中 4。剩余配额 24。`page=1` 是总结果里按总 star 排序后的第 1 到第 5 条。`total_count=31`，本页 5 条不是失败。本页按总 star 是 `SickChill/sickchill`（2451）、`SickGear/SickGear`（806）、`microsoft/Sico`（284）、`siconos/siconos`（188）、`hexlet-volunteers/hexlet-sicp`（114）。人工判断后，本页没有以功率器件为最贴近的完整条目。
  - 名称词边界未命中：`sickchill`（2451；电视剧自动化，`Sick` 不等于 `sic`）、`SickGear`（806；同一类电视工具，`Sick` 不等于 `sic`）、`siconos`（188；非光滑动力系统仿真，名称后面还有字母，不等于 `sic`）、`hexlet-sicp`（114；SICP 读书进度服务，`sicp` 不等于 `sic`）。
  - 命中的是别的领域：`microsoft/Sico`（总 star 284；话题含 `llm`，名称 `Sico` 不等于 `sic`）。它不在 AI 常青前 5，不跨节。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-21 stars:>3`。HTTP 200。`total_count=376`，返回 5，规则保留 2，未命中 2。剩余配额 22。`page=1` 是总结果里按总 star 排序后的第 1 到第 5 条。规则留下的 `Finbuckle.MultiTenant` 经人工剔除。完整条目不放在本节：`flipper-tesla-fsd` 更贴近嵌入式，本节只留一行。按总 star，本页顺序是 Battery-Emulator、OpenDTU、Finbuckle、flipper-tesla-fsd、moteus。
  - 人工剔除：`Finbuckle/Finbuckle.MultiTenant`（总 star 1636）。描述里的 LLC 是 Finbuckle LLC，不是谐振变换器。README 版本仍是 10.1.3，并写本发行支持 .NET 11。正文不收。
  - 名称、话题和搜索描述未命中电力电子：`dalathegreat/Battery-Emulator`（3054；描述里的 solar inverters 是复数，不等于 `inverter`）、`mjbots/moteus`（1402；“motor controller” 是空格写法，不等于 `motor-control`，名称也没有领域词）。
  - 命中的是别的领域、且不在该领域本页前 5：`tbnobody/OpenDTU`（总 star 2218；话题含 esp32，描述里的 Inverters 是复数，不等于 `inverter`）。它不在嵌入式常青前 5，不跨节。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-21 stars:>3`。HTTP 200。`total_count=228`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。正文保留 `AtsushiSakai/PythonRobotics`（30988）、`makerspet/oomwoo`（13239）、`betaflight/betaflight`（11842）、`MichaelGrupp/evo`（4373）。按总 star，本页顺序是 PythonRobotics、oomwoo、betaflight、MPC-BE、evo。本次响应头的剩余配额是 29，前一条自动控制新项目是 21，中间没有失败重试。两次搜索间隔 7 秒，前面的请求已经跨过一分钟，配额窗口滚动，按响应头原样记录。
  - 撞名剔除：`Aleksoid1978/MPC-BE`（总 star 4761）。名称命中 `mpc`。搜索描述写它是 Windows 上的音视频播放器，不是模型预测控制。说明文件是 `docs/README.md`。它夹在 betaflight（11842）和 evo（4373）之间。正文不收。
  - `oomwoo` 的 README 仍写现在不能按物料单组装，只能仿真。`betaflight` 的 README 写了 STM32 和实验性 ESP32，搜索话题没有这些词，不跨嵌入式。`PythonRobotics` 是算法示例加教材，不是公开课清单。
