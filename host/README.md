# Zero 2 W software preparation

## English

Use [niellun/FastCarPlay](https://github.com/niellun/FastCarPlay) and its [Pi setup guide](https://github.com/niellun/FastCarPlay/wiki/Raspbery-Pi-Setup) as the current workload for testing module separation. The compute module must expose documented video, power, and input interfaces rather than coupling its enclosure to the display or energy module.

Review recorded on 2026-11-16: upstream targets Zero 2 W hardware decoding, and its guide lists CPC200-CCPA AutoKit. The README also uses the CCPM name. Validate the delivered hardware/firmware; do not assume every Carlinkit product is interchangeable.

### Bench deployment order

1. Prepare Pi OS Lite 64-bit following upstream guidance. Record OS, kernel, FFmpeg, and upstream commit; compatibility with any arbitrary latest OS is unconfirmed.
2. Install upstream build dependencies, fetch source, and build release. Initially leave networking, partitioning, and overclocking unchanged.
3. Insert CCPA and run `lsusb`. Configure udev and FastCarPlay with the actual VID:PID. udev uses hexadecimal; upstream settings use decimal.
4. Validate wireless pairing, decoding, keyboard control, and reconnection on a normal monitor; retain logs.
5. Pin a passing version before enabling autostart, GPIO service, and display control.

Upstream code is not copied into this repository. Preserve its GPL-3.0 attribution and license if incorporating/modifying it later. This repository currently has no deployable receiver application or GPIO service.

### Adaptation backlog

| Input | Output/behavior |
|---|---|
| EC11 reverse/forward | Left / Right |
| Encoder short press | Enter |
| Back button | Backspace |
| Blanking button | Local display control; no undefined CarPlay key |
| CarPlay disconnect | Blank/disable the display branch; integrate and test the upstream disconnect hook |

Mappings are confirmed in the [upstream README](https://github.com/niellun/FastCarPlay#keys). Proposed implementation: a Python GPIO library for inputs and evdev/uinput for a virtual keyboard. Dependencies, permissions, and systemd units are M3 work.

Support for 640×400 HDMI input is unknown. Panel resolution is not HDMI timing support: read EDID and test scaling. Software black alone does not pass independent hardware-blanking acceptance. A display/energy disconnect must have a documented recovery path without reflashing the compute module.

Audio/Siri require separate input/output device and CarPlay-routing validation; operation without audio peripherals is not promised.

---

# 中文 · Zero 2 W 软件准备

FastCarPlay是模块分离验证的当前负载。运算模块须明确视频、电源和输入接口，不与显示或能源模块的外壳耦合。显示/能源断开后的恢复流程须记录，不应要求重刷运算模块。

采用 [niellun/FastCarPlay](https://github.com/niellun/FastCarPlay) 和其 [Pi安装指南](https://github.com/niellun/FastCarPlay/wiki/Raspbery-Pi-Setup)。2026-11-16核查：上游目标包含Zero 2 W硬解码，指南列出CPC200-CCPA AutoKit。README也出现CCPM称呼，实际须按到货版本验证，不能假定所有Carlinkit产品通用。

## 桌面部署顺序

1. 根据上游指南准备Pi OS Lite 64-bit。记录OS版本、内核、FFmpeg版本与上游commit；不直接认定任意最新OS均兼容。
2. 安装上游列出的构建依赖，拉取源码，构建release；先不改变网络管理、分区或超频设置。
3. 插入CCPA，运行`lsusb`，以真实VID:PID配置udev和FastCarPlay设置。udev用十六进制、上游设置文件使用十进制，注意转换。
4. 使用普通显示器完成无线配对、解码、键盘控制和重连，保留日志。
5. 固定已通过版本再配置开机自启、GPIO服务和显示控制。

不将上游代码复制进本仓库；后续引入/修改时保留GPL-3.0来源和许可证。此仓库当前没有可直接部署的接收程序或GPIO服务。

## 待开发适配

| 输入 | 输出/行为 |
|---|---|
| EC11反转/正转 | Left / Right |
| 编码器短按 | Enter |
| 返回键 | Backspace |
| 黑屏键 | 本地显示控制，不发送无定义CarPlay键 |
| CarPlay断连 | 自动遮黑/关闭显示支路，需接入上游断连钩子验证 |

键映射由[上游README](https://github.com/niellun/FastCarPlay#keys)确认。建议使用Python GPIO库读取硬件、evdev/uinput输出虚拟键盘；具体依赖、权限和systemd单元在M3实现。

HDMI显示板是否支持640×400输入未知。面板分辨率不等于HDMI输入时序，先读EDID并实测缩放。仅软件画黑不能作为独立硬件黑屏验收。

音频、Siri麦克风需要独立确认输出/输入设备及CarPlay路由；当前不承诺无音频外设情况下可用。
