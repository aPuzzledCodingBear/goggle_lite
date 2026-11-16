# Zero 2 W 软件准备

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
