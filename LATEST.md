# GitHub 领域日报 · 2026-11-03

生成时间：2026-11-03 07:32（北京时间）。数据拉取开始于 2026-11-03 07:32:30（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-04（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-27 及之后有推送、总 star > 3。轮换页 `page = (当年第 307 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [wangzan101/Mika](https://github.com/wangzan101/Mika) 在安卓上说一句话，助手就在一块隐藏的后台屏里操作 App 和网页，自己的屏幕还能继续用；创建于 2026-10-29，总 star 5255，没有 24 小时新增数据。
2. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块 7 美元的 ESP32 让视觉模型操作真 iPhone，眼睛走 AirPlay，手走 USB HID，不用 Mac、开发者账号或越狱；近 30 天新建，总 star 4236，没有 24 小时新增数据。
3. [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint) 给只能插 USB 的旧打印机加一块 ESP32-S3，让苹果设备和浏览器能无线打印、扫描；创建于 2026-10-27（北京时间），总 star 235，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 15 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。

嵌入式、AI、功率器件、电力电子电源、自动控制在这 15 条里没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4236
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验台收成一个网页，能看实时引脚、跑交互模拟、读 esp-labs 固件和实验记录，界面有 11 种语言。话题含 education，这是实验台应用，不是公开课清单。
  - 领域：嵌入式 Embedded
  - 总 star：635
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：261
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在 Waveshare 1.75C 圆屏 ESP32 上做语音终端，接 Grok，屏幕有会眨眼的眼睛、字幕和朗读，仓库同时放固件和后端。
  - 领域：嵌入式 Embedded
  - 总 star：245
- [ngxson/esp32-usb-to-airprint](https://github.com/ngxson/esp32-usb-to-airprint)
  - 说明：只能插 USB 的打印机，插上一块 ESP32-S3 就能进 Wi-Fi。README 写明 iPhone、iPad 和 Mac 可以用 AirPrint 打印，浏览器里也能扫描，并要求新驱动先在真机上测过。
  - 领域：嵌入式 Embedded
  - 总 star：235

### AI

- [wangzan101/Mika](https://github.com/wangzan101/Mika)
  - 说明：安卓上的私人助理。说一句话，它在一块隐藏的后台屏里打开 App、点按和打字，自己的屏幕还能继续用。README 的例子是让它在后台打开微信、找到联系人并把消息发出去。
  - 领域：AI
  - 总 star：5255
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4236。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：3553
- [qybaihe/bla](https://github.com/qybaihe/bla)
  - 说明：给自己要发布的程序加一层防护，让自动做逆向的语言模型代理耗在诱饵和资源上限上，使用者跑起来的行为仍和原来一样。话题 `llm-security` 按词边界计入 llm。
  - 领域：AI
  - 总 star：1981
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：261。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 开关直流泵的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：8。

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室开源了 2026 年 RoboMaster 超级对抗赛哨兵的定位。README 写明这是 ROS 2 激光惯性定位栈，能做里程计、点云建图、先验地图定位、回环和重定位，也可接 UWB；示例传感器是 Livox Mid-360。
  - 领域：自动控制 Control
  - 总 star：118
- [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)
  - 说明：用非均匀 B 样条做多传感器里程计。README 写明激光惯导、激光视觉惯导、激光腿式惯导，以及再加上视觉的组合，可以放在一套估计里，还能选带回环后的全局修正，并按实时约束来做。
  - 领域：自动控制 Control
  - 总 star：44
- [prohurtz/BSB-SLAM](https://github.com/prohurtz/BSB-SLAM)
  - 说明：给 Bigscreen Beyond 头显接上 Xvisio XR50 相机，让头显自己做定位，这样不用再摆 Lighthouse 基站；仓库带 SteamVR 驱动和负责安装的桌面程序。
  - 领域：自动控制 Control
  - 总 star：37
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：一套水位控制实验：水箱、超声波测距，市电泵走固态继电器，或者直流泵用 MOSFET 开关；控制律有通断、P 和 PI，并带一个按这台水箱和泵标定的 MATLAB 程序。水位控制比一只 MOSFET 开关更贴近本领域。
  - 领域：自动控制 Control
  - 总 star：8

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

### 嵌入式 Embedded

- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：把一块 ESP32 变成只在本地跑的 Wi-Fi 动作传感器。人走过房间会改变信号怎么传播，它读这些变化来报有没有人动。README 写明不用摄像头、麦克风、可穿戴设备或专用雷达。描述还列出 C++ SDK、ESPHome、Matter 前端和命令行。话题含 embedded；话题里的 `esp-32` 按词边界不等于 esp32，描述里的 ESP32 计入。
  - 领域：嵌入式 Embedded
  - 总 star：9728
- [crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)
  - 说明：给墨水屏做可刷写的阅读器固件，用来读 EPUB 和 TXT，而不是把格式锁在厂商系统里。README 写明目前跑在 ESP32-C3 的 Xteink X4、X3，以及 ESP32-S3 的 X4 Pro、M5Paper Mono 等机型上。
  - 领域：嵌入式 Embedded
  - 总 star：8623
- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的官方固件。没有蜂窝网时，用 LoRa 把文字和位置在节点之间传开。话题含 esp32 与 stm32。
  - 领域：嵌入式 Embedded
  - 总 star：8516
- [FastLED/FastLED](https://github.com/FastLED/FastLED)
  - 说明：用同一套库驱动 Arduino、ESP32 和 Teensy 上的可寻址彩灯，做颜色动画，不必为每种灯珠协议各写一套时序。
  - 领域：嵌入式 Embedded
  - 总 star：7523
- [BruceDevices/firmware](https://github.com/BruceDevices/firmware)
  - 说明：给 M5Stack Cardputer、Stick、T-Deck 一类 ESP32 掌机准备的固件。README 写明它把安全测试工具收成一套可随身刷写的系统。
  - 领域：嵌入式 Embedded
  - 总 star：7137
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：709。
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：541。

### AI

- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：用 Python 写张量和动态神经网络，并在 GPU 上加速。仓库名 pytorch 计入。
  - 领域：AI
  - 总 star：105099
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：给大模型做高吞吐、省内存的推理服务。话题含 llm、pytorch 和 transformer。描述里的 LLMs 按词边界不等于 llm，命中来自话题。
  - 领域：AI
  - 总 star：96163
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：把任意网页爬成适合语言模型使用的 Markdown，可以自己跑。话题含 llm 与 ai-agents。
  - 领域：AI
  - 总 star：86790
- [symforce-org/symforce](https://github.com/symforce-org/symforce) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：1654。

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整常青仓库。规则命中的 `Oire/sic` 是图片转换器，与碳化硅器件无关，正文不收。

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：把阳光电源逆变器接到 Home Assistant，覆盖 SH RT、SHx RS、SH K 和 SxT 几个系列，通信走 Modbus。
  - 领域：电力电子电源 Power Supply
  - 总 star：709
- [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman)
  - 说明：把 Solarman 数据采集棒接到 Home Assistant，用来读逆变器。话题含 inverter，并列出 Deye、Sofar、Solis、Sunsynk 等品牌，通信话题含 modbus。
  - 领域：电力电子电源 Power Supply
  - 总 star：541
- [fl4p/batmon-ha](https://github.com/fl4p/batmon-ha)
  - 说明：在 Home Assistant 里通过蓝牙读 JK、JBD、Daly、ANT、SOK 等电池管理系统。README 写明走主机自己的蓝牙，不另加 ESP32，并能看单体电压和温度。话题 `jikong-bms` 按词边界计入 bms。搜索话题没有 esp32，不跨到嵌入式。
  - 领域：电力电子电源 Power Supply
  - 总 star：531

### 自动控制 Control

- [google-deepmind/mujoco_mpc](https://github.com/google-deepmind/mujoco_mpc)
  - 说明：在 MuJoCo 里做实时预测控制，用来编写并求解机器人任务。README 写明目前带多组打靶式规划器，含 iLQG、梯度下降，以及不依赖导数的 Predictive Sampling。话题含 mpc 与 motor-control。
  - 领域：自动控制 Control
  - 总 star：1758
- [symforce-org/symforce](https://github.com/symforce-org/symforce)
  - 说明：给机器人做快速符号计算和代码生成，用来写状态估计、运动规划和控制，再生成可编译的 C++。话题含 slam。机器人应用比其中一项 computer-vision 话题更贴近本领域。
  - 领域：自动控制 Control
  - 总 star：1654
- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用 MuJoCo 搭一组肌肉骨骼模型的仿真任务，并包成 OpenAI gym 接口。README 写明面向生物力学、神经科学和康复一类研究。话题含 motor-control。
  - 领域：自动控制 Control
  - 总 star：1274
- [SJTU-ViSYS/M2DGR](https://github.com/SJTU-ViSYS/M2DGR)
  - 说明：SJTU-ViSYS 的地面机器人多模态、多场景 SLAM 数据集。搜索描述写明对应 RA-L 2021 与 ICRA 2022。
  - 领域：自动控制 Control
  - 总 star：1223

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`wangzan101/Mika`、`mozihe/z-localization`、`ASIG-X/RESPLE2`、`prohurtz/BSB-SLAM`、`crosspoint-reader/crosspoint-reader`、`BruceDevices/firmware`、`davidrapan/ha-solarman`、`google-deepmind/mujoco_mpc`、`francescopace/espectre`、`ngxson/esp32-usb-to-airprint`、`fl4p/batmon-ha`、`SJTU-ViSYS/M2DGR`、`MyoHub/myosuite`、`symforce-org/symforce`、`qybaihe/bla`。这 15 次是仓库 README 接口，不计入上面 11 次搜索配额。`ha-solarman` 的 README 前段是徽章和文档导航，正文说明没有超出搜索描述和话题。`M2DGR` 的标题与搜索描述一致，没有另补传感器清单。`esp32-iphone-agent`、`esp-labs-web`、`esp32-thinks`、`zongzhu-bot`、`earshot`、`pytorch`、`vllm`、`crawl4ai`、`meshtastic/firmware`、`FastLED`、水位实验和 Sungrow 的说明没有超出搜索描述。`bla` 里「使用者行为不变」来自 README 首段。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 15 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`pingdotgg/t3code`（41788，3216；描述为空）、`vercel-labs/agent-desktop`（9513，2243；描述是 “AI agents”，空格写法不等于 `ai-agents`；AI 是弱词）、`thedotmack/claude-mem`（110702，1799；描述里的 AI 是弱词）、`Donchitos/Claude-Code-Game-Studios`（33507，1380；描述是 “49 AI agents”，空格写法不等于 `ai-agents`）、`mattpocock/skills`（310193，968）、`D4Vinci/Scrapling`（92782，858）、`shiyu-coder/Kronos`（45997，855；金融市场基础模型，没有 llm）、`JustVugg/colibri`（46506，655；MoE 与 model，没有 llm）、`FlashML-org/FreeToken`（16020，654；本地跑大模型，描述没有 llm 这个词）、`hyprwm/Hyprland`（39897，508）、`paperclipai/paperclip`（110366，451；描述里的 agents 是弱词）、`kornia/kornia`（12117，412；“Computer Vision” 是空格，不等于 `computer-vision`；Spatial AI 是弱词）、`p-e-w/heretic`（38064，404；“language model” 不等于 llm）、`karpathy/nanochat`（59862，325；名称 nanochat 与描述里的 ChatGPT 都不含 llm）、`max-sixty/worktrunk`（10012，136；描述里的 AI agent 是弱词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-04 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-04 stars:>2`。`total_count=426`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4236）、`agharsallah/esp-labs-web`（635）、`raullenchai/esp32-thinks`（261）、`Liu-zhongxian/zongzhu-bot`（245）、`ngxson/esp32-usb-to-airprint`（235）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单，正文保留。`esp32-usb-to-airprint` 只有名称和描述里的 esp32，接口 `created_at` 为 `2026-10-26T16:18:54Z`，北京时间是 2026-10-27 00:18。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-04 stars:>2`。`total_count=2509`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 8。正文保留 `wangzan101/Mika`（5255）、`Leonxlnx/earshot`（3553）、`qybaihe/bla`（1981）。另有 2 条跨领域一行：`esp32-iphone-agent`（4236）、`esp32-thinks`（261），来自嵌入式检索。这两条话题含 `llm`，但没有出现在本查询返回的前 5 里。
  - 未命中：`openfilm/openfilm`（总 star 4270；描述里的 AI video agent 是弱词）、`CopilotKit/OpenDuet`（总 star 1856；描述里的 AI agent 是弱词）。名称和 topics 都没有领域关键词。`openfilm` 夹在 `Mika` 与 `earshot` 之间，所以本页按总 star 不是连续的 3 个命中仓库。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-04 stars:>2`。`total_count=4`，返回 4，规则保留 2，未命中 2。剩余配额 8。本查询只有 4 条满足条件，所以不足 5 条。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 8）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems` 与 `pid-control`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`aswin-code513/First-Sick-First-Served`（3）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`First-Sick` 与 `Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-04 stars:>2`。`total_count=67`，返回 5，规则保留 0。剩余配额 6。正文写「本日无新项目」。
  - 名称和描述里没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`SteamDerrick/mwanrytl`（274；描述把 Acrobat Pro DC 当成可分发的安装包，DC 不等于 `dc-dc`）、`CompaLarios18/MH4UltimateDC`（90）、`Lida-V/3DCharaMakeSkills-Lida`（56）、`two-delta/DCOCO`（56；描述为空）、`leftamber/grid-dca-bot`（51；描述里的 DCA 不等于 `dc-dc`）。名称里能看到 DC 的是 `MH4UltimateDC` 和 `DCOCO`。`3DCharaMakeSkills-Lida` 的名称和描述里没有这些词，命中点不在接口返回的名称、话题和描述中。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-04 stars:>2`。`total_count=66`，返回 5，规则保留 4，未命中 1。剩余配额 4。正文保留 `mozihe/z-localization`（118）、`ASIG-X/RESPLE2`（44）、`prohurtz/BSB-SLAM`（37）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（8），因为水位控制比 MOSFET 开关更贴近本领域。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 85）。话题含 `ros2` 与 `slam`，描述写明是机器人开发自学课程地图和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。
  - 名称和 topics 未命中：`lbgos/rift-s-linux`（总 star 38）。描述里的 “Basalt SLAM” 是空格写法，不等于 `slam`。它排在 `RESPLE2` 与 `BSB-SLAM` 之间。

### C. 领域常青（`pushed:>=2026-10-27 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-27 stars:>3`。`total_count=1228`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。`page=4`、`per_page=5`，本页是总结果里的第 16 到第 20 条。正文完整条目 5 条都来自本查询：`francescopace/espectre`（9728）、`crosspoint-reader/crosspoint-reader`（8623）、`meshtastic/firmware`（8516）、`FastLED/FastLED`（7523）、`BruceDevices/firmware`（7137）。`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（709）与 `davidrapan/ha-solarman`（541）来自电力电子检索，话题含 `modbus`，本节各一行。`espectre` 的话题是 `esp-32`，不等于 `esp32`，描述里的 ESP32 计入。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-27 stars:>3`。`total_count=8935`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `pytorch/pytorch`（105099；仓库名 pytorch）、`vllm-project/vllm`（96163；话题 `llm`、`pytorch`、`transformer`）、`unclecode/crawl4ai`（86790；话题 `llm` 与 `ai-agents`）。`symforce-org/symforce`（1654）来自自动控制检索，话题含 `computer-vision`，本节一行。
  - 未命中：`pbakaus/impeccable`（总 star 100432；描述里的 coding agent 与 AI slop 是弱词）、`lobehub/lobehub`（总 star 83717；描述里的 AI team 是弱词）。名称和 topics 都没有领域关键词。`impeccable` 夹在 `pytorch` 与 `vllm` 之间，`lobehub` 排在本页最后，所以本页按总 star 不是连续的 3 个命中仓库。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-27 stars:>3`。`total_count=24`，返回 5，规则保留 1，未命中 4。剩余配额 7。`page=4`、`per_page=5`，本页返回满 5 条，对应总结果里的第 16 到第 20 条，不是失败。规则保留的 1 条经人工剔除后，本节没有完整条目。
  - `Oire/sic`（总 star 5）：简单图片转换器，名称撞上 `sic`，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`SicerBrito/SicerBrito`（6；GitHub 个人主页配置，`Sicer` 不等于 `sic`）、`rvandewater/SICdb_MEDS`（6；萨尔茨堡重症监护数据库，`SICdb` 不等于 `sic`）、`anzeabram/SiCS`（5；斯洛文尼亚洞穴测量，`SiCS` 不等于 `sic`）、`tbermen/SiCoPR`（5；IEEE 802.3 信道工作裕量的 Python 移植，`SiCo` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-27 stars:>3`。`total_count=393`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文完整条目为 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（709）、`davidrapan/ha-solarman`（541）、`fl4p/batmon-ha`（531）。Sungrow 与 ha-solarman 同时话题含 `modbus`，嵌入式一节各一行。`batmon-ha` 的 README 写明不另加 ESP32，搜索话题也没有 esp32，不跨到嵌入式。本页第 2 条和第 5 条是 DC 撞名，所以 3 条正文不是本页星数连续的前 3。
  - 名称和 topics 未命中：`hackthedev/dcts-shipping`（640）、`dcm4che/dcm4chee-arc-light`（507；DICOM 归档）。名称里的 DC 不等于 `dc-dc`。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-27 stars:>3`。`total_count=216`，返回 5，规则保留 5，未命中 0，脚本清单类排除 0。剩余配额 9。正文保留 `google-deepmind/mujoco_mpc`（1758）、`symforce-org/symforce`（1654）、`MyoHub/myosuite`（1274）、`SJTU-ViSYS/M2DGR`（1223）。`symforce` 同时话题含 `computer-vision`，AI 一节一行。`mujoco_mpc` 的 `motor-control` 只归自动控制，不归电力电子（电力电子关键词是 `motor-drive`）。`cv-arxiv-daily` 夹在 `symforce` 与 `myosuite` 之间，所以本页按总 star 不是连续的 4 个命中仓库。
  - 清单类剔除：`Vincentqyw/cv-arxiv-daily`（总 star 1512）。话题含 `slam`，描述写明用 GitHub Actions 每天自动更新计算机视觉论文，属论文清单，不进正文。脚本的清单规则没有命中这条描述，此处人工剔除。
