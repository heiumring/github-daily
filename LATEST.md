# GitHub 领域日报 · 2026-11-04

生成时间：2026-11-04 07:31（北京时间）。数据拉取开始于 2026-11-04 07:31:45（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-05（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-28 及之后有推送、总 star > 3。轮换页 `page = (当年第 308 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句话，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 6032，没有 24 小时新增数据。
2. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块 7 美元的 ESP32 让视觉模型操作真 iPhone，眼睛走 AirPlay，手走 USB HID，不用 Mac、开发者账号或越狱；近 30 天新建，总 star 4302，没有 24 小时新增数据。
3. [ruvnet/RuView](https://github.com/ruvnet/RuView) 用普通 Wi-Fi 和低成本 ESP32 做人的存在、呼吸和心率检测，不用摄像头；本页常青按总 star 排在嵌入式首位，总 star 102247，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 13 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。

嵌入式、AI、功率器件、电力电子电源、自动控制在这 13 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4302
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验收成一个网页，能看实时引脚、跑交互模拟、读固件和实验记录，界面有 11 种语言。README 写明目前是 32 个动手实验。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：646
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：264
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：262
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在 Waveshare 1.75C 圆屏 ESP32 上做语音终端，接 Grok，屏幕有会眨眼的眼睛、字幕和朗读，仓库同时放固件和后端。
  - 领域：嵌入式 Embedded
  - 总 star：255

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 的例子是让它在后台打开微信、找到联系人并把消息发出去。
  - 领域：AI
  - 总 star：6032
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4302。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审，也能用代码做出声音，只在 CPU 上跑。README 写明它把一段声音变成代理可以判断的证据。
  - 领域：AI
  - 总 star：3752
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上资源上限和诱饵，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。
  - 领域：AI
  - 总 star：2060
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：262。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 开关直流泵的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：8。

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室开源了 2026 年 RoboMaster 超级对抗赛哨兵的定位。README 写明这是 ROS 2 激光惯性定位栈，能做里程计、点云建图、先验地图定位、回环和重定位，也可接 UWB；话题标明传感器是 Livox Mid-360。
  - 领域：自动控制 Control
  - 总 star：120
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用非均匀 B 样条做多传感器里程计。README 写明激光惯导、激光视觉惯导、激光腿式惯导，以及再加上视觉的组合，可以放在一套估计里，还能选全局样条修正，并按实时约束来做。搜索描述写的是可选回环修正。
  - 领域：自动控制 Control
  - 总 star：47
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：一套水位控制实验：水箱、超声波测距，市电泵走固态继电器，或者直流泵用 MOSFET 开关；控制律有通断、P 和 PI，并带一个按这台水箱和泵标定的 MATLAB 程序。水位控制比一只 MOSFET 开关更贴近本领域。
  - 领域：自动控制 Control
  - 总 star：8

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：用普通 Wi-Fi 做人的存在、呼吸和心率检测，不用摄像头或可穿戴设备。README 写明靠低成本 ESP32 采集信道状态信息。话题含 esp32 与 firmware，也含 awesome，但这是感知项目本身，不是合集。
  - 领域：嵌入式 Embedded
  - 总 star：102247
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：一套用来写游戏的 C 库，适合做原型和图形工具。README 写明它也面向嵌入式系统和教学。话题含 embedded 与 esp32，因此归入本领域。
  - 领域：嵌入式 Embedded
  - 总 star：35554
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：在 ESP32 上做语音聊天入口。README 写明唤醒后把语音交给 Qwen、DeepSeek 一类大模型，再用 MCP 控制喇叭、灯和 GPIO。搜索描述和话题没有 llm，话题里的 mcp 也不是 AI 关键词，不跨到 AI。
  - 领域：嵌入式 Embedded
  - 总 star：32555
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：给各种厂商的 MCU 和 MPU 做图形界面的开源库。README 写明没有外部依赖，典型界面大约只要 100 kB RAM。话题含 esp32、stm32 与 zephyr。
  - 领域：嵌入式 Embedded
  - 总 star：25084
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：给 ESP8266 和 ESP32 设备换上可本地控制的固件，用网页配置，支持 OTA，也能用定时器和规则做自动化。搜索描述还写了 MQTT、HTTP、串口和 KNX。
  - 领域：嵌入式 Embedded
  - 总 star：24960
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：12959。

### AI

- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
  - 说明：给智能体提供搜网页、抓网页和跟页面交互的接口，把结果整理成适合模型用的 Markdown 或 JSON。README 写明可以自己部署，也有托管服务。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：198324
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
  - 说明：一套让编程代理少写代码的技能。README 写明规则是只写任务需要的东西，不砍校验、错误处理、安全和可访问性。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：183709
- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：给文本、视觉、音频和多模态模型提供统一的模型定义，训练和推理都走这一份。话题含 llm、pytorch 与 transformer。
  - 领域：AI
  - 总 star：168505
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：做大模型应用的开源平台，把工作流、检索管道和代理放在同一处，可以从原型部署到自托管生产环境。话题含 llm。
  - 领域：AI
  - 总 star：160343

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整常青仓库。返回的 5 条都是 `sic` 的名称撞车（sickchill、sicp、Sico、SICK、siconos），与碳化硅器件无关，正文不收。

### 电力电子电源 Power Supply

本页剔除后为空。脚本按描述里的 `llc` 留下的 `Finbuckle/Finbuckle.MultiTenant` 是 .NET 多租户库，LLC 是公司后缀，不是谐振变换器，正文不收。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：用 Python 给出机器人算法的可运行示例，README 目录覆盖定位、建图、SLAM 和路径规划，并配有一本教材。这是算法实现，不是公开课链接清单。话题含 slam。
  - 领域：自动控制 Control
  - 总 star：30855
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：可以自己做的开源扫地机器人。README 写明用树莓派、3D 打印、二维激光雷达、ROS 2 和 Home Assistant，常规功能不依赖云；并写明现在还不能按清单装出实机，今天只能跑仿真。扫地定位比单独的 ESP32 话题更贴近本领域。
  - 领域：自动控制 Control
  - 总 star：12959
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：给各类无人机提供开源飞控固件，从竞速、花式到航拍、长航时、微型机和固定翼。README 写明本仓库是跑在飞控板上的那份固件。话题含 flight-controller。README 还列出 STM32 和实验性 ESP32，搜索话题没有这些词，不跨到嵌入式。
  - 领域：自动控制 Control
  - 总 star：11739
- [MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)
  - 说明：用来比较里程计和 SLAM 算法输出的轨迹。README 写明支持 TUM、KITTI、EuRoC，以及带位姿话题的 ROS 和 ROS 2 bag。
  - 领域：自动控制 Control
  - 总 star：4356

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`wangzan101/Mika`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Leonxlnx/earshot`、`qybaihe/bla`、`ruvnet/RuView`、`raysan5/raylib`、`78/xiaozhi-esp32`、`lvgl/lvgl`、`makerspet/oomwoo`、`mozihe/z-localization`、`ASIG-X/RESPLE2`、`betaflight/betaflight`、`AtsushiSakai/PythonRobotics`、`MichaelGrupp/evo`、`firecrawl/firecrawl`、`DietrichGebert/ponytail`。这 17 次是仓库 README 接口，不计入上面 11 次搜索配额。`esp32-iphone-agent`、`esp32-thinks`、`zongzhu-bot`、水位实验、`Tasmota`、`transformers` 和 `dify` 的说明没有超出搜索描述。`Tasmota` 的 README 还写了 Modbus，搜索话题没有 modbus，不跨到嵌入式以外的领域。`xiaozhi-esp32` 的 README 出现大模型名称，搜索描述和话题没有 llm，不跨到 AI。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 13 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`vercel-labs/agent-desktop`（12623，3792；描述是 “AI agents”，空格写法不等于 `ai-agents`；AI 是弱词）、`D4Vinci/Scrapling`（94741，1658）、`Donchitos/Claude-Code-Game-Studios`（34625，1181；描述是 “49 AI agents”，空格写法不等于 `ai-agents`）、`mattpocock/skills`（311403，1164）、`thedotmack/claude-mem`（111852，1138；描述里的 AI 是弱词）、`JustVugg/colibri`（47224，803；MoE 推理引擎，没有 llm）、`p-e-w/heretic`（38754，699；“language model” 不等于 llm）、`floci-io/floci`（28725，679）、`shiyu-coder/Kronos`（46501，503；金融市场基础模型，没有 llm）、`max-sixty/worktrunk`（10464，437；描述里的 AI agent 是弱词）、`anomalyco/hex`（4554，410；本地语音听写，没有 llm）、`Usagi-org/ai-goofish-monitor`（16333，204；名称和描述里的 AI 是弱词）、`spotify/portal-ai-plugins`（3029，94；描述为空，名称里的 ai 不是领域关键词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-05 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-05 stars:>2`。`total_count=430`，返回 5，规则保留 5，排除清单 0。剩余配额 8。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4302）、`agharsallah/esp-labs-web`（646）、`ngxson/esp32-usb-to-airprint`（264）、`raullenchai/esp32-thinks`（262）、`Liu-zhongxian/zongzhu-bot`（255）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。`esp32-usb-to-airprint` 只有名称和描述里的 esp32，接口 `created_at` 为 `2026-10-26T16:18:54Z`，北京时间是 2026-10-27 00:18。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-05 stars:>2`。`total_count=2442`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `wangzan101/Mika`（6032）、`Leonxlnx/earshot`（3752）、`qybaihe/bla`（2060）。这 3 条是本页星数连续的前 3。另有 2 条跨领域一行：`esp32-iphone-agent`（4302）、`esp32-thinks`（262），来自嵌入式检索。这两条话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`CopilotKit/OpenDuet`（总 star 1903；描述里的 AI agent 是弱词）、`cranebeaker/coop-anything`（总 star 1858；描述里的 AI agent 是弱词，MCP 不是 AI 关键词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-05 stars:>2`。`total_count=4`，返回 4，规则保留 2，未命中 2。剩余配额 9。本查询只有 4 条满足条件，所以不足 5 条。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 8）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`aswin-code513/First-Sick-First-Served`（3）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`First-Sick` 与 `Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-05 stars:>2`。`total_count=67`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`SteamDerrick/mwanrytl`（292；描述把 Acrobat Pro DC 当成可分发的安装包，DC 不等于 `dc-dc`）、`CompaLarios18/MH4UltimateDC`（95）、`Lida-V/3DCharaMakeSkills-Lida`（57）、`two-delta/DCOCO`（56；描述为空）、`leftamber/grid-dca-bot`（48；描述里的 DCA 不等于 `dc-dc`）。名称里能看到 DC 的是 `MH4UltimateDC` 和 `DCOCO`。`3DCharaMakeSkills-Lida` 的名称和描述里没有这些词，命中点不在接口返回的名称、话题和描述中。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-05 stars:>2`。`total_count=66`，返回 5，规则保留 3，未命中 2。剩余配额 7。正文保留 `mozihe/z-localization`（120）、`ASIG-X/RESPLE2`（47）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（8），因为水位控制比 MOSFET 开关更贴近本领域。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 87）。话题含 `ros2` 与 `slam`，描述写明是机器人开发自学课程地图和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。它排在 `z-localization` 与 `RESPLE2` 之间。
  - 名称和 topics 未命中：`snarebes/SampQOL-OS`（总 star 40；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）、`lbgos/rift-s-linux`（总 star 38；描述里的 “Basalt SLAM” 是空格写法，不等于 `slam`）。

### C. 领域常青（`pushed:>=2026-10-28 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-28 stars:>3`。`total_count=1246`，返回 5，规则保留 5，清单类排除 0。剩余配额 4。`page=1`、`per_page=5`，本页是总结果里的第 1 到第 5 条。正文完整条目 5 条都来自本查询：`ruvnet/RuView`（102247）、`raysan5/raylib`（35554）、`78/xiaozhi-esp32`（32555）、`lvgl/lvgl`（25084）、`arendst/Tasmota`（24960）。`makerspet/oomwoo`（12959）来自自动控制检索，话题含 `esp32`，本节一行。`RuView` 话题含 `awesome`，README 写的是 Wi-Fi 感知平台，不是合集，正文保留。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-28 stars:>3`。`total_count=9032`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 3。正文保留 `firecrawl/firecrawl`（198324）、`DietrichGebert/ponytail`（183709）、`huggingface/transformers`（168505）、`langgenius/dify`（160343）。这 4 条是本页星数连续的前 4。`microsoft/Sico` 话题含 `llm`，但不在本查询前 5，不跨节。
  - 未命中：`langflow-ai/langflow`（总 star 156303；描述里的 AI-powered agents 是弱词）。名称和 topics 都没有领域关键词。它排在本页最后。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-28 stars:>3`。`total_count=26`，返回 5，规则保留 0，未命中 4。剩余配额 8。`page=1` 返回满 5 条。另有 1 条只命中 AI 话题、不归入功率器件。5 条都不进正文。
  - 名称词边界未命中：`SickChill/sickchill`（2446；`sickchill` 不等于 `sic`）、`source-academy/sicp`（1026；`sicp` 不等于 `sic`）、`Yuri-NagaSaki/SICK`（244；`SICK` 不等于 `sic`）、`siconos/siconos`（188；`siconos` 不等于 `sic`）。
  - `microsoft/Sico`（总 star 284）：名称 `Sico` 不等于 `sic`，话题含 `llm`。它不在 AI 常青前 5，不跨节。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-28 stars:>3`。`total_count=398`，返回 5，规则保留 1，未命中 3。剩余配额 9。规则保留的 1 条经人工剔除后，本节没有完整条目。
  - `Finbuckle/Finbuckle.MultiTenant`（总 star 1634）：描述里的 LLC 是公司后缀，不是谐振变换器，正文不收。
  - `tbnobody/OpenDTU`（总 star 2206）：描述是 “Inverters”，复数按词边界不等于 `inverter`。话题含 `esp32`，但不在嵌入式常青前 5，不跨节。
  - 名称和 topics 未命中：`dalathegreat/Battery-Emulator`（3004；描述里的 solar inverters 是复数，不等于 `inverter`）、`NVIDIA/dcgm-exporter`（1921）、`dcm4che/dcm4che`（1466；DICOM 实现）。名称里的 DC 不等于 `dc-dc`。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-28 stars:>3`。`total_count=218`，返回 5，规则保留 5，未命中 0，脚本清单类排除 0。剩余配额 8。正文保留 `AtsushiSakai/PythonRobotics`（30855）、`makerspet/oomwoo`（12959）、`betaflight/betaflight`（11739）、`MichaelGrupp/evo`（4356）。`oomwoo` 同时话题含 `esp32`，嵌入式一节一行。`PythonRobotics` 是算法示例代码加教材，不是公开课清单，正文保留。`MPC-BE` 夹在 `betaflight` 与 `evo` 之间，所以本页按总 star 不是连续的 4 个命中仓库。
  - 撞名剔除：`Aleksoid1978/MPC-BE`（总 star 4660）。名称含 `mpc`，描述写明是 Windows 音视频播放器，与模型预测控制无关，正文不收。话题为空。
