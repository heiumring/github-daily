# GitHub 领域日报 · 2026-10-25

生成时间：2026-10-25 07:34（北京时间）。数据拉取开始于 2026-10-25 07:30:37（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-25（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-18 及之后有推送、总 star > 3。轮换页 `page = (当年第 298 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，眼睛走 AirPlay，手走 USB HID，不必用 Mac，也不必越狱；近 30 天新建，总 star 3790。
2. [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) 在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，要确认时可以就地批准；近 30 天新建，总 star 6373。
3. [makerspet/oomwoo](https://github.com/makerspet/oomwoo) 开源扫地机器人，定位和建图走 ROS 2 与激光 SLAM，板上有 ESP32；领域常青，总 star 12382，没有 24 小时新增数据。

## A. 今日热度

Trending 页面解析到 10 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 0 条。嵌入式、AI、功率器件、电力电子电源、自动控制在这 10 条里都没有命中。

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：3790
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：1109
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：438
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：253
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75C 圆屏 ESP32 上做 Grok 语音终端，眼睛会眨眼，带字幕和朗读，固件和后端一起开源。
  - 领域：嵌入式 Embedded
  - 总 star：220

### AI

- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor、Gemini CLI、Antigravity 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：6373
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：4371
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：3790。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：2627
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：253。

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
  - 总 star：87
- [mozihe/z-localization](https://github.com/mozihe/z-localization)
  - 说明：东北大学 T-DT 实验室把 2026 年 RoboMaster 超级对抗赛哨兵的定位开源出来，用 Livox MID360 做激光雷达与 IMU 里程计，并带重定位，跑在 ROS 2 上。
  - 领域：自动控制 Control
  - 总 star：75
- [zhuoligetu123/mid360-campus-slam](https://github.com/zhuoligetu123/mid360-campus-slam)
  - 说明：在 ROS 2 Humble 上用 Livox MID360 做园区三维建图和重定位，用 ScanContext 做回环，并能导出二维地图。
  - 领域：自动控制 Control
  - 总 star：25

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 3。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件，Sub-GHz、NFC、红外这些功能都跑在板载 STM32 上。
  - 领域：嵌入式 Embedded
  - 总 star：16773
- [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder)
  - 说明：跑在 ESP32 上的 Wi-Fi/蓝牙工具固件，既能做探测，也带进攻性测试功能，可以接到 Flipper Zero。
  - 领域：嵌入式 Embedded
  - 总 star：12890
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见下方「自动控制 Control」完整条目。话题含 esp32，此处不展开。领域：嵌入式 Embedded。总 star：12382。
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用 YAML 配置 ESP32、ESP8266 等芯片上的外设，再接到家庭自动化系统里远程控制，不必为每个节点重写固件。
  - 领域：嵌入式 Embedded
  - 总 star：11948
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给小智 ESP32 语音设备提供后端，用来尽快搭起设备控制服务器。
  - 领域：嵌入式 Embedded
  - 总 star：11021
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：705。
- [TheYoctoJester/dutler](https://github.com/TheYoctoJester/dutler)
  - 说明：把 Raspberry Pi Pico 变成被测设备的 USB 串口桥，带电源继电器和 MOSFET 拉带复位，用来给嵌入式 Linux 做上电调试和硬件在环。
  - 领域：嵌入式 Embedded
  - 总 star：23

### AI

- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
  - 说明：把 Gemini 放进终端，做成开源的命令行编程助手。
  - 领域：AI
  - 总 star：108026
- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：用张量和动态计算图在 Python 里做神经网络，并靠 GPU 加速训练和推理。这是框架本体。
  - 领域：AI
  - 总 star：105047
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
  - 说明：编程助手换一次会话就会忘掉刚才做过什么。它把会话里的操作压缩保存，下次再把相关上下文注入回去。
  - 领域：AI
  - 总 star：102817
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
  - 说明：给编程代理补上审美，用美术方向、参考图和浏览器检查来避免千篇一律的页面。
  - 领域：AI
  - 总 star：102008
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2170。

### 功率器件 Power Devices

本页没有以功率器件为最贴近领域的完整条目。`TheYoctoJester/dutler` 是嵌入式 Linux 的上电调试桥，完整说明写在上方嵌入式。`wkcollis1-eng/DIY-LiFePO4-UPS` 是 12V 磷酸铁锂不间断电源，完整说明写在下方电力电子。

- [TheYoctoJester/dutler](https://github.com/TheYoctoJester/dutler) — 见上方「嵌入式 Embedded」完整条目。描述含 MOSFET 拉带复位，此处不展开。领域：功率器件 Power Devices。总 star：23。
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：15。

### 电力电子电源 Power Supply

- [StephanJoubert/home_assistant_solarman](https://github.com/StephanJoubert/home_assistant_solarman)
  - 说明：把接在 Deye、Sofar、Solis、Sunsynk、Sol-Ark 等逆变器上的 Solarman 采集器读进 Home Assistant，用来在家里看这些逆变器的运行数据。
  - 领域：电力电子电源 Power Supply
  - 总 star：741
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：把阳光电源 SH*RT、SHx.RS、SH*K、SxT 这几族逆变器接到 Home Assistant，经 Modbus 读运行数据。
  - 领域：电力电子电源 Power Supply
  - 总 star：705
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 和网络设备做的 12V 磷酸铁锂不间断电源，带设计文档和停电实测记录，掉电时按电压斜率触发关机。
  - 领域：电力电子电源 Power Supply
  - 总 star：15

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：开源扫地机器人，用激光雷达做同步定位与建图，控制栈走 ROS 2；主控侧有 ESP32，但要解决的是清扫机器人怎么走。
  - 领域：自动控制 Control
  - 总 star：12382
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：移动机器人编程工具包，把定位、建图、粒子滤波和传感器处理放在一套 C++ 库里。
  - 领域：自动控制 Control
  - 总 star：2170

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 10 条，规则命中 0 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`cloudflare/security-audit-skill`（44474，2271）、`NVIDIA/OpenShell`（19461，893；描述里的 AI agents 是弱词）、`pbakaus/impeccable`（86366，733）、`Nutlope/hallmark`（32105，570）、`makecindy/cindy`（4074，471；描述里的 AI Agent 是弱词）、`luongnv89/claude-howto`（44530，442）、`pollen-robotics/microduck`（10966，381；双足小鸭机器人，名称和描述都没有领域词）、`jbiaojerry/ebook-treasure-chest`（22580，220；电子书下载链接合集，名称和描述都没有领域词）、`google-gemini/gemini-cli`（108026，38；描述里的 AI agent 是弱词。常青检索因话题 `ai-agents` 收录，搜索总 star 同样是 108026，两处各用各源数字，C 块不写这 38）、`aws/agent-toolkit-for-aws`（3119，11；描述里的 MCP 与 AI agents 都是弱词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-25 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-25 stars:>2`。`total_count=387`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文。`onehumanbeing/esp32-iphone-agent`（3790）和 `raullenchai/esp32-thinks`（253）同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-25 stars:>2`。`total_count=2379`，返回 5，规则保留 3，未命中 2，排除清单 0。剩余配额 9。正文保留 `Louis-CFM/coucou`（6373）、`QingYunA/answer-me-with-html`（4371）、`Leonxlnx/earshot`（2627）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`kaankiziltug/logo-design-skill`（总 star 4457；描述里的 AI agents 是弱词）、`openfilm/openfilm`（总 star 2589；描述里的 AI video agent 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-25 stars:>2`。`total_count=5`，返回 5，规则保留 3，未命中 2。剩余配额 7。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 9）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 5）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（23）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`SiCo`、`Sichuan` 按词边界都不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-25 stars:>2`。`total_count=71`，返回 5，规则保留 0。剩余配额 8。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（190）、`CompaLarios18/MH4UltimateDC`（50）、`Lida-V/3DCharaMakeSkills-Lida`（49）、`lamb2k/re4dc`（36）、`meztinos515/Acrobat-Pro-DC`（36）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-25 stars:>2`。`total_count=52`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `TrentIndeed/kinetiqgym`（87）、`mozihe/z-localization`（75）、`zhuoligetu123/mid360-campus-slam`（25）。
  - 名称和 topics 未命中：`xwtk/hmg_nemesis`（144）、`lbgos/rift-s-linux`（30；描述里的 SLAM 不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-18 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-18 stars:>3`。`total_count=1151`，返回 5，规则保留 5，清单类排除 0。剩余配额 9。这 5 条都写入正文。`makerspet/oomwoo` 同时话题含 `ros2` 与 `slam`，要解决的是扫地机器人怎么走，完整条目在自动控制，本节一行带过。`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant` 不在这 5 条里，来自电力电子检索；话题含 `modbus`，本节一行带过。`TheYoctoJester/dutler` 不在这 5 条里，来自功率器件检索；话题含 `embedded` 与 `firmware`，比描述里的 MOSFET 拉带更贴近嵌入式，完整条目写在本节，功率器件一节一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-18 stars:>3`。`total_count=8882`，返回 5，规则保留 4，未命中 1，清单类排除 0。剩余配额 8。正文保留 `google-gemini/gemini-cli`（108026，topic `ai-agents`）、`pytorch/pytorch`（105047，仓库名 `pytorch`）、`thedotmack/claude-mem`（102817，topic `ai-agents`）、`Leonxlnx/taste-skill`（102008，topic `ai-agents`）。`MRPT/mrpt` 不在这 5 条里，来自自动控制检索，话题含 `computer-vision`，本节一行带过。
  - 未命中：`nexu-io/open-design`（总 star 103759）。描述里的 AI Design Agent 是弱词，名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-18 stars:>3`。`total_count=25`，返回 5，规则保留 2，未命中 3。剩余配额 9。规则保留的 2 条里，`dutler` 完整条目在嵌入式，`DIY-LiFePO4-UPS` 完整条目在电力电子，本节各留一行。本页没有功率器件完整条目。
  - `TheYoctoJester/dutler`（23）：描述命中强特征词 `mosfet`，话题含 `embedded` 与 `firmware`。项目是 Pico 上的串口桥和上电调试器，完整条目在嵌入式。
  - `wkcollis1-eng/DIY-LiFePO4-UPS`（15）：话题含 `mosfet` 与 `power-supply`。项目是 12V 磷酸铁锂 UPS，完整条目在电力电子。
  - 名称按词边界不等于 `sic`，也没有功率器件话题：`ducroo/SICTIC-AI`（14；瑞士商业天使俱乐部 SICTIC）、`MadestSamurai/bd2-sichuan`（13）、`Reinazhard/guacamole_sickness`（12）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-18 stars:>3`。`total_count=381`，返回 5，规则保留 2，未命中电力电子 3。剩余配额 8。正文完整条目为 `StephanJoubert/home_assistant_solarman`（741，topic `inverter`）和 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（705，topic `inverter`）。阳光电源那条同时话题含 `modbus`，嵌入式一节一行带过。`wkcollis1-eng/DIY-LiFePO4-UPS`（15）不在这 5 条里，来自功率器件检索，话题含 `power-supply`，完整条目写在本节。
  - 名称和 topics 未命中电力电子：`NVIDIA/DCGM`（807）、`dcs-liberation/dcs_liberation`（799）、`decred/dcrd`（775）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-18 stars:>3`。`total_count=219`，返回 5，规则保留 1，清单类排除 2，未命中 2。剩余配额 8。正文保留 `MRPT/mrpt`（2170）。`makerspet/oomwoo`（12382）来自嵌入式检索，话题含 `ros2` 与 `slam`，完整条目写在本节。`MRPT/mrpt` 同时话题含 `computer-vision`，AI 一节一行带过。
  - 清单类排除：`jslee02/awesome-robotics-libraries`（总 star 3092）。话题含 `slam`，是机器人库合集，不进正文。
  - 清单类排除：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2151）。话题含 `slam`，是论文清单，不进正文。
  - 未命中：`ldrolez/free-midi-chords`（2348）。描述里的 Akai MPC 是音序器，`mpc` 不是强特征描述词，名称和 topics 都没有领域关键词，正文不收。
  - 未命中：`nvidia-isaac/cuVSLAM`（1876）。名称 `cuVSLAM` 按词边界不等于 `slam`，描述里的 SLAM 不是强特征词，正文不收。
