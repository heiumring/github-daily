# GitHub 领域日报 · 2026-11-05

生成时间：2026-11-05 07:35（北京时间）。数据拉取开始于 2026-11-05 07:35:03（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-06（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-29 及之后有推送、总 star > 3。轮换页 `page = (当年第 309 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) 给智能体查企业数据加一层语义本体：指标在哪、定义是否一致、查询是否符合认证口径，并把出处一起返回，避免答得快但数字是错的；描述含 LLM，总 star 4868，24 小时新增 star 2053。
2. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句要办的事，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 6608，没有 24 小时新增数据。
3. [wled/WLED](https://github.com/wled/WLED) 用一块 ESP32 经 Wi-Fi 驱动可寻址灯带、二维灯阵和 HUB75 面板，不用为每种灯再写一套固件；本页常青按总 star 排在嵌入式首位，总 star 18974，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 16 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

### AI

- [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)
  - 说明：智能体查企业数据时，快不算对。这个库从已有元数据生成语义本体，告诉代理指标在哪、含义是否一致、该不该用、查询是否对得上认证定义，并把出处一并返回。README 写明结果可以通过命令行、API 和 MCP 交给各种代理框架。描述里的 LLM 是强特征词。
  - 领域：AI
  - 总 star：4868
  - 24 小时新增 star：2053

嵌入式、功率器件、电力电子电源、自动控制在这 16 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4372
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验收成一个网页，能看实时引脚、跑交互模拟、读固件和实验记录，界面有 11 种语言。README 写明目前是 32 个动手实验。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：659
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的旧打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，Android 走 Mopria，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：275
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
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 的例子包括翻完一个微信群再做摘要、按预算把充电器放进购物车但停在结账前、以及逐条读完创作者的近期帖子再总结。
  - 领域：AI
  - 总 star：6608
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4372。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵。代理已经能写出影片、演示和游戏的声音，却听不出按键廉价、撞击晚了 80 毫秒或配乐鼓错了地方。README 写明它把声音变成代理可以判断的证据，并且只在 CPU 上跑。
  - 领域：AI
  - 总 star：3894
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给即将发布的程序加一层防护，让自动做逆向的语言模型代理撞上资源上限和诱饵，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。README 写明这是保护自己软件的防御工具。
  - 领域：AI
  - 总 star：2265
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
  - 总 star：121
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用非均匀 B 样条做多传感器里程计的状态估计。同一套框架覆盖激光惯性、激光视觉惯性、激光加腿部惯性，以及再加视觉的组合，并可做全局样条修正。README 写明这些组合都能实时跑，支持 ROS 2 Humble 和 Jazzy。
  - 领域：自动控制 Control
  - 总 star：48
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino Uno 和超声波测距做水箱液位控制。市电泵走固态继电器，直流泵走 MOSFET；固件里有通断、P 和 PI，并带溢流、干转和传感器保护，另有一套按自家水箱和泵标定的 MATLAB 应用与 Simulink 模型。水位控制比 MOSFET 开关更贴近本领域。话题含 education，这是带固件和实测的实验，不是公开课清单。
  - 领域：自动控制 Control
  - 总 star：8

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

`page = 2`，每页 5 条，本页是各查询按总 star 排序后的第 6 到第 10 条。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：给 ESP32 准备的灯控固件，用 Wi-Fi 驱动可寻址灯带、二维矩阵和 HUB75 面板。README 写明内置 200 多种效果，并带音频响应。
  - 领域：嵌入式 Embedded
  - 总 star：18974
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：把 Go 程序编译到单片机、WebAssembly 和命令行工具上，而不必改用 C。话题含 esp32 与 stm32。README 的板载灯闪烁示例可以不改代码，只换目标板，就跑在 Arduino Uno、Circuit Playground Express 或 XIAO-ESP32S3 上。
  - 领域：嵌入式 Embedded
  - 总 star：17893
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：乐鑫维护的 Arduino 内核，让按 Arduino 方式写的程序能编译到 ESP32 系列芯片上跑。
  - 领域：嵌入式 Embedded
  - 总 star：17671
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：给 RepRap 风格的 3D 打印机提供固件，把运动、加热和挤出管起来，8 位和 32 位控制器都能用，不少商品机出厂就刷着它。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：17649
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：面向资源受限设备的实时操作系统，从小传感器和可穿戴灯到智能手表和物联网网关。话题含 embedded、rtos、zephyr、mcu。README 写明内核支持 ARM Cortex-M 与 RISC-V 等架构。
  - 领域：嵌入式 Embedded
  - 总 star：16995

### AI

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图在本地编排扩散模型，生成图像、视频、三维和音频，并把每个模型和参数留在创作者手里。话题含 pytorch；`stable-diffusion` 按词边界计入 diffusion。README 写明目标是在消费级显卡上做本地推理。
  - 领域：AI
  - 总 star：145034
- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：一个尽量小的智能体运行壳，自带统一的 LLM 接口、代理循环、终端界面和编程命令行。README 写明用扩展、技能和提示模板把它改成自己的工作流，默认不做子代理和计划模式。描述里的 LLM 是强特征词。话题为空。
  - 领域：AI
  - 总 star：120061
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：让智能体像人一样操作浏览器，例如找空位、选时间、处理验证码并完成预约。可以接任意 LLM 在本地跑，也可以用它的云端隐蔽浏览器和托管代理接口。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：120038
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
  - 说明：把编程代理每次会话里的工具操作压成可检索的记忆，下一轮自动注回上下文，避免每次重连都从零开始。话题含 ai-agents。Trending 页面没有 topics，描述里的 AI 是弱词，所以同一仓库不进 A；本节只用搜索接口的总 star。
  - 领域：AI
  - 总 star：112811

### 功率器件 Power Devices

本页剔除撞名后没有常青仓库。

### 电力电子电源 Power Supply

- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：给 ESPHome 加一个组件，经 UART-TTL 或蓝牙监视并控制极空电池管理系统（JK-BMS）。话题 `jikong-bms` 按词边界计入 bms。README 写了 ESP32 和 ESP8266 的接线，搜索话题没有 esp32，不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：1045

### 自动控制 Control

- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：提供 RTAB-Map 的库和可单独运行的程序，用来做定位与建图。话题含 slam 与 ros2。README 列出 ROS 2 Humble、Jazzy、Kilted、Lyrical 和 Rolling 的 apt 包。
  - 领域：自动控制 Control
  - 总 star：4079
- [RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)
  - 说明：把 SLAM 和光束法平差写成图，再做非线性最小二乘，新问题通常只要几行代码就能接进去。话题含 slam。README 也提到计算机视觉里的同类问题，搜索描述和话题没有 computer-vision，不跨到 AI。
  - 领域：自动控制 Control
  - 总 star：3478
- [SteveMacenski/slam_toolbox](https://github.com/SteveMacenski/slam_toolbox)
  - 说明：给会变化的大场景做二维激光 SLAM，能在已保存的位姿图上继续建图，也能只做定位。名称 `slam_toolbox` 按词边界计入 slam。搜索描述写的是 ROS；README 写明它是目前配套 ROS 2 Nav2 的 SLAM 库。话题为空。
  - 领域：自动控制 Control
  - 总 star：2701

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`NVIDIA/auto-ontology`、`wangzan101/Mika`、`agharsallah/esp-labs-web`、`ngxson/esp32-usb-to-airprint`、`Liu-zhongxian/zongzhu-bot`、`Leonxlnx/earshot`、`qybaihe/bla`、`wled/WLED`、`tinygo-org/tinygo`、`zephyrproject-rtos/zephyr`、`earendil-works/pi`、`Comfy-Org/ComfyUI`、`browser-use/browser-use`、`thedotmack/claude-mem`、`syssi/esphome-jk-bms`、`mozihe/z-localization`、`ASIG-X/RESPLE2`、`introlab/rtabmap`、`RainerKuemmerle/g2o`、`SteveMacenski/slam_toolbox`、`sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`、`jurem/SicTools`、`YuxuanSnow/Phy-SIC`、`marozols/SIC-existence`。这 24 次是仓库 README 接口，不计入上面 11 次搜索配额。`esp32-iphone-agent`、`esp32-thinks`、`arduino-esp32`、`Marlin` 和水位实验的说明没有超出搜索描述。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 16 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。正文只收 `NVIDIA/auto-ontology`（总 star 4868，stars today 2053；描述含 LLM）。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`vercel-labs/agent-desktop`（14981，2463；描述是 “AI agents”，空格写法不等于 `ai-agents`）、`D4Vinci/Scrapling`（96470，2006）、`JiaFeiMiao-K-Cat/DiscImageStudio`（6550，1792；描述为空）、`mattpocock/skills`（313261，1376）、`thedotmack/claude-mem`（112810，1165；描述里的 AI 是弱词。常青检索因话题 `ai-agents` 收录，搜索总 star 112811，两处各用各源数字）、`floci-io/floci`（29571，1082）、`github/spec-kit`（147273，810）、`harry0703/MoneyPrinterTurbo`（138915，615；描述里的「AI 大模型」不等于 llm）、`max-sixty/worktrunk`（11003，524；描述里的 AI agent 是弱词）、`FareedKhan-dev/kimi-k3-in-c`（10268，351；名称和描述都没有 llm）、`garrytan/gstack`（139305，285）、`The-PR-Agent/pr-agent`（14729，279）、`MichaelCade/90DaysOfDevOps`（30393，264；描述是 DevOps 学习地图，没有领域关键词）、`scenario-labs/skills`（2404，224；描述里的 AI agent 是弱词，MCP 不是 AI 关键词）、`Thysrael/Horizon`（12465，121；描述里的 AI 是弱词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-06 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-06 stars:>2`。`total_count=431`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4372）、`agharsallah/esp-labs-web`（659）、`ngxson/esp32-usb-to-airprint`（275）、`raullenchai/esp32-thinks`（262）、`Liu-zhongxian/zongzhu-bot`（259）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。`esp32-usb-to-airprint` 只有名称和描述里的 esp32，接口 `created_at` 为 `2026-10-26T16:18:54Z`，北京时间是 2026-10-27 00:18。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-06 stars:>2`。`total_count=2457`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 8。正文保留 `wangzan101/Mika`（6608）、`Leonxlnx/earshot`（3894）、`qybaihe/bla`（2265）。这 3 条是本页星数连续的前 3。另有 2 条跨领域一行：`esp32-iphone-agent`（4372）、`esp32-thinks`（262），来自嵌入式检索。这两条话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`CopilotKit/OpenDuet`（总 star 1940；描述里的 AI agent 是弱词）、`benjitaylor/skills`（总 star 1907；描述是 “Skills for AI coding agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-06 stars:>2`。`total_count=5`，返回 5，规则保留 3，未命中 2。剩余配额 9。本查询只有 5 条满足条件，所以不足分页，返回的就是全部结果。规则保留的 3 条里，2 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC。README 写明这是 Lean 对「任意有限维都存在 SIC-POVM」的形式化证明，与碳化硅器件无关，正文不收。
  - `sadhub10/SIC-2026-Aulas-Pa-C-y-Pa-D`（总 star 3）：名称含 SIC，描述为空。README 写明这是 Samsung Innovation Campus 2026 课堂 PA-C 与 PA-D 的课堂笔记本和课程材料，不是碳化硅器件，属课程仓库，正文不收。脚本的清单规则没有命中空描述，此处人工剔除。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 8）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`aswin-code513/First-Sick-First-Served`（3）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`First-Sick` 与 `Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-06 stars:>2`。`total_count=63`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`CompaLarios18/MH4UltimateDC`（102）、`Lida-V/3DCharaMakeSkills-Lida`（57）、`two-delta/DCOCO`（57；描述为空）、`leftamber/grid-dca-bot`（48；描述里的 DCA 不等于 `dc-dc`）、`ernie-research/DCore`（46；描述里的 LLMs 不等于 llm，名称里的 DC 不等于 `dc-dc`）。名称里能看到 DC 的是 `MH4UltimateDC` 和 `DCOCO`。`3DCharaMakeSkills-Lida` 的名称和描述里没有这些词，命中点不在接口返回的名称、话题和描述中。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-06 stars:>2`。`total_count=68`，返回 5，规则保留 3，未命中 2。剩余配额 7。正文保留 `mozihe/z-localization`（121）、`ASIG-X/RESPLE2`（48）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（8），因为水位控制比 MOSFET 开关更贴近本领域。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 88）。话题含 `ros2` 与 `slam`，描述写明是机器人开发自学课程地图和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。它排在 `z-localization` 与 `RESPLE2` 之间。
  - 名称和 topics 未命中：`snarebes/SampQOL-OS`（总 star 53；描述里的 Akai MPC 不是强特征词，名称也不含 `mpc`）、`lbgos/rift-s-linux`（总 star 38；描述里的 “Basalt SLAM” 是空格写法，不等于 `slam`）。

### C. 领域常青（`pushed:>=2026-10-29 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-29 stars:>3`。`total_count=1275`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。`page=2`、`per_page=5`，本页是总结果里的第 6 到第 10 条。正文完整条目 5 条都来自本查询：`wled/WLED`（18974）、`tinygo-org/tinygo`（17893）、`espressif/arduino-esp32`（17671）、`MarlinFirmware/Marlin`（17649）、`zephyrproject-rtos/zephyr`（16995）。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-29 stars:>3`。`total_count=9001`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 8。正文保留 `Comfy-Org/ComfyUI`（145034）、`earendil-works/pi`（120061）、`browser-use/browser-use`（120038）、`thedotmack/claude-mem`（112811）。`addyosmani/agent-skills` 夹在 `browser-use` 与 `claude-mem` 之间，所以本页按总 star 不是连续的 4 个命中仓库。
  - 未命中：`addyosmani/agent-skills`（总 star 113280；描述是 “skills for AI coding agents”，空格写法不等于 `ai-agents`）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-29 stars:>3`。`total_count=28`，返回 5，规则保留 2，未命中 3。剩余配额 6。`page=2` 返回满 5 条，是总结果里的第 6 到第 10 条。5 条都不进正文。
  - 名称词边界未命中：`siconos/siconos`（188；`siconos` 不等于 `sic`）、`hexlet-volunteers/hexlet-sicp`（114；`sicp` 不等于 `sic`）、`sicap-pro/SICAP.ai`（96；名称 `SICAP` 不等于 `sic`，描述是公共采购检索系统）。
  - `YuxuanSnow/Phy-SIC`（总 star 64）：名称 `Phy-SIC` 按词边界命中 sic。README 写明这是从单张图像估计人体与场景接触的论文，不是碳化硅器件，正文不收。
  - `jurem/SicTools`（总 star 57）：描述里的 SIC/XE 按词边界命中 sic。README 写明这是 Leland Beck《System Software》里假想计算机的汇编器、仿真器和链接器，不是碳化硅器件，正文不收。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-29 stars:>3`。`total_count=394`，返回 5，规则保留 1，未命中 3。剩余配额 8。`page=2` 是总结果里的第 6 到第 10 条。正文保留 `syssi/esphome-jk-bms`（1045），它是本页星数最低的一条。另有 1 条命中了别的领域，但不在那些领域本页前 5，不跨节。
  - `pnoker/iot-dc3`（总 star 1267）：名称里的 dc3 不等于 `dc-dc`，分类没有计入电力电子。话题含 `modbus` 与 `ai-agents`，但不在嵌入式和 AI 常青前 5，不跨节。
  - 名称和 topics 未命中：`Evalle/DCA`（1413；Docker 认证考试指南，DCA 不等于 `dc-dc`）、`mjbots/moteus`（1367；描述是 “Brushless DC motor controller”，空格写法不等于 `motor-control`，DC 不等于 `dc-dc`）、`rordenlab/dcm2niix`（1210；DICOM 到 NIfTI 的转换器）。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-29 stars:>3`。`total_count=225`，返回 5，规则保留 3，未命中 1，脚本清单类排除 1。剩余配额 9。正文保留 `introlab/rtabmap`（4079）、`RainerKuemmerle/g2o`（3478）、`SteveMacenski/slam_toolbox`（2701）。`vedderb/bldc` 与 `awesome-robotics-libraries` 夹在中间，所以本页按总 star 不是连续的 3 个命中仓库。
  - 名称和描述未命中：`vedderb/bldc`（总 star 3559）。描述是 “motor control”（空格），名称 `bldc` 不在控制关键词表，正文不收。
  - 清单类剔除：`jslee02/awesome-robotics-libraries`（总 star 3105）。描述写明是机器人库的策展清单，名称含 awesome。话题含 `slam`，脚本已按清单排除。
