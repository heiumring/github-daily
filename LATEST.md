# GitHub 领域日报 · 2026-11-06

生成时间：2026-11-06 07:35（北京时间）。数据拉取开始于 2026-11-06 07:31:19（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-07（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-30 及之后有推送、总 star > 3。轮换页 `page = (当年第 310 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) 给智能体查企业数据加一层语义本体：指标在哪、定义是否一致、查询是否符合认证口径，并把出处一起返回，避免答得快但数字是错的；描述含 LLM，总 star 7244，24 小时新增 star 2707。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 7077，没有 24 小时新增数据。
3. [nv-tlabs/vipe](https://github.com/nv-tlabs/vipe) 从没有标定的原始视频估计相机内参、运动和接近米制的稠密深度，针孔、广角和全景都能用；本页常青按总 star 排在自动控制里，总 star 2171，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 15 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

### AI

- [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)
  - 说明：智能体查企业数据时，快不算对。这个库从已有元数据生成语义本体，告诉代理指标在哪、含义是否一致、该不该用、查询是否对得上认证定义，并把出处一并返回。README 写明结果可以通过命令行、API 和 MCP 交给各种代理框架。描述里的 LLM 是强特征词。
  - 领域：AI
  - 总 star：7244
  - 24 小时新增 star：2707

嵌入式、功率器件、电力电子电源、自动控制在这 15 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4440
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验收成一个网页，能看实时引脚、跑交互模拟、读固件和实验记录，界面有 11 种语言。README 写明目前是 32 个动手实验。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：669
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：280
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：262
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32-S3 上做语音终端。README 写明板子负责听和说，电脑上的后端决定这句话交给 Grok，还是在本机放歌、暂停和调音量；刷过补丁固件的小米智能音箱 Pro 也能接进来。
  - 领域：嵌入式 Embedded
  - 总 star：259

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。
  - 领域：AI
  - 总 star：7077
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4440。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵。代理已经能写出影片、演示和游戏的声音，却听不出按键廉价、撞击晚了 80 毫秒或配乐鼓错了地方。README 写明它把声音变成代理可以判断的证据，并且只在 CPU 上跑。
  - 领域：AI
  - 总 star：3991
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上资源上限和诱饵，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。README 写明这是保护自己软件的防御工具。
  - 领域：AI
  - 总 star：2436
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：262。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 开关直流泵的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：8。

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室 2026 年 RoboMaster 哨兵的定位栈。README 写明它跑在 ROS 2 上，用激光和惯性做里程计、点云建图、先验地图定位、回环和重定位，也可以接入 UWB 做位置辅助；实机和 rosbag 回放走同一套入口。
  - 领域：自动控制 Control
  - 总 star：122
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用非均匀 B 样条做多传感器里程计的状态估计。同一套框架覆盖激光惯性、激光视觉惯性、激光加腿部惯性，以及再加视觉的组合，并可做全局样条修正。README 写明这些组合都能实时跑，支持 ROS 2 Humble 和 Jazzy。
  - 领域：自动控制 Control
  - 总 star：50
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵走 MOSFET；固件里有通断、P 和 PI，并带溢流、干转和传感器保护，另有一套按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：8

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 3`，每页 5 条，本页是各查询按总 star 排序后的第 11 到第 15 条。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件源码。话题含 stm32 与 firmware，也列了红外、NFC、RFID 和 Sub-GHz。README 指向用户文档和开发者文档，没有另写硬件说明。
  - 领域：嵌入式 Embedded
  - 总 star：16843
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：12978。
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用一份 YAML 配置 ESP32、ESP8266、BK72xx 和 RP2040，再交给家庭自动化系统远程控制，不用为每块板各写一套固件。描述里的 ESP32 是强特征词。
  - 领域：嵌入式 Embedded
  - 总 star：12027
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给 xiaozhi-esp32 提供后端，用来搭起设备控制服务器。README 写明按小智通信协议实现，支持 MQTT+UDP、WebSocket、声纹识别和知识库。话题含 mcp-server，mcp 不是 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：11172
- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：把 ESP32 变成只在本地跑的 Wi-Fi 动作传感器。人在房间里走动会改变信号路径，它读这些变化并实时报动作，不用摄像头、麦克风或专用雷达。话题含 embedded；话题里的 `esp-32` 不等于 esp32，描述里的 ESP32 才计入。
  - 领域：嵌入式 Embedded
  - 总 star：9746
- [okalachev/flix](https://github.com/okalachev/flix) — 见下方「自动控制 Control」完整条目。话题含 esp32 与 firmware，此处不展开。领域：嵌入式 Embedded。总 star：2451。
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：711。

### AI

- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
  - 说明：给命令行里的编程代理补上它自己打不开的网站，搜索和阅读 X、Reddit、YouTube、GitHub、Bilibili 和小红书，一条命令，不另买各站 API。话题 `llm-tools` 按词边界计入 llm。
  - 领域：AI
  - 总 star：109201
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：把 Gemini 放进终端的开源代理。话题含 ai-agents。README 写明个人免费档已在 2026-06-18 迁到 Antigravity CLI，这个仓库现在面向 Gemini Code Assist 的标准版和企业版许可。
  - 领域：AI
  - 总 star：108740
- [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
  - 说明：这本书的官方代码，用 PyTorch 从零搭一个类似 GPT 的模型，覆盖预训练和微调。话题含 llm 与 pytorch。这是一本书的实现，不是公开课清单。
  - 领域：AI
  - 总 star：107875
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：Python 里的张量库，带自动求导和 GPU 加速，用来写和训练神经网络。名称 pytorch 计入。话题里没有 llm。
  - 领域：AI
  - 总 star：105167
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2173。

### 功率器件 Power Devices

- [SJTU-YONGFU-RESEARCH-GRP/MESD-MOSFET-Electrical-Simulation-Dataset](https://github.com/SJTU-YONGFU-RESEARCH-GRP/MESD-MOSFET-Electrical-Simulation-Dataset)
  - 说明：一套 MOSFET 电学仿真数据集，用多家工艺的 BSIM 模型扫出 I-V 和 C-V，覆盖 3 纳米到 350 纳米、不同偏压、温度和尺寸，给器件模型做对照基准。名称和描述里的 MOSFET 都计入。README 写明工艺名已替换，避免泄露代工厂信息。
  - 领域：功率器件 Power Devices
  - 总 star：18
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：16。

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：用 YAML 把阳光电源逆变器接进 Home Assistant，覆盖 SH*RT、SHx.RS、SH*K 和 SxT 等系列。话题含 inverter。README 写明一套 HACS 集成还在开发，现有 YAML 包继续可用。
  - 领域：电力电子电源 Power Supply
  - 总 star：711
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 主机和调制解调器做的 12 伏磷酸铁锂不间断电源。市电掉了继续供电，电池见底前让主机关机，来电后再自己恢复。README 写明用 MOSFET 理想二极管浮充电池，18 伏升压给主机，ESPHome 做安时计量。话题含 power-supply 与 mosfet；搜索话题没有 esp32，不跨到嵌入式。完整条目放在这里，功率器件一节一行带过。
  - 领域：电力电子电源 Power Supply
  - 总 star：16

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：可以自己做的开源扫地机器人，用二维激光建图并在家里自己走，常规功能不依赖云。话题含 ros2、slam 与 esp32。README 写明现在还不能按清单装出实机，今天只能跑仿真。扫地定位比 ESP32 话题更贴近本领域，嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：12978
- [okalachev/flix](https://github.com/okalachev/flix)
  - 说明：用通用零件从零做一架基于 ESP32 的四旋翼，固件用 Arduino 写，经 MAVLink 用手柄、遥控或手机控制，并带 Gazebo 仿真。话题含 flight-controller。README 写明它是给教学和研究用的，而且真的飞得起来。嵌入式一节一行带过。
  - 领域：自动控制 Control
  - 总 star：2451
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：从 2005 年维护至今的 C++ 移动机器人工具箱，定位、建图和位姿图优化都在里面。话题含 slam。README 写明 SLAM 部分包括蒙特卡洛定位、RBPF 和位姿图优化。话题还有 computer-vision，AI 一节一行带过。
  - 领域：自动控制 Control
  - 总 star：2173
- [nv-tlabs/vipe](https://github.com/nv-tlabs/vipe)
  - 说明：从没有标定的原始视频估计相机内参、运动和接近米制的稠密深度，针孔、广角和 360 度全景都能用。话题含 slam。README 在 2026-11 写了长视频流水线 ViPE-Long，默认用 MoGe v2 的关键帧深度。
  - 领域：自动控制 Control
  - 总 star：2171
- [ShisatoYano/AutonomousVehicleControlBeginnersGuide](https://github.com/ShisatoYano/AutonomousVehicleControlBeginnersGuide)
  - 说明：用 Python 示例代码讲自动驾驶里的定位、建图、检测、跟踪和路径跟踪，仓库自己把它写成给初学者的技术指南。话题含 slam。这是示例代码，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：1934

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`NVIDIA/auto-ontology`、`wangzan101/Mika`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Liu-zhongxian/zongzhu-bot`、`Leonxlnx/earshot`、`qybaihe/bla`、`marozols/SIC-existence`、`Samarth030312/arduino-water-level-control-lab`、`SJTU-YONGFU-RESEARCH-GRP/MESD-MOSFET-Electrical-Simulation-Dataset`、`wkcollis1-eng/DIY-LiFePO4-UPS`、`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`、`mozihe/z-localization`、`woolimi/robotics-roadmap`、`ASIG-X/RESPLE2`、`flipperdevices/flipperzero-firmware`、`makerspet/oomwoo`、`esphome/esphome`、`xinnan-tech/xiaozhi-esp32-server`、`francescopace/espectre`、`Panniantong/Agent-Reach`、`google-gemini/gemini-cli`、`rasbt/LLMs-from-scratch`、`okalachev/flix`、`MRPT/mrpt`、`nv-tlabs/vipe`、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`、`onehumanbeing/esp32-iphone-agent`、`raullenchai/esp32-thinks`。这 29 次是仓库 README 接口，不计入上面 11 次搜索配额。`esp32-iphone-agent`、`esp32-thinks`、`esphome` 和 `pytorch` 的说明没有超出搜索描述。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 15 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。正文只收 `NVIDIA/auto-ontology`（总 star 7244，stars today 2707；描述含 LLM）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`vercel-labs/agent-desktop`（16783，2173；描述是 “AI agents”，空格写法不等于 `ai-agents`）、`mattpocock/skills`（315161，2053）、`D4Vinci/Scrapling`（97917，1661）、`JiaFeiMiao-K-Cat/DiscImageStudio`（7246，977；描述为空）、`floci-io/floci`（30376，784）、`scenario-labs/skills`（3024，674；描述里的 AI agent 是弱词，MCP 不是 AI 关键词）、`garrytan/gstack`（139923，608）、`max-sixty/worktrunk`（11493，546；描述里的 AI agent 是弱词）、`Usagi-org/ai-goofish-monitor`（17502，242；描述里的 AI 是弱词）、`ConardLi/garden-skills`（14110，241）、`microsoft/VibeVoice`（55877，214；描述里的 Voice AI 是弱词）、`google/skills`（22350，199）、`vercel-labs/agent-browser`（45850，181；描述是 “AI agents”，空格写法不等于 `ai-agents`）、`lz4/lz4`（12362，16）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-07 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-07 stars:>2`。`total_count=431`，返回 5，规则保留 5，排除清单 0。剩余配额 8。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4440）、`agharsallah/esp-labs-web`（669）、`ngxson/esp32-usb-to-airprint`（280）、`raullenchai/esp32-thinks`（262）、`Liu-zhongxian/zongzhu-bot`（259）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。`esp32-usb-to-airprint` 只有名称和描述里的 esp32，接口 `created_at` 为 `2026-10-26T16:18:54Z`，北京时间是 2026-10-27 00:18。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-07 stars:>2`。`total_count=2495`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 8。正文保留 `wangzan101/Mika`（7077）、`Leonxlnx/earshot`（3991）、`qybaihe/bla`（2436）。这 3 条是本页星数连续的前 3。另有 2 条跨领域一行：`esp32-iphone-agent`（4440）、`esp32-thinks`（262），来自嵌入式检索。这两条话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`benjitaylor/skills`（总 star 2104；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）、`DenisSergeevitch/ex-ussr-kinship-research`（总 star 1979；描述是 “skill for AI agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-07 stars:>2`。`total_count=6`，返回 5，规则保留 2，未命中 3。剩余配额 7。`per_page=5`，第 6 条不在本次返回里，正文不猜测它是什么。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC。README 写明这是 Lean 对「任意有限维都存在 SIC-POVM」的形式化证明，与碳化硅器件无关，正文不收。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 8）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`Arafat-shuvo/Sicip-data-sciebce`（3；`Sicip` 不等于 `sic`）、`aswin-code513/First-Sick-First-Served`（3）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`First-Sick` 与 `Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-07 stars:>2`。`total_count=67`，返回 5，规则保留 0。剩余配额 5。正文写「本日无新项目」。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`Dreamyepruner97/gwffttqz`（317；描述声称提供 Acrobat Pro DC 的已激活副本，与电源无关，DC 不等于 `dc-dc`）、`Lida-V/3DCharaMakeSkills-Lida`（57）、`two-delta/DCOCO`（57；描述为空）、`leftamber/grid-dca-bot`（48；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（47；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-07 stars:>2`。`total_count=71`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `mozihe/z-localization`（122）、`ASIG-X/RESPLE2`（50）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（8），因为水位控制比 MOSFET 开关更贴近本领域。`SampQOL-OS` 与 `FrankyRenderer` 夹在 `robotics-roadmap` 和 `RESPLE2` 之间，所以剔除后本页按总 star 不是连续的 2 个命中仓库。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 93）。话题含 `ros2` 与 `slam`，README 写明是 57 讲自学课程和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。它排在 `z-localization` 与 `RESPLE2` 之间。
  - 名称和 topics 未命中：`snarebes/SampQOL-OS`（总 star 64；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）、`mryx007/FrankyRenderer`（总 star 51；描述里的 MPC-BE 是播放器兼容，不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-30 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-30 stars:>3`。`total_count=1293`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。`page=3`、`per_page=5`，本页是总结果里的第 11 到第 15 条。本查询正文完整条目 4 条：`flipperdevices/flipperzero-firmware`（16843）、`esphome/esphome`（12027）、`xinnan-tech/xiaozhi-esp32-server`（11172）、`francescopace/espectre`（9746）。`makerspet/oomwoo`（12978）同时话题含 `ros2` 与 `slam`，完整条目在自动控制，本节一行。另有 2 条一行来自其他领域的检索：`okalachev/flix`（2451，话题含 esp32 与 firmware）、`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（711，话题含 modbus）。`xiaozhi-esp32-server` 话题含 `mcp-server`，mcp 不是 AI 关键词，不跨到 AI。`espectre` 话题里的 `esp-32` 不等于 esp32。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-30 stars:>3`。`total_count=9068`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 9。正文保留 `Panniantong/Agent-Reach`（109201）、`google-gemini/gemini-cli`（108740）、`rasbt/LLMs-from-scratch`（107875）、`pytorch/pytorch`（105167）。`nexu-io/open-design` 夹在 `LLMs-from-scratch` 与 `pytorch` 之间，所以本页按总 star 不是连续的 4 个命中仓库。另有 1 条一行来自自动控制：`MRPT/mrpt`（2173，话题含 computer-vision）。`esp32-iphone-agent` 与 `esp32-thinks` 话题含 `llm`，但不在 AI 常青前 5，不从常青跨节；它们的一行在新项目里。
  - 未命中：`nexu-io/open-design`（总 star 106110；描述是 “with your team and AI agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-30 stars:>3`。`total_count=27`，返回 5，规则保留 2，未命中 3。剩余配额 9。`page=3` 返回满 5 条，是总结果里的第 11 到第 15 条。正文完整条目 1 条：`SJTU-YONGFU-RESEARCH-GRP/MESD-MOSFET-Electrical-Simulation-Dataset`（18）。`wkcollis1-eng/DIY-LiFePO4-UPS`（16）话题含 `mosfet` 与 `power-supply`，完整条目在电力电子，本节一行。两条 19 star 的未命中夹在前面，所以本页按总 star 不是连续的命中仓库。
  - 名称词边界未命中：`vfat-io/sickle-public`（19；`sickle` 不等于 `sic`）、`mira-x/SicMu`（19；`SicMu` 不等于 `sic`，描述是 Android 音乐播放器的分支）、`ducroo/SICTIC-AI`（14；`SICTIC` 不等于 `sic`，描述是瑞士商业天使俱乐部的 AI 引擎）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-30 stars:>3`。`total_count=402`，返回 5，规则保留 1，未命中 3。剩余配额 3。`page=3` 是总结果里的第 11 到第 15 条。正文保留 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（711），它是本页星数最低的一条。另有 1 条完整条目来自功率器件检索：`DIY-LiFePO4-UPS`（16），因为不间断电源比 MOSFET 开关更贴近本领域。另有 1 条命中了别的领域，但不在那个领域本页前 5，不跨节。
  - `wlcrs/huawei_solar`（总 star 942）：描述是 “Huawei Solar inverters”，复数 `inverters` 不等于 `inverter`，分类没有计入电力电子。话题含 `modbus`，但不在嵌入式常青前 5，不跨节。
  - 名称和 topics 未命中：`DCMTK/dcmtk`（917；DICOM 工具包，名称里的 dc 不等于 `dc-dc`）、`dcs-liberation/dcs_liberation`（801；DCS World 动态战役）、`decred/dcrd`（776；Decred 守护进程）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-30 stars:>3`。`total_count=226`，返回 5，规则保留 4，脚本清单类排除 1。剩余配额 4。正文保留 `okalachev/flix`（2451）、`MRPT/mrpt`（2173）、`nv-tlabs/vipe`（2171）、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`（1934）。另有 1 条完整条目来自嵌入式检索：`makerspet/oomwoo`（12978），因为扫地定位比 ESP32 话题更贴近本领域。`awesome-NeRF-and-3DGS-SLAM` 夹在 `vipe` 与自动驾驶示例之间，所以本页按总 star 不是连续的 4 个命中仓库。
  - 清单类剔除：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2159）。描述写明是 NeRF 与 3D Gaussian Splatting 论文清单，名称含 awesome。话题含 `slam`，脚本已按清单排除。
