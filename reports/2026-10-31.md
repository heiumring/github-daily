# GitHub 领域日报 · 2026-10-31

生成时间：2026-10-31 07:31（北京时间）。数据拉取开始于 2026-10-31 07:31:57（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-10-01（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-24 及之后有推送、总 star > 3。轮换页 `page = (当年第 304 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，眼睛走 AirPlay，手走 USB HID，不用 Mac、开发者账号或越狱；近 30 天新建，总 star 4132。
2. [ruvnet/RuView](https://github.com/ruvnet/RuView) 用低成本 ESP32 采集普通 Wi-Fi 的信道状态，隔墙看有没有人并测呼吸和心率，不靠摄像头；领域常青本页，总 star 101760，没有 24 小时新增数据。
3. [mozihe/z-localization](https://github.com/mozihe/z-localization) 东北大学 T-DT 实验室把 2026 年 RoboMaster 哨兵定位开源成 ROS 2 激光惯性定位栈，能建图、重定位，也可接 UWB；近 30 天新建，总 star 111。

## A. 今日热度

Trending 页面解析到 15 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。嵌入式、AI、功率器件、电力电子电源、自动控制在这 15 条里都没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不用 Mac、开发者账号或越狱。
  - 领域：嵌入式 Embedded
  - 总 star：4132
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验台收成一个网页，能看实时引脚、跑交互模拟、读 esp-labs 固件和实验记录，界面有 11 种语言。
  - 领域：嵌入式 Embedded
  - 总 star：608
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：455
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：260
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在 Waveshare 1.75C 圆屏 ESP32 上做语音终端，接 Grok，屏幕有会眨眼的眼睛、字幕和朗读，仓库同时放固件和后端。
  - 领域：嵌入式 Embedded
  - 总 star：231

### AI

- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：4900
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：4132。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：3316
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：260。

### 功率器件 Power Devices

本日没有以功率器件为最贴近领域的完整新项目。描述里用 MOSFET 驱动直流泵的水位实验，完整说明写在下方「自动控制 Control」。

- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab) — 见下方「自动控制 Control」完整条目。描述含 MOSFET，此处不展开。领域：功率器件 Power Devices。总 star：8。

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室开源了 2026 年 RoboMaster 超级对抗赛哨兵的定位。README 写明这是 ROS 2 激光惯性定位栈，能做里程计、点云建图、先验地图定位、回环和重定位，也可接 UWB；示例传感器是 Livox Mid-360。
  - 领域：自动控制 Control
  - 总 star：111
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；网站、组装预览和带价格的零件表已经公开，CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：102
- [prohurtz/BSB-SLAM](https://github.com/prohurtz/BSB-SLAM)
  - 说明：让 Bigscreen Beyond 头显用一颗 Xvisio XR50 SLAM 相机自己定位，这样 Lighthouse 基站可以收起来，并带 SteamVR 驱动和桌面设置程序。
  - 领域：自动控制 Control
  - 总 star：33
- [Samarth030312/arduino-water-level-control-lab](https://github.com/Samarth030312/arduino-water-level-control-lab)
  - 说明：用 Arduino 做水箱水位控制实验：超声波测水位，市电泵走固态继电器，直流泵走 MOSFET，带通断、P 和 PI，以及按水箱和泵参数来的 MATLAB 应用和 Simulink。
  - 领域：自动控制 Control
  - 总 star：8

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 1。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：用低成本 ESP32 采集普通 Wi-Fi 的信道状态，隔墙判断有没有人并测呼吸和心率，不靠摄像头或可穿戴设备。
  - 领域：嵌入式 Embedded
  - 总 star：101760
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：用来写游戏的 C 库，不做可视化编辑器。README 写明它也适合原型、工具、嵌入式和教学；话题含 embedded 与 esp32。
  - 领域：嵌入式 Embedded
  - 总 star：35496
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：在 ESP32 上做语音聊天入口。README 写明它调用 Qwen、DeepSeek 这类大模型，再用 MCP 控制多个终端。
  - 领域：嵌入式 Embedded
  - 总 star：32294
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：给从小单片机到能做 3D 的处理器做嵌入式图形界面，并带专业编辑器 LVGL Pro。
  - 领域：嵌入式 Embedded
  - 总 star：25056
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：给 ESP8266 和 ESP32 设备替换原厂固件，用网页配置，用定时或规则做自动化，并经 MQTT、HTTP、串口或 KNX 在本地控制。
  - 领域：嵌入式 Embedded
  - 总 star：24948
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：12884。

### AI

- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
  - 说明：给 AI 代理准备网页等来源的数据。话题覆盖爬虫、把 HTML 转成 Markdown，以及 llm。
  - 领域：AI
  - 总 star：197099
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
  - 说明：让编程代理按「能不写就不写」来改需求，少交一层没必要的代码。话题含 yagni。
  - 领域：AI
  - 总 star：180947
- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：用同一套接口定义、训练和推理文本、视觉、音频和多模态模型，不必为每种模型另写加载代码。
  - 领域：AI
  - 总 star：168372
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：在一个工作区里搭代理工作流，描述还写了 RAG 管道和多种模型、工具；可以云端、VPC 或自托管，从原型到上线不用换一套栈。
  - 领域：AI
  - 总 star：160025

### 功率器件 Power Devices

本页无符合领域的常青仓库。返回的 5 条里，名称按词边界都不等于 `sic`（`sickchill`、`sickbeard_mp4_automator`、`sicp`、`Sico`、`siconos`），没有功率器件话题。

### 电力电子电源 Power Supply

本页无符合领域的常青仓库。规则命中的 `Finbuckle/Finbuckle.MultiTenant` 描述里的 LLC 是公司后缀，不是谐振变换器，正文不收。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：用 Python 示例和一本教材把机器人算法跑通，话题覆盖 SLAM、定位、建图和路径规划。
  - 领域：自动控制 Control
  - 总 star：30828
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：可自行组装的开源扫地机器人，用二维激光雷达在本地建图和导航，软件含 ROS 2 与 ESP32，日常功能不依赖云端。README 写明现在能跑的是仿真，实机物料清单还没在真机上验证完。
  - 领域：自动控制 Control
  - 总 star：12884
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：给竞速、花飞、航拍、长航时、微型机和固定翼用的开源飞控软件。README 写明这份仓库是刷到飞控上的固件。
  - 领域：自动控制 Control
  - 总 star：11725
- [MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)
  - 说明：用 Python 评估并比较里程计和 SLAM 的轨迹，支持 TUM、KITTI、EuRoC 和 ROS 2 的记录格式。
  - 领域：自动控制 Control
  - 总 star：4352

## 数据源状态

全部 11 次 A/B/C 请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

说明里多出来的句子若搜索描述里没有，均来自对应仓库 README 正文，star 仍用搜索接口或 Trending 页面。补充读取的 README 均 HTTP 200：`mozihe/z-localization`、`prohurtz/BSB-SLAM`、`makerspet/oomwoo`、`betaflight/betaflight`、`raysan5/raylib`、`78/xiaozhi-esp32`、`ruvnet/RuView`、`MichaelGrupp/evo`。这 8 次是核心接口，不计入上面 11 次搜索配额。`lvgl/lvgl`、`arendst/Tasmota`、`AtsushiSakai/PythonRobotics` 的 README 也读过（HTTP 200），说明没有超出搜索描述和话题。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 15 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`pbakaus/impeccable`（97003，2299；描述里的 AI 是弱词）、`HKUDS/DeepTutor`（51738，2282）、`togg53192-cmd/jailbreaks`（10929，2053；描述是 “LIST OF ALL MY JAILBREAKS”，没有领域词，脚本的清单规则也未命中）、`obra/superpowers`（309407，1255；描述里的 agentic 是弱词）、`Renhuai123/ziwei-doushu`（11181，1146）、`thedotmack/claude-mem`（106181，1145；描述里的 AI 是弱词，页面没有 topics）、`pingdotgg/t3code`（32708，920；描述为空）、`milind-soni/OpenMausBot`（8586，899）、`mattpocock/skills`（307443，889）、`JetBrains/thinkrail`（6550，717）、`CopilotKit/OpenBot`（8757，707；描述里的 AI coworkers 是弱词）、`lightpanda-io/browser`（38325，652；描述里的 AI 是弱词）、`anthropics/skills`（185280，287；描述里的 Agent Skills 是弱词）、`macro-inc/macro`（5853，117；描述里的 agents 与 AI memory 是弱词）、`expo/skills`（3880，108；描述里的 AI agent 是弱词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-10-01 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-10-01 stars:>2`。`total_count=435`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文：`onehumanbeing/esp32-iphone-agent`（4132）、`agharsallah/esp-labs-web`（608）、`Adolanium/hermes-gadget-sdk`（455）、`raullenchai/esp32-thinks`（260）、`Liu-zhongxian/zongzhu-bot`（231）。`esp32-iphone-agent` 和 `esp32-thinks` 同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`zongzhu-bot` 话题含 `grok` 与 `voice-assistant`，没有 `llm`，不跨到 AI。`esp-labs-web` 话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单或 awesome 合集，正文保留。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-10-01 stars:>2`。`total_count=2498`，返回 5，规则保留 2，未命中 3，排除清单 0。剩余配额 9。正文保留 `QingYunA/answer-me-with-html`（4900）、`Leonxlnx/earshot`（3316）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`openfilm/openfilm`（总 star 3763；描述里的 AI video agent 是弱词）、`cranebeaker/coop-anything`（总 star 1648；描述里的 AI agent 与 MCP 是弱词）、`CopilotKit/OpenDuet`（总 star 1644；描述里的 AI agent 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-10-01 stars:>2`。`total_count=3`，返回 3，规则保留 2，未命中 1。剩余配额 9。本查询只有 3 条满足条件，所以不足 5 条。规则保留的 2 条里，1 条撞名剔除，1 条更贴近自动控制，本节只留一行。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `Samarth030312/arduino-water-level-control-lab`（总 star 8）：描述里的 MOSFET 是直流泵的开关，话题含 `control-systems`。完整条目在自动控制，本节一行带过。
  - 名称和 topics 未命中：`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`Sichuan` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-10-01 stars:>2`。`total_count=68`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称、话题和描述都没有 `mppt`、`bms`、`inverter`、`dc-dc`、`llc`：`4DCodeBench/4DCodeBench`（200）、`CompaLarios18/MH4UltimateDC`（79）、`two-delta/DCOCO`（56；描述为空）、`Lida-V/3DCharaMakeSkills-Lida`（54）、`meztinos515/Acrobat-Pro-DC`（36；描述是 PDF 工具）。检索词 `dc-dc` 在搜索侧会撞上仓库名或 README 里的 DC。名称里能看到 DC 的是 `MH4UltimateDC`、`DCOCO`、`Acrobat-Pro-DC`。`4DCodeBench` 与 `3DCharaMakeSkills-Lida` 的名称和描述里没有这些词，命中点不在接口返回的名称、话题和描述中。分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-10-01 stars:>2`。`total_count=64`，返回 5，规则保留 4，未命中 1。剩余配额 8。正文保留 `mozihe/z-localization`（111）、`TrentIndeed/kinetiqgym`（102）、`prohurtz/BSB-SLAM`（33）。另有 1 条完整条目来自功率器件检索：`arduino-water-level-control-lab`（8），因为水位控制比 MOSFET 开关更贴近本领域。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 82）。话题含 `ros2` 与 `slam`，描述写明是机器人开发自学课程地图和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。
  - 名称和 topics 未命中：`lbgos/rift-s-linux`（32；描述里的 SLAM 是空格写法，不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-24 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-24 stars:>3`。`total_count=1228`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。正文完整条目 5 条：`ruvnet/RuView`（101760）、`raysan5/raylib`（35496）、`78/xiaozhi-esp32`（32294）、`lvgl/lvgl`（25056）、`arendst/Tasmota`（24948）。`makerspet/oomwoo`（12884）来自自动控制检索，话题含 `esp32`，本节一行。`RuView` 话题含 `awesome`，仓库名不是 awesome 合集，README 写的是 Wi-Fi 感知平台，正文保留。`xiaozhi-esp32` 话题含 `mcp`，裸 `mcp` 不是 AI 关键词；README 里出现 LLM，但搜索描述和话题没有 `llm`，不跨到 AI。`raylib` 是游戏编程库，README 写明适合嵌入式和教学，不是公开课清单。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-24 stars:>3`。`total_count=8885`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 9。正文保留 `firecrawl/firecrawl`（197099；话题 `llm` 与 `ai-agents`）、`DietrichGebert/ponytail`（180947；话题 `llm` 与 `ai-agents`）、`huggingface/transformers`（168372；话题 `llm`、`pytorch`、`transformer`）、`langgenius/dify`（160025；话题 `llm`）。
  - 未命中：`msitarzewski/agency-agents`（总 star 165496；名称 `agency-agents` 按词边界不等于 `ai-agents`，描述里的 AI agency 是弱词）。它夹在本页 `huggingface/transformers` 与 `langgenius/dify` 之间，所以本页按总 star 不是连续的 4 个命中仓库。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-24 stars:>3`。`total_count=27`，返回 5，规则保留 0，未命中 4。剩余配额 9。`page=1`、`per_page=5`，本页返回满 5 条。正文写「本页无符合领域的常青仓库」。
  - 名称按词边界不等于 `sic`，也没有功率器件话题：`SickChill/sickchill`（2445）、`mdhiggins/sickbeard_mp4_automator`（1589；`sickbeard` 不等于 `sic`）、`source-academy/sicp`（1026）、`siconos/siconos`（188）。
  - `microsoft/Sico`（283）名称不等于 `sic`，话题含 `llm`，但不在 AI 常青前 5，不跨节。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-24 stars:>3`。`total_count=397`，返回 5，规则保留 1，未命中 3。剩余配额 8。规则保留的 `Finbuckle/Finbuckle.MultiTenant`（1633）人工剔除后，正文没有电力电子条目。
  - `Finbuckle/Finbuckle.MultiTenant`：描述里的 LLC 是维护者公司后缀，不是谐振变换器，正文不收。
  - 名称和 topics 未命中：`dalathegreat/Battery-Emulator`（2997；描述是 solar inverters，复数按词边界不等于 `inverter`）、`mjbots/moteus`（1354；描述是 “Brushless DC motor controller”，空格写法不是 `motor-control`，名称也没有 `bldc`）、`rordenlab/dcm2niix`（1210；名称里的 DC 不等于 `dc-dc`）。
  - `tbnobody/OpenDTU`（2205）描述是 Inverters（复数，不等于 `inverter`），话题含 `esp32`，因此归入嵌入式而不是电力电子。它不在嵌入式常青前 5，不跨节。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-24 stars:>3`。`total_count=234`，返回 5，规则保留 5，清单类排除 0。剩余配额 7。正文保留 `AtsushiSakai/PythonRobotics`（30828）、`makerspet/oomwoo`（12884）、`betaflight/betaflight`（11725）、`MichaelGrupp/evo`（4352）。`oomwoo` 同时话题含 `esp32`，嵌入式一节一行。`PythonRobotics` 是示例代码和教材，不是公开课清单或 awesome 合集，正文保留。`betaflight` 的 README 写了 STM32 目标，并写了实验性 ESP32；搜索话题只有 `flight-controller` 等，搜索描述没有这些芯片名，不跨到嵌入式。
  - 撞名剔除：`Aleksoid1978/MPC-BE`（总 star 4634）。名称含 `mpc`，描述写明是 Windows 上的音视频播放器，与模型预测控制无关，正文不收。
