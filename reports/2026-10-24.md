# GitHub 领域日报 · 2026-10-24

生成时间：2026-10-24 07:34（北京时间）。数据拉取开始于 2026-10-24 07:30:55（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-24（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-17 及之后有推送、总 star > 3。轮换页 `page = (当年第 297 天 mod 4) + 1 = 2`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) 在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，要确认时可以就地批准；近 30 天新建，总 star 6312。
2. [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) 让代理把难问题答成一页能直接读的 HTML；近 30 天新建，总 star 4313。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，不必用 Mac，也不必越狱；近 30 天新建，总 star 3627。

## A. 今日热度

Trending 页面解析到 8 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。嵌入式、AI、功率器件、电力电子电源、自动控制在这 8 条里都没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：3627
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：1083
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：433
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：251
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32 上做 Grok 语音终端，眼睛会眨眼，带字幕和朗读，固件和后端一起开源。
  - 领域：嵌入式 Embedded
  - 总 star：220

### AI

- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor、Gemini CLI、Antigravity 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：6312
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：4313
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：3627。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：2453
- [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu)
  - 说明：把 AI 写出来的日语改成读起来自然的日语，作为给编程代理用的推敲技能，而不是另做一套翻译器。
  - 领域：AI
  - 总 star：2439
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：251。

### 功率器件 Power Devices

- [tPkl/OpenRdson](https://github.com/tPkl/OpenRdson)
  - 说明：用开源网格和有限元做场效应管版图的寄生参数提取，用来替代 Synopsys / SFT 的 R3D。
  - 领域：功率器件 Power Devices
  - 总 star：6

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：85
- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室把 2026 年 RoboMaster 超级对抗赛哨兵的定位开源出来，用 Livox MID360 做激光雷达与 IMU 里程计，并带重定位，跑在 ROS 2 上。
  - 领域：自动控制 Control
  - 总 star：62
- [zhuoligetu123/mid360-campus-slam](https://github.com/zhuoligetu123/mid360-campus-slam)
  - 说明：在 ROS 2 Humble 上用 Livox MID360 做园区三维建图和重定位，用 ScanContext 做回环，并能导出二维地图。
  - 领域：自动控制 Control
  - 总 star：25

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 2。

### 嵌入式 Embedded

- [wled/WLED](https://github.com/wled/WLED)
  - 说明：用 ESP32 经 WiFi 控制 WS2812B 等数字灯带，把灯效放在这块芯片上，不必另接专用灯控器。
  - 领域：嵌入式 Embedded
  - 总 star：18904
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)
  - 说明：面向小地方的 Go 编译器，能把 Go 编到单片机、WebAssembly 和命令行工具上。
  - 领域：嵌入式 Embedded
  - 总 star：17840
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)
  - 说明：RepRap 3D 打印机固件，8 位和 32 位单片机都能跑，很多商用机器出厂就带它。
  - 领域：嵌入式 Embedded
  - 总 star：17633
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)
  - 说明：ESP32 系列的 Arduino 核心，让按 Arduino 写法写的程序能跑在乐鑫这族芯片上。
  - 领域：嵌入式 Embedded
  - 总 star：17610
- [zephyrproject-rtos/zephyr](https://github.com/zephyrproject-rtos/zephyr)
  - 说明：可扩展的实时操作系统，覆盖多种硬件架构，用来在单片机上跑要守时的任务。
  - 领域：嵌入式 Embedded
  - 总 star：16878
- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd)
  - 说明：用 Flipper Zero 和 ESP32 经 OBD 或 X179 接特斯拉的 CAN，能抓总线，也能看 BMS 仪表。
  - 领域：嵌入式 Embedded
  - 总 star：1159
- [TheYoctoJester/dutler](https://github.com/TheYoctoJester/dutler)
  - 说明：把 Raspberry Pi Pico 变成被测设备的 USB 串口桥，带电源继电器和 MOSFET 拉带复位，用来给嵌入式 Linux 做上电调试和硬件在环。
  - 领域：嵌入式 Embedded
  - 总 star：23

### AI

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
  - 说明：用节点图搭扩散模型的界面、接口和后端，在本地把生成流程拆开编排。
  - 领域：AI
  - 总 star：142338
- [browser-use/browser-use](https://github.com/browser-use/browser-use)
  - 说明：用 Python 让智能体操作浏览器，并提供隐匿浏览器和托管接口，把网页上的点击和填写交给模型。
  - 领域：AI
  - 总 star：118982
- [earendil-works/pi](https://github.com/earendil-works/pi)
  - 说明：给编程代理一套工具包，把各家大模型收成同一接口，并带上代理循环、终端界面和命令行。
  - 领域：AI
  - 总 star：117437

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。`epilys/sic` 是按标签组织的链接聚合，与碳化硅器件无关，正文不收。`TheYoctoJester/dutler` 是嵌入式 Linux 的上电调试桥，完整说明写在上方嵌入式。

- [TheYoctoJester/dutler](https://github.com/TheYoctoJester/dutler) — 见上方「嵌入式 Embedded」完整条目。描述含 MOSFET 拉带复位，此处不展开。领域：功率器件 Power Devices。总 star：23。

### 电力电子电源 Power Supply

- [hypery11/flipper-tesla-fsd](https://github.com/hypery11/flipper-tesla-fsd) — 见上方「嵌入式 Embedded」完整条目。描述含 BMS 仪表，此处不展开。领域：电力电子电源 Power Supply。总 star：1159。
- [syssi/esphome-jk-bms](https://github.com/syssi/esphome-jk-bms)
  - 说明：用 ESPHome 经串口或蓝牙读写 Jikong 电池管理系统（JK-BMS），用来看电芯并下发控制。
  - 领域：电力电子电源 Power Supply
  - 总 star：1040

### 自动控制 Control

- [introlab/rtabmap](https://github.com/introlab/rtabmap)
  - 说明：定位与建图库，带独立程序，覆盖 SLAM 和扫描，能接到 ROS 2，也能跑在手机上。
  - 领域：自动控制 Control
  - 总 star：4054
- [RainerKuemmerle/g2o](https://github.com/RainerKuemmerle/g2o)
  - 说明：通用的图优化框架，给 SLAM 解位姿图，把约束收成可以一起优化的图。
  - 领域：自动控制 Control
  - 总 star：3474

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 8 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`cloudflare/security-audit-skill`（42068，2706）、`NVIDIA/OpenShell`（18759，1240；描述里的 AI agents 是弱词）、`php/php-src`（41549，722）、`anthropics/knowledge-work-plugins`（32190，643）、`Renhuai123/ziwei-doushu`（6841，547）、`SnailSploit/Claude-Red`（8446，209）、`OpenBMB/VoxCPM`（40236，144；名称 VoxCPM 按词边界不等于领域词）、`nodejs/node`（122846，93）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-24 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-24 stars:>2`。`total_count=389`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文。`onehumanbeing/esp32-iphone-agent`（3627）和 `raullenchai/esp32-thinks`（251）同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-24 stars:>2`。`total_count=2367`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 9。正文保留 `Louis-CFM/coucou`（6312）、`QingYunA/answer-me-with-html`（4313）、`Leonxlnx/earshot`（2453）、`nanaism/yomiyasu`（2439）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`kaankiziltug/logo-design-skill`（总 star 4301；描述里的 AI agents 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-24 stars:>2`。`total_count=5`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 9）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 5）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（21）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`SiCo`、`Sichuan` 按词边界都不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-24 stars:>2`。`total_count=70`，返回 5，规则保留 0。剩余配额 8。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（186）、`Lida-V/3DCharaMakeSkills-Lida`（49）、`CompaLarios18/MH4UltimateDC`（45）、`lamb2k/re4dc`（36）、`meztinos515/Acrobat-Pro-DC`（36）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-24 stars:>2`。`total_count=50`，返回 5，规则保留 3，未命中 2。剩余配额 7。正文保留 `TrentIndeed/kinetiqgym`（85）、`mozihe/z-localization`（62）、`zhuoligetu123/mid360-campus-slam`（25）。
  - 名称和 topics 未命中：`xwtk/hmg_nemesis`（112）、`lbgos/rift-s-linux`（29；描述里的 SLAM 不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-17 stars:>3`，`sort=stars`，`per_page=5`，`page=2`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-17 stars:>3`。`total_count=1148`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。这 5 条都写入正文。`hypery11/flipper-tesla-fsd` 不在这 5 条里，来自电力电子检索；话题含 `can-bus`、描述含 ESP32，比 BMS 仪表更贴近嵌入式，完整条目写在本节，电力电子一节一行带过。`TheYoctoJester/dutler` 不在这 5 条里，来自功率器件检索；话题含 `embedded` 与 `firmware`，比描述里的 MOSFET 拉带更贴近嵌入式，完整条目写在本节，功率器件一节一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-17 stars:>3`。`total_count=8773`，返回 5，规则保留 3，未命中 1，清单类排除 1。剩余配额 9。正文保留 `Comfy-Org/ComfyUI`（142338，topic `pytorch`；话题 `stable-diffusion` 按词边界命中 `diffusion`）、`browser-use/browser-use`（118982，topic `llm` 与 `ai-agents`）、`earendil-works/pi`（117437，描述命中强特征词 `llm`，话题为空）。
  - 清单类排除：`Shubhamsaboo/awesome-llm-apps`（总 star 142815）。名称含 awesome 与 llm，是代理应用合集，不进正文。
  - 未命中：`langflow-ai/langflow`（总 star 155967）。描述里的 AI-powered agents 是弱词，名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-17 stars:>3`。`total_count=22`，返回 5，规则保留 2，未命中 3。剩余配额 8。规则保留的 2 条里，`epilys/sic` 人工剔除，`dutler` 完整条目在嵌入式，本节只留一行。本页没有功率器件完整条目。
  - `epilys/sic`（总 star 26）：仓库名命中 `sic`，内容是按标签组织的链接聚合，与碳化硅器件无关，正文不收。
  - `TheYoctoJester/dutler`（23）：描述命中强特征词 `mosfet`，话题含 `embedded` 与 `firmware`。项目是 Pico 上的串口桥和上电调试器，完整条目在嵌入式，功率器件一节一行带过。
  - 名称按词边界不等于 `sic`，也没有功率器件话题：`hexlet-volunteers/hexlet-sicp`（114）、`neo954/sichuan-cookbook`（38）、`opencad-abu/SiCo`（21）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-17 stars:>3`。`total_count=377`，返回 5，规则保留 2，未命中电力电子 3。剩余配额 9。正文完整条目为 `syssi/esphome-jk-bms`（1040）。`flipper-tesla-fsd` 在本节只留一行。
  - `hypery11/flipper-tesla-fsd`（1159）：描述含 `BMS`（电池管理仪表），话题含 `can-bus`，描述含 ESP32。完整条目在嵌入式。
  - `syssi/esphome-jk-bms`（1040）：topic `bms`，是极空电池管理系统，正文保留。
  - 名称和 topics 未命中电力电子：`rordenlab/dcm2niix`（1205）、`postgrespro/rum`（847）、`NVIDIA/DCGM`（807）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-17 stars:>3`。`total_count=211`，返回 5，规则保留 2，清单类排除 1，未命中 2。剩余配额 9。正文保留 `introlab/rtabmap`（4054）、`RainerKuemmerle/g2o`（3474）。
  - 清单类排除：`jslee02/awesome-robotics-libraries`（总 star 3091）。话题含 `slam`，是机器人库合集，不进正文。
  - 未命中：`vedderb/bldc`（3531）。描述是 “motor control”（空格），名称 `bldc` 不在自动控制关键词表，正文不收。
  - 未命中：`ldrolez/free-midi-chords`（2346）。描述里的 Akai MPC 是音序器，`mpc` 不是强特征描述词，名称和 topics 都没有领域关键词，正文不收。
