# GitHub 领域日报 · 2026-10-19

生成时间：2026-10-19 07:35（北京时间）。数据拉取开始于 2026-10-19 07:30:58（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-19（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-12 及之后有推送、总 star > 3。轮换页 `page = (当年第 292 天 mod 4) + 1 = 1`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) 在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，要确认时可以就地批准；近 30 天新建，总 star 5525。
2. [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) 让代理把难问题答成一页能直接读的 HTML；近 30 天新建，总 star 3695。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，不必用 Mac，也不必越狱；近 30 天新建，总 star 3107。

## A. 今日热度

Trending 页面解析到 13 条。页面不带 topics，因此只按仓库名和强特征描述归类。规则命中 1 条：`mlabonne/llm-course`（总 star 84001，24 小时新增 star 81）。它是大模型入门路线图，README 写明是一份 notebook 和文章清单，话题含 `course`、`roadmap`，按公开课清单不进正文。

本日无命中领域的热门仓库。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：3107
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：1022
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：407
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：222
- [andrisgauracs/wifi-sensing-kit](https://github.com/andrisgauracs/wifi-sensing-kit)
  - 说明：用三块约 10 美元的 ESP32-S3，靠 WiFi 信号判断人在做什么，训练时用摄像头当老师。
  - 领域：嵌入式 Embedded
  - 总 star：176

### AI

- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：5525
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：3695
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：3107。
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：222。

### 功率器件 Power Devices

- [tPkl/OpenRdson](https://github.com/tPkl/OpenRdson)
  - 说明：用开源网格和有限元做场效应管版图的寄生参数提取，用来替代 Synopsys / SFT 的 R3D。
  - 领域：功率器件 Power Devices
  - 总 star：6

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [cocel-postech/genz-lio](https://github.com/cocel-postech/genz-lio)
  - 说明：激光雷达加 IMU 的里程计，针对室内外和退化场景把位姿估稳；仓库标明发表于 IEEE T-FR 2026。
  - 领域：自动控制 Control
  - 总 star：113
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：52

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 1。

### 嵌入式 Embedded

- [ruvnet/RuView](https://github.com/ruvnet/RuView)
  - 说明：把普通 Wi-Fi 信号变成实时的空间感知、生命体征和在场检测，全程不用摄像头。话题含 esp32 与 firmware。
  - 领域：嵌入式 Embedded
  - 总 star：98652
- [raysan5/raylib](https://github.com/raysan5/raylib)
  - 说明：一套用来写游戏的简单 C 库，话题标明也能用在嵌入式和 ESP32 上，不必先搭一整套引擎。
  - 领域：嵌入式 Embedded
  - 总 star：35296
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
  - 说明：跑在 ESP32 上的聊天机器人，用 MCP 把语音设备和模型接起来。
  - 领域：嵌入式 Embedded
  - 总 star：31435
- [lvgl/lvgl](https://github.com/lvgl/lvgl)
  - 说明：给从单片机到带 3D 的处理器做嵌入式界面，ESP32、STM32 和 Zephyr 都能用，用来在小屏上画控件而不必从帧缓冲写起。
  - 领域：嵌入式 Embedded
  - 总 star：24960
- [arendst/Tasmota](https://github.com/arendst/Tasmota)
  - 说明：给 ESP8266 和 ESP32 设备换一套可本地配置的固件，用网页、定时规则和 MQTT 做控制，不把设备交给云。
  - 领域：嵌入式 Embedded
  - 总 star：24874
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：12124。

### AI

- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
  - 说明：给 AI 代理补上网页和外部数据，把抓到的内容变成模型能直接用的材料。
  - 领域：AI
  - 总 star：192766
- [huggingface/transformers](https://github.com/huggingface/transformers)
  - 说明：用同一套接口定义、训练和推理文本、视觉、音频和多模态模型，不必为每种模型另写一套加载代码。
  - 领域：AI
  - 总 star：167823
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
  - 说明：让编程代理按「能不写就不写」来做事，少交一堆没必要的代码。
  - 领域：AI
  - 总 star：167017
- [langgenius/dify](https://github.com/langgenius/dify)
  - 说明：在一个工作区里搭代理工作流和检索流水线，云端、专有网络或自托管都能部署，从原型到上线不用换一套栈。
  - 领域：AI
  - 总 star：158810

### 功率器件 Power Devices

本页无符合领域的常青仓库。返回的 5 条里，名称按词边界都不等于 `sic`（`sickchill`、`sicp`、`Sico`、`siclaw`、`siconos`），没有功率器件话题。

### 电力电子电源 Power Supply

本页无符合领域的常青仓库。规则命中的 `Finbuckle/Finbuckle.MultiTenant` 描述里的 LLC 是公司后缀，不是谐振变换器，正文不收。

### 自动控制 Control

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)
  - 说明：用 Python 示例和讲义实现机器人算法，话题覆盖 SLAM、定位、建图和路径规划，用来对着代码把这些算法跑通。
  - 领域：自动控制 Control
  - 总 star：30728
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：开源扫地机器人，用 ROS 2 和激光 SLAM 做导航，主控可以是 ESP32。
  - 领域：自动控制 Control
  - 总 star：12124
- [betaflight/betaflight](https://github.com/betaflight/betaflight)
  - 说明：开源飞控固件，给飞行器提供现成的飞控程序，不必从零写姿态控制。
  - 领域：自动控制 Control
  - 总 star：11672

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

`mlabonne/llm-course` 的总 star 与 24 小时新增 star 来自 Trending 页面（84001 / 81）。为确认它是不是清单，另读了仓库 README 开头：课程分成基础、科学家、工程师三部分，并写明 “A list of notebooks and articles”。这篇说明不使用仓库接口上稍后读到的 star 数。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 13 条，规则命中 1 条，清单类排除 0 条（脚本未把 `llm-course` 标成清单）。页面没有 `X-RateLimit-Remaining`。
- 规则命中后人工不进正文：`mlabonne/llm-course`（总 star 84001，stars today 81）。名称命中 `llm`。内容是大模型入门路线图和 notebook / 文章清单，话题含 `course`、`roadmap`，按公开课清单不进正文。
- 未命中（名称与强特征描述都没有领域词），括号内为总 star、stars today：`MadsLorentzen/ai-job-search`（53032，2213；名称和描述里的 AI 是弱词）、`anthropics/claude-plugins-official`（42651，1187）、`anomalyco/opencode`（216534，1417）、`cursor/plugins`（12721，351）、`ruvnet/ruflo`（76490，502；描述里的 RAG 是弱词，未计入）、`akitaonrails/ai-memory`（10454，513；名称里的 AI 是弱词）、`stablyai/orca`（96584，1146）、`HKUDS/CLI-Anything`（54568，582）、`debpalash/VoiceStudio`（75252，2098）、`android/skills`（8748，381；描述为空）、`Kruk2/jasna`（2380，115）、`Comfy-Org/ComfyUI`（138580，155；描述里的 diffusion 不是强特征词，未计入）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-19 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-19 stars:>2`。`total_count=395`，返回 5，规则保留 5，排除清单 0。剩余配额 7。这 5 条都写入正文。`onehumanbeing/esp32-iphone-agent`（3107）和 `raullenchai/esp32-thinks`（222）同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-19 stars:>2`。`total_count=2165`，返回 5，规则保留 2，未命中 3，排除清单 0。剩余配额 9。正文保留 `Louis-CFM/coucou`（5525）、`QingYunA/answer-me-with-html`（3695）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`zai-org/ZCode`（总 star 7932）、`mizorewww/laya-mlx`（6970；描述里的 PyTorch 出现在否定句里，且 `pytorch` 不是强特征描述词）、`kaankiziltug/logo-design-skill`（3690；描述里的 AI agents 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-19 stars:>2`。`total_count=5`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 6）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 4）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（18）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`SiCo`、`Sichuan` 按词边界都不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-19 stars:>2`。`total_count=75`，返回 5，规则保留 0。剩余配额 8。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（172）、`KawaiiBunga/MKVDCU-Recomp`（41）、`ningbainb/Dcode`（37）、`meztinos515/Acrobat-Pro-DC`（35）、`lamb2k/re4dc`（34）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-19 stars:>2`。`total_count=49`，返回 5，规则保留 3，未命中 2。剩余配额 7。正文保留 `cocel-postech/genz-lio`（113）、`TrentIndeed/kinetiqgym`（52）。
  - `sd88me/mpc-vst-plugins`（总 star 121）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，与模型预测控制无关，正文不收。
  - 名称和 topics 未命中：`xwtk/hmg_nemesis`（70）、`lbgos/rift-s-linux`（24；描述里的 SLAM 不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-12 stars:>3`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-12 stars:>3`。`total_count=1147`，返回 5，规则保留 5，清单类排除 0。剩余配额 6。这 5 条都写入正文。另有一行 `makerspet/oomwoo`，来自自动控制检索，话题含 `esp32`。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-12 stars:>3`。`total_count=8541`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 9。正文保留 `firecrawl/firecrawl`（192766，topic `llm` 与 `ai-agents`）、`huggingface/transformers`（167823）、`DietrichGebert/ponytail`（167017）、`langgenius/dify`（158810）。
  - 未命中：`msitarzewski/agency-agents`（总 star 161180）。`agency-agents` 按词边界不等于 `ai-agents`，名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-12 stars:>3`。`total_count=18`，返回 5，规则保留 0，未命中功率器件 5。剩余配额 9。本页正文为空。
  - 名称按词边界不等于 `sic`，也没有功率器件话题：`SickChill/sickchill`（2442）、`source-academy/sicp`（1023）、`microsoft/Sico`（283；话题含 `llm`，但不是本页 AI 检索结果，不跨节）、`scitix/siclaw`（238；话题含 `llm` 与 `ai-agents`，同样不跨节）、`siconos/siconos`（187）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-12 stars:>3`。`total_count=344`，返回 5，规则保留 1，未命中电力电子 4。剩余配额 8。规则保留的 1 条人工剔除后，本页正文为空。
  - `Finbuckle/Finbuckle.MultiTenant`（总 star 1630）：描述 “maintained by Finbuckle LLC” 命中强特征词 `llc`，这是公司后缀，不是谐振变换器，正文不收。
  - 名称和 topics 未命中电力电子：`dalathegreat/Battery-Emulator`（2978；描述写 solar inverters，复数 `inverters` 按词边界不等于 `inverter`）、`tbnobody/OpenDTU`（2198；描述是 “talk to … Inverters”，同样是复数，未归入电力电子；话题含 `esp32`，但不是本页嵌入式检索的前 5，不跨节）、`dcm4che/dcm4che`（1463）、`ajnart/dcm`（1443）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-12 stars:>3`。`total_count=210`，返回 5，规则保留 4，未命中 1。剩余配额 6。正文保留 `AtsushiSakai/PythonRobotics`（30728）、`makerspet/oomwoo`（12124）、`betaflight/betaflight`（11672）。`oomwoo` 同时话题含 `esp32`，嵌入式一节一行带过。
  - `Aleksoid1978/MPC-BE`（总 star 4598）：仓库名命中 `mpc`，实为 Windows 音视频播放器，与模型预测控制无关，正文不收。
  - 未命中：`wesbos/beginner-javascript`（6771；描述 “Slam Dunk JavaScript” 里的 Slam 不是强特征词）。
