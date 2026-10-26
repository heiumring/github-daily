# GitHub 领域日报 · 2026-10-27

生成时间：2026-10-27 07:34（北京时间）。数据拉取开始于 2026-10-27 07:31:11（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-27（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-20 及之后有推送、总 star > 3。轮换页 `page = (当年第 300 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) 用多个大模型代理搭一套金融交易框架；今日热度里新增最多，总 star 116032，24 小时新增 star 1376。
2. [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) 用一份 CLAUDE.md 约束 Claude Code，针对 Karpathy 指出的大模型写代码时容易踩的坑；总 star 224611，24 小时新增 star 702。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，眼睛走 AirPlay，手走 USB HID；近 30 天新建，总 star 3946。

## A. 今日热度

Trending 页面解析到 14 条。页面不带 topics，因此只按仓库名和强特征描述归类。规则命中 2 条，清单类排除 0 条。按 24 小时新增 star 降序。

- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
  - 说明：多个大模型代理组成一套金融交易框架，用来把交易决策交给这组代理。
  - 领域：AI
  - 总 star：116032
  - 24 小时新增 star：1376
- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
  - 说明：一份 CLAUDE.md，用来纠正 Claude Code 写代码时的典型大模型毛病，依据是 Karpathy 对 LLM 编程坑的观察。
  - 领域：AI
  - 总 star：224611
  - 24 小时新增 star：702

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：3946
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：1134
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：446
- [agharsallah/esp-labs-web](https://github.com/agharsallah/esp-labs-web)
  - 说明：把 ESP32-S3 实验台收成一个网页，能看实时引脚、跑交互模拟、读 esp-labs 固件和实验记录，界面有 11 种语言。
  - 领域：嵌入式 Embedded
  - 总 star：342
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：255

### AI

- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor、Gemini CLI、Antigravity 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：6567
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：4496
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：3946。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：2905
- [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu)
  - 说明：把 AI 写出来的日语改成读起来自然的日语，作为给编程代理用的推敲技能，而不是另做一套翻译器。
  - 领域：AI
  - 总 star：2575
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：255。

### 功率器件 Power Devices

本日无新项目。

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：92
- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室把 2026 年 RoboMaster 超级对抗赛哨兵的定位开源出来，用 Livox MID360 做激光雷达与 IMU 里程计，并带重定位，跑在 ROS 2 上。
  - 领域：自动控制 Control
  - 总 star：89

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 1。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：把普通 Wi-Fi 信号变成实时的空间感知、生命体征和在场检测，全程不用摄像头。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：99748
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：一套用来写游戏的简单 C 库，话题标明也能用在嵌入式和 ESP32 上，不必先搭一整套引擎。
  - 领域：嵌入式 Embedded
  - 总 star：35433
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：跑在 ESP32 上的聊天机器人，仓库写明基于 MCP。
  - 领域：嵌入式 Embedded
  - 总 star：32006
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：给从单片机到带 3D 的处理器做嵌入式界面，ESP32、STM32 和 Zephyr 都能用，用来在小屏上画控件而不必从帧缓冲写起。
  - 领域：嵌入式 Embedded
  - 总 star：25011
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：给 ESP8266 和 ESP32 设备换一套可本地配置的固件，用网页、定时规则和 MQTT、HTTP、串口或 KNX 做控制，不把设备交给云。
  - 领域：嵌入式 Embedded
  - 总 star：24922
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：12767。

### AI

- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
  - 说明：给 AI 代理补上网页和外部数据，把抓到的内容变成模型能直接用的材料。
  - 领域：AI
  - 总 star：195690
- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：用同一套接口定义、训练和推理文本、视觉、音频和多模态模型，不必为每种模型另写一套加载代码。
  - 领域：AI
  - 总 star：168211
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：在一个工作区里搭代理工作流和检索流水线，云端、专有网络或自托管都能部署，从原型到上线不用换一套栈。
  - 领域：AI
  - 总 star：159627

### 功率器件 Power Devices

本页无符合领域的常青仓库。返回的 5 条里，名称按词边界都不等于 `sic`（`sickbeard`、`sicp`、`Sico`、`siconos`、`sicp-racket`），没有功率器件话题。

### 电力电子电源 Power Supply

本页无符合领域的常青仓库。规则命中的 `Finbuckle/Finbuckle.MultiTenant` 描述里的 LLC 是公司后缀，不是谐振变换器，正文不收。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：用 Python 示例和讲义实现机器人算法，话题覆盖 SLAM、定位、建图和路径规划，用来对着代码把这些算法跑通。
  - 领域：自动控制 Control
  - 总 star：30808
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：开源扫地机器人，话题覆盖 ROS 2、激光 SLAM 和 ESP32。
  - 领域：自动控制 Control
  - 总 star：12767
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：开源飞控固件，用来直接刷飞行控制器，不必从零写飞控程序。
  - 领域：自动控制 Control
  - 总 star：11706
- [MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)
  - 说明：用 Python 评估里程计和 SLAM 的轨迹，对着 KITTI、EuRoC、TUM 这些公开序列算误差，用来比较算法，而不是再写一套建图程序。
  - 领域：自动控制 Control
  - 总 star：4347

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 14 条，规则命中 2 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中：`TauricResearch/TradingAgents`（总 star 116032，stars today 1376）、`multica-ai/andrej-karpathy-skills`（总 star 224611，stars today 702）。两条描述都含强特征词 LLM，归入 AI。`andrej-karpathy-skills` 描述写明是一份 CLAUDE.md，不是公开课清单或 awesome 合集，正文保留。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`debpalash/VoiceStudio`（89139，2292）、`Nutlope/hallmark`（36222，2235；描述里的 AI 是弱词）、`pbakaus/impeccable`（89133，1551；描述里的 AI 是弱词）、`makecindy/cindy`（6417，1268；描述里的 AI Agent 是弱词）、`JetBrains/thinkrail`（2854，1156）、`affaan-m/ECC`（289808，987）、`pollen-robotics/microduck`（12383，844；双足小鸭机器人，名称和描述都没有领域词）、`Panniantong/Agent-Reach`（103517，723；描述里的 AI agent 是弱词）、`alchaincyf/huashu-design`（26715，409；描述里的 agent 是弱词）、`nightly-labs/openbot`（1449，312；描述里的 AI teammates 是弱词）、`NVIDIA/SkillSpector`（22143，203；描述里的 AI agent 与 MCP 都不是强特征词）、`gitroomhq/postiz-app`（38417，146；描述里的 agentic 是弱词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-27 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-27 stars:>2`。`total_count=414`，返回 5，规则保留 5，排除清单 0。剩余配额 8。这 5 条都写入正文。`onehumanbeing/esp32-iphone-agent`（3946）和 `raullenchai/esp32-thinks`（255）同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。`agharsallah/esp-labs-web`（342）话题含 `education`，描述是 ESP32-S3 实验台网页，不是公开课清单或 awesome 合集，正文保留。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-27 stars:>2`。`total_count=2409`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 8。正文保留 `Louis-CFM/coucou`（6567）、`QingYunA/answer-me-with-html`（4496）、`Leonxlnx/earshot`（2905）、`nanaism/yomiyasu`（2575）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`openfilm/openfilm`（总 star 3019；描述里的 AI video agent 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-27 stars:>2`。`total_count=4`，返回 4，规则保留 2，未命中 2。剩余配额 7。规则保留的 2 条都是撞名，正文写「本日无新项目」。
  - `marozols/SIC-existence`（总 star 10）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 5）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（25）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`SiCo`、`Sichuan` 按词边界都不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-27 stars:>2`。`total_count=77`，返回 5，规则保留 0。剩余配额 8。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（190）、`CompaLarios18/MH4UltimateDC`（62）、`two-delta/DCOCO`（54；描述为空）、`Lida-V/3DCharaMakeSkills-Lida`（52）、`lamb2k/re4dc`（37）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-27 stars:>2`。`total_count=58`，返回 5，规则保留 3，未命中 2。剩余配额 7。正文保留 `TrentIndeed/kinetiqgym`（92）、`mozihe/z-localization`（89）。
  - 清单类剔除：`woolimi/robotics-roadmap`（总 star 56）。话题含 `ros2` 与 `slam`，描述写明是机器人开发自学课程地图和面试型测验，属课程清单，不进正文。脚本的清单规则没有命中这条韩文描述，此处人工剔除。
  - 名称和 topics 未命中：`xwtk/hmg_nemesis`（225）、`lbgos/rift-s-linux`（32；描述里的 SLAM 不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-20 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-20 stars:>3`。`total_count=1169`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。这 5 条都写入正文。`ruvnet/RuView` 话题里有 `awesome`，仓库名和描述都不是合集，是 Wi-Fi 空间感知项目，正文保留。另有一行 `makerspet/oomwoo`，来自自动控制检索，话题含 `esp32`。`78/xiaozhi-esp32` 话题含 `mcp`，裸 `mcp` 不是 AI 关键词，不跨到 AI。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-20 stars:>3`。`total_count=8802`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `firecrawl/firecrawl`（195690，topic `llm` 与 `ai-agents`）、`huggingface/transformers`（168211，topic `llm`、`pytorch`、`transformer`）、`langgenius/dify`（159627，topic `llm`）。
  - 未命中：`msitarzewski/agency-agents`（总 star 164258）。`agency-agents` 按词边界不等于 `ai-agents`，名称和 topics 都没有领域关键词。`langflow-ai/langflow`（总 star 156041）。描述里的 AI-powered agents 是弱词，名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-20 stars:>3`。`total_count=24`，返回 5，规则保留 0，未命中功率器件 5。剩余配额 9。`page=1`、`per_page=5`。本页正文为空。
  - 名称按词边界不等于 `sic`，也没有功率器件话题：`mdhiggins/sickbeard_mp4_automator`（1588）、`source-academy/sicp`（1024）、`microsoft/Sico`（282；话题含 `llm`，但不是本页 AI 检索结果，不跨节）、`siconos/siconos`（187）、`hexlet-boilerplates/sicp-racket`（136；描述为空）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-20 stars:>3`。`total_count=390`，返回 5，规则保留 1，未命中电力电子 3，另有 1 条命中嵌入式但不在嵌入式检索前 5。剩余配额 8。规则保留的 1 条人工剔除后，本页正文为空。
  - `Finbuckle/Finbuckle.MultiTenant`（总 star 1631）：描述 “maintained by Finbuckle LLC” 命中强特征词 `llc`，这是公司后缀，不是谐振变换器，正文不收。
  - 名称和 topics 未命中电力电子：`dalathegreat/Battery-Emulator`（2992；描述写 solar inverters，复数 `inverters` 按词边界不等于 `inverter`）、`tbnobody/OpenDTU`（2203；描述是 “talk to … Inverters”，同样是复数，未归入电力电子；话题含 `esp32`，但不是本页嵌入式检索的前 5，不跨节）、`dcm4che/dcm4che`（1465）、`ajnart/dcm`（1448）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-20 stars:>3`。`total_count=232`，返回 5，规则保留 5，未命中 0。剩余配额 9。正文保留 `AtsushiSakai/PythonRobotics`（30808）、`makerspet/oomwoo`（12767）、`betaflight/betaflight`（11706）、`MichaelGrupp/evo`（4347）。`oomwoo` 同时话题含 `esp32`，完整条目在本节，嵌入式一节一行带过。
  - `Aleksoid1978/MPC-BE`（总 star 4631）：仓库名命中 `mpc`，实为 Windows 音视频播放器，与模型预测控制无关，正文不收。
