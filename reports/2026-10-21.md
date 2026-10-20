# GitHub 领域日报 · 2026-10-21

生成时间：2026-10-21 07:36（北京时间）。数据拉取开始于 2026-10-21 07:32:21（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-21（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-14 及之后有推送、总 star > 3。轮换页 `page = (当年第 294 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) 在工具输出、日志和检索片段进大模型之前先压缩，让编程代理少烧 token；今日热度命中，总 star 76736，24 小时新增 star 555。
2. [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) 在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，要确认时可以就地批准；近 30 天新建，总 star 5643。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，不必用 Mac，也不必越狱；近 30 天新建，总 star 3395。

## A. 今日热度

Trending 页面解析到 13 条。页面不带 topics，因此只按仓库名和强特征描述归类。规则命中 1 条，清单类排除 0 条。按 24 小时新增 star 降序。

- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)
  - 说明：在工具输出、日志、文件和检索片段送进大模型之前先压缩，编程代理大约少用两成 token，JSON 可以压掉大部分，答案保持不变。
  - 领域：AI
  - 总 star：76736
  - 24 小时新增 star：555

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：3395
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：1049
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：420
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：236
- [andrisgauracs/wifi-sensing-kit](https://github.com/andrisgauracs/wifi-sensing-kit)
  - 说明：用三块约 10 美元的 ESP32-S3，靠 WiFi 信号判断人在做什么，训练时用摄像头当老师。
  - 领域：嵌入式 Embedded
  - 总 star：183

### AI

- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：5643
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：4098
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：3395。
- [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu)
  - 说明：把 AI 写出来的日语改成读起来自然的日语，作为给编程代理用的推敲技能，而不是另做一套翻译器。
  - 领域：AI
  - 总 star：2346
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：1942
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：236。

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
  - 总 star：126
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：74

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 3。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件，Sub-GHz、NFC、红外这些功能都跑在板载 STM32 上。
  - 领域：嵌入式 Embedded
  - 总 star：16754
- [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder)
  - 说明：跑在 ESP32 上的 WiFi/蓝牙探测固件，用来看周围无线环境，也可以接到 Flipper Zero 上。
  - 领域：嵌入式 Embedded
  - 总 star：12856
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：12219。
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用 YAML 配置 ESP32、ESP8266 等芯片上的外设，再接到家庭自动化系统里远程控制，不必为每个节点重写固件。
  - 领域：嵌入式 Embedded
  - 总 star：11926
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给小智 ESP32 语音设备提供后端，用来尽快搭起设备控制服务器。
  - 领域：嵌入式 Embedded
  - 总 star：10952
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：706。

### AI

- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：把 Gemini 放进终端，做成开源的命令行编程助手。
  - 领域：AI
  - 总 star：107473
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：用张量和动态计算图在 Python 里做神经网络，并靠 GPU 加速训练和推理。这是框架本体。
  - 领域：AI
  - 总 star：104944
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
  - 说明：编程助手换一次会话就会忘掉刚才做过什么。它把会话里的操作压缩保存，下次再把相关上下文注入回去。
  - 领域：AI
  - 总 star：101957
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
  - 说明：给智能体一个命令行去读和搜索推特、Reddit、YouTube、GitHub、B 站和小红书，不用按网站分别接付费 API。
  - 领域：AI
  - 总 star：100279
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2169。
- [pypose/pypose](https://github.com/pypose/pypose) — 见下方「自动控制 Control」完整条目。话题含 pytorch，此处不展开。领域：AI。总 star：1614。

### 功率器件 Power Devices

本页无符合领域的常青仓库。规则命中的 `miha42-github/company_dns` 是 SEC 行业分类里的 SIC 查询，与碳化硅器件无关，不进正文。

### 电力电子电源 Power Supply

- [StephanJoubert/home_assistant_solarman](https://github.com/StephanJoubert/home_assistant_solarman)
  - 说明：把接在 Deye、Sofar、Solis、Sunsynk、Sol-Ark 等逆变器上的 Solarman 采集器读进 Home Assistant，用来在家里看这些逆变器的运行数据。
  - 领域：电力电子电源 Power Supply
  - 总 star：741
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：把阳光电源 SH*RT、SHx.RS、SH*K、SxT 这几族逆变器接到 Home Assistant，经 Modbus 读运行数据。
  - 领域：电力电子电源 Power Supply
  - 总 star：706

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：开源扫地机器人，用激光雷达做同步定位与建图，控制栈走 ROS 2；主控侧有 ESP32，但要解决的是清扫机器人怎么走。
  - 领域：自动控制 Control
  - 总 star：12219
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：移动机器人编程工具包，把定位、建图和传感器处理放在一套 C++ 库里。
  - 领域：自动控制 Control
  - 总 star：2169
- [pypose/pypose](https://github.com/pypose/pypose)
  - 说明：在流形上做可微机器人学，把李群、卡尔曼滤波和 SLAM 放进能反传的库里，用来把几何估计和网络训练接在一起。
  - 领域：自动控制 Control
  - 总 star：1614

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 13 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中并写入正文：`headroomlabs-ai/headroom`（总 star 76736，stars today 555）。描述中的 `LLM` 是强特征词。同一句里的 RAG、MCP 是弱词，不单独作为归类依据。
- 未命中（名称与强特征描述都没有领域词），括号内为总 star、stars today：`MadsLorentzen/ai-job-search`（60462，3890；名称和描述里的 AI 是弱词）、`cloudflare/security-audit-skill`（34095，1680）、`stablyai/orca`（99682，1559）、`DietrichGebert/ponytail`（169582，1396；描述里的 AI agent 是弱词）、`Comfy-Org/ComfyUI`（140726，1201；描述里的 diffusion 不是强特征词，未计入）、`ruvnet/ruflo`（77817，683；描述里的 RAG 是弱词，未计入）、`Graphify-Labs/graphify`（130192，906）、`anomalyco/opencode`（218880，1256）、`msitarzewski/agency-agents`（162311，590；名称里的 agents 不是 `ai-agents`）、`anthropics/knowledge-work-plugins`（30779，262）、`shiyu-coder/Kronos`（42334，719）、`vllm-project/vllm`（94422，98；仓库名 `vllm` 和描述里的 `LLMs` 按词边界都不等于 `llm`）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-21 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-21 stars:>2`。`total_count=394`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文。`onehumanbeing/esp32-iphone-agent`（3395）和 `raullenchai/esp32-thinks`（236）同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-21 stars:>2`。`total_count=2283`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 9。正文保留 `Louis-CFM/coucou`（5643）、`QingYunA/answer-me-with-html`（4098）、`nanaism/yomiyasu`（2346）、`Leonxlnx/earshot`（1942）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`kaankiziltug/logo-design-skill`（总 star 3852；描述里的 AI agents 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-21 stars:>2`。`total_count=5`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 7）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 5）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（18）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`SiCo`、`Sichuan` 按词边界都不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-21 stars:>2`。`total_count=75`，返回 5，规则保留 0。剩余配额 8。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（178）、`KawaiiBunga/MKVDCU-Recomp`（44）、`Lida-V/3DCharaMakeSkills-Lida`（42）、`ningbainb/Dcode`（37）、`meztinos515/Acrobat-Pro-DC`（36）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-21 stars:>2`。`total_count=49`，返回 5，规则保留 3，未命中 2。剩余配额 8。正文保留 `cocel-postech/genz-lio`（126）、`TrentIndeed/kinetiqgym`（74）。
  - `sd88me/mpc-vst-plugins`（总 star 121）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，与模型预测控制无关，正文不收。
  - 名称和 topics 未命中：`xwtk/hmg_nemesis`（80）、`lbgos/rift-s-linux`（25；描述里的 SLAM 不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-14 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-14 stars:>3`。`total_count=1151`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。这 5 条都写入正文。`makerspet/oomwoo` 同时话题含 `ros2` 与 `slam`，要解决的是扫地机器人怎么走，完整条目在自动控制，本节一行带过。`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant` 不在这 5 条里，来自电力电子检索；话题含 `modbus`，本节一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-14 stars:>3`。`total_count=8569`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 8。正文保留 `google-gemini/gemini-cli`（107473，topic `ai-agents`）、`pytorch/pytorch`（104944，仓库名命中 `pytorch`）、`thedotmack/claude-mem`（101957，topic `ai-agents`）、`Panniantong/Agent-Reach`（100279，话题 `llm-tools` 按词边界命中 `llm`）。另有两行来自自动控制检索：`MRPT/mrpt`（话题含 `computer-vision`）、`pypose/pypose`（话题含 `pytorch`）。
  - 未命中：`nexu-io/open-design`（总 star 102803）。描述里的 AI agents 是弱词，名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-14 stars:>3`。`total_count=18`，返回 5，规则保留 1，清单类排除 1，未命中 3。剩余配额 7。规则保留的那条人工剔除后，本页没有功率器件完整条目。
  - `miha42-github/company_dns`（总 star 10）：话题和描述含 SIC，内容是 SEC EDGAR 的公司数据与行业分类 SIC 查询，与碳化硅器件无关，正文不收。
  - 清单类排除：`satnamrsm/https-github.com-sickn33-antigravity-awesome-skills`（总 star 8）。名称含 awesome，是技能合集镜像，且 `sickn33` 按词边界不等于 `sic`，不进正文。
  - 名称按词边界不等于 `sic`：`linuxserver/docker-sickgear`（12）、`feddelegrand7/sicher`（10）、`reekta92/sicth`（7）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-14 stars:>3`。`total_count=363`，返回 5，规则保留 2，未命中 3。剩余配额 9。正文完整条目为 `StephanJoubert/home_assistant_solarman`（741，topic `inverter`）和 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（706，topic `inverter`）。阳光电源那条同时话题含 `modbus`，嵌入式一节一行带过。
  - 名称和 topics 未命中电力电子：`decred/dcrd`（775）、`hackthedev/dcts-shipping`（645）、`AAFOptimus/AAFFamilyDCHAudio`（556）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-14 stars:>3`。`total_count=198`，返回 5，规则保留 2，清单类排除 1，未命中 2。剩余配额 9。正文保留 `MRPT/mrpt`（2169）、`pypose/pypose`（1614）。`makerspet/oomwoo`（12219）来自嵌入式检索，话题含 `ros2` 与 `slam`，完整条目写在本节。`MRPT/mrpt` 同时话题含 `computer-vision`，`pypose/pypose` 同时话题含 `pytorch`，AI 一节各一行带过。
  - 清单类排除：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2151）。话题含 `slam`，是 NeRF / 3DGS 论文合集，不进正文。
  - 未命中：`ldrolez/free-midi-chords`（2344；描述里的 Akai MPC 不是仓库名上的 `mpc`）、`nvidia-isaac/cuVSLAM`（1871；名称按词边界不等于 `slam`）。
