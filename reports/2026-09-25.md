# GitHub 领域日报 · 2026-09-25

生成时间：2026-09-25 06:49（北京时间）。

覆盖时间窗：过去 24 小时，即北京时间 2026-09-24 06:49 至 2026-09-25 06:49。OSS Insight 的 24 小时热榜没有返回仓库，热榜改用 GitHub Trending 的 daily 页（页面上的 stars today）。五个领域的补漏检索是 2026-09-18 及之后有推送、star 大于 3 的仓库，按总 star 取前 10，再按关键词归类，不是 24 小时增星榜。

各节排序：先看 24 小时新增 star，再看总 star。检索结果没有 24 小时新增 star，因此不写这项。一个仓库可以同时出现在多个领域。

## 今日速览

1. [dream-num/univer](https://github.com/dream-num/univer) 是今天领域命中里 24 小时加星最多的仓库（+1,060）：它把表格、文档、幻灯片和 PDF 收进同一个运行时，让 agent 直接改办公文件，而不必分别对接每一种办公软件。
2. [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) 在 ESP32 上做基于 MCP 的聊天机器人，把工具调用落到端侧硬件，而不是只在云端对话。
3. [Aalto-Electric-Drives/motulator](https://github.com/Aalto-Electric-Drives/motulator) 用 Python 仿真电机驱动和并网变流器，方便先验证控制再上硬件；它同时落到功率器件、电力电子电源和自动控制。

## 嵌入式

- [ruvnet/RuView](https://github.com/ruvnet/RuView)：用普通 WiFi 信号做空间感知、生命体征和在场检测，这样不必安装摄像头。领域标签：嵌入式。总 star 94,927。
- [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses)：把带视频的计算机公开课按学科收成一份清单，主题里含嵌入式与计算机视觉，方便按方向找课。领域标签：嵌入式、AI。总 star 83,552。
- [raysan5/raylib](https://github.com/raysan5/raylib)：用简单的 C 接口写游戏和图形程序，并提供 ESP32 等目标，让同一套图形代码能跑到小设备上。领域标签：嵌入式。总 star 34,857。
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)：在 ESP32 上跑基于 MCP 的聊天机器人，把语音助手和工具调用放进可独立部署的小硬件。领域标签：嵌入式、AI。总 star 30,191。
- [arendst/Tasmota](https://github.com/arendst/Tasmota)：给 ESP8266/ESP32 设备提供可本地控制的替代固件，用网页、定时和 MQTT 做智能家居，而不把开关交给云。领域标签：嵌入式。总 star 24,773。
- [lvgl/lvgl](https://github.com/lvgl/lvgl)：给从单片机到带 3D 能力的处理器做嵌入式图形界面，避免每块板子从零画 UI。领域标签：嵌入式。总 star 24,746。
- [wled/WLED](https://github.com/wled/WLED)：用 ESP32 经 WiFi 控制 WS2812B 等可编程灯带，把灯效配置从逐颗写代码变成设备内完成。领域标签：嵌入式。总 star 18,711。
- [tinygo-org/tinygo](https://github.com/tinygo-org/tinygo)：把 Go 编译到单片机和 WebAssembly，让小设备也能用 Go 写固件。领域标签：嵌入式。总 star 17,782。
- [MarlinFirmware/Marlin](https://github.com/MarlinFirmware/Marlin)：给常见 8 位和 32 位控制器提供 3D 打印机固件，让不同机器共用一套运动控制。领域标签：嵌入式。总 star 17,592。
- [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32)：把 Arduino 的写法接到 ESP32 系列上，这样不必一上来就从 ESP-IDF 写起。领域标签：嵌入式。总 star 17,427。
- [betaflight/betaflight](https://github.com/betaflight/betaflight)：开源飞控固件，用来驱动穿越机一类竞速无人机，而不是从零写姿态环。领域标签：嵌入式、自动控制。总 star 11,577。
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)：开源扫地机器人方案，把激光雷达、SLAM 和清扫控制放在可自制的平台上。领域标签：嵌入式、自动控制。总 star 11,155。
- [tbnobody/OpenDTU](https://github.com/tbnobody/OpenDTU)：在 ESP32 上和禾迈、TSUN、Solenso 微型逆变器通信，把阳台光伏的运行数据读出来。领域标签：嵌入式。总 star 2,191。
- [wlcrs/huawei_solar](https://github.com/wlcrs/huawei_solar)：通过 Modbus 把华为光伏逆变器接入 Home Assistant，避免在集成里自己拆寄存器。领域标签：嵌入式。总 star 933。
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)：通过 Modbus 把阳光电源户用逆变器接入 Home Assistant，用来在家庭能源面板里读运行状态。领域标签：嵌入式、电力电子电源。总 star 699。
- [kellerza/sunsynk](https://github.com/kellerza/sunsynk)：读取德业/Sunsynk 逆变器的 Python 库和 Home Assistant 插件，把储能逆变器数据接进本地自动化。领域标签：嵌入式、电力电子电源。总 star 337。

## AI

- [dream-num/univer](https://github.com/dream-num/univer)：把表格、文档、幻灯片、画布和 PDF 收进同一个运行时，让 AI agent 直接操作办公文件。领域标签：AI。总 star 17,525，24 小时新增 star 1,060。
- [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)：提供可端到端控制的 agent harness SDK，用来把模型、工具和运行环境收成能上线的 agent。领域标签：AI。总 star 8,229，24 小时新增 star 463。
- [leejet/stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp)：用纯 C/C++ 跑 SD、Flux、Wan 等扩散模型，让没有 Python 深度学习栈的环境也能做图像生成推理。领域标签：AI。总 star 7,229，24 小时新增 star 69。
- [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)：用量化、剪枝、蒸馏和投机解码压缩模型，以便接到 TensorRT-LLM、vLLM 上加快推理。领域标签：AI。总 star 4,050，24 小时新增 star 22。
- [affaan-m/ECC](https://github.com/affaan-m/ECC)：给 Claude Code、Codex、Cursor 等编程助手补技能、记忆和安全约束，用来稳住 agent 的执行质量，而不是只换一个更大的模型。领域标签：AI。总 star 266,850。
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)：做一个会随着使用积累能力的 agent，避免每次任务都从空白上下文重新开始。领域标签：AI。总 star 248,706。
- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)：DeepSeek 的 agent harness，用插件扩展能力，而不必改核心运行时。领域标签：AI。总 star 235,118。
- [n8n-io/n8n](https://github.com/n8n-io/n8n)：可自托管的工作流平台，用可视化把数百个集成和 AI 能力串起来，减少为每个连接手写胶水代码。领域标签：AI。总 star 205,887。
- [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)：提供搭建和运行自主 agent 的工具，让人不必从模型调用一层层自己搭。领域标签：AI。总 star 187,529。
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)：把网页搜索、抓取和交互收成 API，给 agent 提供能直接用的网页数据。领域标签：AI。总 star 184,292。
- [ollama/ollama](https://github.com/ollama/ollama)：在本机把 Kimi、GLM、DeepSeek、Qwen、Gemma 等开源模型拉起来跑，省掉自己配推理环境。领域标签：AI。总 star 181,640。
- [huggingface/transformers](https://github.com/huggingface/transformers)：用同一套接口定义、训练和推理文本、视觉、音频模型，避免每个模型家族各写一套加载代码。领域标签：AI。总 star 166,616。
- [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide)：把 Java 与后端面试要考的计算机基础、数据库、分布式和 AI 应用收成一份可复习的指南。领域标签：AI。总 star 158,860。
- [langgenius/dify](https://github.com/langgenius/dify)：在一个工作区里搭 agent 工作流和 RAG，从原型到可私有部署不用另起一套栈。领域标签：AI。总 star 157,116。
- [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses)：计算机视频公开课清单，主题覆盖计算机视觉和强化学习，用来按课找公开资源。领域标签：嵌入式、AI。总 star 83,552。
- [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)：基于 MCP 的 ESP32 聊天机器人，把工具调用做到端侧板子上。领域标签：嵌入式、AI。总 star 30,191。
- [cyberbotics/webots](https://github.com/cyberbotics/webots)：机器人仿真器，用来在虚拟环境里验证控制、感知和多机器人场景，而不必先有真机。领域标签：AI、自动控制。总 star 4,663。
- [XHToken/Spark-X2.5](https://github.com/XHToken/Spark-X2.5)：面向端侧的开源模型系列，把 agent 能力放进设备本地能跑的模型，减少对云端大模型的依赖。领域标签：AI。总 star 364。
- [microsoft/Sico](https://github.com/microsoft/Sico)：开源的数字员工平台，让企业 agent 能持续执行并沉淀成资产，而不是停在一次演示。领域标签：AI。总 star 268。
- [siconos/siconos](https://github.com/siconos/siconos)：仿真带碰撞和摩擦的非光滑动力系统。主题里的 mcp 指互补问题求解，不是模型上下文协议，按关键词规则仍归入 AI。领域标签：AI。总 star 187。

## 功率器件

- [mohammadrezwankhan/matlab-simulink-energy-lab](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab)：提供可直接运行的 MATLAB/Simulink 参考模型，覆盖锂电池、功率变换器和储能变流器，用来对照复现而不是从空白模型搭起。领域标签：功率器件、电力电子电源、自动控制。总 star 286。
- [Aalto-Electric-Drives/motulator](https://github.com/Aalto-Electric-Drives/motulator)：用 Python 仿真电机驱动和并网变流器，把功率变换器与电机控制放在同一套可重复的仿真里验证。领域标签：功率器件、电力电子电源、自动控制。总 star 229。
- [medwatt/gmid](https://github.com/medwatt/gmid)：用 gm/Id 查找表和多角点自动选型给 MOSFET 模拟电路定尺寸，减少手工扫管子参数。领域标签：功率器件。总 star 158。

## 电力电子电源

- [MyEMS/myems](https://github.com/MyEMS/myems)：能源管理系统，用来监测微网、光伏和用能，而不是只看一块总表。领域标签：电力电子电源。总 star 732。
- [nominal-io/instro](https://github.com/nominal-io/instro)：用一套库控制电源、示波器、电子负载等测试仪器，避免自动化测试为每台仪器单独写驱动。领域标签：电力电子电源。总 star 706。
- [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant)：把阳光电源户用逆变器经 Modbus 接入 Home Assistant，方便在家庭能源系统里读逆变器状态。领域标签：嵌入式、电力电子电源。总 star 699。
- [springfall2008/batpred](https://github.com/springfall2008/batpred)：预测家庭电池何时充放电并自动调度，用来配合分时电价和多种逆变器。领域标签：电力电子电源。总 star 346。
- [kellerza/sunsynk](https://github.com/kellerza/sunsynk)：德业/Sunsynk 逆变器的 Python 库和 Home Assistant 插件，用来把储能逆变器纳入本地控制。领域标签：嵌入式、电力电子电源。总 star 337。
- [mohammadrezwankhan/matlab-simulink-energy-lab](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab)：可运行的电池、直流变换和构网/跟网储能控制模型，用来复现电力电子与储能案例。领域标签：功率器件、电力电子电源、自动控制。总 star 286。
- [Aalto-Electric-Drives/motulator](https://github.com/Aalto-Electric-Drives/motulator)：仿真电机驱动和并网变流器，用来在上硬件之前检查逆变与控制。领域标签：功率器件、电力电子电源、自动控制。总 star 229。

## 自动控制

- [AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)：用 Python 示例把路径规划、定位和 SLAM 串成可运行的机器人算法教材，方便对照公式做实验。领域标签：自动控制。总 star 30,583。
- [PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot)：开源自动驾驶仪软件，用来飞多旋翼、固定翼等无人系统，而不必自研整套飞控。领域标签：自动控制。总 star 12,695。
- [autowarefoundation/autoware](https://github.com/autowarefoundation/autoware)：开源自动驾驶软件栈，用来做感知、规划和控制这一整条车端链路。领域标签：自动控制。总 star 12,088。
- [betaflight/betaflight](https://github.com/betaflight/betaflight)：开源飞控固件，解决穿越机姿态控制与遥控混控要自己写环路的问题。领域标签：嵌入式、自动控制。总 star 11,577。
- [makerspet/oomwoo](https://github.com/makerspet/oomwoo)：开源扫地机器人，用激光雷达和 SLAM 完成室内定位与清扫，而不是只做遥控小车。领域标签：嵌入式、自动控制。总 star 11,155。
- [ros2/ros2](https://github.com/ros2/ros2)：ROS 2 本体，给机器人提供节点通信和工具链这一层，避免每个机器人项目自造中间件。领域标签：自动控制。总 star 6,084。
- [ros-navigation/navigation2](https://github.com/ros-navigation/navigation2)：ROS 2 导航框架，解决移动机器人定位之后如何规划并跟上路径。领域标签：自动控制。总 star 4,741。
- [cyberbotics/webots](https://github.com/cyberbotics/webots)：在仿真里跑机器人控制与感知，用来在没有样机时验证算法。领域标签：AI、自动控制。总 star 4,663。
- [mohammadrezwankhan/matlab-simulink-energy-lab](https://github.com/mohammadrezwankhan/matlab-simulink-energy-lab)：用 Simulink 模型演示 SOC 扩展卡尔曼滤波，以及构网/跟网储能控制。领域标签：功率器件、电力电子电源、自动控制。总 star 286。
- [Aalto-Electric-Drives/motulator](https://github.com/Aalto-Electric-Drives/motulator)：把电机驱动和并网变流器的控制放进 Python 仿真，用来调试控制算法。领域标签：功率器件、电力电子电源、自动控制。总 star 229。

## 数据源状态

- **OSS Insight**（`GET https://api.ossinsight.io/v1/trends/repos/?period=past_24_hours&language=All`）：失败。HTTP 200，但 `data.rows` 为空，没有仓库可收录。原因：`data_quality.status` 为 `unavailable`，自 2026-03-01 起不可用。原文：This ranking is ordered by recent star/PR/issue event counts, and our capture of those events fell to roughly 0.3% of baseline, so the ordering would be noise. An empty result here means the metric cannot be computed, not that there are no matching repositories.
- **GitHub Trending 兜底**（`https://github.com/trending?since=daily`）：成功。因为 OSS Insight 失败才抓取。HTTP 200，解析出 14 条，含总 star 与 stars today；stars today 记为 24 小时新增 star。该页不提供 topic，这 14 条只按仓库名和描述归类。其中 4 条命中领域关键词：`dream-num/univer`、`strands-agents/harness-sdk`、`leejet/stable-diffusion.cpp`、`NVIDIA/Model-Optimizer`。另外 10 条在今日热榜上，但名称和描述都没有命中五个领域的关键词，所以没有写入分节。
- **GitHub Search**（`https://api.github.com/search/repositories`）：成功，5 个领域全部 HTTP 200。未认证，串行 5 次，每次间隔 2 秒。没有按字面量发送 `pushed:>7d`：GitHub 会返回 HTTP 422，要求 ISO 8601 日期。也没有把一个领域的全部关键词用 OR 连成一条查询：超过 5 个 OR 同样返回 HTTP 422。实际查询为每个领域 6 个代表性关键词，加上 `pushed:>=2026-09-18 stars:>3`，`sort=stars&order=desc&per_page=10`。归类仍使用完整关键词表。检索命中若只出现在 README 等字段、仓库名/描述/topic 都未命中，则不列入正文。各域 `total_count` / 返回条数：嵌入式 1,287/10，AI 17,621/10，功率器件 45/10，电力电子电源 84/10，自动控制 460/10。检索条目没有 24 小时新增 star。

抓取由仓库内 `scripts/fetch_github_daily.py` 完成，只使用 Python 标准库，脚本中没有账号或密钥。
