# Implementation checklist

## English

The goal is modular display/compute/energy validation. CarPlay is the first workload. Estimated development effort is 18–29 hours, excluding shipping, compatibility problems, and rework. Completed items require evidence; planning is not a hardware test.

Current checkpoint: [progress record](progress.md). SD base-image write/readback passed; first boot, software installation and hardware checks remain pending.

### M0 · Preparation (1–2h)

- [x] Create the local Git project.
- [x] Create the GitHub repository and push initial content.
- [x] Select FastCarPlay and define phased purchasing.
- [ ] Confirm OL23 HDMI connector, input timings, and original external-power instructions.
- [ ] Confirm CCPA hardware/firmware version, AutoKit support, and return conditions.
- [ ] Inventory power supplies, microSD, tools, and printing materials.
- [ ] Purchase the first batch; record links and delivered versions.

### M1 · CarPlay bench prototype (3–5h)

- [x] Select and record official Bookworm Lite 64-bit, 2026-10-06; complete image write and raw readback verification.
- [ ] Confirm safe ejection, first boot, account setup and internet connection.
- [ ] Fetch FastCarPlay, record its commit, and build release.
- [ ] Connect CCPA through OTG; record VID:PID with lsusb and configure USB permissions.
- [ ] Verify wireless pairing and hardware video decoding on a normal HDMI monitor.
- [ ] Verify Left/Right/Enter/Backspace, reconnection, and stability.

Gate: stabilize the normal-monitor chain before optical integration. Do not remove the adapter enclosure yet.

### M2 · Optical validation (2–3h)

- [ ] Confirm voltage, polarity, and original power instructions before connecting OL23.
- [ ] Record EDID, input timings, scaling, mirroring, and active image area.
- [ ] Assess map text and readability against indoor/outdoor backgrounds.
- [ ] Measure display-board power at maximum brightness.
- [ ] Determine monocular placement and adjustment range.

Gate: HDMI timing compatibility and readability must pass before wearable geometry is finalized.

### M3 · Physical interaction (2–4h)

- [ ] Breadboard EC11 and two buttons.
- [ ] Implement GPIO debouncing and an encoder state machine, including rapid reversal.
- [ ] Emit Left/Right/Enter/Backspace through uinput.
- [ ] Implement display blank/restore; distinguish software black from display-power switching.
- [ ] Define boot, service failure, and CarPlay-disconnect display states.
- [ ] Test sustained scrolling, unintended input, and latency.

### M4 · Energy module and separation (2–3h)

- [ ] Start with a power bank; record supply-side and board-side voltages.
- [ ] Measure average/peak power and low-battery behavior.
- [ ] Measure steady-state temperature rise.
- [ ] Confirm USB power-bank 5V capability, USB cables, distribution wiring and optional display load switch from measurements; no battery/charger development.
- [ ] Verify normal shutdown and power-removal strategy.
- [ ] Verify replaceable energy, retained compute, and an independently connected display; record interfaces and failure behavior.
- [ ] Purchase the second batch.

### M5 · CAD and printing (5–8h)

- [ ] Measure all PCBs, connectors, cable bend radii, and goggle internal clearances.
- [ ] Design adjustable optical mounting and an HDMI-driver enclosure.
- [ ] Design the chest enclosure, board isolation, and thermal paths.
- [ ] Design printed encoder wheel, button caps, and travel limits.
- [ ] Design strain relief and a cable path that actually disconnects under breakaway.
- [ ] Print, trial-fit, revise, and save CAD/slicer parameters.

### M6 · Assembly and testing (3–4h)

- [ ] After bench validation, remove the CCPA enclosure and measure its PCB.
- [ ] Remove the breadboard; solder, insulate, and secure flying wires.
- [ ] Assemble compute, energy interfaces, neck harness, and optical mount.
- [ ] Execute the test plan; record runtime, heat, reconnection, and blanking.
- [ ] Update the final BOM, assembly photos, and version.

Next: confirm safe removal, boot the Pi, run the prepared installer, and establish the normal-monitor bench chain. Parts receipt is user-reported; delivered versions and end-to-end hardware remain unverified.

---

# 中文 · 实施待办

目标是验证显示、运算及能源模块分离，CarPlay作为首个验证负载。

开发估算18–29小时，不含到货、兼容问题及返工。完成项需有记录；不以规划文档代替实测。

当前检查点见[进展记录](progress.md)：SD系统镜像刷写／读回已通过，首次启动、软件安装和硬件验证待完成。

## M0 · 准备（1–2h）

- [x] 建立本地 Git 项目。
- [x] 建立 GitHub 仓库并推送初始内容。
- [x] 固定 FastCarPlay 路线和分批 BOM。
- [ ] 确认 OL23 HDMI 插座、输入时序、外接供电原图。
- [ ] 确认 CCPA 具体硬件/固件、AutoKit 支持及退换条件。
- [ ] 检查已有供电、microSD、工具和打印耗材。
- [ ] 完成第一批采购，登记商品链接及到货版本。

## M1 · CarPlay 桌面原型（3–5h）

- [x] 选定并记录官方Bookworm Lite 64位2026-10-06版，完成镜像写入及完整读回校验。
- [ ] 确认安全推出、首次启动、账户设置及联网。
- [ ] 拉取并记录 FastCarPlay commit，编译 release。
- [ ] OTG 接 CCPA，用 lsusb 记录 VID:PID 并配置 USB 权限。
- [ ] 普通 HDMI 显示器验证无线配对及视频硬解码。
- [ ] 验证 Left / Right / Enter / Backspace、重连和运行稳定性。

关卡：普通屏链路稳定后才进入光学集成；不要提前拆壳。

## M2 · 光学验证（2–3h）

- [ ] 核对电压、极性、原厂外接供电说明后连接 OL23。
- [ ] 记录 EDID、输入时序、缩放、镜像和有效显示区域。
- [ ] 验证地图文字、室内/室外背景可读性。
- [ ] 测量显示板功耗和最大亮度状态。
- [ ] 确认单目位置和可调范围。

关卡：HDMI 时序与可读性通过后才定稿佩戴结构。

## M3 · 物理交互（2–4h）

- [ ] 面包板连接 EC11 和两个按键。
- [ ] 编写 GPIO 消抖和编码器状态机，支持快速反转。
- [ ] 通过 uinput 输出 Left/Right/Enter/Backspace。
- [ ] 实现显示关闭/恢复，明确软件遮黑与切断显示电源的区别。
- [ ] 定义开机、服务异常、CarPlay断连的显示状态。
- [ ] 验证长时间滚动、误触与输入延迟。

## M4 · 能源模块与分离验证（2–3h）

- [ ] 先用移动电源验证，记录供电端和板端电压。
- [ ] 测量整机平均、峰值功耗、低电量行为。
- [ ] 测量连续运行温升。
- [ ] 根据实测确认充电宝5V输出、USB线、分支供电线径及可选显示负载开关；不开发电池或充电板。
- [ ] 验证正常关机与断电策略。
- [ ] 验证能源模块可拆换、运算模块保留、显示模块独立连接，记录接口和故障行为。
- [ ] 完成第二批采购。

## M5 · CAD与打印（5–8h）

- [ ] 测量全部PCB、接口、线缆弯曲半径及风镜内部空间。
- [ ] 设计可调光学支架及 HDMI 驱动板保护壳。
- [ ] 设计胸前外壳、板间隔离及散热路径。
- [ ] 设计打印滚轮、按键帽及限位。
- [ ] 设计线束应力释放和真正可脱离的连接路径。
- [ ] 打印试装、修正，保存CAD及切片参数。

## M6 · 总装和测试（3–4h）

- [ ] 桌面验证完成后拆 CCPA 外壳并记录裸板尺寸。
- [ ] 去面包板、飞线焊接、绝缘和固定。
- [ ] 装配运算模块、能源接口、挂绳及光学支架。
- [ ] 完成测试计划，记录续航、热、重连及黑屏结果。
- [ ] 更新最终BOM、装配照片和版本号。

下一步：确认安全移除，启动树莓派并执行已准备的安装脚本，再完成普通显示器桌面链路。到货为用户报告，实物版本和完整硬件链路仍未验证。
