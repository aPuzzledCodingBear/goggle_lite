# Zero 2 W FastCarPlay bench

## English

The scripts in [fastcarplay](fastcarplay/) reproduce the Bookworm bench configuration. Requirements are Raspberry Pi OS Lite Bookworm arm64, a normal account with sudo and `plugdev` membership, internet access, an HDMI monitor, and the CPC200-CCPA variant enumerating as `1314:1521`.

Run from the Goggle Lite repository as the normal Pi user:

```sh
bash host/fastcarplay/install.sh
bash host/fastcarplay/run-bench.sh
journalctl -u goggle-fastcarplay-bench.service -f
```

Both scripts default to `$HOME/FastCarPlay` and accept a checkout directory as their only argument. The installer updates APT indexes, installs build/runtime dependencies, fetches the pinned upstream revision, checks and applies the compatibility patch, and builds the release with one job. It preserves the existing `conf/settings.txt`. A checkout at another revision or with unexpected tracked edits is rejected. Resolve those edits separately or use a fresh directory.

Connect the box to the Pi data port via USB OTG. The bench launcher installs the [scoped udev rule](fastcarplay/70-goggle-ccpa.rules) and sets the [decimal USB identifiers](fastcarplay/ccpa-1314-1521.conf) when no active USB IDs are set. It backs up the configuration before this change. Resolve conflicting IDs or an existing different rule before retrying. The program runs as the invoking regular user in a transient service. Stop it with `sudo systemctl stop goggle-fastcarplay-bench.service`. The video path uses SDL KMSDRM; iPhone pairing is performed locally with Bluetooth and Wi-Fi enabled. There is no boot-time activation.

### Source and test scope

The [compatibility patch](fastcarplay/ccpa-usb-configuration.patch) modifies [FastCarPlay f483456](https://github.com/niellun/FastCarPlay/commit/f483456318344710d2890fc7ee0d67608892dea2). The CPC200-CCPA exposes a vendor interface and a storage interface. When configuration 1 is already active, the patch skips the redundant `libusb_set_configuration` call, which failed with `LIBUSB_ERROR_BUSY` when the storage driver held its interface. USB reset, selecting configuration 1 when necessary, and claiming interface 0 remain part of the flow. Upstream authorship is retained and the patch is distributed under the upstream [GNU GPL v3 license](fastcarplay/COPYING).

The underlying patched build and bench configuration ran on the Pi. The public install entry point was checked on an isolated pinned-source fixture; fresh installation with these wrappers on another physical Pi remains unverified. See [observations and timing](../docs/progress.md) and the [upstream Pi guide](https://github.com/niellun/FastCarPlay/wiki/Raspbery-Pi-Setup).

### Next input check

Use the working HDMI chain before connecting the optics. The pinned receiver has a `key-pipe-path` FIFO that consumes one byte per SDL key event. Use a dedicated FIFO path inside a directory owned by the bench account with mode `0700`; the receiver unlinks and recreates the path. Native SDL arrow codes do not fit in one byte. Test the documented single-byte left/right aliases or explicit ASCII mappings, confirm Enter including release handling, and verify Backspace on screen. The software input path has not been tested on this bench.

Then breadboard the EC11 and back button using the [GPIO wiring](../hardware/wiring.md). Verify direction, fast reversals, debounce, repeated presses and response using the [acceptance plan](../tests/test_plan.md). Keep the local display blanking control separate from CarPlay commands. OL23 HDMI timing, independent power blanking and audio routing are later validation items.

## 中文 · Zero 2 W FastCarPlay 台架

[fastcarplay](fastcarplay/) 内的脚本用于复现 Bookworm 台架。需要 Raspberry Pi OS Lite Bookworm arm64、拥有 sudo 和 `plugdev` 权限的普通账号、联网、普通 HDMI 显示器，以及 USB 枚举为 `1314:1521` 的 CPC200-CCPA。

在 Pi 上用普通账号进入 Goggle Lite 仓库后运行：

```sh
bash host/fastcarplay/install.sh
bash host/fastcarplay/run-bench.sh
journalctl -u goggle-fastcarplay-bench.service -f
```

两个脚本默认使用 `$HOME/FastCarPlay`，也可以传入一个源码目录。安装脚本刷新 APT 索引、安装构建和运行依赖、取固定版本、校验并应用补丁，再单线程构建 release。它保留已有 `conf/settings.txt`。若已有源码版本不匹配或存在额外的已跟踪修改，请先处理这些改动或改用一个新目录。

用 USB OTG 把盒子接到 Pi 数据口。启动脚本安装[仅匹配该盒子的 udev 规则](fastcarplay/70-goggle-ccpa.rules)。如果配置中还没有启用的 USB ID，先备份，再写入[十进制 USB ID](fastcarplay/ccpa-1314-1521.conf)。已有规则或 ID 有冲突时，先检查再重试。程序以当前普通账号由临时服务运行，可用 `sudo systemctl stop goggle-fastcarplay-bench.service` 停止。视频用 SDL KMSDRM。iPhone 打开蓝牙和 Wi-Fi 后在手机上完成配对。该服务未设置开机自启。

### 源码与验证范围

[兼容补丁](fastcarplay/ccpa-usb-configuration.patch)针对 [FastCarPlay f483456](https://github.com/niellun/FastCarPlay/commit/f483456318344710d2890fc7ee0d67608892dea2)。盒子同时提供厂商接口和存储接口。存储驱动占用接口时，重复调用 `libusb_set_configuration` 会报 `LIBUSB_ERROR_BUSY`。配置 1 已启用时，补丁跳过重复设置。设备重置、必要时选择配置 1、申请接口 0 的流程照常。保留上游署名，补丁遵循上游 [GNU GPL v3](fastcarplay/COPYING)。

打过补丁的程序和台架配置已在 Pi 上运行。公开安装入口已用固定版本的隔离源码检查，在另一台实物 Pi 上从头运行公开脚本仍待验证。[实测与计时](../docs/progress.md) · [上游 Pi 指南](https://github.com/niellun/FastCarPlay/wiki/Raspbery-Pi-Setup)

### 下一步验证输入

先用当前普通 HDMI 链路。固定版本的 `key-pipe-path` 读取 FIFO 中的单字节，并转换为 SDL 按键。接收器会删除并重建这个路径，使用由台架账号拥有、权限为 `0700` 的目录和专用 FIFO 文件名。SDL 方向键码超过一个字节。先验证已记录的单字节左右别名或显式设置的 ASCII 映射，再确认 Enter 的按下与释放以及 Backspace 都在屏幕上正确响应。台架尚未实测这一软件输入路径。

软件验证通过后，按照[ GPIO 接线](../hardware/wiring.md)在面包板上接 EC11 和返回键，按[验收计划](../tests/test_plan.md)测试方向、快速反转、消抖、连续按压和响应。黑屏键独立控制显示。OL23 的 HDMI 时序，独立电源黑屏和音频路径后续验证。
