# Progress — 2026-11-22

## English

The project validates separation of display, compute and energy modules, with sustained wear driving a minimal head-worn assembly. CarPlay is the V1 demonstration workload. V1 uses an external USB 5V power bank; no custom battery, charger or boost-board development is planned.

### Current state

| Item | Status | Evidence / scope |
|---|---|---|
| Parts availability | User-reported | Parts reported ordered or available and subsequently received; exact delivered versions remain to be checked |
| Base OS image | PASS | Official Raspberry Pi OS Legacy Lite 64-bit, Debian Bookworm, release 2026-10-06 |
| Image integrity | PASS | Extracted image: 2,743,074,816 bytes; SHA-256 below matches official catalog metadata |
| System image write | PASS | 64KiB writes completed; raw device readback over the exact image length matched the same SHA-256 |
| Boot layout and files | PASS | FAT32 boot and Linux partitions identified; config.txt, cmdline.txt, kernel8.img and Zero 2 W device tree checked |
| Installer preparation | PASS, preparation only | Manual installation script and bilingual instructions copied to boot partition and read back; shell syntax checked; macOS execution rejected by platform guard |
| Safe removal | UNVERIFIED | Command-line unmount/eject timed out. A later read-only check still found the boot volume mounted, with no listed writer/mount/eject processes and no open files reported by lsof; safe removal has not completed |
| Pi first boot / network | UNVERIFIED | No on-device boot or network evidence yet |
| FastCarPlay installation / build | PENDING | Must run on the Pi after first login and internet access; source commit is resolved and recorded at installation, not yet selected on the Pi |
| CCPA / optics / GPIO | UNVERIFIED | No end-to-end device validation yet |

Official image SHA-256:
`3503be87118ead788bef3842723715fc12989723fea1990d761cd490e56892f3`

Prepared installer SHA-256:
`c0b81a06d3aa3267aeb200ade693240132e480062dc04b0af9c5d8f005d47469`

The raw-image hash was checked **before** copying the installer files. Subsequent boot-partition additions were separately read back; the final customized card is not claimed to retain the original whole-image hash. These are recorded checks, not evidence of a successful Pi boot or a full-media health test.

### Storage preparation note

Large-transfer attempts encountered USB storage errors. Reformatting restored a mountable volume and a small-file test passed. A subsequent 64KiB write plus full exact-length readback succeeded. This does not isolate the original cause to card, reader, hub or transfer behavior, and does not certify media health.

### Next actions

1. Confirm successful safe ejection before removing the card. If Finder also fails, resolve removal before transferring it to the Pi.
2. Insert the card into Zero 2 W. Temporarily use the USB data port for a keyboard, with a compatible display connected; leave CCPA disconnected during initial setup.
3. Create a personal login locally and connect the Pi to the internet. No passwords, Wi-Fi settings or SSH credentials are included in the prepared files.
4. Run `sudo bash /boot/firmware/setup-fastcarplay.sh "$USER"` on the Pi. The script installs SDL2/FFmpeg/libusb/OpenSSL dependencies, build tools, GPIO Python libraries and diagnostics; it builds FastCarPlay with one job and records logs and the resolved commit.
5. Confirm build output and dependencies, then inspect the actual CCPA USB ID and configure permissions/settings. Validate on a normal monitor before OL23 integration. No autostart or GPIO control implementation is claimed yet.

Procurement working documents, disk identifiers, device/volume UUIDs, local machine paths, original card-file details, raw logs and authentication material are excluded from this public record. Installation scripts and detailed evidence remain local in this update.

References: [official OS catalog](https://downloads.raspberrypi.com/os_list_imagingutility_v4.json), [FastCarPlay](https://github.com/niellun/FastCarPlay).

---

# 中文 · 进展记录（2026-11-22）

项目验证显示、运算、能源模块分离，以长期佩戴需求推动头部模块尽量轻、小、简单；CarPlay为V1演示负载。供电固定为外置充电宝经USB输出5V，不做自制电池、充电板或升压管理板。

## 当前状态

| 项目 | 状态 | 证据与范围 |
|---|---|---|
| 物料 | 用户报告 | 已报告下单或已有，随后报告全部到货；实际硬件版本仍待核对 |
| 基础系统镜像 | PASS | 官方Raspberry Pi OS Legacy Lite 64位，Debian Bookworm，2026-10-06版 |
| 镜像完整性 | PASS | 解压镜像2,743,074,816字节，SHA-256与官方目录一致 |
| 系统镜像刷写 | PASS | 64KiB块写入完成，对卡上完整镜像长度读回计算SHA-256，一致 |
| 启动布局和文件 | PASS | 已识别FAT32启动分区及Linux分区，核对config.txt、cmdline.txt、kernel8.img及Zero 2 W设备树 |
| 安装准备 | PASS，仅准备 | 安装脚本和双语说明已复制到启动分区并读回；Shell语法检查通过，在Mac执行会被平台保护拒绝 |
| 安全推出 | UNVERIFIED | 命令行卸载／推出超时；随后只读复查仍挂载，没有列出的刷写／挂载／推出进程，lsof未报告打开文件；安全移除尚未完成 |
| 树莓派首次启动／联网 | UNVERIFIED | 尚无上板启动和联网证据 |
| FastCarPlay安装／编译 | PENDING | 需在树莓派首次登录、联网后执行；安装时解析并记录源码提交号，目前未在树莓派选定 |
| CCPA／光学／GPIO | UNVERIFIED | 尚未验证完整硬件链路 |

系统镜像SHA-256：
`3503be87118ead788bef3842723715fc12989723fea1990d761cd490e56892f3`

准备的安装脚本SHA-256：
`c0b81a06d3aa3267aeb200ade693240132e480062dc04b0af9c5d8f005d47469`

完整镜像哈希在复制安装文件**之前**验证；新增启动分区文件另行读回核对，不声称修改后的卡仍保持原始整镜像哈希。以上是已记录的检查，不代表已成功启动树莓派或完成整卡健康测试。

## 制卡过程说明

较大传输块刷写时出现USB存储错误。格式化后恢复挂载，小文件读写通过；随后采用64KiB块写入并完成整个镜像长度读回校验。尚未隔离最初故障来自卡、读卡器、扩展坞还是传输行为，不据此认定卡健康或损坏。

## 下一步

1. 确认安全推出成功后再拔卡；Finder若也失败，先解决移除问题，再将卡装入树莓派。
2. 将卡插入Zero 2 W，临时用USB数据口接键盘并连接匹配的显示器；初始化时不接CCPA。
3. 在本机设置个人账户并联网；准备文件未设置密码、Wi-Fi或SSH凭据。
4. 在树莓派运行 `sudo bash /boot/firmware/setup-fastcarplay.sh "$USER"`。脚本安装SDL2／FFmpeg／libusb／OpenSSL依赖、编译工具、GPIO Python库和诊断工具，单线程编译FastCarPlay并记录日志与提交号。
5. 确认编译和依赖后，再检查真实CCPA USB ID并配置权限／设置。先在普通显示器验证，再接OL23；尚未实现自启或GPIO控制程序。

本公开记录不包含采购工作文档、磁盘编号、设备／卷UUID、本机路径、原卡文件细节、原始日志或认证资料。安装脚本和详细证据本次保留本地。

资料：[官方系统目录](https://downloads.raspberrypi.com/os_list_imagingutility_v4.json)、[FastCarPlay](https://github.com/niellun/FastCarPlay)。
