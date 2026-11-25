# Progress · 2026-11-25

## English

The Zero 2 W receives wireless CarPlay from an iPhone through a CPC200-CCPA and outputs it to a standard HDMI monitor. The user confirmed pairing and a normal picture. The project still validates display, compute and energy as separable modules, with CarPlay as the V1 workload.

| Check | Observed result |
|---|---|
| System boot | Raspberry Pi OS Lite 64-bit, Debian Bookworm. Local and SSH login worked. Boot and root filesystems were mounted read/write. No MMC, filesystem or undervoltage errors matched the checks in that boot after installation. Cold-boot repeatability remains unverified. |
| Native build | FastCarPlay built on the Zero 2 W at [f483456](https://github.com/niellun/FastCarPlay/commit/f483456318344710d2890fc7ee0d67608892dea2), with the USB compatibility patch applied for the bench run. The ARM64 executable launched with its dynamic libraries resolved. |
| USB receiver | The box enumerated as `1314:1521`. FastCarPlay opened it as a regular user after the scoped udev rule and USB configuration patch. |
| HDMI and decoder | The user confirmed the standard monitor showed a normal CarPlay picture. H.264 initialized through `h264_v4l2m2m` and `bcm2835-codec-decode`. Frame timing and sustained decode performance were not measured. |
| Reconnect | The iPhone automatically reconnected in **22.56 s** from starting the new FastCarPlay service, including **18.68 s** to USB box recognition and **3.88 s** from USB recognition to the phone-connected event. This single software-restart sample exceeded the **15 s** target on that timing basis. Five-run repeatability, screen recovery timing and cold boot remain open. |
| Remaining gates | Software input, physical GPIO controls, display blanking, OL23 integration, audio behavior, detachable power and wear testing still need validation. |

The original image passed exact-length readback on the Mac. Earlier first-boot MMC errors were followed by a mismatch between the card's disk identifier and its boot and mount configuration. Restoring the expected identifier enabled boot on the 16 GB card. The earlier intermittent I/O faults were not isolated. Card health, cold starts and sustained reliability are still open.

Next, use the existing HDMI bench to verify left, right, select and back through the receiver's software input interface. Then test the EC11 and physical back button. Use the [bench deployment guide](../host/README.md) and [acceptance plan](../tests/test_plan.md).

## 中文

Zero 2 W 已能通过 CPC200-CCPA 接收 iPhone 无线 CarPlay，并输出到普通 HDMI 显示器。用户确认配对成功、画面正常。项目继续用 CarPlay 验证显示、运算和能源模块分离。

| 项目 | 实测结果 |
|---|---|
| 系统启动 | Raspberry Pi OS Lite 64 位，Debian Bookworm。本地和 SSH 登录成功，启动及根分区均可写。安装后检查的本次启动日志里未发现匹配的 MMC、文件系统或欠压错误。冷启动复测尚未完成。 |
| 本机编译 | 在 Zero 2 W 上编译固定版本 [f483456](https://github.com/niellun/FastCarPlay/commit/f483456318344710d2890fc7ee0d67608892dea2)，台架运行版本已应用 USB 兼容补丁。ARM64 程序能启动，动态库引用齐全。 |
| USB 盒子 | 实物枚举为 `1314:1521`。配置专用 udev 规则并应用 USB 补丁后，FastCarPlay 以普通账号打开盒子。 |
| HDMI 与解码 | 用户确认普通屏的 CarPlay 画面正常。H.264 经 `h264_v4l2m2m` 和 `bcm2835-codec-decode` 成功初始化。帧时序和持续解码性能尚未测量。 |
| 重连 | 单次软件重启，从启动新 FastCarPlay 服务到手机协议连上共 **22.56 秒**，其中识别盒子 **18.68 秒**，盒子识别到手机连上 **3.88 秒**。以此次计时口径超过 **15 秒**目标。五轮复测、画面恢复计时和冷启动尚未完成。 |
| 待验证 | 软件输入、GPIO 实物控件、显示黑屏、OL23、音频、可拆离供电和佩戴测试。 |

原版镜像曾在 Mac 上通过完整镜像范围读回校验。早期首次启动出现 MMC 写入错误，随后发现卡的磁盘编号与启动、挂载配置不一致。恢复预期编号后，16 GB 卡可以启动。此前的间歇 I/O 错误尚未归因，整卡健康、冷启动和持续可靠性仍待验证。

下一步在现有 HDMI 台架验证左、右、确认、返回的软件输入，再接 EC11 和实物返回键。[部署指南](../host/README.md) · [验收计划](../tests/test_plan.md)
