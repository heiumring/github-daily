# GitHub 领域日报 · 2026-10-29

生成时间：2026-10-29 07:35（北京时间）。数据拉取开始于 2026-10-29 07:35:35（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-29（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-22 及之后有推送、总 star > 3。轮换页 `page = (当年第 302 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，眼睛走 AirPlay，手走 USB HID，不用 Mac、开发者账号或越狱；近 30 天新建，总 star 4059。
2. [makerspet/oomwoo](https://github.com/makerspet/oomwoo) 开源扫地机器人，用二维激光雷达在本地建图导航，软件栈含 ROS 2 与 ESP32；README 写明现在能跑仿真，实机物料清单还没验证。领域常青本页，总 star 12845，没有 24 小时新增数据。
3. [okalachev/flix](https://github.com/okalachev/flix) 用通用零件从零做一架基于 ESP32 的四旋翼，固件走 MAVLink；README 写明样机已经能飞。领域常青本页，总 star 2399，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 14 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。嵌入式、AI、功率器件、电力电子电源、自动控制在这 14 条里都没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4059
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验台收成一个网页，能看实时引脚、跑交互模拟、读 esp-labs 固件和实验记录，界面有 11 种语言。
  - 领域：嵌入式 Embedded
  - 总 star：569
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：451
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：260
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在 Waveshare 1.75C 圆屏 ESP32 上做语音终端，接 Grok，屏幕有会眨眼的眼睛、字幕和朗读，仓库同时放固件和后端。
  - 领域：嵌入式 Embedded
  - 总 star：223

### AI

- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：4592
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4059。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：3147
- [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu)
  - 说明：把 AI 写出来的日语改成读起来自然的日语，作为给编程代理用的推敲技能。
  - 领域：AI
  - 总 star：2653
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：260。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 驱动直流泵的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：8。

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室开源了 2026 年 RoboMaster 超级对抗赛哨兵的定位。README 写明这是 ROS 2 激光惯性定位栈，含里程计、点云建图、先验地图定位和重定位，示例传感器是 Livox Mid-360，也可以接 UWB。
  - 领域：自动控制 Control
  - 总 star：104
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；网站、组装预览和带价格的零件表已经公开，CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：101
- [prohurtz/BSB-SLAM](https://github.com/prohurtz/BSB-SLAM)
  - 说明：让 Bigscreen Beyond 头显用一颗 Xvisio XR50 SLAM 相机自己定位，这样 Lighthouse 基站可以收起来，并带 SteamVR 驱动和桌面设置程序。
  - 领域：自动控制 Control
  - 总 star：32
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino 做水箱水位控制实验：超声波测水位，市电泵走固态继电器，直流泵走 MOSFET，带通断、P 和 PI，以及按水箱和泵参数来的 MATLAB 应用和 Simulink。
  - 领域：自动控制 Control
  - 总 star：8

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 3。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的固件源码，跑在 STM32 上，覆盖 NFC、RFID、红外和 Sub-GHz，用来改这台多功能工具的系统软件。
  - 领域：嵌入式 Embedded
  - 总 star：16795
- [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder)
  - 说明：给 ESP32 准备的一套 Wi-Fi 和蓝牙攻防工具，用来在这块芯片上做无线扫描和安全实验。
  - 领域：嵌入式 Embedded
  - 总 star：12925
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：12845。
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用配置文件控制 ESP32、ESP8266、BK72xx 和 RP2040，再接到家庭自动化系统，用来远程管这些板子。
  - 领域：嵌入式 Embedded
  - 总 star：11977
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给 xiaozhi-esp32 语音设备提供后端，用来搭起能控制这些 ESP32 设备的服务器。
  - 领域：嵌入式 Embedded
  - 总 star：11073
- [okalachev/flix](https://github.com/okalachev/flix) — 见下方「自动控制 Control」完整条目。话题含 esp32 与 firmware，此处不展开。领域：嵌入式 Embedded。总 star：2399。

### AI

- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
  - 说明：给 AI 代理一个命令行，用来读和搜索 Twitter、Reddit、YouTube、GitHub、Bilibili 和小红书，按描述不收取各平台 API 费用。
  - 领域：AI
  - 总 star：105603
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：在 Python 里做张量和动态神经网络，带 GPU 加速，话题含自动求导，用来写深度学习训练代码。
  - 领域：AI
  - 总 star：105153
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
  - 说明：给编程代理补上页面审美：先定美术方向和参考图，再用浏览器对照检查，用来改掉千篇一律的生成界面。
  - 领域：AI
  - 总 star：104421
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
  - 说明：记下代理在每次会话里做了什么，压缩后在以后的会话里把相关上下文注回去，让 Claude Code、Codex 等代理跨会话接着干活。
  - 领域：AI
  - 总 star：104030
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2173。

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整常青仓库。返回的 5 条里，只有磷酸铁锂 UPS 命中功率器件话题，它同时带 `power-supply`，完整说明写在下方「电力电子电源 Power Supply」。其余 4 条名称按词边界都不等于 `sic`。

- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：15。

### 电力电子电源 Power Supply

- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：用 ESPHome 经串口或蓝牙监测并控制极空电池管理系统（JK-BMS），用来看电芯并下发控制。
  - 领域：电力电子电源 Power Supply
  - 总 star：1041
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 和网络设备做的 12V 磷酸铁锂 UPS。描述记录了 2026-05-06 的一次整段断电验证：断电 217 分钟，放出 4.18 Ah / 53.3 Wh，并按电压斜率触发优雅关机。
  - 领域：电力电子电源 Power Supply
  - 总 star：15

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：可自行组装的开源扫地机器人，用二维激光雷达在本地建图和导航，软件含 ROS 2、Arduino 和 ESP32，日常功能不依赖云端。README 写明现在能跑的是仿真，实机物料清单还没在真机上验证完。
  - 领域：自动控制 Control
  - 总 star：12845
- [SteveMacenski/slam_toolbox](https://github.com/SteveMacenski/slam_toolbox)
  - 说明：在 ROS 里做二维 SLAM，面向零售、仓库这类可能很大的地图，并能在已保存的位姿图上继续建图。README 写明它是当前在维护的 ROS 2 SLAM 库。
  - 领域：自动控制 Control
  - 总 star：2696
- [okalachev/flix](https://github.com/okalachev/flix)
  - 说明：用通用零件从零做一架基于 ESP32 的四旋翼，Arduino 固件经 MAVLink 走 Wi-Fi 或 ESP-NOW，并带 Gazebo 仿真。README 写明样机已经能飞，定位是教学和研究。
  - 领域：自动控制 Control
  - 总 star：2399
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：从 2005 年持续开发的 C++ 移动机器人框架，话题覆盖 SLAM、地图、计算机视觉、粒子滤波和运动估计，用来写移动机器人程序。
  - 领域：自动控制 Control
  - 总 star：2173
- [ShisatoYano/AutonomousVehicleControlBeginnersGuide](https://github.com/ShisatoYano/AutonomousVehicleControlBeginnersGuide)
  - 说明：用 Python 示例和文档讲自动驾驶里的标定、定位、建图、检测跟踪和路径规划，给初学者看控制算法和软件结构。
  - 领域：自动控制 Control
  - 总 star：1922

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`prohurtz/BSB-SLAM`、`makerspet/oomwoo`、`okalachev/flix`、`MRPT/mrpt`、`mozihe/z-localization`、`SteveMacenski/slam_toolbox`。这 6 次是核心接口，不计入上面 11 次搜索配额。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 14 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`HKUDS/DeepTutor`（47916，2376）、`Nutlope/hallmark`（40659，2109；描述里的 AI 是弱词）、`elayadesign/ai-design-skills`（11071，1938；描述为空，名称里的 ai 是弱词）、`togg53192-cmd/jailbreaks`（7046，1478；描述是 “LIST OF ALL MY JAILBREAKS”，没有领域词，脚本的清单规则也未命中）、`pbakaus/impeccable`（92565，1471；描述里的 AI 是弱词）、`hmjz100/LinkSwift`（34512，1380）、`obra/superpowers`（307419，1096；描述里的 agentic 是弱词）、`JetBrains/thinkrail`（5006，1075）、`nightly-labs/openbot`（3224，1053；描述里的 AI teammates 是弱词）、`makecindy/cindy`（8065，740；描述里的 AI Agent 是弱词）、`ruvnet/RuView`（101009，596；页面没有 topics，描述没有强特征词）、`xiaolai/the-craft-of-selfteaching`（18480，295）、`expo/skills`（3554，216；描述里的 AI agent 是弱词）、`macro-inc/macro`（5404，106；描述里的 agents 不是 `ai-agents`）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-29 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-29 stars:>2`。`total_count=436`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4059）、`agharsallah/esp-labs-web`（569）、`Adolanium/hermes-gadget-sdk`（451）、`raullenchai/esp32-thinks`（260）、`Liu-zhongxian/zongzhu-bot`（223）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单或 awesome 合集，正文保留。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-29 stars:>2`。`total_count=2445`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `QingYunA/answer-me-with-html`（4592）、`Leonxlnx/earshot`（3147）、`nanaism/yomiyasu`（2653）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`openfilm/openfilm`（总 star 3362；描述里的 AI video agent 是弱词）、`oil-oil/oil-ui`（总 star 2456；描述里的 AI agents 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-29 stars:>2`。`total_count=3`，返回 3，规则保留 2，未命中 1。剩余配额 9。本查询只有 3 条满足条件，所以不足 5 条。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 8）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-29 stars:>2`。`total_count=73`，返回 5，规则保留 0。剩余配额 7。正文写「本日无新项目」。
  - 名称、话题和描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`4DCodeBench/4DCodeBench`（195）、`CompaLarios18/MH4UltimateDC`（74）、`two-delta/DCOCO`（55；描述为空）、`Lida-V/3DCharaMakeSkills-Lida`（54）、`meztinos515/Acrobat-Pro-DC`（36；描述是 PDF 工具）。检索词 `dc-dc` 在搜索侧会撞上仓库名或 README 里的 DC。名称里能看到 DC 的是 `MH4UltimateDC`、`DCOCO`、`Acrobat-Pro-DC`。`4DCodeBench` 与 `3DCharaMakeSkills-Lida` 的名称和描述里没有这些词，命中点不在接口返回的名称、话题和描述中。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-29 stars:>2`。`total_count=58`，返回 5，规则保留 4，未命中 1。剩余配额 6。正文保留 `mozihe/z-localization`（104）、`TrentIndeed/kinetiqgym`（101）、`prohurtz/BSB-SLAM`（32）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（8），因为水位控制比 MOSFET 开关更贴近本领域。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 75）。话题含 `ros2` 与 `slam`，描述写明是机器人开发自学课程地图和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。
  - 名称和 topics 未命中：`lbgos/rift-s-linux`（32；描述里的 SLAM 是空格写法，不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-22 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-22 stars:>3`。`total_count=1191`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。正文完整条目 4 条：`flipperdevices/flipperzero-firmware`（16795）、`justcallmekoko/ESP32Marauder`（12925）、`esphome/esphome`（11977）、`xinnan-tech/xiaozhi-esp32-server`（11073）。`makerspet/oomwoo`（12845）话题同时含 `esp32`、`ros2` 与 `slam`，完整条目在自动控制，本节一行。`okalachev/flix` 来自自动控制检索，话题含 `esp32` 与 `firmware`，本节再一行。`xiaozhi-esp32-server` 话题含 `mcp-server`，裸 `mcp` 不是 AI 关键词，不跨到 AI。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-22 stars:>3`。`total_count=8802`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 6。正文保留 `Panniantong/Agent-Reach`（105603；话题 `llm-tools` 按词边界计入 `llm`）、`pytorch/pytorch`（105153；仓库名 `pytorch`）、`Leonxlnx/taste-skill`（104421；话题 `ai-agents`）、`thedotmack/claude-mem`（104030；话题 `ai-agents`）。另有 1 条跨领域一行：`MRPT/mrpt`（2173），来自自动控制检索，话题含 `computer-vision`。
  - 未命中：`nexu-io/open-design`（总 star 104638；描述里的 AI agents 是弱词）。名称和 topics 都没有领域关键词。它夹在本页 `pytorch/pytorch` 与 `Leonxlnx/taste-skill` 之间，所以本页按总 star 不是连续的 5 个命中仓库。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-22 stars:>3`。`total_count=24`，返回 5，规则保留 1，未命中 4。剩余配额 5。`page=3`、`per_page=5`，本页返回满 5 条。规则保留的 1 条是 `wkcollis1-eng/DIY-LiFePO4-UPS`（15；话题 `mosfet` 与 `power-supply`），更贴近电力电子电源，完整条目在那边，本节一行。
  - 名称按词边界不等于 `sic`，也没有功率器件话题：`opencad-abu/SiCo`（26；描述是集成电路设计助手）、`ducroo/SICTIC-AI`（14；描述写明是瑞士商业天使俱乐部 SICTIC）、`Reinazhard/guacamole_sickness`（13；`sickness` 不等于 `sic`）、`linuxserver/docker-sickgear`（12；描述为空，`sickgear` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-22 stars:>3`。`total_count=385`，返回 5，规则保留 1，未命中 4。剩余配额 4。正文保留 `syssi/esphome-jk-bms`（1041；话题 `jikong-bms` 按词边界计入 `bms`，描述含 `JK-BMS`）。搜索话题没有 `esp32`，描述写的是 ESPHome，不跨到嵌入式。另有 1 条完整条目来自功率器件检索：`wkcollis1-eng/DIY-LiFePO4-UPS`（15）。
  - 名称和 topics 未命中：`dcnetio/web-dc-api`（817）、`NVIDIA/DCGM`（810）、`dcs-liberation/dcs_liberation`（800）、`decred/dcrd`（775）。检索词 `dc-dc` 撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-22 stars:>3`。`total_count=239`，返回 5，规则保留 4，清单类排除 1。剩余配额 8。正文保留 `SteveMacenski/slam_toolbox`（2696）、`okalachev/flix`（2399）、`MRPT/mrpt`（2173）、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`（1922）。另有 1 条完整条目来自嵌入式检索：`makerspet/oomwoo`（12845），因为扫地机的 ROS 2 / 激光 SLAM 比 ESP32 话题更贴近本领域。`flix` 同时话题含 `esp32`，嵌入式一节一行。`MRPT/mrpt` 同时话题含 `computer-vision`，AI 一节一行。`AutonomousVehicleControlBeginnersGuide` 是示例代码和算法文档，不是公开课清单或 awesome 合集，正文保留。
  - 清单类剔除：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2158）。话题含 `slam`，仓库是 NeRF 与 3D 高斯 SLAM 论文合集，不进正文。
