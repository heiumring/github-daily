# GitHub 领域日报 · 2026-11-20

生成时间：2026-11-20 07:32（北京时间）。数据拉取开始于 2026-11-20 07:32:30（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-21（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-11-13 及之后有推送、总 star > 3。轮换页 `page = (当年第 324 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 让人用自己的显卡从零训一个大约 64M 的小模型，而不是只调用现成的大模型；总 star 66833，24 小时新增 star 301。这是今日热度里唯一命中领域的仓库。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 9176，没有 24 小时新增数据。这是近 30 天新项目里星数最高的命中仓库。
3. [ruvnet/RuView](https://github.com/ruvnet/RuView) 用房间里已有的 Wi-Fi 看有没有人、呼吸和心率，不靠摄像头；总 star 104639，没有 24 小时新增数据。这是本页嵌入式常青里星数最高的仓库。

## A. 今日热度

Trending 页面解析到 16 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

嵌入式、功率器件、电力电子电源、自动控制在这 16 条里都没有命中。

### AI

- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
  - 说明：把大模型的训练过程拆到个人显卡上能跑完，用来看懂预训练、微调和对齐，而不是只调一个封装好的接口。README 写主线最小版本大约 64M，并用 PyTorch 从零实现整条训练链路。同一段注明「2 小时」是监督微调阶段在单张 NVIDIA 3090 上跑完 1 个 epoch 的实测，「3 块钱」是这段时间的租卡费用。搜索描述里的 LLM 计入 AI。
  - 领域：AI
  - 总 star：66833
  - 24 小时新增 star：301

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 的实验台收成一个网页。README 写明目前是 32 个动手实验，每课先在浏览器里跑，带实时引脚、交互模拟、逐行讲解固件的阅读器，以及一块 3D 板；数据手册部分把芯片手册收成可引用的章节。搜索描述写 11 种语言；README 徽章写 12 languages，列出英语、法语、西班牙语、意大利语、德语、波兰语、土耳其语、简体中文、繁体中文、日语，以及从右到左的阿拉伯语和波斯语。话题含 education，这是实验台应用，不是公开课清单。`created_at` 为 `2026-10-21T13:40:04Z`，落在本次窗口的第一天。
  - 领域：嵌入式 Embedded
  - 总 star：915
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。表格里 MG2500 系列的 MG2550S 标成绿，意思是已在真机验证；其余型号标成黄，预期能用但还没上真机。
  - 领域：嵌入式 Embedded
  - 总 star：339
- [Kristian8606/esp32-airplay2-surround](https://github.com/Kristian8606/esp32-airplay2-surround)
  - 说明：用便宜的板子自己组一套无线环绕声。README 写明 Apple TV 只看到网关这一台 AirPlay 2 音箱，网关把 5.1 / 7.1 码流原样分给音箱板，每块 ESP32-S3 只解码自己的声道。目前写明网关加五只音箱（前左右、中置、两侧）已经能同步播放 5.1 和 7.1，iPhone 的立体声也能跟上；闪存建议买 16 MB 的 N16R8，8 MB 板仍能编译，音箱固件副本只剩大约 117 KB。搜索描述为空，话题也为空，只靠仓库名里的 esp32 归入嵌入式。
  - 领域：嵌入式 Embedded
  - 总 star：312
- [FlashCat-Jordan/Flashduck](https://github.com/FlashCat-Jordan/Flashduck)
  - 说明：一只六舵机的桌面机器鸭，让模型在运行时直接写六个关节的角度，而不是只播放写死的动作。README 写明同一套 ESP32-S3 硬件二选一刷语音版或 DuckClaw，不能同时跑；ESP-IDF 6.0.1 起，外壳可 3D 打印，小白用闪猫 1 号套件大约 30 分钟能拼起来。搜索描述和话题都没有 llm，话题里的 esp32-s3 按词边界计入 esp32，不跨到 AI。`created_at` 为 `2026-10-31T05:10:09Z`。
  - 领域：嵌入式 Embedded
  - 总 star：186
- [tahaalakhras53-boop/dma-firmware-customization](https://github.com/tahaalakhras53-boop/dma-firmware-customization)
  - 说明：仓库自称是一份给 PCIe DMA 板改写固件身份、让主机把它认成别的设备的说明。README 标题把它称为安全工具。这是在总线上隐瞒设备身份，正文不写安装、配置和改写步骤。话题含 embedded 与 esp32，仓库名含 firmware，因此归入嵌入式；README 全文没有 ESP32，不把话题里的 esp32 写成这块板的主控。`created_at` 为 `2026-11-15T19:45:19Z`。
  - 领域：嵌入式 Embedded
  - 总 star：153

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 徽章写安装包要求 Android 11 及以上；正文把聊天、网页和文件放在 Android 11，把操作手机 App 放在 Android 12 及以上，并建议 Android 14 及以上，因为后台屏有自己的焦点。话题含 llm。`created_at` 为 `2026-10-29T14:34:07Z`。
  - 领域：AI
  - 总 star：9176
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给作者自己即将发布的程序加一层防护，让自动做逆向的语言模型代理在受保护的产物上得不到可用结果。README 徽章写 npm 包 `bla-agents` v3.5.2，并写明在 14 个对照目标上验证过；正文限定用途是作者和安全团队保护自己的发布物。话题 `llm-security` 按词边界计入 llm。防护参数和绕过细节不写入正文。
  - 领域：AI
  - 总 star：6206
- [expo/exact](https://github.com/expo/exact)
  - 说明：写一次界面，让它在网页、macOS、iOS 和 Linux 上原生跑，编程代理可以自己建、自己跑、自己看、自己测。README 写界面用一种叫 Contract 的声明式语言，布局和属性名沿用 CSS；网页产物是大约 20 KB 的运行时加上一个 ES 模块，各平台的界面都不走 webview。Android 写明已经能用，Material 3 的打磨还在进行；Windows 仍在早期。仓库仍是 pre-1.0，没有打包发布。话题含 ai-agents。`created_at` 为 `2026-11-02T01:29:01Z`。
  - 领域：AI
  - 总 star：4729
- [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)
  - 说明：给团队自托管的一件工作引擎。提一句需求不算做完，要等提出的人签收；可以指定一个代理干活，另一个代理按验收标准复查，不过就退回。README 写它能接上 Pi、OpenCode、DeepSeek Harness、Qwen Code、Kimi Code、Codex Harness 和 Codex。话题含 llm 与 ai-agents。`created_at` 为 `2026-10-29T02:43:14Z`。
  - 领域：AI
  - 总 star：4168

### 功率器件 Power Devices

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：9。

本窗口没有以功率器件为最贴近领域的完整新项目。名称撞上 `sic` 的课堂笔记本已剔除。详见数据源状态。

### 电力电子电源 Power Supply

本日无新项目。返回的 5 条里，1 条是公司后缀 LLC，不是谐振变换器；另外 4 条的名称、话题和搜索描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`。详见数据源状态。

### 自动控制 Control

- [jacobvm04/slam-dunk](https://github.com/jacobvm04/slam-dunk)
  - 说明：给第一人称、野外长轨迹的视觉惯性里程计补上相机标定漂移和陀螺仪内参。README 写一套常规的离线光束法平差能缩小和行业系统的差距，但会停在公开提交的水平；把这两项物理现象放进同一条流水线后，LaMAria 训练集的控制点分数从 69.1 到 82.4。它在 LaMAria 测试集上与 Aria 的 SLAM 打平，并在五个类别里的三个上第一次超过 Aria，UZH-FPV 排行榜上排第二。仓库名里的 slam 计入自动控制。`created_at` 为 `2026-11-13T01:47:26Z`。
  - 领域：自动控制 Control
  - 总 star：152
- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：给移动机器人一套 ROS 2 激光惯性定位，覆盖里程计、点云建图、先验地图定位、回环和重定位，也可以接 UWB。README 写这是 2026 年东北大学 T-DT 实验室 RoboMaster 超级对抗赛的哨兵定位开源，实机和 rosbag 回放走同一个入口，依赖徽章写 ROS 2 Humble、C++17。话题含 ros2 与 slam。`created_at` 为 `2026-10-22T08:49:49Z`。
  - 领域：自动控制 Control
  - 总 star：130
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用一个水箱、超声测距和一台泵，把通断、P 和 PI 液位控制做成可以对照仿真的实验。README 写实验台是 15 L 罐子，由 500 L 水箱经一台约 0.5 马力、230 V 的泵补水，市电泵走 Fotek SSR-40DA，直流泵则用 MOSFET 做 PWM；MATLAB 应用的物理量来自你自己的水箱、出口和泵，徽章写 MATLAB R2023b 及以上。话题含 control-systems，话题 `pid-control` 按词边界计入 pid。水位控制比 MOSFET 开关更贴近本领域，功率器件一节一行带过。这条来自功率器件新项目检索，不在自动控制本页前 5。
  - 领域：自动控制 Control
  - 总 star：9

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page=1`、`per_page=5`，本页是各查询按总 star 排序后的第 1 到第 5 条。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：人在房间里会扰动已经铺开的 Wi-Fi，这个项目读这些扰动，用来判断有没有人、呼吸和心率，不靠摄像头。README 写采集用的是廉价 ESP32 上的信道状态信息，并写可以隔墙；统一射频世界模型那一节写明精度目前仍是合成数据，真实数据验证还没做完。话题含 esp32 与 firmware，也含裸 mcp。裸 mcp 不是本报告的 AI 关键词，搜索描述没有 llm，不跨到 AI。本次话题里没有 awesome。
  - 领域：嵌入式 Embedded
  - 总 star：104639
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：用一套不依赖外部库的 C 接口写小游戏和图形程序，让原型和教学不用先搭引擎。README 写它适合原型、工具、图形应用、嵌入式和教育，用 C99 写成。话题含 embedded 与 esp32。话题里的 `riscv` 不等于 `risc-v`。README 正文没有把 ESP32 写成已支持的平台，归类靠话题。
  - 领域：嵌入式 Embedded
  - 总 star：35734
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：给 ESP32 做一个能说话的聊天机器人，把语音进出和大模型对话接在设备上，并用 MCP 去控灯、舵机和 GPIO。README 点名 Qwen 与 DeepSeek，并要求 ESP-IDF v6.0.1 或更新，推荐 `release/v6.1`。搜索描述和话题没有 llm，话题里的 mcp 不是 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：33473
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：在单片机和微处理器的屏幕上画界面，让小设备不用上桌面图形栈。README 写它不依赖外部库，典型界面大约要 100 kB 内存和 200 到 300 kB 闪存。话题 `embedded-ui` 按词边界计入 embedded，并含 esp32、stm32、zephyr。
  - 领域：嵌入式 Embedded
  - 总 star：25207
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：给现成的插座、开关和灯换一套可本地配置的固件，用网页、定时和规则做自动化，不把控制交给云。README 写它从 ESP8266 起，现在覆盖 ESP32 系列，并可以用 MQTT、HTTP、串口或 KNX 在本地控制。话题含 esp32 与 firmware。README 写了 Modbus 桥，搜索话题没有 modbus，不另开一节。
  - 领域：嵌入式 Embedded
  - 总 star：25000
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：13153。这条不在嵌入式常青本页前 5。

### AI

- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：把模型结构定义收成一份大家共用的实现，训练框架和推理引擎都对着同一份定义接，免得每个库各写一遍。README 写它覆盖文本、计算机视觉、音频、视频和多模态，既做推理也做训练，并写 Hugging Face Hub 上有超过 100 万个 Transformers 检查点。话题含 llm、pytorch 与 transformer。
  - 领域：AI
  - 总 star：169284
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：把模型、工作流和代理放在一个可以自己部署的工作台里，让一个原型不用换栈就能接到正式环境。README 写它是开源的大模型应用开发平台，代理可以在自己的沙箱里跑命令、装软件和处理文件。话题含 llm。搜索描述里的 RAG 不是本报告的关键词。
  - 领域：AI
  - 总 star：161519
- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用一张节点图在自己的电脑上把图像、视频、三维和音频生成串起来，每一步用哪个模型、什么参数都看得见。README 写它面向要控制每一步输出的视觉工作，并写本地消费级硬件上的扩散模型推理是它的重点。话题含 pytorch，话题 `stable-diffusion` 按词边界计入 diffusion。
  - 领域：AI
  - 总 star：147676

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。`imagineer` 是命令行图片处理，旧名 `sic`，已剔除。详见数据源状态。

### 电力电子电源 Power Supply

本页剔除公司后缀 LLC 后没有完整条目。`inverters` 的复数不计入 `inverter`。详见数据源状态。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：把定位、建图、路径规划这些机器人算法做成可以运行的 Python 示例，并配一份放在本仓库体系里的教材，用来对照公式看代码。README 目录里有扩展卡尔曼滤波、粒子滤波、ICP、FastSLAM，以及 Dijkstra、A* 等规划。话题含 slam。这是算法示例加教材，不是一份外部公开课链接清单，正文保留。
  - 领域：自动控制 Control
  - 总 star：30951
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：一台可以自己做的扫地机器人。README 写明用树莓派、3D 打印、Home Assistant、Arduino 和 ROS 2，靠二维激光建图和导航，常规功能不依赖云。开头同时写明现在还不能按物料单组装，今天只能跑仿真，物料单要等真机验证之后才给。话题含 ros2 与 slam，也含 esp32。扫地导航比板子更贴近本领域，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：13153
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：穿越机飞控上跑的开源固件，用来把遥控和传感器变成电机指令。README 写本仓库就是跑在飞控上的固件，并列出 STM32 F4、F7、G4、H5、H7 等目标，以及实验性的 ESP32。搜索话题只有 flight-controller 等，没有 stm32 或 esp32，不跨到嵌入式。
  - 领域：自动控制 Control
  - 总 star：11808
- [MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)
  - 说明：把不同里程计和 SLAM 输出的轨迹放到同一套工具里比误差，用来看一套算法到底比另一套好多少。README 写它支持 TUM、KITTI、EuRoC，以及 ROS 和 ROS 2 的 bag。话题含 ros2 与 slam。
  - 领域：自动控制 Control
  - 总 star：4368

## 数据源状态

脚本 `scripts/fetch_github_daily.py` 已存在，`STRONG_DESC_WORDS` 与 `STRONG_WORD_DOMAINS` 已包含 inverter、bms、motor-control、motor-drive、dc-dc、power-supply、microgrid、mosfet、wide-bandgap、device-modeling、llm 及对应映射。本次未改脚本。没有加入 buck、boost、pll、pid。

认证方式：使用本机 `gh` 登录令牌作为环境变量 `GH_TOKEN`，令牌未写入仓库。11 次逻辑请求全部第一次 HTTP 200，没有 403/429，没有重试。相邻请求间隔 7 秒。各搜索响应的 `incomplete_results` 均为 false。另一次 Trending 核对和 README 读取不计入这 11 次。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取走 GitHub README API（定位仓库默认说明文件），下列仓库全部 HTTP 200：`jingyaogong/minimind`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Kristian8606/esp32-airplay2-surround`、`FlashCat-Jordan/Flashduck`、`tahaalakhras53-boop/dma-firmware-customization`、`wangzan101/Mika`、`qybaihe/bla`、`expo/exact`、`mdiri-ai/SoduWork`、`ruvnet/RuView`、`raysan5/raylib`、`78/xiaozhi-esp32`、`lvgl/lvgl`、`arendst/Tasmota`、`huggingface/transformers`、`langgenius/dify`、`Comfy-Org/ComfyUI`、`Samarth030312/arduino-water-level-control-lab`、`jacobvm04/slam-dunk`、`mozihe/z-localization`、`AtsushiSakai/PythonRobotics`、`makerspet/oomwoo`、`betaflight/betaflight`、`MichaelGrupp/evo`、`sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`、`inmusic-software/mpc-plugin-builder-sdk`、`foresterre/imagineer`、`Finbuckle/Finbuckle.MultiTenant`、`Aleksoid1978/MPC-BE`、`darkfibr/artex-forensics`。`dma-firmware-customization` 的 README 没有 ESP32，身份改写的安装、配置和步骤未写入正文。`artex-forensics` 的 README 只用来确认公司后缀，其中的漏洞复现步骤未写入正文。`bla` 的防护参数和绕过细节未写入正文。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 16 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`jingyaogong/minimind`（66833，301；描述含 LLM）。
- 核对：脚本解析出 16 条后，另一次 GET 同一 URL 仍是 HTTP 200，`<article class="Box-row">` 仍是 16 个，仓库集合和顺序相同，stars today 全部不变。9 个仓库的总 star 有变化：`Claude-BugHunter` 12458→12462，`CLI-Anything` 60525→60526，`plugins` 17539→17540，`firecrawl` 204160→204161，`diagram-design` 68608→68609，`last30days-skill` 70770→70771，`stitch-skills` 10701→10702，`opensre` 13104→13105，`Ghost-Downloader-3` 12665→12666。`minimind`（66833，301）、`superpowers`（322045，2029）、`nginx`（32319，66）、`openvino`（11552，246）、`AFFiNE`（75144，170）、`app-store-compliance`（1805，426）、`autoclip`（11186，110）两次一致。正文用第一次解析的数字。今日页面本身有 16 条，不是解析丢条。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`obra/superpowers`（322045，2029；代理技能框架，没有 `llm`）、`elementalsouls/Claude-BugHunter`（12458，1353；技能包，没有 `llm`）、`mvanhorn/last30days-skill`（70770，952；“AI agent skill”，没有 `llm`）、`HKUDS/CLI-Anything`（60525，899；把软件做成代理能调用的命令行，没有 `llm`）、`firecrawl/firecrawl`（204160，795；给代理做搜索和抓取，没有 `llm`）、`XiaoYouChR/Ghost-Downloader-3`（12665，449）、`mjmirza/app-store-compliance`（1805，426；“AI coding agents” 是空格写法，不等于 `ai-agents`）、`cathrynlavery/diagram-design`（68608，402；图示设计，没有 `llm`）、`cursor/plugins`（17539，383；Cursor 插件规范）、`google-labs-code/stitch-skills`（10701，303；“coding agents” 与 “Stitch MCP server” 里的裸 mcp 都不计入）、`openvinotoolkit/openvino`（11552，246；“AI inference” 是弱词，没有 `llm`）、`toeverything/AFFiNE`（75144，170）、`zhouxiaoka/autoclip`（11186，110；AI 视频剪辑，没有 `llm`）、`nginx/nginx`（32319，66）、`Tracer-Cloud/opensre`（13104，25）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-21 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-21 stars:>2`。HTTP 200。`total_count=446`，返回 5，规则保留 5，排除清单 0，未命中 0。剩余配额 29。这 5 条都写入正文：`agharsallah/esp-labs-web`（915）、`ngxson/esp32-usb-to-airprint`（339）、`Kristian8606/esp32-airplay2-surround`（312）、`FlashCat-Jordan/Flashduck`（186）、`tahaalakhras53-boop/dma-firmware-customization`（153）。`esp-labs-web` 的 `created_at` 为 `2026-10-21T13:40:04Z`。`Flashduck` 的 `created_at` 为 `2026-10-31T05:10:09Z`。`dma-firmware-customization` 的 `created_at` 为 `2026-11-15T19:45:19Z`。`Flashduck` 的搜索描述和话题都没有 `llm`，不跨到 AI。`esp32-airplay2-surround` 的搜索描述和话题都为空，只靠仓库名 `esp32`。`esp-labs-web` 话题含 `education`，是带模拟器的实验台，不是公开课清单，正文保留。`dma-firmware-customization` 的话题含 `esp32`，README 全文没有 ESP32。窗口起点从昨日的 2026-10-20 移到 2026-10-21，这 5 条的创建时间都仍在窗口内。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-21 stars:>2`。HTTP 200。`total_count=2853`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 27。正文保留 `wangzan101/Mika`（9176）、`qybaihe/bla`（6206）、`expo/exact`（4729）、`mdiri-ai/SoduWork`（4168）。`exact` 的 `created_at` 为 `2026-11-02T01:29:01Z`。`Mika` 的 `created_at` 为 `2026-10-29T14:34:07Z`。`SoduWork` 的 `created_at` 为 `2026-10-29T02:43:14Z`。`bla` 的 npm 徽章现为 v3.5.2。
  - 未命中：`benjitaylor/skills`（总 star 3813；描述是 “Skills for AI coding agents.”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。按总 star 它是返回的第 5 条，排在 `SoduWork`（4168）之后。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-21 stars:>2`。HTTP 200。`total_count=5`，返回 5，规则保留 2，未命中 3。剩余配额 25。`total_count` 等于返回条数，本次没有第 6 条。规则保留的 2 条里，1 条是课堂笔记本，剔除；1 条更贴近自动控制，本节只留一行。返回的 5 条里星数最高的是水位实验（9），其次是课堂笔记本（7），然后是 `SicnuJw`（6），`SicoAutoTerms` 与 `Sicip-data-science` 都是 3。
  - `sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`（总 star 7）：名称含 SIC，搜索描述为空。README 标题写明这是 Samsung Innovation Campus 2026 的 PA-C 与 PA-D 课堂材料，含 Google Colab 笔记本，与碳化硅器件无关，正文不收。接口 `created_at` 为 `2026-10-24T17:55:41Z`。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 9）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`zjy2968466837/SicnuJw`（6；四川师范大学教务客户端，`Sicnu` 不等于 `sic`）、`SicoKaleb/SicoAutoTerms`（3；`Sico` 不等于 `sic`，描述与碳化硅无关）、`Arafat-shuvo/Sicip-data-science`（3；`Sicip` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-21 stars:>2`。HTTP 200。`total_count=74`，返回 5，规则保留 1，未命中 4。剩余配额 23。规则留下的 1 条是公司后缀，剔除后本日无新项目。按总 star，本页是 `acrobat-dc-desktop`（211）、`isometric-cities`（85）、`AcrobatDC-Latest2026`（85）、`artex-forensics`（77）、`mvc2-naomi-dc`（58）。两个 85 的先后按接口返回顺序：`isometric-cities` 在前。
  - 撞名剔除：`darkfibr/artex-forensics`（总 star 77）。描述末尾是 “Blackfish Security LLC”，README 标题同样是 Blackfish Security LLC。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。搜索描述和话题没有 `llm`，不因 README 里出现的模型字样跨到 AI。漏洞复现步骤未写入正文。
  - 名称、话题和搜索描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`cindy-murray-39/acrobat-dc-desktop`（211；Acrobat DC 不等于 `dc-dc`）、`Statecraft-Labs/isometric-cities`（85；描述里的 DC 是华盛顿特区，不等于 `dc-dc`；“coding agent” 也不等于 `ai-agents`）、`FinancialPuzzle/AcrobatDC-Latest2026`（85；Adobe Acrobat 2026 的获取说明，Acrobat DC 不等于 `dc-dc`）、`gibletto/mvc2-naomi-dc`（58；街机游戏反编译，名称里的 dc 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-21 stars:>2`。HTTP 200。`total_count=108`，返回 5，规则保留 3，未命中 2。剩余配额 21。正文保留 `jacobvm04/slam-dunk`（152）、`mozihe/z-localization`（130）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（9），因为水位控制比 MOSFET 开关更贴近本领域。按总 star，本页顺序是 `mpc-plugin-builder-sdk`（193）、`slam-dunk`（152）、`FrankyRenderer`（143）、`z-localization`（130）、`SampQOL-OS`（127）。
  - 撞名剔除：`inmusic-software/mpc-plugin-builder-sdk`（总 star 193）。名称命中 `mpc`。描述和 README 写明这是给 Akai MPC 独立硬件做乐器和效果插件的 SDK，插件支持要求 MPC OS 3.10.1 或更新，不是模型预测控制，正文不收。描述里的 “AI coding agent” 是空格写法，不等于 `ai-agents`。
  - 名称和 topics 未命中：`mryx007/FrankyRenderer`（总 star 143；描述里的 MPC-BE 与 MPC-HC 是播放器兼容，不是强特征词）、`snarebes/SampQOL-OS`（总 star 127；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）。

### C. 领域常青（`pushed:>=2026-11-13 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-11-13 stars:>3`。HTTP 200。`total_count=1368`，返回 5，规则保留 5，清单类排除 0，未命中 0。剩余配额 28。`page=1`、`per_page=5`，本页是总结果里按总 star 排序后的第 1 到第 5 条。本查询正文：`ruvnet/RuView`（104639）、`raysan5/raylib`（35734）、`78/xiaozhi-esp32`（33473）、`lvgl/lvgl`（25207）、`arendst/Tasmota`（25000）。另有 1 条一行不在本页前 5：`makerspet/oomwoo`（13153，话题含 esp32，完整条目在自动控制）。`RuView` 话题含裸 mcp，搜索描述没有 llm，不跨到 AI。`xiaozhi-esp32` 的 README 点名 Qwen 与 DeepSeek，搜索描述和话题没有 llm，话题 mcp 不是 AI 关键词，不跨到 AI。`raylib` 话题里的 `riscv` 不等于 `risc-v`。`Tasmota` 的 README 写了 Modbus 桥，搜索话题没有 modbus，不另开一节。`OpenDTU` 话题含 esp32，但不在本页前 5，不跨节。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-11-13 stars:>3`。HTTP 200。`total_count=9833`，返回 5，规则保留 3，排除清单 1，未命中 1。剩余配额 26。正文保留 `huggingface/transformers`（169284）、`langgenius/dify`（161519）、`Comfy-Org/ComfyUI`（147676）。按总 star，本页顺序是 transformers、dify、langflow、ComfyUI、awesome-llm-apps。
  - 未命中：`langflow-ai/langflow`（总 star 156781；描述是 “AI-powered agents”，不等于 `ai-agents`）。它夹在 dify 与 ComfyUI 之间。
  - 清单类排除：`Shubhamsaboo/awesome-llm-apps`（总 star 145090；名称含 awesome，脚本已按合集排除。描述是代理和 RAG 应用合集，裸 rag 本来就不是本报告的关键词）。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-11-13 stars:>3`。HTTP 200。`total_count=33`，返回 5，规则保留 1，排除清单 0，未命中 4。剩余配额 24。`page=1` 是总结果里按总 star 排序后的第 1 到第 5 条。返回的星数是 2450、1025、805、284、224。规则留下的 1 条是图片处理命令行，剔除。本节没有完整条目。
  - 撞名剔除：`foresterre/imagineer`（总 star 224）。话题含 sic，描述写 Formerly 'sic'。README 写明这是 `image` 与 `imageproc` 的命令行前端，用来做图片转换和处理，不是碳化硅器件，正文不收。
  - 名称词边界未命中：`SickChill/sickchill`（2450；`sickchill` 不等于 `sic`）、`source-academy/sicp`（1025；SICP 教材源文，`sicp` 不等于 `sic`）、`SickGear/SickGear`（805；`SickGear` 不等于 `sic`）、`microsoft/Sico`（284；`Sico` 不等于 `sic`。话题含 llm，但不在 AI 常青前 5，不跨节）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-11-13 stars:>3`。HTTP 200。`total_count=422`，返回 5，规则保留 1，未命中 4。剩余配额 22。`page=1` 是总结果里按总 star 排序后的第 1 到第 5 条。规则留下的 1 条是公司后缀，剔除后本节没有完整条目。按总 star，本页顺序是 `Battery-Emulator`（3035）、`OpenDTU`（2211）、`Finbuckle.MultiTenant`（1634）、`dcm4che`（1466）、`moteus`（1392）。
  - 撞名剔除：`Finbuckle/Finbuckle.MultiTenant`（总 star 1634）。描述写 created and maintained by Finbuckle LLC，README 标题同样是 Finbuckle LLC，版本号写 10.1.3。这里的 LLC 是公司后缀，不是谐振变换器，正文不收。
  - 名称和 topics 未命中电力电子：`dalathegreat/Battery-Emulator`（3035；描述里的 solar inverters 是复数，词边界不等于 `inverter`）、`tbnobody/OpenDTU`（2211；描述里的 Inverters 是复数，不等于 `inverter`。话题含 esp32，不在嵌入式常青前 5，不跨节）、`dcm4che/dcm4che`（1466；DICOM 实现，名称里的 dcm 不等于 `dc-dc`）、`mjbots/moteus`（1392；描述是 “Brushless DC motor controller”，空格写法不等于 `motor-control`，DC 也不等于 `dc-dc`）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-11-13 stars:>3`。HTTP 200。`total_count=249`，返回 5，规则保留 5，未命中 0，排除清单 0。剩余配额 29。剔除播放器后，正文保留 `AtsushiSakai/PythonRobotics`（30951）、`makerspet/oomwoo`（13153）、`betaflight/betaflight`（11808）、`MichaelGrupp/evo`（4368）。`oomwoo` 在嵌入式一行。按总 star，本页顺序是 PythonRobotics、oomwoo、betaflight、MPC-BE、evo。本次响应头的剩余配额是 29，前一条电力电子常青是 22，中间没有失败重试，按响应头原样记录。
  - 撞名剔除：`Aleksoid1978/MPC-BE`（总 star 4738）。名称命中 `mpc`。搜索描述写明这是 Windows 上的音视频播放器。本次 README API 返回 HTTP 200，标题是 Media Player Classic - Black Edition，确认是播放器，不是模型预测控制，正文不收。
  - `oomwoo` 的 README 仍写明现在不能按物料单组装，只能仿真。`betaflight` 的 README 写了 STM32 与实验性 ESP32，搜索话题没有这些词，不跨嵌入式。
