# GitHub 领域日报 · 2026-10-12

生成时间：2026-10-12 07:34（北京时间）。数据拉取开始于 2026-10-12 07:31:08（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-12（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-05 及之后有推送、总 star > 3。轮换页 `page = (当年第 285 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [pytorch/pytorch](https://github.com/pytorch/pytorch) 是今日 Trending 里唯一命中领域关键词的仓库，24 小时新增 star 314，总 star 104466。
2. [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) 用一次前向做分类、打分和是否判断，而不是逐字生成；近 30 天新建，总 star 32342。
3. [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr) 用 ESP32 未公开的原始 I/Q 采集把它做成低占空比软件无线电；近 30 天新建，总 star 836。

## A. 今日热度

Trending 页面解析到 8 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。嵌入式、功率器件、电力电子电源、自动控制在这 8 条里没有命中。

### AI

- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：提供带 GPU 加速的张量和动态神经网络，用来训练和跑模型，而不必自己实现底层张量与自动求导。
  - 领域：AI
  - 总 star：104466
  - 24 小时新增 star：314

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：836
- [MaxGramser/homeassistant_espscreen](https://github.com/MaxGramser/homeassistant_espscreen)
  - 说明：把便宜的 ESP32 触摸屏做成 Home Assistant 面板，用拖拽编辑界面，不用手写 YAML，也不走 MQTT。
  - 领域：嵌入式 Embedded
  - 总 star：527
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：366
- [dashersw/coyopedal](https://github.com/dashersw/coyopedal)
  - 说明：在 ESP32-S3 上做 NAM 吉他效果器踏板，模型直接从 SD 卡加载，前面板编译成原生界面，用来在板上跑音色模型。
  - 领域：嵌入式 Embedded
  - 总 star：253
- [Frankweb33/flybrain-robot-bridge](https://github.com/Frankweb33/flybrain-robot-bridge)
  - 说明：把果蝇神经回路的思路接到相机和电机上，用光流和 IMU 把看见的画面变成机器人动作；现在仍是实验桥接，不是完整飞控。
  - 领域：嵌入式 Embedded
  - 总 star：227

### AI

- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
  - 说明：很多地方只要分类、打分或是否判断，却还在用自回归模型逐字生成。它一次前向给出这类决定，并按请求挑选检查点。
  - 领域：AI
  - 总 star：32342
- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：4827
- [Frankweb33/flybrain-robot-bridge](https://github.com/Frankweb33/flybrain-robot-bridge) — 见上方「嵌入式 Embedded」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：227。

### 功率器件 Power Devices

- [tPkl/OpenRdson](https://github.com/tPkl/OpenRdson)
  - 说明：开源的场效应管设计与寄生参数提取，用网格和有限元去对标 Synopsys / SFT 的 R3D，给模拟版图做提取。
  - 领域：功率器件 Power Devices
  - 总 star：6

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [HengyiWang/amb3r-slam](https://github.com/HengyiWang/amb3r-slam)
  - 说明：面向公里级范围的 SLAM，用分层后端处理很长的轨迹，而不是只在室内小地图里定位。
  - 领域：自动控制 Control
  - 总 star：72
- [cocel-postech/genz-lio](https://github.com/cocel-postech/genz-lio)
  - 说明：激光雷达加 IMU 的里程计，针对室内外和退化场景把位姿估稳；仓库标明发表于 IEEE T-FR 2026。
  - 领域：自动控制 Control
  - 总 star：53

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 2。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：用 ESP32 经 WiFi 控制 WS2812B 等数字灯带，把灯效和颜色收成可远程调的灯光。
  - 领域：嵌入式 Embedded
  - 总 star：18791
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：基于 LLVM 的 Go 编译器，面向单片机、WebAssembly 和命令行，让 Go 能写到 ESP32、STM32 这类小芯片上。
  - 领域：嵌入式 Embedded
  - 总 star：17809
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：RepRap 3D 打印机固件，同时照顾 8 位和 32 位微控制器，把切片后的运动变成电机和加热控制。
  - 领域：嵌入式 Embedded
  - 总 star：17619
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：乐鑫 ESP32 系列的 Arduino 核心，让人用 Arduino 的写法直接给 ESP32 写固件。
  - 领域：嵌入式 Embedded
  - 总 star：17507
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：可扩展的实时操作系统，面向多种硬件架构，用来在 MCU 上跑有时限要求的嵌入式软件。
  - 领域：嵌入式 Embedded
  - 总 star：16754
- [simplefoc/Arduino-FOC](https://github.com/simplefoc/Arduino-FOC) — 见下方「自动控制 Control」完整条目。描述命中 bldc，此处不展开。领域：嵌入式 Embedded。总 star：3058。
- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd)
  - 说明：在 Flipper Zero 和 ESP32 上经 OBD-II 或 X179 接特斯拉 CAN，用来看电池数据、抓报文，并改车上的提示和模式。
  - 领域：嵌入式 Embedded
  - 总 star：1125
- [ACMmodel/ACM-MOSFET-models](https://github.com/ACMmodel/ACM-MOSFET-models) — 见下方「功率器件 Power Devices」完整条目。话题含 verilog，此处不展开。领域：嵌入式 Embedded。总 star：55。

### AI

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图把扩散模型的界面、API 和本地推理串起来，用来在自己机器上搭出图流程。
  - 领域：AI
  - 总 star：136946
- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：编程助手工具包，把多家模型收成一套 LLM 接口，并带上代理循环、终端界面和命令行，用来少写重复的模型接入。
  - 领域：AI
  - 总 star：114315
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：把 Gemini 做成可在终端里用的开源智能体，用来在命令行里直接让模型处理当前项目。
  - 领域：AI
  - 总 star：107286

### 功率器件 Power Devices

- [ACMmodel/ACM-MOSFET-models](https://github.com/ACMmodel/ACM-MOSFET-models)
  - 说明：给模拟和射频集成电路用的简单 MOSFET 模型，带 Verilog-A，用来在开源流程里做管子级仿真。
  - 领域：功率器件 Power Devices
  - 总 star：55
- [OpenVVVF/Hardware](https://github.com/OpenVVVF/Hardware) — 见下方「电力电子电源 Power Supply」完整条目。话题含 igbt，此处不展开。领域：功率器件 Power Devices。总 star：17。

### 电力电子电源 Power Supply

- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS 仪表，此处不展开。领域：电力电子电源 Power Supply。总 star：1125。
- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：ESPHome 组件，经 UART 或蓝牙监视和控制极空电池管理系统（JK-BMS），把电芯数据接进家庭自动化。
  - 领域：电力电子电源 Power Supply
  - 总 star：1035
- [OpenVVVF/Hardware](https://github.com/OpenVVVF/Hardware)
  - 说明：开源的大功率三相电压源逆变器，带独立安全协处理器和隔离栅极驱动，用来做牵引或变频驱动；固件和遥测在 OpenVVVF/RTE。
  - 领域：电力电子电源 Power Supply
  - 总 star：17

### 自动控制 Control

- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：带独立程序的 SLAM 库，话题含定位、建图、机器人和 ROS 2，用来一边走一边建图。
  - 领域：自动控制 Control
  - 总 star：4032
- [RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)
  - 说明：通用图优化框架，话题标了 SLAM，用来把位姿和约束收成一张图再求解。
  - 领域：自动控制 Control
  - 总 star：3471
- [simplefoc/Arduino-FOC](https://github.com/simplefoc/Arduino-FOC)
  - 说明：在 Arduino 上对无刷和步进电机做磁场定向控制，用编码器把力矩和速度控稳，而不是开环转。
  - 领域：自动控制 Control
  - 总 star：3058
- [SteveMacenski/slam_toolbox](https://github.com/SteveMacenski/slam_toolbox)
  - 说明：给 ROS 用的 SLAM 工具箱，面向可能很大的地图做长期建图和定位，地图一直长大时还能接着定位。
  - 领域：自动控制 Control
  - 总 star：2669

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`。本次补上强特征描述词 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，并写入对应领域映射。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。`OpenVVVF/Hardware` 还命中 `motor-control`（自动控制），因已在功率器件与电力电子电源两节出现，自动控制节不再列入。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 8 条，规则命中 1 条（`pytorch/pytorch`，仓库名含 pytorch，总 star 104466，stars today 314），清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词）：`morluto/rea`（总 star 102731，stars today 25585）、`boykopovar/AnyPS5`（29983，3977）、`storytold/artcraft`（17760，2956）、`cathrynlavery/diagram-design`（50276，1083）、`bilawalsidhu/gods-eye-view`（51607，872）、`lyogavin/airllm`（36447，541；`airllm` 不能按词边界拆出 `llm`）、`chrislgarry/Apollo-11`（74226，581）。
- 说明：页面有 stars today，没有 topics。描述里的 agent 等弱词未计入。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-12 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-12 stars:>2`。`total_count=373`，返回 5，规则保留 5，排除清单 0。剩余配额 9。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-12 stars:>2`。`total_count=1905`，返回 5，规则保留 2，未命中 3，排除清单 0。剩余配额 9。未命中：`zai-org/ZCode`（总 star 7681）、`mizorewww/laya-mlx`（6876；描述里的 PyTorch 不是强特征词，且句子是否定用法）、`mhtsec/ARTEX`（3138）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-12 stars:>2`。`total_count=5`，返回 5，规则保留 2，未命中 3。剩余配额 9。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 4）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，不是碳化硅器件，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（16）、`MadestSamurai/bd2-sichuan`（12）、`MicroFarmerVoyage/hellraiser-revival-motion-sickness-tool`（9）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-12 stars:>2`。`total_count=69`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（132）、`ningbainb/Dcode`（37）、`meztinos515/Acrobat-Pro-DC`（35）、`KawaiiBunga/MKVDCU-Recomp`（33）、`DAGroup-PKU/DCSAE`（23）。`DCSAE` 描述写到 Diffusion，但 `diffusion` 不是强特征描述词，不因此计入 AI。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-12 stars:>2`。`total_count=48`，返回 5，规则保留 3，未命中控制关键词 2。剩余配额 8。正文保留 2 条。
  - `sd88me/mpc-vst-plugins`（总 star 111）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，不是模型预测控制，正文不收。
  - `Frankweb33/flybrain-robot-bridge`（227）：本查询返回，但未命中控制关键词；已写入嵌入式，并在 AI 一行带过。
  - `xwtk/hmg_nemesis`（51）：名称和 topics 未命中。

### C. 领域常青（`pushed:>=2026-10-05 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-05 stars:>3`。`total_count=1125`，返回 5，规则保留 5，排除清单 0。剩余配额 9。`simplefoc/Arduino-FOC`、`hypery11/flipper-tesla-fsd`、`ACMmodel/ACM-MOSFET-models` 不在这 5 条里，因同时命中嵌入式，在本节按总 star 插入一行或完整条目。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-05 stars:>3`。`total_count=8132`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。`earendil-works/pi`（总 star 114315）没有 topics，靠描述中的强特征词 `llm` 计入。
  - 未命中：`langflow-ai/langflow`（155510）、`addyosmani/agent-skills`（105008）。名称和 topics 没有 llm / pytorch / transformer / diffusion / ai-agents。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-05 stars:>3`。`total_count=28`，返回 5，规则保留 3，未命中 2。剩余配额 8。正文保留 `ACMmodel/ACM-MOSFET-models`（总 star 55）全文，以及 `OpenVVVF/Hardware`（17）指向电源节的一行。
  - `epilys/sic`（总 star 27）：仓库名是 `sic`，描述是按标签组织的链接聚合站，不是碳化硅，正文不收。
  - 名称和 topics 未命中：`SICKAG/sick_safetyscanners_base`（19）、`opencad-abu/SiCo`（16）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-05 stars:>3`。`total_count=352`，返回 5，规则保留 3，另有 1 条只命中嵌入式、1 条未命中。剩余配额 7。
  - `bemusic/bemuse`（总 star 1252）：topic `bms` 是节奏游戏谱面格式（同时有 `bmson`），描述是网页音游，不是电池管理系统，正文不收。
  - `hypery11/flipper-tesla-fsd`（1125）：描述命中强特征词 `bms`，话题含 `can-bus`、描述含 `esp32`。完整条目写在嵌入式，本节一行带过。
  - `syssi/esphome-jk-bms`（1035）：topic `bms`，是极空电池管理系统，正文保留。
  - `wlcrs/huawei_solar`（934）：描述写 Huawei Solar inverters，复数 `inverters` 按词边界不等于 `inverter`，未计入电源；topic 命中 `modbus`，不在嵌入式查询前 5，正文不单列。
  - `DCMTK/dcmtk`（911）：名称和 topics 未命中，是 DICOM 工具包。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-05 stars:>3`。`total_count=210`，返回 5，规则保留 4，清单类排除 1。剩余配额 7。
  - 排除清单：`jslee02/awesome-robotics-libraries`（总 star 3079），awesome 合集。
