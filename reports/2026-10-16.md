# GitHub 领域日报 · 2026-10-16

生成时间：2026-10-16 07:35（北京时间）。数据拉取开始于 2026-10-16 07:32:03（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-16（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-09 及之后有推送、总 star > 3。轮换页 `page = (当年第 289 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [lightseekorg/tokenspeed](https://github.com/lightseekorg/tokenspeed) 把 LLM 推理做成追求极限速度的引擎；今日热度里唯一命中领域的仓库，24 小时新增 star 25，总 star 2470。
2. [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) 用一次前向做分类、打分和是否判断，而不是逐字生成；近 30 天新建，总 star 33046。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真机 iPhone；近 30 天新建，总 star 2423。

## A. 今日热度

Trending 页面解析到 12 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。

- [lightseekorg/tokenspeed](https://github.com/lightseekorg/tokenspeed)
  - 说明：把大模型推理解成追求极限速度的引擎，用来把已经训练好的 LLM 跑得更快。
  - 领域：AI
  - 总 star：2470
  - 24 小时新增 star：25

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：2423
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：967
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：385
- [andrisgauracs/wifi-sensing-kit](https://github.com/andrisgauracs/wifi-sensing-kit)
  - 说明：用三块约 10 美元的 ESP32-S3，靠 WiFi 信号判断人在做什么，训练时用摄像头当老师。
  - 领域：嵌入式 Embedded
  - 总 star：159
- [cyber-murmel/esp-sdr-zephyr](https://github.com/cyber-murmel/esp-sdr-zephyr)
  - 说明：在 Zephyr 上做 ESP32 的 2.4 GHz 软件无线电，用实时系统来收这一频段的信号。
  - 领域：嵌入式 Embedded
  - 总 star：121

### AI

- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
  - 说明：用一次前向完成文本上的分类、打分和是否判断，并按请求挑选检查点，覆盖描述中的 100 多种语言。
  - 领域：AI
  - 总 star：33046
- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：5311
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：2423。

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
  - 总 star：102
- [HengyiWang/amb3r-slam](https://github.com/HengyiWang/amb3r-slam)
  - 说明：面向公里级范围的 SLAM，用分层后端处理很长的轨迹，而不是只在室内小地图里定位。
  - 领域：自动控制 Control
  - 总 star：77
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：21

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 2。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：用 ESP32 经 WiFi 控制 WS2812B 等数字灯带，把灯效放在这块芯片上，不必另接专用灯控器。
  - 领域：嵌入式 Embedded
  - 总 star：18856
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：面向小地方的 Go 编译器，能把 Go 编到单片机、WebAssembly 和命令行工具上。
  - 领域：嵌入式 Embedded
  - 总 star：17817
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：RepRap 3D 打印机固件，8 位和 32 位单片机都能跑，很多商用机器出厂就带它。
  - 领域：嵌入式 Embedded
  - 总 star：17620
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：ESP32 系列的 Arduino 核心，让按 Arduino 写法写的程序能跑在乐鑫这族芯片上。
  - 领域：嵌入式 Embedded
  - 总 star：17553
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：可扩展的实时操作系统，覆盖多种硬件架构，用来在单片机上跑要守时的任务。
  - 领域：嵌入式 Embedded
  - 总 star：16803
- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd)
  - 说明：用 Flipper Zero 和 ESP32 经 OBD 或 X179 改特斯拉的车载功能，能抓 CAN，也能看 BMS 仪表；平台是嵌入式，不是一台电源变换器。
  - 领域：嵌入式 Embedded
  - 总 star：1140

### AI

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图搭扩散模型的界面、接口和后端，在本地把生成流程拆开编排。
  - 领域：AI
  - 总 star：137708
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：用 Python 让智能体操作浏览器，并提供隐匿浏览器和托管接口，把网页上的点击和填写交给模型。
  - 领域：AI
  - 总 star：118097

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。检索命中、且确实相关的两条，完整说明写在下方「电力电子电源 Power Supply」，这里只留链接。

- [OpenVVVF/Hardware](https://github.com/OpenVVVF/Hardware) — 见下方「电力电子电源 Power Supply」完整条目。话题含 igbt，此处不展开。领域：功率器件 Power Devices。总 star：17。
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：15。

### 电力电子电源 Power Supply

- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS 仪表，此处不展开。领域：电力电子电源 Power Supply。总 star：1140。
- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：用 ESPHome 经串口或蓝牙读写 Jikong 电池管理系统（JK-BMS），用来看电芯并下发控制。
  - 领域：电力电子电源 Power Supply
  - 总 star：1036
- [OpenVVVF/Hardware](https://github.com/OpenVVVF/Hardware)
  - 说明：开源的大功率三相电压源逆变器，用 IGBT 和全隔离栅极驱动，并带独立安全协处理器，用来做牵引逆变和变频传动；固件在 OpenVVVF/RTE。
  - 领域：电力电子电源 Power Supply
  - 总 star：17
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 和网络设备做的 12V 磷酸铁锂后备电源，断电后按电压斜率判断该关机，避免电池放空。
  - 领域：电力电子电源 Power Supply
  - 总 star：15

### 自动控制 Control

- [MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)
  - 说明：用 Python 评估里程计和 SLAM 轨迹，拿 KITTI、EuRoC、TUM 这些基准比算法好坏。
  - 领域：自动控制 Control
  - 总 star：4337
- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：定位与建图库，带独立程序，覆盖 SLAM 和扫描，能接到 ROS 2，也能跑在手机上。
  - 领域：自动控制 Control
  - 总 star：4039
- [RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)
  - 说明：通用的图优化框架，给 SLAM 解位姿图，把约束收成可以一起优化的图。
  - 领域：自动控制 Control
  - 总 star：3471

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 12 条，规则命中 1 条（`lightseekorg/tokenspeed`，描述含 LLM，总 star 2470，stars today 25），清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），括号内为总 star、stars today：`morluto/rea`（269131，32282）、`anthropics/claude-plugins-official`（39032，525）、`K-Dense-AI/scientific-agent-skills`（50430，1091；名称和描述里的 AI 是弱词）、`JuliusBrussee/caveman`（112510，530）、`debpalash/VoiceStudio`（69003，3027）、`obra/superpowers`（299860，688）、`ruvnet/ruflo`（75097，224；描述里的 RAG 是弱词，未计入）、`mksglu/context-mode`（29776，902；描述里的 AI、MCP 是弱词）、`NationalSecurityAgency/ghidra`（88706，1366）、`affaan-m/ECC`（280335，1015）、`xerj-org/xerj`（5604，725；描述里的 RAG 是弱词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-16 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-16 stars:>2`。`total_count=387`，返回 5，规则保留 5，排除清单 0。剩余配额 9。`onehumanbeing/esp32-iphone-agent` 同时话题含 `llm`，完整条目在本节，AI 一节一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-16 stars:>2`。`total_count=2115`，返回 5，规则保留 2，未命中 3，排除清单 0。剩余配额 9。正文另有 1 条跨领域一行：`esp32-iphone-agent` 来自嵌入式检索。
  - 未命中：`zai-org/ZCode`（总 star 7854）、`mizorewww/laya-mlx`（6943；描述里的 PyTorch 出现在否定句里，且 `pytorch` 不是强特征描述词）、`mhtsec/ARTEX`（4254）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-16 stars:>2`。`total_count=4`，返回 4，规则保留 3，未命中 1。剩余配额 9。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 6）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 3）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（18）。`SiCo` 按词边界不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-16 stars:>2`。`total_count=72`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（158）、`KawaiiBunga/MKVDCU-Recomp`（39）、`ningbainb/Dcode`（37）、`meztinos515/Acrobat-Pro-DC`（35）、`lamb2k/re4dc`（28）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-16 stars:>2`。`total_count=50`，返回 5，规则保留 4，未命中 1。剩余配额 8。正文保留 3 条。
  - `sd88me/mpc-vst-plugins`（总 star 119）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，与模型预测控制无关，正文不收。
  - `xwtk/hmg_nemesis`（67）：名称和 topics 未命中。

### C. 领域常青（`pushed:>=2026-10-09 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-09 stars:>3`。`total_count=1128`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。这 5 条都写入正文。`hypery11/flipper-tesla-fsd` 不在这 5 条里，来自电力电子检索；话题含 `can-bus`、描述含 ESP32，比 BMS 仪表更贴近嵌入式，完整条目写在本节，电力电子一节一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-09 stars:>3`。`total_count=8419`，返回 5，规则保留 2，未命中 2，排除清单 1。剩余配额 9。正文保留 `Comfy-Org/ComfyUI`（137708）和 `browser-use/browser-use`（118097）。
  - 清单排除：`Shubhamsaboo/awesome-llm-apps`（总 star 141886）。仓库名是 awesome 合集，不进正文。
  - 未命中：`langflow-ai/langflow`（155716）、`x1xhlol/system-prompts-and-models-of-ai-tools`（144047）。名称和 topics 没有 llm / pytorch / transformer / diffusion / ai-agents。描述里的 AI 是弱词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-09 stars:>3`。`total_count=20`，返回 5，规则保留 3，未命中 2。剩余配额 8。规则保留的 3 条里，1 条人工剔除，另外 2 条更贴近电力电子电源，完整条目写在那一节，本节只留一行。
  - `libsidplayfp/libresidfp`（总 star 15）：话题含 `mosfet`，内容是 Commodore 64 SID 芯片的周期精确仿真，不是功率器件，正文不收。
  - `OpenVVVF/Hardware`（17）：话题同时含 `igbt`、`inverter`、`motor-control`。最贴近电力电子电源（三相电压源逆变器），功率器件一节一行带过。自动控制是第三领域，本节数已满 2，正文不单列。
  - `wkcollis1-eng/DIY-LiFePO4-UPS`（15）：话题同时含 `mosfet` 与 `power-supply`。项目是 12V 后备电源，完整条目在电力电子电源，功率器件一节一行带过。
  - 名称和 topics 未命中：`klutometis/sicp`（19；`sicp` 不等于 `sic`）、`ducroo/SICTIC-AI`（14；`sictic` 不等于 `sic`）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-09 stars:>3`。`total_count=367`，返回 5，规则保留 2，未命中电力电子关键词 2，另有 1 条只命中嵌入式。剩余配额 8。正文完整条目为 `syssi/esphome-jk-bms`（1036），加上从功率器件检索移来的 `OpenVVVF/Hardware`（17）和 `DIY-LiFePO4-UPS`（15）。`flipper-tesla-fsd` 在本节只留一行。
  - `hypery11/flipper-tesla-fsd`（1140）：描述含 `BMS`（电池管理仪表），话题含 `can-bus`，描述含 ESP32。完整条目在嵌入式。
  - `wlcrs/huawei_solar`（935）：描述写到 solar inverters。`inverters` 按词边界不等于 `inverter`，未计入电力电子。话题含 `modbus`，命中嵌入式，但不在嵌入式查询的前 5 条里，正文不单列。
  - 名称和 topics 未命中电力电子：`rordenlab/dcm2niix`（1202）、`DCMTK/dcmtk`（911）。检索词 `dc-dc` 撞上了 DICOM 工具名里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-09 stars:>3`。`total_count=220`，返回 5，规则保留 3，清单类排除 1，未命中 1。剩余配额 9。正文保留 `MichaelGrupp/evo`（4337）、`introlab/rtabmap`（4039）、`RainerKuemmerle/g2o`（3471）。
  - 清单排除：`jslee02/awesome-robotics-libraries`（总 star 3083）。awesome 合集，不进正文。
  - `vedderb/bldc`（3510）：描述是 “The VESC motor control firmware”。`motor control` 中间是空格，分类按词边界不等于 `motor-control`；仓库名 `bldc` 不在自动控制的名称/话题关键词里（`bldc` 只在描述强特征词中，描述本身没有这个词），正文不收。
