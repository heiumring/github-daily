# GitHub 领域日报 · 2026-10-20

生成时间：2026-10-20 07:33（北京时间）。数据拉取开始于 2026-10-20 07:31:00（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-20（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-13 及之后有推送、总 star > 3。轮换页 `page = (当年第 293 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) 在工具输出、日志和检索片段进大模型之前先压缩，让编程代理少烧 token；今日热度命中，总 star 76221，24 小时新增 star 317。
2. [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) 在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，要确认时可以就地批准；近 30 天新建，总 star 5585。
3. [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) 让代理把难问题答成一页能直接读的 HTML；近 30 天新建，总 star 3901。

## A. 今日热度

Trending 页面解析到 12 条。页面不带 topics，因此只按仓库名和强特征描述归类。规则命中 1 条，清单类排除 0 条。按 24 小时新增 star 降序。

- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)
  - 说明：在工具输出、日志、文件和检索片段送进大模型之前先压缩，编程代理大约少用两成 token，JSON 可以压掉大部分，答案保持不变。
  - 领域：AI
  - 总 star：76221
  - 24 小时新增 star：317

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：3280
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：1037
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：415
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：231
- [andrisgauracs/wifi-sensing-kit](https://github.com/andrisgauracs/wifi-sensing-kit)
  - 说明：用三块约 10 美元的 ESP32-S3，靠 WiFi 信号判断人在做什么，训练时用摄像头当老师。
  - 领域：嵌入式 Embedded
  - 总 star：179

### AI

- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：5585
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：3901
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：3280。
- [feder-cr/invisible_playwright_mcp](https://github.com/feder-cr/invisible_playwright_mcp)
  - 说明：给代理一套不容易被网站反爬拦住的浏览器，让模型在隐蔽的 Firefox 里打开网页、抓取和操作，而不必先写专用爬虫。
  - 领域：AI
  - 总 star：2771
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：231。

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
  - 总 star：119
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：67

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 2。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：用 ESP32 经 WiFi 控制 WS2812B 等数字灯带，把灯效放在这块芯片上，不必另接专用灯控器。
  - 领域：嵌入式 Embedded
  - 总 star：18880
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：面向小地方的 Go 编译器，能把 Go 编到单片机、WebAssembly 和命令行工具上。
  - 领域：嵌入式 Embedded
  - 总 star：17824
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：RepRap 3D 打印机固件，8 位和 32 位单片机都能跑，很多商用机器出厂就带它。
  - 领域：嵌入式 Embedded
  - 总 star：17626
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：ESP32 系列的 Arduino 核心，让按 Arduino 写法写的程序能跑在乐鑫这族芯片上。
  - 领域：嵌入式 Embedded
  - 总 star：17580
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：可扩展的实时操作系统，覆盖多种硬件架构，用来在单片机上跑要守时的任务。
  - 领域：嵌入式 Embedded
  - 总 star：16836
- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd)
  - 说明：用 Flipper Zero 和 ESP32 经 OBD 或 X179 接特斯拉的 CAN，能抓总线，也能看 BMS 仪表；平台是嵌入式，不是一台电源变换器。
  - 领域：嵌入式 Embedded
  - 总 star：1148

### AI

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图搭扩散模型的界面、接口和后端，在本地把生成流程拆开编排。
  - 领域：AI
  - 总 star：139677
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：用 Python 让智能体操作浏览器，并提供隐匿浏览器和托管接口，把网页上的点击和填写交给模型。
  - 领域：AI
  - 总 star：118543
- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：给编程代理一套工具包，把各家大模型收成同一接口，并带上代理循环、终端界面和命令行。
  - 领域：AI
  - 总 star：116415

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。`epilys/sic` 是按标签组织的链接聚合，`libsidplayfp/libresidfp` 是 C64 的 SID 芯片仿真，话题里的 mosfet 不是功率器件，这两条不进正文。`DIY-LiFePO4-UPS` 是 12V 后备电源，完整说明写在下方电力电子电源。

- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：15。

### 电力电子电源 Power Supply

- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS 仪表，此处不展开。领域：电力电子电源 Power Supply。总 star：1148。
- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：用 ESPHome 经串口或蓝牙读写 Jikong 电池管理系统（JK-BMS），用来看电芯并下发控制。
  - 领域：电力电子电源 Power Supply
  - 总 star：1039
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 和网络设备做的 12V 磷酸铁锂后备电源，断电后按电压斜率判断该关机，避免电池放空。
  - 领域：电力电子电源 Power Supply
  - 总 star：15

### 自动控制 Control

- [MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)
  - 说明：用 Python 评估里程计和 SLAM 轨迹，拿 KITTI、EuRoC、TUM 这些基准比算法好坏。
  - 领域：自动控制 Control
  - 总 star：4342
- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：定位与建图库，带独立程序，覆盖 SLAM 和扫描，能接到 ROS 2，也能跑在手机上。
  - 领域：自动控制 Control
  - 总 star：4046
- [SteveMacenski/slam_toolbox](https://github.com/SteveMacenski/slam_toolbox)
  - 说明：给 ROS 做能长期接着用的 SLAM，在可能很大的地图里持续建图和定位。
  - 领域：自动控制 Control
  - 总 star：2682

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 12 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中并写入正文：`headroomlabs-ai/headroom`（总 star 76221，stars today 317）。描述中的 `LLM` 是强特征词。同一句里的 RAG、MCP 是弱词，不单独作为归类依据。
- 未命中（名称与强特征描述都没有领域词），括号内为总 star、stars today：`MadsLorentzen/ai-job-search`（57108，3860；名称和描述里的 AI 是弱词）、`anomalyco/opencode`（217759，1310）、`akitaonrails/ai-memory`（11297，666；名称里的 AI 是弱词）、`Comfy-Org/ComfyUI`（139677，1011；描述里的 diffusion 不是强特征词，未计入；常青 AI 页因话题含 pytorch 与 diffusion 另有完整条目）、`ruvnet/ruflo`（77164，564；描述里的 RAG 是弱词，未计入）、`stablyai/orca`（98214，1591）、`withmarbleapp/os-taxonomy`（6097，301；描述为空）、`Kruk2/jasna`（2872，502）、`HKUDS/CLI-Anything`（55209，607）、`anthropics/claude-code`（152630，167）、`shiyu-coder/Kronos`（41626，355）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-20 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-20 stars:>2`。`total_count=394`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文。`onehumanbeing/esp32-iphone-agent`（3280）和 `raullenchai/esp32-thinks`（231）同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-20 stars:>2`。`total_count=2229`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `Louis-CFM/coucou`（5585）、`QingYunA/answer-me-with-html`（3901）、`feder-cr/invisible_playwright_mcp`（2771；话题 `llm-agent` 按词边界命中 `llm`）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`zai-org/ZCode`（总 star 7994）、`kaankiziltug/logo-design-skill`（3771；描述里的 AI agents 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-20 stars:>2`。`total_count=5`，返回 5，规则保留 3，未命中 2。剩余配额 8。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 6）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 4）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（18）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`SiCo`、`Sichuan` 按词边界都不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-20 stars:>2`。`total_count=73`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（175）、`KawaiiBunga/MKVDCU-Recomp`（42）、`ningbainb/Dcode`（37）、`meztinos515/Acrobat-Pro-DC`（36）、`lamb2k/re4dc`（34）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-20 stars:>2`。`total_count=51`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `cocel-postech/genz-lio`（119）、`TrentIndeed/kinetiqgym`（67）。
  - `sd88me/mpc-vst-plugins`（总 star 121）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，与模型预测控制无关，正文不收。
  - 名称和 topics 未命中：`xwtk/hmg_nemesis`（75）、`lbgos/rift-s-linux`（24；描述里的 SLAM 不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-13 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-13 stars:>3`。`total_count=1140`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。这 5 条都写入正文。`hypery11/flipper-tesla-fsd` 不在这 5 条里，来自电力电子检索；话题含 `can-bus`、描述含 ESP32，比 BMS 仪表更贴近嵌入式，完整条目写在本节，电力电子一节一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-13 stars:>3`。`total_count=8525`，返回 5，规则保留 3，未命中 1，清单类排除 1。剩余配额 8。正文保留 `Comfy-Org/ComfyUI`（139677，topic `pytorch` 与 `diffusion`）、`browser-use/browser-use`（118543，topic `llm` 与 `ai-agents`）、`earendil-works/pi`（116415，描述命中强特征词 `llm`）。
  - 清单类排除：`Shubhamsaboo/awesome-llm-apps`（总 star 142327）。名称含 awesome 与 llm，是代理应用合集，不进正文。
  - 未命中：`langflow-ai/langflow`（总 star 155848）。描述里的 AI-powered agents 是弱词，名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-13 stars:>3`。`total_count=20`，返回 5，规则保留 3，未命中 2。剩余配额 9。规则保留的 3 条里，2 条人工剔除，剩下的 `DIY-LiFePO4-UPS` 完整条目在电力电子，本节只留一行。本页没有功率器件完整条目。
  - `epilys/sic`（总 star 26）：仓库名命中 `sic`，内容是按标签组织的链接聚合，与碳化硅器件无关，正文不收。
  - `libsidplayfp/libresidfp`（总 star 15）：话题含 `mosfet`，内容是 C64 SID 芯片的周期精确仿真，不是功率器件，正文不收。
  - `wkcollis1-eng/DIY-LiFePO4-UPS`（15）：话题同时含 `mosfet` 与 `power-supply`。项目是 12V 后备电源，完整条目在电力电子电源，功率器件一节一行带过。
  - 名称按词边界不等于 `sic`，也没有功率器件话题：`hexlet-volunteers/hexlet-sicp`（114）、`MadestSamurai/bd2-sichuan`（13）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-13 stars:>3`。`total_count=354`，返回 5，规则保留 2，未命中电力电子 2，另有 1 条只命中其它领域。剩余配额 8。正文完整条目为 `syssi/esphome-jk-bms`（1039），加上从功率器件检索移来的 `DIY-LiFePO4-UPS`（15）。`flipper-tesla-fsd` 在本节只留一行。
  - `hypery11/flipper-tesla-fsd`（1148）：描述含 `BMS`（电池管理仪表），话题含 `can-bus`，描述含 ESP32。完整条目在嵌入式。
  - `syssi/esphome-jk-bms`（1039）：topic `bms`，是极空电池管理系统，正文保留。
  - `pnoker/iot-dc3`（1287）：名称被检索词 `dc-dc` 撞上。话题含 `modbus` 与 `ai-agents`，不命中电力电子。它不在本页嵌入式或 AI 检索的前 5 里，不跨节。
  - 名称和 topics 未命中电力电子：`rordenlab/dcm2niix`（1204）、`DCMTK/dcmtk`（914）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-13 stars:>3`。`total_count=203`，返回 5，规则保留 3，清单类排除 1，未命中 1。剩余配额 8。正文保留 `MichaelGrupp/evo`（4342）、`introlab/rtabmap`（4046）、`SteveMacenski/slam_toolbox`（2682）。
  - 清单类排除：`jslee02/awesome-robotics-libraries`（总 star 3084）。话题含 `slam`，是机器人库合集，不进正文。
  - 未命中：`vedderb/bldc`（3515）。描述是 “motor control”（空格），名称 `bldc` 不在自动控制关键词表，正文不收。
