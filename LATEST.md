# GitHub 领域日报 · 2026-11-24

生成时间：2026-11-24 07:40（北京时间）。数据拉取开始于 2026-11-24 07:35:13（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-25（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-17 及之后有推送、总 star > 3。轮换页 `page = (当年第 328 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 让人用自己的显卡从零训一个大约 64M 的小模型，而不是只调用现成的大模型；总 star 69424，24 小时新增 star 828。这是今日热度里唯一命中领域的仓库。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 9762，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) 给编程代理一条「能不写就不写」的提示，先用仓库里已有的代码、标准库或一行能解决的办法，而不是新造一套；总 star 197496，没有 24 小时新增数据。这是本页常青里星数最高的命中仓库。

## A. 今日热度

Trending 页面解析到 16 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

嵌入式、功率器件、电力电子电源、自动控制在这 16 条里都没有命中。

### AI

- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
  - 说明：把大模型的训练过程拆到个人显卡上能跑完，用来看懂预训练、微调和对齐，而不是只调一个封装好的接口。README 写主线最小版本大约 64M，并用 PyTorch 从零实现整条训练链路。同一段注明「2 小时」是监督微调阶段在单张 NVIDIA 3090 上跑完 1 个 epoch 的实测，「3 块钱」是这段时间的租卡费用。搜索描述里的 LLM 计入 AI。
  - 领域：AI
  - 总 star：69424
  - 24 小时新增 star：828

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，Linux 不用另装驱动，浏览器里也能扫描，并要求新驱动先在真机上测过。表格里绿色（已在真机验证）只有 MG2550S；黄色那行写的是 MG2510 到 MG2590（MG2500S 除外），和绿色行的型号写法不一致，按 README 原文记录，黄色表示预期能用但还没上真机。
  - 领域：嵌入式 Embedded
  - 总 star：347
- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑；ESP-IDF 6.0.1 起，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：189
- [tahaalakhras53-boop/dma-firmware-customization](https://github.com/tahaalakhras53-boop/dma-firmware-customization)
  - 说明：仓库自称是一份给 PCIe DMA 板改写固件身份、让主机把它认成别的设备的说明。README 标题是 “DMA Firmware Customization — Security Tool”，搜索描述写成针对 PCIe Screamer Squirrel 的硬件混淆指南。这是在总线上隐瞒设备身份，正文不写安装、配置和改写步骤。话题含 embedded 与 esp32，仓库名含 firmware，因此归入嵌入式；README 全文没有 ESP32，不把话题里的 esp32 写成这块板的主控。话题里同时有 adc、battery-monitor、hub75、oled 等和这份说明对不上的标签。`created_at` 为 `2026-11-15T19:45:19Z`。
  - 领域：嵌入式 Embedded
  - 总 star：153
- [andrisgauracs/bevel-os](https://github.com/andrisgauracs/bevel-os)
  - 说明：在一块 ESP32-S3 上跑一个能开窗口的小桌面，用六只电阻把 640×480、64 色的画面送到 VGA 显示器。README 写它由模型 Claude Fable 5.2 写成，人负责接线和 3D 打印；开机到桌面 0.7 秒，窗口里的 Doom（共享版 E1M1）大约 32 帧。硬件写明 16 MB 闪存、8 MB 八线 PSRAM 的 N16R8，系统跑在 ESP-IDF 5.5.3 和 FreeRTOS 上。搜索描述里的 ESP32-S3 按词边界计入 esp32。`created_at` 为 `2026-11-14T14:18:34Z`。
  - 领域：嵌入式 Embedded
  - 总 star：132
- [zacharyinserra/deskhub](https://github.com/zacharyinserra/deskhub)
  - 说明：把一块 Waveshare ESP32-S3 触控屏放在桌上，看电脑的占用、日历、正在播放的媒体，以及 Claude Code 的用量，也能按屏幕上的按钮去操作这台电脑。README 写固件是 ESP-IDF v5.5 加 LVGL，屏是 4.3 英寸 B 款、800×480 电容触摸，只连 2.4 GHz Wi-Fi；Windows 上的配套程序负责把电脑数据送过来，时钟和天气在电脑关机后仍由板子自己显示。搜索描述没有天气和 Codex，这两项来自 README。描述里的 Claude Code 不是 llm，不跨到 AI。`created_at` 为 `2026-11-17T16:57:49Z`。
  - 领域：嵌入式 Embedded
  - 总 star：131

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：9762
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
  - 说明：给团队自托管的一件工作引擎。提一句需求不算做完，要等提出的人签收；可以指定一个代理干活，另一个代理按验收标准复查，不过就退回。README 首页列出 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code、Codex Harness 和 Codex。展开的表标题写支持 9 个 harness，表里实际列出这 7 个，没有写出的两个不计入。话题含 llm 与 ai-agents。`created_at` 为 `2026-10-29T02:43:14Z`。
  - 领域：AI
  - 总 star：7050
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给作者和安全团队保护自己即将发布的程序，让自动做逆向的语言模型代理在受保护的产物上得不到可用结果。README 徽章写 npm 包 `bla-agents` v3.5.9，并写明有一组 14 个对照目标的本地基准。话题 `llm-security` 按词边界计入 llm。防护参数和绕过细节不写入正文。`created_at` 为 `2026-10-25T05:25:45Z`，落在窗口起点当天。
  - 领域：AI
  - 总 star：6558
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、iOS、macOS、Android 和 Linux 上按各自的原生控件跑，编程代理可以自己建、自己跑、自己看、自己测。README 写界面用一种叫 Contract 的声明式语言，布局和属性名沿用 CSS；网页产物是大约 20 KB 的运行时。Android 写明已经能用，Material 3 的打磨还在进行；Windows 仍在早期。仓库仍是 pre-1.0，没有打包发布，并写 Bun 钉在 1.4.2。搜索描述只写了网页、macOS、iOS 和 Linux，Android 的状态来自 README。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：4970
- [simplexai-labs/linger](https://github.com/simplexai-labs/linger)
  - 说明：在自己的电脑上跑一个私人代理，模型和记忆留在本机，而不是按次把对话送到别人的服务器。README 写 MoE 推理把常用专家留在显卡上，其余放在内存或固态硬盘，并给出一张对照：Qwen3.8-Flash-Next（125B，2-bit 文件 39 GB）在 12 GB 的 RTX 3060 上为 45.5 token/s。这些数字是 README 和图注里的说法，不是本次实测。话题 `local-llm` 按词边界计入 llm。`created_at` 为 `2026-11-10T03:50:38Z`。
  - 领域：AI
  - 总 star：4184

### 功率器件 Power Devices

本日无新项目。`total_count=4`，4 条全部返回，名称都没落到 `sic` 的词边界上。详见数据源状态。

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
  - 总 star：80
- [be2rlab/ACCORD](https://github.com/be2rlab/ACCORD)
  - 说明：只用一台相机和一只 IMU，在线做出带闭环的度量稠密地图。README 写 OpenVINS 负责跟踪相机，Depth Anything 3 给关键帧窗口出深度，再放进位姿图里用回环修正。默认深度模型是 DA3-Giant，README 写显存大约 24 GB；换成 DA3-Base 大约 6 GB。话题含 slam。`created_at` 为 `2026-11-04T15:37:22Z`。
  - 领域：自动控制 Control
  - 总 star：76

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=1`、`per_page=5`，本页是各查询按总 star 排序后的第 1 到第 5 条。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：用普通 Wi-Fi 看房间里有没有人、人怎么动，以及呼吸和心率，不用摄像头。搜索描述写的是把现成 Wi-Fi 变成实时空间感知、生命体征和存在检测，不产生画面。README 进一步写可以隔墙、在暗处工作，并接到 Home Assistant、Apple Home、Google Home 和 Alexa。话题含 esp32 与 firmware。话题里的 mcp 不是本次 AI 关键词，搜索描述没有 llm，不跨到 AI。本次搜索话题没有 awesome。
  - 领域：嵌入式 Embedded
  - 总 star：104951
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：一个用来写游戏和小工具的 C 库，接口收得很窄，换平台时不用先学一套引擎。README 写它适合原型、工具、图形程序、嵌入式和教育。话题含 embedded 与 esp32。话题 `riscv` 不等于 `risc-v`，不另计。
  - 领域：嵌入式 Embedded
  - 总 star：35772
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：给 ESP32 做的语音聊天固件，让一块小板接上麦克风和扬声器就能对话，并按协议去控制外设。搜索描述写的是基于 MCP 的聊天机器人。README 写现在要求 ESP-IDF v6.0.1 或更新，推荐 `release/v6.1`，5.x 不再支持，当前构建矩阵有 171 个变体，ESP32-S31 需要 IDF 6.1 或更新；正文点名 Qwen 和 DeepSeek。这些模型名称在 README 里，搜索描述和话题没有 llm，话题 mcp 不是本次 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：33668
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：给单片机到带 3D 的处理器做嵌入式界面，按钮、列表和动画不用每个屏自己从像素画起。搜索描述写它是免费的嵌入式 UI 库，并配有编辑器 LVGL Pro。话题 `embedded-ui` 按词边界计入 embedded，话题里还有 esp32、stm32 与 zephyr。
  - 领域：嵌入式 Embedded
  - 总 star：25234
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：给 ESP8266 和 ESP32 的插座、开关一类设备换一套固件，在本地用网页配置，用定时或规则做自动化，不把控制交给外部云。搜索描述写的就是这套本地控制，通道包括 MQTT、HTTP、串口和 KNX。话题含 esp32 与 firmware。README 写了 Modbus，搜索话题没有 modbus，不跨到电力电子。
  - 领域：嵌入式 Embedded
  - 总 star：25015
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13196。

### AI

- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
  - 说明：让编程代理先像一个怕写多余代码的老手那样停一下：这件事要不要存在、仓库里有没有、标准库或平台能不能做、能不能一行解决，最后才写最少的新代码。README 写它的本体是一条提示词，徽章写兼容 20 个代理。搜索描述没有 llm 这个词，归类靠话题 llm 与 ai-agents。
  - 领域：AI
  - 总 star：197496
- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：把各类模型的结构定义收成一套，训练框架和推理引擎都对着这套定义接，而不是每个模型各写一份加载代码。README 写它覆盖文本、视觉、音频、视频和多模态，推理和训练都用，并要求 Python 3.11 及以上、PyTorch 2.6 及以上。话题含 llm、pytorch 与 transformer。README 里的 “computer vision” 是空格写法，不等于 `computer-vision`，不另计。
  - 领域：AI
  - 总 star：169273
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：用一块工作区画智能体流程，把模型和工具接进来，从原型做到可以自己托管的应用。搜索描述写了智能体工作流，以及云上、专有网络或自托管。话题含 llm。话题里的 mcp 不是本次 AI 关键词，不另计。
  - 领域：AI
  - 总 star：161763
- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图把扩散模型的出图、出视频串成可复用的流程，在自己的显卡上跑，而不是每次都交到别人的网站。搜索描述写它是模块化的扩散模型界面，也是本地推理后端。README 写即便显存大约 4 GB、内存大约 8 GB，也可以靠异步加载权重去跑较大的开源模型。话题含 pytorch；话题 `stable-diffusion` 按词边界计入 diffusion。
  - 领域：AI
  - 总 star：148291

### 功率器件 Power Devices

本页没有完整条目。返回的 5 条都是名称撞上 `sic` 的词边界之外，或并不做功率器件。详见数据源状态。

### 电力电子电源 Power Supply

本页剔除公司后缀 LLC 后没有完整条目。返回的 5 条里，1 条的 LLC 是公司名；另外 4 条的名称、话题和搜索描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`。详见数据源状态。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：用 Python 把定位、建图、路径规划这些机器人算法写成可以跑的例子，并配了一本讲这些算法的教材。搜索描述写的就是示例代码加教材。话题含 slam。这是仓库自己的算法示例和教材，不是外部公开课清单，正文保留。
  - 领域：自动控制 Control
  - 总 star：30962
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：一台开源扫地机器人，想把清扫、激光定位和户内导航放在同一套可改的机器上。README 开头仍写明现在不能按物料单组装，今天只能在仿真里跑。话题含 ros2 与 slam，也含 esp32。扫地和定位比「用了 ESP32」更贴近本领域，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：13196
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：穿越机飞控上跑的开源固件，用来把遥控指令收成电机转速，而不是只存一份接线图。搜索描述写的就是飞控固件。话题含 flight-controller。README 写了 STM32，以及实验性的 ESP32，搜索话题没有这些词，不跨到嵌入式。
  - 领域：自动控制 Control
  - 总 star：11821
- [TixiaoShan/LIO-SAM](https://github.com/TixiaoShan/LIO-SAM)
  - 说明：把激光雷达和 IMU 紧耦合在一起，边走边做里程计和建图，用因子图把两者的约束一起优化。搜索描述写的就是 Lidar Inertial Odometry via Smoothing and Mapping。README 写明本仓库是原来的 ROS 1 实现，ROS 2 在 `ros2` 分支，默认不是 ROS 2。话题含 slam，没有 ros2。
  - 领域：自动控制 Control
  - 总 star：4983

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。本次跨节的是 oomwoo（嵌入式一行，自动控制完整）。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API，下列仓库全部 HTTP 200。默认说明文件名是 `README.md` 的有：`jingyaogong/minimind`、`ngxson/esp32-usb-to-airprint`、`FlashCat-Jordan/Flashduck`、`tahaalakhras53-boop/dma-firmware-customization`、`andrisgauracs/bevel-os`、`zacharyinserra/deskhub`、`ruvnet/RuView`、`raysan5/raylib`、`78/xiaozhi-esp32`、`lvgl/lvgl`、`arendst/Tasmota`、`wangzan101/Mika`、`mdiri-ai/SoduWork`、`qybaihe/bla`、`expo/exact`、`simplexai-labs/linger`、`DietrichGebert/ponytail`、`huggingface/transformers`、`langgenius/dify`、`Comfy-Org/ComfyUI`、`jacobvm04/slam-dunk`、`ekrrems/Stereo-inertial-slam`、`be2rlab/ACCORD`、`inmusic-software/mpc-plugin-builder-sdk`、`AtsushiSakai/PythonRobotics`、`makerspet/oomwoo`、`betaflight/betaflight`、`TixiaoShan/LIO-SAM`、`Finbuckle/Finbuckle.MultiTenant`、`langflow-ai/langflow`。`Aleksoid1978/MPC-BE` 的说明文件是 `docs/README.md`。`dma-firmware-customization` 的 README 没有 ESP32，身份改写的安装、配置和步骤未写入正文。`bla` 的防护参数和绕过细节未写入正文。`Claude-BugHunter` 的攻击步骤未写入正文。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 16 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`jingyaogong/minimind`（69424，828；描述含 LLM）。
- 核对：脚本解析出 16 条后，另一次 GET 同一 URL 仍是 HTTP 200，`<article class="Box-row">` 仍是 16 个，仓库集合和顺序相同，stars today 全部不变。总 star 有变化的是：`Claude-BugHunter` 19691→19695，`superpowers` 325022→325024，`CLI-Anything` 63584→63586，`minimind` 69424→69427，`plugins` 18790→18791，`firecrawl` 207881→207883，`openvino` 12273→12274，`diagram-design` 70936→70940，`last30days-skill` 73420→73421，`stitch-skills` 12261→12262，`app-store-compliance` 4929→4934，`opensre` 14814→14816，`Ghost-Downloader-3` 16276→16277，`autoclip` 14359→14360。`nginx`（33045，174）与 `AFFiNE`（77371，593）两次一致。正文用第一次解析的数字。今日页面本身有 16 条，不是解析丢条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`elementalsouls/Claude-BugHunter`（19691，2037；技能包，没有 `llm`，攻击步骤不写入正文）、`XiaoYouChR/Ghost-Downloader-3`（16276，1078）、`firecrawl/firecrawl`（207881，920；给代理做搜索和抓取，没有 `llm`）、`zhouxiaoka/autoclip`（14359，908；AI 视频剪辑，没有 `llm`）、`obra/superpowers`（325022，838；代理技能框架，没有 `llm`）、`mvanhorn/last30days-skill`（73420，790；“AI agent skill”，没有 `llm`）、`HKUDS/CLI-Anything`（63584，783；把软件做成代理能调用的命令行，没有 `llm`）、`mjmirza/app-store-compliance`（4929，755；“AI coding agents” 是空格写法，不等于 `ai-agents`）、`cathrynlavery/diagram-design`（70936，624；图示设计，没有 `llm`）、`toeverything/AFFiNE`（77371，593）、`Tracer-Cloud/opensre`（14814，438；CI/CD 代理，没有 `llm`）、`google-labs-code/stitch-skills`（12261，425；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`cursor/plugins`（18790，395；Cursor 插件规范）、`openvinotoolkit/openvino`（12273，183；“AI inference” 是弱词，没有 `llm`）、`nginx/nginx`（33045，174）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-25 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-25 stars:>2`。HTTP 200。`total_count=433`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`ngxson/esp32-usb-to-airprint`（347）、`FlashCat-Jordan/Flashduck`（189）、`tahaalakhras53-boop/dma-firmware-customization`（153）、`andrisgauracs/bevel-os`（132）、`zacharyinserra/deskhub`（131）。`deskhub` 的 `created_at` 为 `2026-11-17T16:57:49Z`，是本页新进入前 5 的一条。`bevel-os` 的 `created_at` 为 `2026-11-14T14:18:34Z`。`dma-firmware-customization` 的 `created_at` 为 `2026-11-15T19:45:19Z`，话题含 `esp32`，README 全文没有 ESP32。`Flashduck` 的搜索描述和话题都没有 `llm`。窗口起点从昨日的 2026-10-24 移到 2026-10-25。昨日的 `Kristian8606/esp32-airplay2-surround` 创建于 2026-10-24，落在窗口外，本次前 5 没有它，不猜 star。昨日同查询里仍在窗口内的总 star 是 airprint 347、Flashduck 187、dma 153、bevel-os 128；本次是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-25 stars:>2`。HTTP 200。`total_count=2812`，返回 5，规则保留 5，未命中 0，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（9762）、`mdiri-ai/SoduWork`（7050）、`qybaihe/bla`（6558）、`expo/exact`（4970）、`simplexai-labs/linger`（4184）。`linger` 的 `created_at` 为 `2026-11-10T03:50:38Z`，话题 `local-llm` 计入 llm，本次新进入前 5。`bla` 的 `created_at` 为 `2026-10-25T05:25:45Z`，npm 徽章现为 v3.5.9。`SoduWork` 的表标题仍写 9 个 harness，表内列出 7 个。昨日同查询的总 star 是 Mika 9631、SoduWork 6815、bla 6426、exact 4918；昨日未命中的 `benjitaylor/skills`（当时 4001）不在本次前 5，不猜 star。这些都是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-25 stars:>2`。HTTP 200。`total_count=4`，返回 4，规则保留 0，未命中 4。剩余配额 25。4 条就是全部结果，不是接口少给。返回顺序按总 star 是 `zjy2968466837/SicnuJw`（7）、`EngineerHabib/DOKKHO-E_Commerce-Porject-SICIP`（4）、`SicoKaleb/SicoAutoTerms`（3）、`Arafat-shuvo/Sicip-data-science`（3）。两条 3 星的先后按接口返回，是 `SicoAutoTerms` 在前。昨日窗口内的水位实验和 Samsung Innovation Campus 笔记本都不在这 4 条里。课堂笔记本的 `created_at` 昨日记录为 `2026-10-24T17:55:41Z`，落在本次窗口外。水位实验也不在全部 4 条里，不猜 star。
  - 名称词边界未命中：`SicnuJw`（四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`DOKKHO-E_Commerce-Porject-SICIP`（名称 `SICIP` 不等于 `sic`，搜索描述为空）、`SicoAutoTerms`（`Sico` 不等于 `sic`，描述与碳化硅无关）、`Sicip-data-science`（`Sicip` 不等于 `sic`，描述是署名，与碳化硅无关）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-25 stars:>2`。HTTP 200。`total_count=75`，返回 5，规则保留 0，未命中 5。剩余配额 23。按总 star，本页是 `acrobat-dc-desktop`（210）、`adobe-acrobat-pro-2026-x64-patcher`（106）、`adobe-acrobat-pro-2026-x64-patcher`（105）、`isometric-cities`（90）、`mvc2-naomi-dc`（78）。
  - 名称和搜索描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（210；Acrobat DC 不等于 `dc-dc`）、`hernandez3236/adobe-acrobat-pro-2026-x64-patcher`（106；Acrobat Pro DC 不等于 `dc-dc`，补丁步骤不写入正文）、`Kanokwanu461/adobe-acrobat-pro-2026-x64-patcher`（105；同上）、`Statecraft-Labs/isometric-cities`（90；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`gibletto/mvc2-naomi-dc`（78；NAOMI 街机的反编译移植，名称里的 dc 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-25 stars:>2`。HTTP 200。`total_count=105`，返回 5，规则保留 4，未命中 1。剩余配额 21。正文保留 `jacobvm04/slam-dunk`（160）、`ekrrems/Stereo-inertial-slam`（80）、`be2rlab/ACCORD`（76）。`Stereo-inertial-slam` 的 `created_at` 为 `2026-11-01T17:38:10Z`，README 标题是 RigVis。按总 star，本页顺序是 `mpc-plugin-builder-sdk`（208）、`slam-dunk`（160）、`SampQOL-OS`（132）、`Stereo-inertial-slam`（80）、`ACCORD`（76）。昨日同查询里 slam-dunk 是 157、ACCORD 是 72；本次是搜索接口的总 star，没有 24 小时新增字段，不把差值写成 24 小时新增。昨日的 `ASIG-X/RESPLE2` 和水位实验都不在本次前 5，不猜 star。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 208）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。描述里的 “AI coding agent” 是空格写法，不等于 `ai-agents`。
  - 名称和 topics 未命中：`snarebes/SampQOL-OS`（总 star 132；描述里的 Akai MPC Sample 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-17 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-17 stars:>3`。HTTP 200。`total_count=1367`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=1`、`per_page=5`，本页是总结果里按总 star 排序后的第 1 到第 5 条。本查询正文：`ruvnet/RuView`（104951）、`raysan5/raylib`（35772）、`78/xiaozhi-esp32`（33668）、`lvgl/lvgl`（25234）、`arendst/Tasmota`（25015）。另有 1 条一行不在本页前 5：`makerspet/oomwoo`（13196，话题含 esp32，完整条目在自动控制）。`raylib` 的话题 `riscv` 不等于 `risc-v`。`xiaozhi-esp32` 的 README 点名 Qwen/DeepSeek 并要求 ESP-IDF v6.0.1，搜索没有 `llm`，不跨 AI。`Tasmota` 的 README 写了 Modbus，搜索话题没有 modbus，不跨节。`RuView` 的话题含裸 mcp，不跨 AI；本次话题没有 awesome。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-17 stars:>3`。HTTP 200。`total_count=9439`，返回 5，规则保留 4，排除清单 0，未命中 1。剩余配额 26。正文保留 `DietrichGebert/ponytail`（197496）、`huggingface/transformers`（169273）、`langgenius/dify`（161763）、`Comfy-Org/ComfyUI`（148291）。按总 star，本页顺序是 ponytail、transformers、dify、langflow、ComfyUI。`page=1` 是总结果里的第 1 到第 5 条。`ponytail` 靠话题 `llm` 与 `ai-agents`，搜索描述没有 llm 这个词。`transformers` 靠话题 `llm`、`pytorch` 与 `transformer`。`dify` 靠话题 `llm`。`ComfyUI` 靠话题 `pytorch`，以及 `stable-diffusion` 计入 diffusion。
  - 未命中：`langflow-ai/langflow`（总 star 156885；搜索描述是 “AI-powered agents”，不等于 `ai-agents`，搜索描述也没有 `llm`）。它夹在 dify（161763）和 ComfyUI（148291）之间。README 里的 LLMs 是复数，且不参与归类。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-17 stars:>3`。HTTP 200。`total_count=32`，返回 5，规则保留 0，未命中 5。剩余配额 24。`page=1` 是总结果里按总 star 排序后的第 1 到第 5 条。返回的星数是 2450、805、284、188、114。`total_count=32`，本页 5 条不是末页，也不是接口失败。
  - 名称词边界未命中：`SickChill/sickchill`（2450；`SickChill` 不等于 `sic`）、`SickGear/SickGear`（805；`SickGear` 不等于 `sic`）、`siconos/siconos`（188；非光滑动力系统仿真，`siconos` 不等于 `sic`）、`hexlet-volunteers/hexlet-sicp`（114；SICP 一书的进度服务，`sicp` 不等于 `sic`）。
  - `microsoft/Sico`（284）：`Sico` 不等于 `sic`，不归入功率器件。话题含 `llm`，但不在 AI 常青前 5，不跨节。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-17 stars:>3`。HTTP 200。`total_count=420`，返回 5，规则保留 1，未命中 4。剩余配额 22。`page=1` 是总结果里按总 star 排序后的第 1 到第 5 条。规则留下的 1 条是公司后缀，剔除后本页没有完整条目。按总 star，本页顺序是 `Battery-Emulator`（3047）、`OpenDTU`（2216）、`Finbuckle.MultiTenant`（1634）、`dcm4che`（1466）、`moteus`（1399）。
  - 撞名剔除：`Finbuckle/Finbuckle.MultiTenant`（总 star 1634）。搜索描述末尾是 Finbuckle LLC，README 标题下的版本是 10.1.3。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。
  - 名称、话题和搜索描述未命中电力电子：`dalathegreat/Battery-Emulator`（3047；描述里的 “solar inverters” 是复数，不等于 `inverter`）、`tbnobody/OpenDTU`（2216；描述里的 “Inverters” 是复数，不等于 `inverter`；话题含 `esp32`，不在嵌入式常青前 5，不跨节）、`dcm4che/dcm4che`（1466；DICOM 实现，`dcm` 不等于 `dc-dc`）、`mjbots/moteus`（1399；“Brushless DC motor controller” 里的 DC 不等于 `dc-dc`，“motor controller” 空格不等于 `motor-control`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-17 stars:>3`。HTTP 200。`total_count=242`，返回 5，规则保留 5，未命中 0，排除清单 0。剩余配额 29。正文保留 `AtsushiSakai/PythonRobotics`（30962）、`makerspet/oomwoo`（13196）、`betaflight/betaflight`（11821）、`TixiaoShan/LIO-SAM`（4983）。`oomwoo` 在嵌入式一行。按总 star，本页顺序是 PythonRobotics、oomwoo、betaflight、LIO-SAM、MPC-BE。本次响应头的剩余配额是 29，前一条自动控制新项目是 21，中间没有失败重试。两次搜索间隔 7 秒，前面的请求已经跨过一分钟，配额窗口滚动，按响应头原样记录。
  - 撞名剔除：`Aleksoid1978/MPC-BE`（总 star 4751）。名称命中 `mpc`。README 路径是 `docs/README.md`，标题写明这是 Windows 上的音视频播放器 Media Player Classic - Black Edition，不是模型预测控制，正文不收。
  - `oomwoo` 话题含 esp32，嵌入式一节一行带过；README 仍写明现在不能按物料单组装，只能仿真。`betaflight` 的 README 写了 STM32 与实验性 ESP32，搜索话题没有这些词，不跨嵌入式。`LIO-SAM` 的 README 写本仓库是 ROS 1，ROS 2 在 `ros2` 分支。
