# GitHub 领域日报 · 2026-11-02

生成时间：2026-11-02 07:32（北京时间）。数据拉取开始于 2026-11-02 07:32:53（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-03（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-26 及之后有推送、总 star > 3。轮换页 `page = (当年第 306 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [beenuar/AiSOC](https://github.com/beenuar/AiSOC) 把安全设备的遥测收成可审计的调查：语言模型代理负责分诊，每一步留记录，动作要人批准才发出去；Trending 上 24 小时新增 star 436，总 star 6193。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句话，助手就在一块后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 3794，没有 24 小时新增数据。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，眼睛走 AirPlay，手走 USB HID，不用 Mac、开发者账号或越狱；近 30 天新建，总 star 4197，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 17 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

- [beenuar/AiSOC](https://github.com/beenuar/AiSOC)
  - 说明：自托管的安全运营台。安全工具的遥测进来以后先归一、关联成事件，再交给语言模型代理调查；代理的推理留档，提议的动作要人点头才会发到外部系统。描述里的 LLM-agent 按词边界计入 llm。
  - 领域：AI
  - 总 star：6193
  - 24 小时新增 star：436

嵌入式、功率器件、电力电子电源、自动控制在这 17 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4197
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验台收成一个网页，能看实时引脚、跑交互模拟、读 esp-labs 固件和实验记录，界面有 11 种语言。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：628
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：458
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：260
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在 Waveshare 1.75C 圆屏 ESP32 上做语音终端，接 Grok，屏幕有会眨眼的眼睛、字幕和朗读，仓库同时放固件和后端。
  - 领域：嵌入式 Embedded
  - 总 star：240

### AI

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4197。
- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块单独的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。
  - 领域：AI
  - 总 star：3794
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：3442
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给自己要发布的程序加一层防护，让自动做逆向的语言模型代理耗在诱饵和资源上限上，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。
  - 领域：AI
  - 总 star：1821
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：260。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 开关直流泵的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：8。

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室开源了 2026 年 RoboMaster 超级对抗赛哨兵的定位。README 写明这是 ROS 2 激光惯性定位栈，能做里程计、点云建图、先验地图定位、回环和重定位，也可接 UWB；示例传感器是 Livox Mid-360。
  - 领域：自动控制 Control
  - 总 star：116
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用非均匀 B 样条做多传感器里程计，激光惯导、视觉和腿式运动学可以放在一套估计里，还能选带回环后的全局修正，并按实时约束来做。
  - 领域：自动控制 Control
  - 总 star：38
- [prohurtz/BSB-SLAM](https://github.com/prohurtz/BSB-SLAM)
  - 说明：给 Bigscreen Beyond 头显接上 Xvisio XR50 相机，让头显自己做定位，这样不用再摆 Lighthouse 基站；仓库带 SteamVR 驱动和负责安装的桌面程序。
  - 领域：自动控制 Control
  - 总 star：36
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：一套水位控制实验：水箱、超声波测距，市电泵走固态继电器，或者直流泵用 MOSFET 开关；控制律有通断、P 和 PI，并带一个按这台水箱和泵标定的 MATLAB 程序。水位控制比一只 MOSFET 开关更贴近本领域。
  - 领域：自动控制 Control
  - 总 star：8

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件源码，话题含 stm32。
  - 领域：嵌入式 Embedded
  - 总 star：16817
- [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder)
  - 说明：跑在 ESP32 上的一套 Wi-Fi 与蓝牙工具固件，作者写明进攻和防御两类都能用。
  - 领域：嵌入式 Embedded
  - 总 star：12968
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：12927。
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用配置文件而不是手写固件去控制 ESP32、ESP8266、BK72xx 和 RP2040，再交到家庭自动化系统里远程管。
  - 领域：嵌入式 Embedded
  - 总 star：12001
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给小智 ESP32 硬件配的后端，用来自己搭设备控制服务；README 写明支持 MQTT+UDP、WebSocket、声纹识别和知识库。话题 `mcp-server` 不是 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：11116
- [okalachev/flix](https://github.com/okalachev/flix) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：2426。
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：709。

### AI

- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：把 Gemini 放进终端里用的开源代理。
  - 领域：AI
  - 总 star：108655
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
  - 说明：一组给编程代理的技能，用美术方向、参考图和浏览器检查来避免生成千篇一律的页面。
  - 领域：AI
  - 总 star：107746
- [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
  - 说明：《Build a Large Language Model (From Scratch)》的官方代码，用 PyTorch 从头实现、预训练并微调一个类似 GPT 的模型。这是一本书的配套仓库，不是公开课清单。
  - 领域：AI
  - 总 star：107650
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
  - 说明：给代理一条命令，去读和搜索 Twitter、Reddit、YouTube、GitHub、Bilibili 和小红书，不必为这些平台的官方 API 付费。话题 `llm-tools` 按词边界计入 llm。
  - 领域：AI
  - 总 star：107593
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2173。

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整常青仓库。12V 磷酸铁锂备用电源的完整说明写在下方「电力电子电源 Power Supply」。

- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：15。

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：把阳光电源逆变器接到 Home Assistant，覆盖 SH RT、SHx RS、SH K 和 SxT 几个系列，通信走 Modbus。
  - 领域：电力电子电源 Power Supply
  - 总 star：709
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 和网络设备做的 12V 磷酸铁锂备用电源。描述写明 2026-05-06 有过一次完整停电验证：交流断开 217 分钟，送出 4.18 Ah / 53.3 Wh，并在电压悬崖前提前关机。
  - 领域：电力电子电源 Power Supply
  - 总 star：15

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：打算做成能自己 3D 打印、用树莓派和二维激光雷达在本地建图清扫的扫地机，软件走 ROS 2。README 写明现在还不能照着装出实物，今天只能跑仿真。
  - 领域：自动控制 Control
  - 总 star：12927
- [okalachev/flix](https://github.com/okalachev/flix)
  - 说明：用通用零件和 ESP32 从零做一台四旋翼。README 写明固件是不到两千行的 Arduino 代码，用 MAVLink 经 Wi-Fi 或 ESP-NOW 遥控，并带 Gazebo 仿真；作者给出了实飞视频。飞行控制比「用了哪块芯片」更贴近本领域。
  - 领域：自动控制 Control
  - 总 star：2426
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：马拉加大学从 2005 年维护至今的移动机器人 C++ 工具箱。README 写明覆盖蒙特卡洛定位、粒子滤波、占据栅格和路径规划。
  - 领域：自动控制 Control
  - 总 star：2173
- [ShisatoYano/AutonomousVehicleControlBeginnersGuide](https://github.com/ShisatoYano/AutonomousVehicleControlBeginnersGuide)
  - 说明：把自动驾驶里的定位、建图、规划和跟踪拆成可以单独跑的 Python 示例。README 写明这是给初学者看的示例代码，作者打算以后收成一本技术书，不是公开课清单或 awesome 合集。
  - 领域：自动控制 Control
  - 总 star：1928

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`beenuar/AiSOC`、`wangzan101/Mika`、`makerspet/oomwoo`、`prohurtz/BSB-SLAM`、`ASIG-X/RESPLE2`、`mozihe/z-localization`、`MRPT/mrpt`、`okalachev/flix`、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`、`qybaihe/bla`、`rasbt/LLMs-from-scratch`、`Panniantong/Agent-Reach`、`xinnan-tech/xiaozhi-esp32-server`。这 13 次是仓库 README 接口，不计入上面 11 次搜索配额。`esp32-iphone-agent`、`esp-labs-web`、`hermes-gadget-sdk`、`esp32-thinks`、`zongzhu-bot`、`earshot`、`gemini-cli`、`taste-skill`、`esphome`、`flipperzero-firmware`、水位实验和 Sungrow 的说明没有超出搜索描述。`DIY-LiFePO4-UPS` 的 217 分钟、4.18 Ah 和 53.3 Wh 来自搜索描述，不是估算。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 17 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`beenuar/AiSOC`（总 star 6193，stars today 436；描述含 LLM-agent）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`pingdotgg/t3code`（37856，3100；描述为空）、`thedotmack/claude-mem`（109177，1527；描述里的 AI 是弱词）、`anomalyco/hex`（3222，1329；本地语音听写）、`Donchitos/Claude-Code-Game-Studios`（32214，970；描述是 “49 AI agents”，空格写法不等于 `ai-agents`）、`Renhuai123/ziwei-doushu`（13060，953）、`milind-soni/OpenMausBot`（10484，919）、`lightpanda-io/browser`（40074，827；描述里的 AI 是弱词）、`togg53192-cmd/jailbreaks`（12916，730；描述是一份 jailbreak 清单，没有领域词；脚本清单规则匹配的是 curated list / a list of / interview guide，这条未标成清单）、`shiyu-coder/Kronos`（45344，611；金融市场基础模型，没有 llm）、`patchy631/ai-engineering-hub`（40191，573；“LLMs” 不等于 llm，RAG 与 AI agent 是弱词）、`cjpais/Handy`（36506，383；离线语音转文字）、`public-apis/public-apis`（494548，298；免费 API 合集，没有领域词）、`FlashML-org/FreeToken`（15372，232；本地跑大模型，描述没有 llm 这个词）、`CopilotKit/OpenBot`（9498，178；描述里的 AI coworkers 是弱词）、`hyprwm/Hyprland`（39347，91）、`kornia/kornia`（11765，88；“Computer Vision” 是空格，不等于 `computer-vision`；Spatial AI 是弱词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-03 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-03 stars:>2`。`total_count=435`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4197）、`agharsallah/esp-labs-web`（628）、`Adolanium/hermes-gadget-sdk`（458）、`raullenchai/esp32-thinks`（260）、`Liu-zhongxian/zongzhu-bot`（240）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。`hermes-gadget-sdk` 话题没有 `llm`，不跨到 AI。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-03 stars:>2`。`total_count=2475`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `wangzan101/Mika`（3794）、`Leonxlnx/earshot`（3442）、`qybaihe/bla`（1821）。另有 2 条跨领域一行：`esp32-iphone-agent`（4197）、`esp32-thinks`（260），来自嵌入式检索。这两条话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`openfilm/openfilm`（总 star 4091；描述里的 AI video agent 是弱词）、`CopilotKit/OpenDuet`（总 star 1789；描述里的 AI agent 是弱词）。名称和 topics 都没有领域关键词。`openfilm` 夹在 `Mika` 与 `earshot` 之间，所以本页按总 star 不是连续的 3 个命中仓库。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-03 stars:>2`。`total_count=4`，返回 4，规则保留 2，未命中 2。剩余配额 9。本查询只有 4 条满足条件，所以不足 5 条。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 8）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`aswin-code513/First-Sick-First-Served`（3）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`First-Sick` 与 `Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-03 stars:>2`。`total_count=65`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称、话题和描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`SpawnEmancipate/vxxzgfby`（259；描述把 Acrobat Pro DC 当成可分发的安装包，DC 不等于 `dc-dc`）、`CompaLarios18/MH4UltimateDC`（87）、`two-delta/DCOCO`（56；描述为空）、`Lida-V/3DCharaMakeSkills-Lida`（55）、`leftamber/CEXTrader-Grid-Dca-Automation-Bot-Platform`（52；描述里的 DCA 不等于 `dc-dc`）。名称里能看到 DC 的是前两条和 `DCOCO`。`3DCharaMakeSkills-Lida` 的名称和描述里没有这些词，命中点不在接口返回的名称、话题和描述中。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-03 stars:>2`。`total_count=65`，返回 5，规则保留 4，未命中 1。剩余配额 7。正文保留 `mozihe/z-localization`（116）、`ASIG-X/RESPLE2`（38）、`prohurtz/BSB-SLAM`（36）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（8），因为水位控制比 MOSFET 开关更贴近本领域。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 85）。话题含 `ros2` 与 `slam`，描述写明是机器人开发自学课程地图和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。
  - 名称和 topics 未命中：`lbgos/rift-s-linux`（总 star 35）。描述里的 “Basalt SLAM” 是空格写法，不等于 `slam`。它排在本页最后，所以前面 4 条规则命中在星数上是连续的，其中 `robotics-roadmap` 再被人工剔除。

### C. 领域常青（`pushed:>=2026-10-26 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-26 stars:>3`。`total_count=1227`，返回 5，规则保留 5，清单类排除 0。剩余配额 8。正文完整条目 4 条来自本查询：`flipperdevices/flipperzero-firmware`（16817）、`justcallmekoko/ESP32Marauder`（12968）、`esphome/esphome`（12001）、`xinnan-tech/xiaozhi-esp32-server`（11116）。`makerspet/oomwoo`（12927）话题同时含 `esp32`、`ros2`、`slam`，扫地和定位更贴近自动控制，完整条目在自动控制，本节一行。`okalachev/flix`（2426）来自自动控制检索，话题含 `esp32`，本节一行。`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（709）来自电力电子检索，话题含 `modbus`，本节一行。`xiaozhi-esp32-server` 的 README 提到 MCP 接入点，搜索话题是 `mcp-server`，不是 AI 关键词，不跨到 AI。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-26 stars:>3`。`total_count=8933`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 3。正文保留 `google-gemini/gemini-cli`（108655；话题 `ai-agents`）、`Leonxlnx/taste-skill`（107746；话题 `ai-agents`）、`rasbt/LLMs-from-scratch`（107650；话题 `llm` 与 `pytorch`，描述含 LLM）、`Panniantong/Agent-Reach`（107593；话题 `llm-tools` 按词边界计入 llm）。`MRPT/mrpt`（2173）来自自动控制检索，话题含 `computer-vision`，本节一行。
  - 未命中：`nexu-io/open-design`（总 star 105339；描述里的 AI Design Agent 是弱词）。名称和 topics 都没有领域关键词。它排在本页最后，所以前面 4 条按总 star 是连续的。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-26 stars:>3`。`total_count=25`，返回 5，规则保留 2，未命中 2。剩余配额 9。`page=3`、`per_page=5`，本页返回满 5 条，对应总结果里的第 11 到第 15 条，不是失败。规则保留的 2 条经人工处理后，没有以功率器件为最贴近领域的完整条目。
  - `epilys/sic`（总 star 27）：标签聚合的链接社区，名称撞上 `sic`，与碳化硅器件无关，正文不收。
  - `wkcollis1-eng/DIY-LiFePO4-UPS`（总 star 15）：话题含 `mosfet` 与 `power-supply`。备用电源比一只 MOSFET 更贴近电力电子，完整条目在电力电子，本节一行。
  - `JacobJandon/Sicry`（总 star 19）：搜索把名称里的 Sicry 当成 `sic` 的子串召回。分类按词边界不等于 `sic`。话题含 `llm` 与 `ai-agents`，但不在 AI 常青前 5，不跨节。
  - 名称和 topics 未命中：`ducroo/SICTIC-AI`（14；`SICTIC` 不等于 `sic`）、`linuxserver/docker-sickgear`（12；描述为空，`sickgear` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-26 stars:>3`。`total_count=402`，返回 5，规则保留 1，未命中 4。剩余配额 9。正文完整条目为 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（709）。`DIY-LiFePO4-UPS`（15）来自功率器件检索，话题含 `power-supply`，完整条目在本节。Sungrow 同时话题含 `modbus`，嵌入式一节一行。本页前 4 条都是 DC 撞名，所以 Sungrow 不是本页星数最高的返回项。
  - 名称和 topics 未命中：`dcnetio/web-dc-api`（817）、`NVIDIA/DCGM`（811；数据中心 GPU 管理）、`dcs-liberation/dcs_liberation`（801）、`decred/dcrd`（775）。名称里的 DC 不等于 `dc-dc`。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-26 stars:>3`。`total_count=215`，返回 5，规则保留 3，未命中 1，清单类排除 1。剩余配额 8。正文保留 `okalachev/flix`（2426）、`MRPT/mrpt`（2173）、`ShisatoYano/AutonomousVehicleControlBeginnersGuide`（1928）。`makerspet/oomwoo`（12927）来自嵌入式检索，话题含 `ros2` 与 `slam`，完整条目在本节。`flix` 同时话题含 `esp32`，嵌入式一节一行。`MRPT` 同时话题含 `computer-vision`，AI 一节一行。`awesome-NeRF-and-3DGS-SLAM` 夹在 `mrpt` 与自动驾驶示例之间，所以本页按总 star 不是连续的 3 个命中仓库。
  - 清单类剔除：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2157）。名称含 awesome，话题含 `slam`，脚本已标成清单，正文不收。
  - 名称和 topics 未命中：`nvidia-isaac/cuVSLAM`（总 star 1888）。名称 `cuVSLAM` 按词边界不等于 `slam`；描述里的 SLAM 是弱词，不在强特征词表里，正文不收。
