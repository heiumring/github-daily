# GitHub 领域日报 · 2026-10-15

生成时间：2026-10-15 07:35（北京时间）。数据拉取开始于 2026-10-15 07:31:18（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-15（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-08 及之后有推送、总 star > 3。轮换页 `page = (当年第 288 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) 用一次前向做分类、打分和是否判断，而不是逐字生成；近 30 天新建，总 star 32909。
2. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真机 iPhone；近 30 天新建，总 star 2068。
3. [lokutor-ai/oido](https://github.com/lokutor-ai/oido) 把开放词表语音识别放进约 5 美元的 ESP32-S3，仓库写明 LibriSpeech 词错误率 3.7%，不走云端；近 30 天新建，总 star 110。

## A. 今日热度

Trending 页面解析到 12 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。嵌入式、AI、功率器件、电力电子电源、自动控制在这 12 条里都没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：2068
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：913
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：384
- [andrisgauracs/wifi-sensing-kit](https://github.com/andrisgauracs/wifi-sensing-kit)
  - 说明：用三块约 10 美元的 ESP32-S3，靠 WiFi 信号判断人在做什么，训练时用摄像头当老师。
  - 领域：嵌入式 Embedded
  - 总 star：147
- [lokutor-ai/oido](https://github.com/lokutor-ai/oido)
  - 说明：在约 5 美元的 ESP32-S3 上做开放词表语音识别，不依赖云端，也不依赖 NPU；仓库写明 LibriSpeech 词错误率 3.7%。
  - 领域：嵌入式 Embedded
  - 总 star：110

### AI

- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
  - 说明：用一次前向完成文本上的分类、打分和是否判断，并按请求挑选检查点，覆盖描述中的 100 多种语言。
  - 领域：AI
  - 总 star：32909
- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：5214
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：2068。
- [Lee-Jun-Hyuk-37/Lambda-Hold](https://github.com/Lee-Jun-Hyuk-37/Lambda-Hold) — 见下方「自动控制 Control」完整条目。话题含 reinforcement-learning，此处不展开。领域：AI。总 star：20。

### 功率器件 Power Devices

- [tPkl/OpenRdson](https://github.com/tPkl/OpenRdson)
  - 说明：开源的场效应管版图寄生参数提取，用网格和有限元去对标 Synopsys / SFT 的 R3D，给模拟版图做提取。
  - 领域：功率器件 Power Devices
  - 总 star：6

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [cocel-postech/genz-lio](https://github.com/cocel-postech/genz-lio)
  - 说明：激光雷达加 IMU 的里程计，针对室内外和退化场景把位姿估稳；仓库标明发表于 IEEE T-FR 2026。
  - 领域：自动控制 Control
  - 总 star：93
- [HengyiWang/amb3r-slam](https://github.com/HengyiWang/amb3r-slam)
  - 说明：面向公里级范围的 SLAM，用分层后端处理很长的轨迹，而不是只在室内小地图里定位。
  - 领域：自动控制 Control
  - 总 star：75
- [Lee-Jun-Hyuk-37/Lambda-Hold](https://github.com/Lee-Jun-Hyuk-37/Lambda-Hold)
  - 说明：λ-Hold 控制的官方实现，用来做肌肉骨骼系统的预测仿真，让仿真里的肌肉按这种保持策略往前推。
  - 领域：自动控制 Control
  - 总 star：20

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 1。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：用普通 WiFi 信号做实时空间感知、生命体征和有没有人在场，不靠摄像头画面。
  - 领域：嵌入式 Embedded
  - 总 star：97981
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：用来写游戏的 C 库；话题标明也能跑在嵌入式和 ESP32 上，因此列入这一节。
  - 领域：嵌入式 Embedded
  - 总 star：35184
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：跑在 ESP32 上的聊天机器人，通过 MCP 去接外部工具，把对话放在这块微控制器上。
  - 领域：嵌入式 Embedded
  - 总 star：31089
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：给从很小的单片机到能做 3D 的处理器做界面的嵌入式图形库，用来画屏幕上的控件。
  - 领域：嵌入式 Embedded
  - 总 star：24917
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：ESP8266 和 ESP32 的替代固件，用网页、OTA 和 MQTT 在本地控制设备，不必把开关交给云。
  - 领域：嵌入式 Embedded
  - 总 star：24860
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：11590。

### AI

- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
  - 说明：给智能体抓网页和其它来源的数据，把网站内容变成模型能读的材料。
  - 领域：AI
  - 总 star：191575
- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：定义、训练和推理文本、视觉、音频和多模态模型的框架，用来把模型真正跑起来。
  - 领域：AI
  - 总 star：167692
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
  - 说明：给编程智能体一套少写代码的技能，能不写的逻辑就不写，避免生成一堆用不上的实现。
  - 领域：AI
  - 总 star：163594
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：在一个工作区里搭智能体工作流，可以放在云上、专有网络或自己的机器上，从原型到上线不必另起一套。
  - 领域：AI
  - 总 star：158487

### 功率器件 Power Devices

本页没有可列入正文的功率器件仓库。

### 电力电子电源 Power Supply

本页没有可列入正文的电力电子电源仓库。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：用 Python 示例把 SLAM、定位、路径规划这些机器人算法收成能直接跑的代码和讲义。
  - 领域：自动控制 Control
  - 总 star：30693
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：开源飞控固件，用来在穿越机等飞行器上做姿态解算和电机输出。
  - 领域：自动控制 Control
  - 总 star：11657
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：开源扫地机器人，用激光雷达 SLAM 和 ROS 2 做导航，而不是只沿墙乱走。
  - 领域：自动控制 Control
  - 总 star：11590

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 12 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），括号内为总 star、stars today：`morluto/rea`（240680，41187）、`debpalash/VoiceStudio`（66223，3547）、`ifixai-ai/iFixAi`（27334，2143）、`xtool-org/xtool`（10749，1510）、`vxcontrol/pentagi`（29394，1070；描述写 “AI Agents”，中间是空格，不是 `ai-agents`，且该词不是强特征描述词）、`NationalSecurityAgency/ghidra`（87445，1002）、`mksglu/context-mode`（29081，946；描述里的 AI、MCP 是弱词，未计入）、`rust-lang/rust`（120007，205）、`ntdevlabs/tiny11builder`（20198，194）、`K-Dense-AI/scientific-agent-skills`（49296，146；名称和描述里的 AI 是弱词）、`HKUDS/CLI-Anything`（52465，94）、`nvm-sh/nvm`（95445，70）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-15 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-15 stars:>2`。`total_count=378`，返回 5，规则保留 5，排除清单 0。剩余配额 9。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-15 stars:>2`。`total_count=2072`，返回 5，规则保留 2，未命中 3，排除清单 0。剩余配额 9。正文另有 2 条跨领域一行：`esp32-iphone-agent` 来自嵌入式检索，`Lambda-Hold` 来自自动控制检索。
  - 未命中：`zai-org/ZCode`（总 star 7826）、`mizorewww/laya-mlx`（6931；描述里的 PyTorch 出现在否定句里，且 `pytorch` 不是强特征描述词）、`mhtsec/ARTEX`（4074）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-15 stars:>2`。`total_count=6`，返回 5，规则保留 2，未命中 3。剩余配额 9。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 6）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（16）、`MadestSamurai/bd2-sichuan`（13）、`MicroFarmerVoyage/hellraiser-revival-motion-sickness-tool`（8）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-15 stars:>2`。`total_count=71`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（146）、`ningbainb/Dcode`（37）、`KawaiiBunga/MKVDCU-Recomp`（36）、`meztinos515/Acrobat-Pro-DC`（35）、`lamb2k/re4dc`（27）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-15 stars:>2`。`total_count=50`，返回 5，规则保留 4，未命中控制关键词 1。剩余配额 8。正文保留 3 条。`Lambda-Hold` 同时话题含 `reinforcement-learning`，完整条目在本节，AI 一节一行带过。
  - `sd88me/mpc-vst-plugins`（总 star 116）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，与模型预测控制无关，正文不收。
  - `xwtk/hmg_nemesis`（65）：名称和 topics 未命中。

### C. 领域常青（`pushed:>=2026-10-08 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-08 stars:>3`。`total_count=1123`，返回 5，规则保留 5，清单类排除 0。剩余配额 7。`ruvnet/RuView` 的话题里有 `awesome`，仓库名不是 awesome 合集，描述是 WiFi 空间感知，不按清单排除。`makerspet/oomwoo` 不在这 5 条里，因话题含 `esp32`，本节一行带过，完整条目在自动控制。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-08 stars:>3`。`total_count=8379`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 8。
  - 未命中：`msitarzewski/agency-agents`（总 star 160098）。名称和 topics 没有 llm / pytorch / transformer / diffusion / ai-agents。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-08 stars:>3`。`total_count=20`，返回 5，规则保留 1，未命中 3，另有 1 条只命中 AI。剩余配额 9。本页没有可展开的功率器件条目。
  - `epilys/sic`（总 star 26）：仓库名是 `sic`，内容是按标签组织的链接聚合站，与碳化硅器件无关，正文不收。
  - `scitix/siclaw`（总 star 238）：`siclaw` 按词边界不等于 `sic`，不归入功率器件。话题含 `llm` 与 `ai-agents`，但不在 AI 查询的前 5 条里，正文不单列。
  - 名称和 topics 未命中：`SickChill/sickchill`（2442）、`siconos/siconos`（186）、`SICKAG/sick_safetyscanners_base`（20）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-08 stars:>3`。`total_count=367`，返回 5，规则保留 1，未命中功率电子关键词 4。剩余配额 9。规则保留的那条经人工剔除后，本页没有可列入正文的仓库。
  - `Finbuckle/Finbuckle.MultiTenant`（总 star 1630）：描述里的 `LLC` 是公司后缀（Finbuckle LLC），不是谐振变换器 LLC，正文不收。
  - `dalathegreat/Battery-Emulator`（2971）：描述写到 solar inverters。`inverters` 按词边界不等于 `inverter`，未计入。
  - `tbnobody/OpenDTU`（2196）：描述里的 Inverters 同样是复数，未计入电力电子；话题含 `esp32`，因此命中嵌入式，但不在嵌入式查询的前 5 条里，正文不单列。
  - 名称和 topics 未命中电力电子：`ajnart/dcm`（1443）。
  - `pnoker/iot-dc3`（1287）：名称里的 DC3 被检索词 `dc-dc` 撞上。分类未命中电力电子；话题含 `modbus` 与 `ai-agents`，但不在嵌入式或 AI 查询的前 5 条里，正文不单列。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-08 stars:>3`。`total_count=217`，返回 5，规则保留 4，未命中 1。剩余配额 8。正文保留 3 条。`makerspet/oomwoo` 同时话题含 `esp32`，完整条目在本节，嵌入式一节一行带过。
  - `Aleksoid1978/MPC-BE`（总 star 4584）：仓库名命中 `mpc`，实为 Windows 音视频播放器，与模型预测控制无关，正文不收。
  - 未命中：`wesbos/beginner-javascript`（6772）。描述是 “Slam Dunk JavaScript”，`slam` 不是强特征描述词，名称和 topics 也没有控制关键词。
