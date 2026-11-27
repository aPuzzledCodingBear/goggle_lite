# Progress · 2026-11-27

## English

### 2026-11-27 · Physical controls

- Software input over the FastCarPlay FIFO passed for Left, Right, Enter, and Backspace on the standard HDMI bench. The EC11 and a separate return button then controlled CarPlay through the same path in two short bench runs.
- Rotation initially pulled the encoder's switch input low with the module supply floating. With the module supplied at 3.3 V, ten detents produced no switch event. A separate press still registered.
- A Linux `uinput` bridge was tested on the Pi. Two four-action runs completed with matching Linux input events. The revised launcher passed an on-device module reload and a permissions rollback followed by re-enablement.
- With hardware decoding, one leftward move appeared only after a long delay. Three subsequent runs with software decoding and forced redraw showed the intended moves without the earlier seconds-long delay. On the Phone Favorites page, the first Backspace focused the Favorites tab and the second returned to the app grid.
- The second EC11 adds Up and Down. Three short HDMI bench checks passed. X turned three detents each way with immediate reversal, Y moved down and up once, and alternating the axes moved right, down, left and up. Each returned the focus to its starting point and matched the Linux input sequence. The longer press-count, restart and quantitative latency checks remain open.

### 2026-11-27 · OL23 waveguide

- The Pi identified the HDMI driver as `OL23B`. The external connection to the driver was HDMI alone. A 720p60 pattern was visible, followed by the FastCarPlay waiting screen and wireless CarPlay at the same timing. The display-mode override applies to the current boot only. See the [wiring record](../hardware/wiring.md).
- On the waveguide, alternating the two encoders moved focus right, down, left and up and returned it to the starting icon. The Pi logged the same sequence. The icon names and focus outline were legible.
- In the wear trial, the full image was visible and text was legible. The existing mount and lens contours differ, and the image appears to the right of center. Mount geometry and boot-time display recovery remain open.

### 2026-11-25 · Wireless HDMI bench

The Zero 2 W receives wireless CarPlay from an iPhone through a CPC200-CCPA and outputs it to a standard HDMI monitor. The user confirmed pairing and a normal picture. The project still validates display, compute and energy as separable modules, with CarPlay as the V1 workload.

| Check | Observed result |
|---|---|
| System boot | Raspberry Pi OS Lite 64-bit, Debian Bookworm. Local and SSH login worked. Boot and root filesystems were mounted read/write. No MMC, filesystem or undervoltage errors matched the checks in that boot after installation. Cold-boot repeatability remains unverified. |
| Native build | FastCarPlay built on the Zero 2 W at [f483456](https://github.com/niellun/FastCarPlay/commit/f483456318344710d2890fc7ee0d67608892dea2), with the USB compatibility patch applied for the bench run. The ARM64 executable launched with its dynamic libraries resolved. |
| USB receiver | The box enumerated as `1314:1521`. FastCarPlay opened it as a regular user after the scoped udev rule and USB configuration patch. |
| HDMI and decoder | The user confirmed the standard monitor showed a normal CarPlay picture. H.264 initialized through `h264_v4l2m2m` and `bcm2835-codec-decode`. Frame timing and sustained decode performance were not measured. |
| Reconnect | The iPhone automatically reconnected in **22.56 s** from starting the new FastCarPlay service, including **18.68 s** to USB box recognition and **3.88 s** from USB recognition to the phone-connected event. This single software-restart sample exceeded the **15 s** target on that timing basis. Five-run repeatability, screen recovery timing and cold boot remain open. |
| Remaining gates at this checkpoint | Software input, physical GPIO controls, display blanking, OL23 integration, audio behavior, detachable power and wear testing were still open. |

The original image passed exact-length readback on the Mac. Earlier first-boot MMC errors were followed by a mismatch between the card's disk identifier and its boot and mount configuration. Restoring the expected identifier enabled boot on the 16 GB card. The earlier intermittent I/O faults were not isolated. Card health, cold starts and sustained reliability are still open.

## 中文

### 2026-11-27 · 实体控件

- 普通 HDMI 台架通过 FastCarPlay FIFO 验证了左、右、确认和返回。随后接入 EC11 和独立返回键，通过同一路径完成两轮快速台架验证。
- 模块电源悬空时，旋转会带动确认输入拉低。模块接 3.3 V 后，复测转动 10 格均未触发确认，单独按压仍有信号。
- Pi 上已试用 Linux `uinput` 桥接。两轮四个屏幕动作均完成，Linux 输入日志与操作一致。修订后的启动器通过了实机内核模块重新加载、权限回退及重新启用检查。
- 硬解码时曾出现左移长延迟。后续用软件解码和强制刷新做的三轮对照中，方向正确，未再复现秒级延迟。电话收藏页第一次收到 Backspace 时会聚焦 Favorites 标签，第二次才回到图标页。
- 第二只 EC11 控制上下。普通 HDMI 台架的三项原型短测均通过，分别是 X 轴连续顺拧三格并立刻反拧三格、Y 轴下和上各一格，以及双轴交替右、下、左、上一圈。每项都回到起点，画面与 Linux 输入序列一致。长次数按压、完整重启验证和量化延迟仍未完成。

### 2026-11-27 · OL23 光波导

- Pi 识别到 HDMI 驱动板自报 `OL23B`。驱动板对外只接 HDMI。720p60 彩条可见，随后同一时序下显示了 FastCarPlay 等待页和无线 CarPlay。显示模式覆盖仅在本次开机有效。[接线记录](../hardware/wiring.md)
- 通过光波导看到双旋钮依次使焦点右、下、左、上并回到起点。Pi 日志一致，图标名称和选中框清晰。
- 正常佩戴能看全，文字清晰。现有支架与镜片轮廓有出入，画面偏右。支架形状、位置以及重启后自动恢复画面仍待确认。

### 2026-11-25 · 无线 HDMI 台架

Zero 2 W 已能通过 CPC200-CCPA 接收 iPhone 无线 CarPlay，并输出到普通 HDMI 显示器。用户确认配对成功、画面正常。项目继续用 CarPlay 验证显示、运算和能源模块分离。

| 项目 | 实测结果 |
|---|---|
| 系统启动 | Raspberry Pi OS Lite 64 位，Debian Bookworm。本地和 SSH 登录成功，启动及根分区均可写。安装后检查的本次启动日志里未发现匹配的 MMC、文件系统或欠压错误。冷启动复测尚未完成。 |
| 本机编译 | 在 Zero 2 W 上编译固定版本 [f483456](https://github.com/niellun/FastCarPlay/commit/f483456318344710d2890fc7ee0d67608892dea2)，台架运行版本已应用 USB 兼容补丁。ARM64 程序能启动，动态库引用齐全。 |
| USB 盒子 | 实物枚举为 `1314:1521`。配置专用 udev 规则并应用 USB 补丁后，FastCarPlay 以普通账号打开盒子。 |
| HDMI 与解码 | 用户确认普通屏的 CarPlay 画面正常。H.264 经 `h264_v4l2m2m` 和 `bcm2835-codec-decode` 成功初始化。帧时序和持续解码性能尚未测量。 |
| 重连 | 单次软件重启，从启动新 FastCarPlay 服务到手机协议连上共 **22.56 秒**，其中识别盒子 **18.68 秒**，盒子识别到手机连上 **3.88 秒**。以此次计时口径超过 **15 秒**目标。五轮复测、画面恢复计时和冷启动尚未完成。 |
| 当时待验证 | 软件输入、GPIO 实物控件、显示黑屏、OL23、音频、可拆离供电和佩戴测试。 |

原版镜像曾在 Mac 上通过完整镜像范围读回校验。早期首次启动出现 MMC 写入错误，随后发现卡的磁盘编号与启动、挂载配置不一致。恢复预期编号后，16 GB 卡可以启动。此前的间歇 I/O 错误尚未归因，整卡健康、冷启动和持续可靠性仍待验证。
