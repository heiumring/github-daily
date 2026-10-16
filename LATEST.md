# GitHub 领域日报 · 2026-10-17

生成时间：2026-10-17 07:33（北京时间）。数据拉取开始于 2026-10-17 07:30:44（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-17（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-10 及之后有推送、总 star > 3。轮换页 `page = (当年第 290 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) 用一次前向做分类、打分和是否判断，而不是逐字生成；近 30 天新建，总 star 33167。
2. [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) 在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，要确认时可以就地批准；近 30 天新建，总 star 5374。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真机 iPhone；近 30 天新建，总 star 2850。

## A. 今日热度

Trending 页面解析到 13 条。页面不带 topics，因此只按仓库名和强特征描述归类。没有仓库的名称或强特征描述命中领域关键词。

本日无命中领域的热门仓库。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：2850
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：997
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：392
- [andrisgauracs/wifi-sensing-kit](https://github.com/andrisgauracs/wifi-sensing-kit)
  - 说明：用三块约 10 美元的 ESP32-S3，靠 WiFi 信号判断人在做什么，训练时用摄像头当老师。
  - 领域：嵌入式 Embedded
  - 总 star：166
- [cyber-murmel/esp-sdr-zephyr](https://github.com/cyber-murmel/esp-sdr-zephyr)
  - 说明：在 Zephyr 上做 ESP32 的 2.4 GHz 软件无线电，用实时系统来收这一频段的信号。
  - 领域：嵌入式 Embedded
  - 总 star：133

### AI

- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
  - 说明：用一次前向完成文本上的分类、打分和是否判断，并按请求挑选检查点，覆盖描述中的 100 多种语言。
  - 领域：AI
  - 总 star：33167
- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：5374
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：2850。

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
  - 总 star：108
- [HengyiWang/amb3r-slam](https://github.com/HengyiWang/amb3r-slam)
  - 说明：面向公里级范围的 SLAM，用分层后端处理很长的轨迹，而不是只在室内小地图里定位。
  - 领域：自动控制 Control
  - 总 star：79
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：31

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 3。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件，Sub-GHz、NFC、红外这些功能都跑在板载 STM32 上。
  - 领域：嵌入式 Embedded
  - 总 star：16735
- [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder)
  - 说明：跑在 ESP32 上的 WiFi/蓝牙探测固件，用来看周围无线环境，也可以接到 Flipper Zero 上。
  - 领域：嵌入式 Embedded
  - 总 star：12803
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：11968。
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用 YAML 配置 ESP32、ESP8266 等芯片上的外设，再接到家庭自动化系统里远程控制，不必为每个节点重写固件。
  - 领域：嵌入式 Embedded
  - 总 star：11905
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给小智 ESP32 语音设备提供后端，用来尽快搭起设备控制服务器。
  - 领域：嵌入式 Embedded
  - 总 star：10875
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：705。

### AI

- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：把大模型接口、代理循环、终端界面和编程助手命令行收成一套，用来自己搭编程代理，而不是只绑一家模型。
  - 领域：AI
  - 总 star：115735
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：把 Gemini 放进终端，做成开源的命令行编程助手。
  - 领域：AI
  - 总 star：107411
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：用张量和动态计算图在 Python 里做神经网络，并靠 GPU 加速训练和推理。这是框架本体。
  - 领域：AI
  - 总 star：104805
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2169。

### 功率器件 Power Devices

本页无符合领域的常青仓库。规则命中的 `miha42-github/company_dns` 是 SEC 行业分类里的 SIC 查询，与碳化硅器件无关，不进正文。

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：把阳光电源 SH*RT、SHx.RS、SH*K、SxT 这几族逆变器接到 Home Assistant，经 Modbus 读运行数据。
  - 领域：电力电子电源 Power Supply
  - 总 star：705

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：开源扫地机器人，用激光雷达做同步定位与建图，控制栈走 ROS 2；主控侧有 ESP32，但要解决的是清扫机器人怎么走。
  - 领域：自动控制 Control
  - 总 star：11968
- [SteveMacenski/slam_toolbox](https://github.com/SteveMacenski/slam_toolbox)
  - 说明：给 ROS 做长期建图和定位，地图可以很大，不必每次重开一张新图。
  - 领域：自动控制 Control
  - 总 star：2676
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：移动机器人编程工具包，把定位、建图和传感器处理放在一套 C++ 库里。
  - 领域：自动控制 Control
  - 总 star：2169

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 13 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），括号内为总 star、stars today：`anthropics/claude-plugins-official`（40507，1552）、`K-Dense-AI/scientific-agent-skills`（51471，1158；名称和描述里的 AI 是弱词）、`affaan-m/ECC`（281465，1057）、`HKUDS/CLI-Anything`（53471，323）、`mksglu/context-mode`（30214，449；描述里的 AI、MCP 是弱词）、`ruvnet/ruflo`（75613，672；描述里的 RAG 是弱词，未计入）、`android/skills`（8051，163；描述为空）、`obra/superpowers`（300665，973）、`cursor/plugins`（11925，282）、`debpalash/VoiceStudio`（71086，2301）、`MadsLorentzen/ai-job-search`（48461，879；名称和描述里的 AI 是弱词）、`hmjz100/LinkSwift`（23649，702）、`xerj-org/xerj`（6898，1647；描述里的 RAG 是弱词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-17 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-17 stars:>2`。`total_count=391`，返回 5，规则保留 5，排除清单 0。剩余配额 9。`onehumanbeing/esp32-iphone-agent` 同时话题含 `llm`，完整条目在本节，AI 一节一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-17 stars:>2`。`total_count=2151`，返回 5，规则保留 2，未命中 3，排除清单 0。剩余配额 8。正文另有 1 条跨领域一行：`esp32-iphone-agent` 来自嵌入式检索。
  - 未命中：`zai-org/ZCode`（总 star 7890）、`mizorewww/laya-mlx`（6954；描述里的 PyTorch 出现在否定句里，且 `pytorch` 不是强特征描述词）、`kaankiziltug/logo-design-skill`（3528）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-17 stars:>2`。`total_count=4`，返回 4，规则保留 3，未命中 1。剩余配额 7。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 6）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 4）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（18）。`SiCo` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-17 stars:>2`。`total_count=74`，返回 5，规则保留 0。剩余配额 5。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（163）、`KawaiiBunga/MKVDCU-Recomp`（39）、`ningbainb/Dcode`（37）、`meztinos515/Acrobat-Pro-DC`（35）、`lamb2k/re4dc`（30）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-17 stars:>2`。`total_count=53`，返回 5，规则保留 4，未命中 1。剩余配额 9。正文保留 3 条。
  - `sd88me/mpc-vst-plugins`（总 star 120）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，与模型预测控制无关，正文不收。
  - `xwtk/hmg_nemesis`（67）：名称和 topics 未命中。

### C. 领域常青（`pushed:>=2026-10-10 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-10 stars:>3`。`total_count=1124`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。这 5 条都写入正文。`makerspet/oomwoo` 同时话题含 `ros2` 与 `slam`，要解决的是扫地机器人怎么走，完整条目在自动控制，本节一行带过。`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant` 不在这 5 条里，来自电力电子检索；话题含 `modbus`，本节一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-10 stars:>3`。`total_count=8453`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 8。正文保留 `earendil-works/pi`（115735）、`google-gemini/gemini-cli`（107411）、`pytorch/pytorch`（104805）。另有一行 `MRPT/mrpt`，来自自动控制检索，话题含 `computer-vision`。
  - 未命中：`addyosmani/agent-skills`（总 star 107389）、`nexu-io/open-design`（101620）。名称和 topics 没有 llm / pytorch / transformer / diffusion / ai-agents。描述里的 AI 是弱词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-10 stars:>3`。`total_count=20`，返回 5，规则保留 1，未命中 3，清单类排除 1。剩余配额 6。规则保留的 1 条人工剔除后，本页正文为空。
  - `miha42-github/company_dns`（总 star 10）：话题和描述含 `sic`，内容是 EDGAR 公司数据加 SEC 行业分类 SIC 查询，与碳化硅器件无关，正文不收。
  - 清单排除：`satnamrsm/https-github.com-sickn33-antigravity-awesome-skills`（总 star 8）。仓库名含 awesome，不进正文。
  - 名称和 topics 未命中：`linuxserver/docker-sickgear`（12）、`feddelegrand7/sicher`（11）、`CAPS-DGU/UmJoonSIC`（9；`UmJoonSIC` 按词边界不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-10 stars:>3`。`total_count=357`，返回 5，规则保留 1，未命中 4。剩余配额 9。正文完整条目为 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（705，topic `inverter`）。嵌入式一节因话题 `modbus` 一行带过。
  - 名称和 topics 未命中电力电子：`NVIDIA/DCGM`（802）、`dcs-liberation/dcs_liberation`（798）、`decred/dcrd`（775）、`Tencent/DCache`（745）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-10 stars:>3`。`total_count=215`，返回 5，规则保留 2，清单类排除 1，未命中 2。剩余配额 8。正文保留 `SteveMacenski/slam_toolbox`（2676）、`MRPT/mrpt`（2169）。`makerspet/oomwoo`（11968）来自嵌入式检索，话题含 `ros2` 与 `slam`，完整条目写在本节。`MRPT/mrpt` 同时话题含 `computer-vision`，AI 一节一行带过。
  - 清单排除：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2151）。awesome 合集，不进正文。
  - 未命中：`Syncplay/syncplay`（2695；描述里的 MPC-HC/MPC-BE 是播放器，`mpc` 不是强特征描述词）、`nvidia-isaac/cuVSLAM`（1868；名称 `cuVSLAM` 按词边界不等于 `slam`，描述里的 SLAM 是弱词）。
