# GitHub 领域日报 · 2026-10-22

生成时间：2026-10-22 07:33（北京时间）。数据拉取开始于 2026-10-22 07:31:02（北京时间）。

时间口径：

- **A. 今日热度**：GitHub Trending `since=daily`。页面上的 stars today 就是约 24 小时新增 star，下文「24 小时新增 star」都来自这个字段。
- **B. 领域新项目**：创建时间不早于 2026-09-22（运行日往前 30 天），且总 star > 2。按总 star 排序。没有 24 小时新增数据。
- **C. 领域常青**：2026-10-15 及之后有推送、总 star > 3。轮换页 `page = (当年第 295 天 mod 4) + 1 = 4`。按总 star 排序，不是今日新增。

未调用 OSS Insight 的 24 小时热榜接口。

## 今日速览

1. [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) 在工具输出、日志和检索片段进大模型之前先压缩，让编程代理少烧 token；今日热度命中，总 star 77234，24 小时新增 star 477。
2. [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) 在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor 这些编程助手，要确认时可以就地批准；近 30 天新建，总 star 5877。
3. [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) 用一块约 7 美元的 ESP32 让视觉模型操作真 iPhone，不必用 Mac，也不必越狱；近 30 天新建，总 star 3478。

## A. 今日热度

Trending 页面解析到 11 条。页面不带 topics，因此只按仓库名和强特征描述归类。规则命中 1 条，清单类排除 0 条。按 24 小时新增 star 降序。

- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)
  - 说明：在工具输出、日志、文件和检索片段送进大模型之前先压缩，编程代理大约少用两成 token，JSON 可以压掉大部分，答案保持不变。
  - 领域：AI
  - 总 star：77234
  - 24 小时新增 star：477

## B. 领域新项目

按总 star 降序。本节没有 24 小时新增 star，不写这项。

### 嵌入式 Embedded

- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)
  - 说明：让视觉模型操作一台真 iPhone，眼睛走 AirPlay，手走 USB HID，中间只加一块约 7 美元的 ESP32，不必用 Mac，也不必越狱。
  - 领域：嵌入式 Embedded
  - 总 star：3478
- [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr)
  - 说明：利用 ESP32 未公开的原始 I/Q 采集，把这块常见芯片做成低占空比的软件无线电，用来收信号而不必另买 SDR。
  - 领域：嵌入式 Embedded
  - 总 star：1067
- [Adolanium/hermes-gadget-sdk](https://github.com/Adolanium/hermes-gadget-sdk)
  - 说明：给 Hermes Agent 做能说话、能打字的外设，带 ESP32 固件、Linux 客户端和桌面模拟器，用来把语音设备接到已有助手上。
  - 领域：嵌入式 Embedded
  - 总 star：427
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks)
  - 说明：在 ESP32 上做个人语音助手，唤醒词或旋钮都能开口，识别、对话和合成可以混搭任意兼容 OpenAI 的服务，并流式回放。
  - 领域：嵌入式 Embedded
  - 总 star：242
- [Liu-zhongxian/zongzhu-bot](https://github.com/Liu-zhongxian/zongzhu-bot)
  - 说明：在微雪 1.75 寸圆屏 ESP32 上做 Grok 语音终端，眼睛会眨眼，带字幕和朗读，固件和后端一起开源。
  - 领域：嵌入式 Embedded
  - 总 star：216

### AI

- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou)
  - 说明：在 Mac 刘海和 iPhone 上盯着 Claude Code、Codex、Cursor、Gemini CLI、Antigravity 这些编程助手，需要确认时可以直接在刘海或锁屏上批准。
  - 领域：AI
  - 总 star：5877
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)
  - 说明：让代理把难问题答成一页能直接读的 HTML，用来替代一长串聊天记录。
  - 领域：AI
  - 总 star：4174
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：3478。
- [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu)
  - 说明：把 AI 写出来的日语改成读起来自然的日语，作为给编程代理用的推敲技能，而不是另做一套翻译器。
  - 领域：AI
  - 总 star：2380
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)
  - 说明：给编程代理补上耳朵，让它能听、能审、也能生成声音，只在 CPU 上跑。
  - 领域：AI
  - 总 star：2049
- [raullenchai/esp32-thinks](https://github.com/raullenchai/esp32-thinks) — 见上方「嵌入式 Embedded」完整条目。话题含 llm，此处不展开。领域：AI。总 star：242。

### 功率器件 Power Devices

- [tPkl/OpenRdson](https://github.com/tPkl/OpenRdson)
  - 说明：用开源网格和有限元做场效应管版图的寄生参数提取，用来替代 Synopsys / SFT 的 R3D。
  - 领域：功率器件 Power Devices
  - 总 star：6

### 电力电子电源 Power Supply

本日无新项目。

### 自动控制 Control

- [cocel-postech/genz-lio](https://github.com/cocel-postech/genz-lio)
  - 说明：激光雷达加 IMU 的里程计，话题覆盖室内外、退化和灾害场景；仓库标明发表于 IEEE T-FR 2026。
  - 领域：自动控制 Control
  - 总 star：132
- [TrentIndeed/kinetiqgym](https://github.com/TrentIndeed/kinetiqgym)
  - 说明：用开源硬件做可编程的智能健身器，阻力由直驱电机控制；CAD、构建文件和软件要等样机测完才放出。
  - 领域：自动控制 Control
  - 总 star：77

## C. 领域常青

以下按总 star 排序，没有 24 小时新增数据，属领域内知名仓库而非今日新增。

轮换页为 4。

### 嵌入式 Embedded

- [francescopace/espectre](https://github.com/francescopace/espectre)
  - 说明：用 ESP32 采集 Wi-Fi 信道状态做人体移动感知，带 C++ SDK、ESPHome、Matter 和命令行，覆盖设备从烧录到接入的整段流程。
  - 领域：嵌入式 Embedded
  - 总 star：9670
- [platformio/platformio-core](https://github.com/platformio/platformio-core)
  - 说明：嵌入式固件的构建和包管理入口，把 Arduino、ESP32、Zephyr 等平台的编译、调试和库依赖收进同一套命令行。
  - 领域：嵌入式 Embedded
  - 总 star：9548
- [meshtastic/firmware](https://github.com/meshtastic/firmware)
  - 说明：Meshtastic 的官方固件，用 LoRa 在没有蜂窝和互联网的地方组网，板子覆盖 ESP32、STM32 和 nRF52。
  - 领域：嵌入式 Embedded
  - 总 star：8461
- [crosspoint-reader/crosspoint-reader](https://github.com/crosspoint-reader/crosspoint-reader)
  - 说明：开源电纸书固件，在 ESP32 上读 EPUB。
  - 领域：嵌入式 Embedded
  - 总 star：8450
- [FastLED/FastLED](https://github.com/FastLED/FastLED)
  - 说明：在 Arduino、ESP32、Teensy 上驱动 WS2812 这类可寻址彩灯，用库做动画，不必自己写时序。
  - 领域：嵌入式 Embedded
  - 总 star：7515

### AI

- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
  - 说明：给编程代理补审美：先定美术方向、对参考图，再用浏览器检查，避免生成千篇一律的页面。
  - 领域：AI
  - 总 star：100551
- [vllm-project/vllm](https://github.com/vllm-project/vllm)
  - 说明：高吞吐、省显存的大模型推理和在线服务引擎。
  - 领域：AI
  - 总 star：94846
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
  - 说明：把任意网站爬成适合大模型读的 Markdown，可以自己部署，也可以用他们的云。
  - 领域：AI
  - 总 star：85990
- [unslothai/unsloth](https://github.com/unslothai/unsloth)
  - 说明：在本机界面里跑和微调大模型与扩散模型，支持 GGUF、MLX，以及描述里列出的 Qwen、DeepSeek、Gemma、FLUX 等。
  - 领域：AI
  - 总 star：78375
- [stereolabs/zed-sdk](https://github.com/stereolabs/zed-sdk) — 见下方「自动控制 Control」完整条目。话题含 computer-vision，此处不展开。领域：AI。总 star：1242。

### 功率器件 Power Devices

本页无符合领域的常青仓库。规则命中的 `Oire/sic` 是 Simple Image Converter，`SIC-GT-26-27/Contenido_Colabs_SIC` 是同步课 Colab，都与碳化硅器件无关，不进正文。

### 电力电子电源 Power Supply

- [fl4p/batmon-ha](https://github.com/fl4p/batmon-ha)
  - 说明：Home Assistant 插件，用蓝牙接 JK、JBD、Daly、ANT、SOK、Supervolt 等电池管理系统，把电芯数据读进家里的自动化系统。
  - 领域：电力电子电源 Power Supply
  - 总 star：527

### 自动控制 Control

- [amap-cvlab/ABot-Recon](https://github.com/amap-cvlab/ABot-Recon)
  - 说明：只靠视频做流式三维重建，针对长时间序列把局部上下文接回去，避免建图越跑越漂。
  - 领域：自动控制 Control
  - 总 star：1407
- [MyoHub/myosuite](https://github.com/MyoHub/myosuite)
  - 说明：用 MuJoCo 仿真肌肉骨骼模型，并包成 Gym 任务，用来训练肌肉驱动的运动控制，而不是抽象关节。
  - 领域：自动控制 Control
  - 总 star：1260
- [stereolabs/zed-sdk](https://github.com/stereolabs/zed-sdk)
  - 说明：ZED 深度相机的空间感知套件，用来给机器人和空间应用接立体视觉、点云和 SLAM。
  - 领域：自动控制 Control
  - 总 star：1242

## 数据源状态

全部 11 次请求均 HTTP 200，无 403/429，无重试。相邻请求按脚本间隔 7 秒。搜索响应里的 `X-RateLimit-Remaining` 记在各项后面。`incomplete_results` 均为 false。未认证，未使用令牌。

GitHub 仓库搜索对多个 `topic:` 做 OR 会返回 `total_count=0` 且不报 422。因此每组只用 1 个 `topic:`，其余用关键词表里的词，OR 仍不超过 5 个。功率器件检索没有用裸 `gan`，避免生成对抗网络挤占前 5。复用 `scripts/fetch_github_daily.py`，本次未改脚本。`STRONG_DESC_WORDS` 已含 `inverter`、`bms`、`motor-control`、`motor-drive`、`dc-dc`、`power-supply`、`microgrid`、`mosfet`、`wide-bandgap`、`device-modeling`、`llm`，对应映射已在。未加入 `buck`、`boost`、`pll`、`pid`。

同一仓库最多出现在 2 个领域节。跨领域时，最贴近的领域写完整条目，另一领域只留一行。

### A. Trending

- 来源：`GET https://github.com/trending?since=daily`
- 结果：成功。解析 11 条，规则命中 1 条，清单类排除 0 条。页面没有 `X-RateLimit-Remaining`。
- 命中并写入正文：`headroomlabs-ai/headroom`（总 star 77234，stars today 477）。描述中的 `LLM` 是强特征词。同一句里的 RAG、MCP 是弱词，不单独作为归类依据。
- 未命中（名称与强特征描述都没有领域词），按 stars today 降序，括号内为总 star、stars today：`DietrichGebert/ponytail`（171549，2051；描述里的 AI agent 是弱词）、`cloudflare/security-audit-skill`（36341，1997）、`stablyai/orca`（101191，1543；名称里的 agents 不是 `ai-agents`）、`Graphify-Labs/graphify`（131579，1434）、`Comfy-Org/ComfyUI`（141484，914；描述里的 diffusion 不是强特征词，未计入）、`shiyu-coder/Kronos`（42806，570）、`supabase/supabase`（112973，509；描述里的 AI 是弱词）、`vllm-project/vllm`（94846，439；仓库名 `vllm` 和描述里的 `LLMs` 按词边界都不等于 `llm`。同一仓库在 C 块因话题含 `llm` 写入正文，总 star 与本页一致）、`akitaonrails/ai-memory`（12305，303；名称里的 ai 是弱词）、`twentyhq/twenty`（59134，105；描述里的 AI 是弱词）。
- 说明：页面有 stars today，没有 topics。未调用 `https://api.ossinsight.io/v1/trends/repos/`。

### B. 领域新项目（`created:>=2026-09-22 stars:>2`，`sort=stars`，`per_page=5`，`page=1`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) created:>=2026-09-22 stars:>2`。`total_count=384`，返回 5，规则保留 5，排除清单 0。剩余配额 9。这 5 条都写入正文。`onehumanbeing/esp32-iphone-agent`（3478）和 `raullenchai/esp32-thinks`（242）同时话题含 `llm`，完整条目在本节，AI 一节各一行带过。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) created:>=2026-09-22 stars:>2`。`total_count=2304`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 9。正文保留 `Louis-CFM/coucou`（5877）、`QingYunA/answer-me-with-html`（4174）、`nanaism/yomiyasu`（2380）、`Leonxlnx/earshot`（2049）。另有 2 条跨领域一行：`esp32-iphone-agent`、`esp32-thinks`，来自嵌入式检索。
  - 未命中：`kaankiziltug/logo-design-skill`（总 star 4023；描述里的 AI agents 是弱词）。名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) created:>=2026-09-22 stars:>2`。`total_count=5`，返回 5，规则保留 3，未命中 2。剩余配额 9。正文保留 `tPkl/OpenRdson`（总 star 6，topic `mosfet`）。
  - `marozols/SIC-existence`（总 star 9）：名称和描述含 SIC，内容是 Lean 对「任意维度 SIC 存在性」的形式化证明，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 5）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。
  - 名称和 topics 未命中：`opencad-abu/SiCo`（18）、`XMMO-zzy/Sichuan-College-Upgrade-Progress-Assessment-Platform`（3）。`SiCo`、`Sichuan` 按词边界都不等于 `sic`。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) created:>=2026-09-22 stars:>2`。`total_count=75`，返回 5，规则保留 0。剩余配额 9。正文写「本日无新项目」。
  - 名称和 topics 未命中：`4DCodeBench/4DCodeBench`（182）、`Lida-V/3DCharaMakeSkills-Lida`（48）、`KawaiiBunga/MKVDCU-Recomp`（44）、`ningbainb/Dcode`（37）、`lamb2k/re4dc`（36）。检索词 `dc-dc` 在搜索侧撞上了名称里的 DC，分类按词边界没有计入。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) created:>=2026-09-22 stars:>2`。`total_count=49`，返回 5，规则保留 3，未命中 2。剩余配额 8。正文保留 `cocel-postech/genz-lio`（132）、`TrentIndeed/kinetiqgym`（77）。
  - `sd88me/mpc-vst-plugins`（总 star 121）：仓库名命中 `mpc`，实为 Akai MPC 音序器的 VST 皮肤，与模型预测控制无关，正文不收。
  - 名称和 topics 未命中：`xwtk/hmg_nemesis`（93）、`lbgos/rift-s-linux`（26；描述里的 SLAM 不是强特征词）。

### C. 领域常青（`pushed:>=2026-10-15 stars:>3`，`sort=stars`，`per_page=5`，`page=4`）

- 嵌入式：成功。查询 `(topic:embedded OR esp32 OR stm32 OR zephyr OR freertos) pushed:>=2026-10-15 stars:>3`。`total_count=1155`，返回 5，规则保留 5，清单类排除 0。剩余配额 8。这 5 条都写入正文。
- AI：成功。查询 `(topic:llm OR pytorch OR transformer OR diffusion OR ai-agents) pushed:>=2026-10-15 stars:>3`。`total_count=8592`，返回 5，规则保留 4，未命中 1，排除清单 0。剩余配额 8。正文保留 `Leonxlnx/taste-skill`（100551，topic `ai-agents`）、`vllm-project/vllm`（94846，话题含 `llm`、`pytorch`、`transformer`）、`unclecode/crawl4ai`（85990，话题含 `llm` 与 `ai-agents`）、`unslothai/unsloth`（78375，话题含 `llm`，`stable-diffusion` 按词边界命中 `diffusion`，另有 `reinforcement-learning`）。另有一行来自自动控制检索：`stereolabs/zed-sdk`（话题含 `computer-vision`）。
  - 未命中：`lobehub/lobehub`（总 star 83393）。描述里的 agents、AI 是弱词，名称和 topics 都没有领域关键词。
- 功率器件：成功。查询 `(topic:power-electronics OR igbt OR sic OR mosfet OR wide-bandgap) pushed:>=2026-10-15 stars:>3`。`total_count=19`，返回 4，规则保留 2，未命中 2。剩余配额 8。`per_page=5` 时第 4 页是末页，所以本页只有 4 条，不是请求失败。规则保留的两条人工剔除后，本页没有功率器件完整条目。
  - `Oire/sic`（总 star 5）：名称和描述含 SIC，内容是 Simple Image Converter，与碳化硅器件无关，正文不收。
  - `SIC-GT-26-27/Contenido_Colabs_SIC`（总 star 5）：名称含 SIC，描述是同步课用的 Colab 文件，与碳化硅器件无关，正文不收。同一仓库也出现在本日新项目检索里，两边都不进正文。
  - 名称按词边界不等于 `sic`：`PanosMagic32/sick-fansubs`（4）、`tbermen/SiCoPR`（4）。
- 电力电子电源：成功。查询 `(topic:mppt OR bms OR inverter OR dc-dc OR llc) pushed:>=2026-10-15 stars:>3`。`total_count=364`，返回 5，规则保留 1，未命中 4。剩余配额 7。正文完整条目为 `fl4p/batmon-ha`（527，topic `bms`）。
  - 名称和 topics 未命中电力电子：`AAFOptimus/AAFFamilyDCHAudio`（557）、`hashicorp/consul-replicate`（525）、`dcm4che/dcm4chee-arc-light`（506）、`DCS-Skunkworks/dcs-bios`（437）。检索词 `dc-dc` 撞上了名称里的 DC。
- 自动控制：成功。查询 `(topic:ros2 OR slam OR motor-control OR flight-controller OR mpc) pushed:>=2026-10-15 stars:>3`。`total_count=208`，返回 5，规则保留 4，清单类排除 1，未命中 0。剩余配额 7。正文保留 `amap-cvlab/ABot-Recon`（1407）、`MyoHub/myosuite`（1260）、`stereolabs/zed-sdk`（1242）。`stereolabs/zed-sdk` 同时话题含 `computer-vision`，AI 一节一行带过。
  - 清单类排除：`Awesome-Image-Registration-Organization/awesome-image-registration`（总 star 1550）。话题含 `slam`，是图像配准资料合集，不进正文。
  - 人工剔除：`Vincentqyw/cv-arxiv-daily`（总 star 1507）。话题含 `slam`，仓库是每日自动更新的计算机视觉论文清单，不进正文。
