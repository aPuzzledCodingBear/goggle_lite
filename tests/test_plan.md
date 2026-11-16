# V1 acceptance plan

## English

All entries are targets, not executed results. Use the [measurement template](test_results/README.md). The primary outcome is evidence for separation of display, compute, and energy; CarPlay exercises the interfaces.

| Test | Method | Target |
|---|---|---|
| Module separation | Document interfaces; disconnect, replace, and reconnect display/compute/energy modules | Individually identifiable and replaceable; no compute reflash; hot-plug support is not assumed |
| Energy separation | After centralized 5V bench tests, substitute a separate energy module | Record voltage, cable drop, and failure behavior; no display-module battery |
| Bench chain | Normal monitor, cold start, pairing, map interaction | Stable output without persistent USB resets |
| Cold start | Power-on to ready-to-connect | ≤45s |
| Auto connection | Repeat with paired phone at least 5 times | ≤15s; document timing start point |
| Optical output | Record EDID/timings, scaling, orientation, and text | Readable map text; no critical content clipped |
| Outdoor readability | Record indoor, overcast, shade, and bright backgrounds | Measurements determine supported conditions |
| GPIO | Forward/reverse, rapid reversal, 100 consecutive presses | No missed/duplicate events; response ≤200ms |
| Blanking | Video-record button to dark display | ≤100ms; distinguish software and hardware paths |
| Disconnect | Disable phone radio, unplug CCPA, terminate process | Record automatic blanking and failure states |
| Recovery | Display off/on, CCPA reconnect, phone reconnect | No reflash or system reconfiguration |
| Power/temperature | Navigation ≥2h; record ambient temperature and measurement points | Enclosure target ≤40°C; no thermal throttling/restarts |
| Supply | Measure peaks, board voltage, low battery, shutdown | No undervoltage or abnormal power-loss damage |
| Runtime | Full discharge at fixed brightness/workload | ≥2h after final battery integration |
| Mass | Include cables and fasteners | Added goggle mass ≤30g; chest assembly ≤150g |
| Mount/strap | Stationary wear, normal head turns, controlled pull | No eye contact; stable image; cable breakaway |

Do not conduct initial tests while cycling/driving on public roads. Outdoor dynamic use follows display, power, and fit gates.

---

# 中文 · V1 验收计划

下列均为目标，未执行。记录模板见[test_results/README.md](test_results/README.md)。

| 项目 | 方法 | 目标 |
|---|---|---|
| 模块分离 | 显示/运算/能源分别列出接口、拆换并恢复连接 | 可独立识别和更换，不重刷运算模块；不承诺热插拔 |
| 能源分离 | 集中5V台架供电通过后，更换为独立能源模块 | 供电电压、压降和故障行为有记录，显示模块不装电池 |
| 桌面链路 | 普通屏冷启动、配对、地图操作 | 可稳定输出、无持续USB重置 |
| 冷启动 | 记录上电至可连接时间 | ≤45s |
| 自动连接 | 已配对手机重复测试至少5次 | ≤15s，注明计时起点 |
| 光学显示 | 记录EDID/时序、缩放、方向、文字 | 地图文字可读，无裁切关键内容 |
| 户外可读性 | 室内、阴天、阴影、明亮背景分别拍照记录 | 实测决定可用场景 |
| GPIO | 正反转、快速反转、连续100次按压 | 无漏触或重复触发，响应≤200ms |
| 黑屏 | 录影测量按键至显示灭 | ≤100ms；区分软件和硬件路径 |
| 断连 | 关闭手机无线/拔CCPA/终止进程 | 记录自动黑屏及故障状态 |
| 恢复 | 显示关开、CCPA重插、手机重连 | 无需重刷或重配系统 |
| 功耗/温升 | 运行导航≥2h，记录环境温度和测点 | 外壳目标≤40°C，无热降频/重启 |
| 供电 | 测峰值、板端电压、低电量、关机 | 无欠压和异常断电损坏 |
| 续航 | 固定亮度与负载完整放电测试 | ≥2h（最终电池装配后） |
| 重量 | 含线材固定件称重 | 风镜新增≤30g；胸前≤150g |
| 结构/挂绳 | 静止佩戴、正常转头、受控牵拉 | 不触眼、画面稳定、线缆可脱离 |

首轮不在公共道路骑行/驾驶中测试。未通过显示、供电和佩戴关卡前不做户外动态试用。
