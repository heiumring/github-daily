# GitHub 领域日报 · 2026-10-13

生成时间：2026-10-13 07:36（北京时间）。数据拉取开始于 2026-10-13 07:31:06（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-13（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-06 及之后有推送、总 star > 3。轮换页 `page = (当年第 286 天 mod 4) + 1 = 3`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [lyogavin/airllm](https://github.com/lyogavin/airllm) 是今日 Trending 里唯一命中领域关键词的仓库，24 小时新增 star 886，总 star 37491，要在单张 4GB 显卡上跑超大语言模型推理。
2. [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) 用一次前向做分类、打分和是否判断，而不是逐字生成；近 30 天新建，总 star 32565。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真机 iPhone；近 30 天新建，总 star 545。

## A. 今日热度

Trending 页面解析到 9 条。页面不带 topics，因此只按仓库名和强特征描述归类。按 24 小时新增 star 降序后，命中 1 条。嵌入式、功率器件、电力电子电源、自动控制在这 9 条里没有命中。

### AI

- [lyogavin/airllm](https://github.com/lyogavin/airllm)
  - 说明：在单张 4GB 显卡上做超大语言模型推理，用来在小显存机器上跑本来装不下的模型。
  - 领域：AI
  - 总 star：37491
  - 24 小时新增 star：886

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：855
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：545
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：372
- [Frankweb33/flybrain-robot-bridge](https://github.com/Frankweb33/flybrain-robot-bridge)
  - 说明：把果蝇神经回路的思路接到相机和电机上，用光流和 IMU 把看见的画面变成机器人动作；现在仍是实验桥接，不是完整飞控。
  - 领域：嵌入式 Embedded
  - 总 star：226
- [hyj-STAR/voiceshell-muse-bridge](https://github.com/hyj-STAR/voiceshell-muse-bridge)
  - 说明：声壳是给 Muse 搭的实验桥：ESP32 负责配对，Linux 侧做文本往返，并附有走通记录和兼容性说明。
  - 领域：嵌入式 Embedded
  - 总 star：110

### AI

- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
  - 说明：文本上的分类、打分和是否判断往往还在用自回归模型逐字生成。它一次前向给出这类决定，并按请求挑选检查点。
  - 领域：AI
  - 总 star：32565
- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：4972
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：545。
- [Frankweb33/flybrain-robot-bridge](https://github.com/Frankweb33/flybrain-robot-bridge) — 见上方「嵌入式 Embedded」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：226。
- [hyj-STAR/voiceshell-muse-bridge](https://github.com/hyj-STAR/voiceshell-muse-bridge) — 见上方「嵌入式 Embedded」完整条目。话题含 ai-agents，此处不展开。领域：AI。总 star：110。

### 功率器件 Power Devices

- [tPkl/OpenRdson](https://github.com/tPkl/OpenRdson)
  - 说明：开源的场效应管版图寄生参数提取，用网格和有限元去对标 Synopsys / SFT 的 R3D，给模拟版图做提取。
  - 领域：功率器件 Power Devices
  - 总 star：6

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [HengyiWang/amb3r-slam](https://github.com/HengyiWang/amb3r-slam)
  - 说明：面向公里级范围的 SLAM，用分层后端处理很长的轨迹，而不是只在室内小地图里定位。
  - 领域：自动控制 Control
  - 总 star：74
- [cocel-postech/genz-lio](https://github.com/cocel-postech/genz-lio)
  - 说明：激光雷达加 IMU 的里程计，针对室内外和退化场景把位姿估稳；仓库标明发表于 IEEE T-FR 2026。
  - 领域：自动控制 Control
  - 总 star：71

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 3。

### 嵌入式 Embedded

- [flipperdevices/flipperzero-firmware](https://github.com/flipperdevices/flipperzero-firmware)
  - 说明：Flipper Zero 的官方固件，在 STM32 上提供红外、NFC、RFID 和 Sub-GHz 等板载无线功能。
  - 领域：嵌入式 Embedded
  - 总 star：16711
- [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder)
  - 说明：在 ESP32 上集成一套 WiFi 和蓝牙的检测与测试工具，刷进板子就能带着用。
  - 领域：嵌入式 Embedded
  - 总 star：12732
- [esphome/esphome](https://github.com/esphome/esphome)
  - 说明：用配置文件控制 ESP32、ESP8266 等芯片，并接到家庭自动化系统，把传感器和开关收成可远程管理的设备。
  - 领域：嵌入式 Embedded
  - 总 star：11830
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)
  - 说明：开源扫地机器人，用激光雷达和 SLAM 建图清扫，主控侧用 ESP32，导航栈带 ROS 2。
  - 领域：嵌入式 Embedded
  - 总 star：11473
- [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)
  - 说明：给小智 ESP32 语音设备搭后端控制服务，用来尽快把设备接到自己的服务器，而不必先写一整套后端。
  - 领域：嵌入式 Embedded
  - 总 star：10807
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) — 见下方「电力电子电源 Power Supply」完整条目。话题含 modbus，此处不展开。领域：嵌入式 Embedded。总 star：704。

### AI

- [pytorch/pytorch](https://github.com/pytorch/pytorch)
  - 说明：提供带 GPU 加速的张量和动态神经网络，用来训练和跑模型，而不必自己实现底层张量与自动求导。
  - 领域：AI
  - 总 star：104736
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
  - 说明：编程助手换一次会话就会忘掉刚才做过什么。它把会话里的操作压缩保存，下次再把相关上下文注入回去。
  - 领域：AI
  - 总 star：100078
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
  - 说明：给智能体一个命令行去读和搜索推特、Reddit、YouTube、GitHub、B 站和小红书，不用按网站分别接付费 API。
  - 领域：AI
  - 总 star：96578
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：做高吞吐、省内存的大模型推理和在线服务，用来把模型稳定地对外提供，而不是只在本地单次跑。
  - 领域：AI
  - 总 star：93665
- [MRPT/mrpt](https://github.com/MRPT/mrpt) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：2169。

### 功率器件 Power Devices

- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS) — 见下方「电力电子电源 Power Supply」完整条目。话题含 mosfet，此处不展开。领域：功率器件 Power Devices。总 star：15。

### 电力电子电源 Power Supply

- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)
  - 说明：把阳光电源 SH 等系列逆变器的 Modbus 数据接进 Home Assistant，用来在家里看逆变器状态。
  - 领域：电力电子电源 Power Supply
  - 总 star：704
- [wkcollis1-eng/DIY-LiFePO4-UPS](https://github.com/wkcollis1-eng/DIY-LiFePO4-UPS)
  - 说明：给 Home Assistant 和网络设备做 12V 磷酸铁锂不间断电源，停电时按电压下降斜率决定要不要关机。
  - 领域：电力电子电源 Power Supply
  - 总 star：15

### 自动控制 Control

- [makerspet/oomwoo](https://github.com/makerspet/oomwoo) — 见上方「嵌入式 Embedded」完整条目。话题含 ros2 与 slam，此处不展开。领域：自动控制 Control。总 star：11473。
- [MRPT/mrpt](https://github.com/MRPT/mrpt)
  - 说明：移动机器人编程工具箱，带 SLAM 和运动估计，用来给机器人做定位建图，而不必从零写这些模块。
  - 领域：自动控制 Control
  - 总 star：2169
- [koide3/glim](https://github.com/koide3/glim)
  - 说明：用点云做三维定位和建图，可接到 ROS 2，把激光雷达扫到的场景收成能反复定位的地图。
  - 领域：自动控制 Control
  - 总 star：1873
- [google-deepmind/mujoco_mpc](https://github.com/google-deepmind/mujoco_mpc)
  - 说明：在 MuJoCo 里用模型预测控制实时合成行为，用来在仿真中直接算出下一步动作。
  - 领域：自动控制 Control
  - 总 star：1744

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 9 条，规则命中 1 条（`lyogavin/airllm`，描述中的 `LLM` 命中强特征词 `llm`；仓库名 `airllm` 不能按词边界拆出 `llm`。总 star 37491，stars today 886），清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 未命中（名称与强特征描述都没有领域词）：`morluto/rea`（总 star 154930，stars today 45495）、`bilawalsidhu/gods-eye-view`（53593，1903）、`mksglu/context-mode`（27251，394）、`storytold/artcraft`（21851，4106）、`open-webui/open-webui`（154945，142）、`cathrynlavery/diagram-design`（52533，2100）、`microsoft/BitNet`（40892，134；描述是 “1-bit LLMs”，复数 `LLMs` 按词边界不等于 `llm`）、`Alishahryar1/free-claude-code`（59057，705）。
- 说明：页面有 stars today，没有 topics。描述里的 agent、AI、MCP 等弱词未计入。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-13 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-13 stars:>2`。`total_count=374`，返回 5，规则保留 5，排除清单 0。剩余配额 9。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-13 stars:>2`。`total_count=1960`，返回 5，规则保留 2，未命中 3，排除清单 0。剩余配额 8。正文另有 3 条来自嵌入式检索的跨领域一行（`esp32-iphone-agent`、`flybrain-robot-bridge`、`voiceshell-muse-bridge`）。
  - 未命中：`zai-org/ZCode`（总 star 7724）、`mizorewww/laya-mlx`（6891；描述里的 PyTorch 不是强特征词，且句子是否定用法）、`mhtsec/ARTEX`（3559）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-13 stars:>2`。`total_count=5`，返回 5，规则保留 2，未命中 3。剩余配额 6。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 6）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，不是碳化硅器件，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（16）、`MadestSamurai/bd2-sichuan`（12）、`MicroFarmerVoyage/hellraiser-revival-motion-sickness-tool`（8）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-13 stars:>2`。`total_count=70`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（138）、`ningbainb/Dcode`（37）、`meztinos515/Acrobat-Pro-DC`（35）、`KawaiiBunga/MKVDCU-Recomp`（34）、`lamb2k/re4dc`（24）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-13 stars:>2`。`total_count=51`，返回 5，规则保留 3，未命中控制关键词 2。剩余配额 9。正文保留 2 条。
  - `sd88me/mpc-vst-plugins`（总 star 114）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，不是模型预测控制，正文不收。
  - `Frankweb33/flybrain-robot-bridge`（226）：本查询返回，但未命中控制关键词；已写入嵌入式，并在 AI 一行带过。描述里的 “motor control” 是两个词，不等于 `motor-control`。
  - `xwtk/hmg_nemesis`（56）：名称和 topics 未命中。

### C. 领域常青（`pushed:>=2026-10-06 stars:>3`，`sort=stars`，`per_page=5`，`page=3`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-06 stars:>3`。`total_count=1124`，返回 5，规则保留 5，排除清单 0。剩余配额 8。`mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant` 不在这 5 条里，因话题含 `modbus` 同时命中嵌入式，本节一行带过，完整条目在电源节。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-06 stars:>3`。`total_count=8161`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 7。`pytorch/pytorch` 靠仓库名命中 `pytorch`。`Panniantong/Agent-Reach` 的话题是 `llm-tools`，按词边界命中 `llm`。`MRPT/mrpt` 不在这 5 条里，因话题含 `computer-vision`，本节一行带过。
  - 未命中：`addyosmani/agent-skills`（总 star 105612）。名称和 topics 没有 llm / pytorch / transformer / diffusion / ai-agents。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-06 stars:>3`。`total_count=26`，返回 5，规则保留 2，未命中 3。剩余配额 7。本页没有可展开的功率器件条目。`wkcollis1-eng/DIY-LiFePO4-UPS`（总 star 15）话题含 `mosfet`，完整条目写在电源节，本节一行带过。
  - `libsidplayfp/libresidfp`（总 star 15）：话题含 `mosfet`，内容是 Commodore 64 的 SID 芯片周期精确仿真，不是功率半导体，正文不收。
  - 名称和 topics 未命中：`ducroo/SICTIC-AI`（13；`SICTIC` 按词边界不等于 `sic`）、`SICKAG/sick_perception_sdk`（13）、`linuxserver/docker-sickgear`（12）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-06 stars:>3`。`total_count=351`，返回 5，规则保留 1，未命中 4。剩余配额 9。正文保留 `mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant`（总 star 704，topic `inverter`）。`DIY-LiFePO4-UPS` 来自功率器件检索，话题含 `power-supply`，在本节展开。
  - 名称和 topics 未命中：`Tencent/DCache`（745）、`hackthedev/dcts-shipping`（646）、`ciribob/DCS-SimpleRadioStandalone`（560）、`hashicorp/consul-replicate`（525）。检索词 `dc-dc` 在搜索侧撞上了名称或描述里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-06 stars:>3`。`total_count=221`，返回 5，规则保留 3，清单类排除 1，未命中 1。剩余配额 9。`makerspet/oomwoo` 不在这 5 条里，因话题含 `ros2` 与 `slam`，本节一行带过，完整条目在嵌入式。`google-deepmind/mujoco_mpc` 的话题含 `mpc` 与 `motor-control`，是模型预测控制，不是音序器撞名。
  - 排除清单：`3D-Vision-World/awesome-NeRF-and-3DGS-SLAM`（总 star 2146），awesome 合集。
  - 未命中：`nvidia-isaac/cuVSLAM`（1860）。描述写到 SLAM，但 `slam` 不是强特征描述词；仓库名 `cuVSLAM` 按词边界不能拆出 `slam`。
