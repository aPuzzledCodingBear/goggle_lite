# Wiring and bench connections

English first; Chinese follows. These connections implement a detachable display module, compute module and energy module. CarPlay is the demonstration workload, not the architecture boundary.

GPIO numbers are BCM. The six input lines in the tested dual-axis setup use internal pull-ups and 3.3 V logic.

| Function | BCM GPIO | Physical pin |
|---|---:|---:|
| X encoder `VCC` | 3.3 V supply | 1 |
| X encoder `GND` and Back switch ground | GND | 9 |
| X encoder `A` | 17 | 11 |
| X encoder `B` | 27 | 13 |
| X encoder `SW` (Enter) | 22 | 15 |
| Back switch input (Backspace) | 23 | 16 |
| Y encoder `VCC` | 3.3 V supply | 17 |
| Y encoder `A` | 5 | 29 |
| Y encoder `GND` | GND | 30 |
| Y encoder `B` | 6 | 31 |

For the tested EmbedFire EC11 module, connect `GND` to pin 9, `VCC` to pin 1 (3.3 V), `A` to pin 11, `B` to pin 13, and `SW` to pin 15. Leave the internally grounded `C` pin open. With VCC floating, rotation pulled SW low. Resistance measurements point to coupling through the common VCC rail. Connecting VCC to 3.3 V eliminated the false presses in the bench retest. A bare EC11 uses the encoder common and the separate switch contact to ground. Confirm the actual part with a meter, fit a header where needed, and keep battery/high-current power off the breadboard rails.

B05 is a four-pin normally open tactile switch. Identify its two internally joined pairs with a meter. Connect one pair to ground (pin 9) and the other to GPIO23 (pin 16). Using two contacts from the same pair grounds the input permanently.

Both encoders are EmbedFire EC11 modules. Leave `C` on both modules and `SW` on the Y module open. X clockwise/counterclockwise moves Right/Left and Y clockwise/counterclockwise moves Down/Up. GPIO24 (pin 18) for display blanking and GPIO25 (pin 22) for a display load switch are reserved and unwired in this setup.

## Module interfaces

- **Compute:** Zero 2 W + CCPA + GPIO controls; CCPA connects through a USB-A female OTG cable to Zero's data port. The other Micro USB port powers Zero.
- **Display:** Zero **Mini HDMI Type C** → the tested HDMI cable → OL23 driver (reports `OL23B`) → factory FPC → optical module. The driver-end plug type and cable model have not been documented. The driver's only external connection during the successful test was HDMI.
- **Energy:** the finished 5 V USB power bank feeds the Zero's Micro USB `PWR IN` port. The two encoders take 3.3 V from the Zero header. The power bank cable does not run to the OL23.
- **Wireless:** iPhone connects to CPC200-CCPA over wireless CarPlay. The receiver connects to the Pi over the USB data path above.

## Power and shutdown

The OL23 bench ran with the factory wiring in place. Display blanking and load-switch wiring remain future work. Use the matching vendor drawing before any display-power modification.

A mechanical switch does not shut Linux down cleanly. Use normal shutdown before disconnecting compute power until a shutdown/readonly-filesystem strategy has been verified. Detachable means removable after an appropriate shutdown, not guaranteed hot-swappable.

Pin reference: [Raspberry Pi GPIO documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio).

---

# 接线与台架验证

GPIO 编号为 BCM。当前双轴台架的六路输入均使用内部上拉和 3.3 V 逻辑电平。

| 功能 | BCM GPIO | 40针物理位置 |
|---|---:|---:|
| X 轴旋钮 `VCC` | 3.3 V 电源 | 1 |
| X 轴旋钮 `GND` 和独立返回键地线 | GND | 9 |
| X 轴旋钮 `A` | 17 | 11 |
| X 轴旋钮 `B` | 27 | 13 |
| X 轴旋钮 `SW`（确认） | 22 | 15 |
| 独立返回键输入（Backspace） | 23 | 16 |
| Y 轴旋钮 `VCC` | 3.3 V 电源 | 17 |
| Y 轴旋钮 `A` | 5 | 29 |
| Y 轴旋钮 `GND` | GND | 30 |
| Y 轴旋钮 `B` | 6 | 31 |

实测野火小智 EC11 模块接法为 `GND` 接 9 脚，`VCC` 接 1 脚（3.3 V），`A` 接 11 脚，`B` 接 13 脚，`SW` 接 15 脚。模块的 `C` 已在板内接地，外部留空。模块 VCC 悬空时，旋转会使 SW 拉低。电阻测量显示三路共用 VCC，支持由该节点串扰的判断。VCC 接 3.3 V 后，台架复测未再出现旋转误触。若用裸 EC11，旋转公共端和按压开关的一端分别接地。先用万用表确认实际端子，Zero 无排针时先装排针。电池等大电流供电另走线。

B05 采用常开自复位四脚轻触开关。用万用表识别两组触点，一组接地（9 脚），另一组接 GPIO23（16 脚）。同组两脚分别接 GPIO 和地会使输入常低。

两个旋钮都是野火小智 EC11 模块。两者的 `C` 以及 Y 轴的 `SW` 悬空。X 轴顺转向右、逆转向左，Y 轴顺转向下、逆转向上。GPIO24（18 脚）预留黑屏键，GPIO25（22 脚）预留显示负载开关使能，当前均未接线。

## USB与HDMI

- iPhone 通过无线 CarPlay 连接 CPC200-CCPA。CCPA 经 USB-A 母口 OTG 线接 Zero 2 W 的 Micro USB **数据口**。
- Zero 2 W 的 **Mini HDMI（Type C）** 经实测可用的 HDMI 线接 OL23 驱动板（自报 `OL23B`），驱动板经原厂 FPC 接光机。驱动板一侧的插头规格和线材型号还未记录。
- OL23 驱动板实测只接 HDMI，未接独立电源线。已验证的输出是 **1280×720 @ 60 Hz**，当前设置重启会丢失。见[光波导进展](../docs/progress.md)。

## 电源

5 V 成品充电宝经 USB 电源线接 Zero 的 Micro USB **PWR IN** 口。两个旋钮从 Pi 排针取 3.3 V。OL23 沿用出厂接法。

独立黑屏和显示负载开关仍是后续功能。若以后改显示供电，按对应板卡的原厂图处理，并复测断电和画面恢复。

机械拨动开关不是Linux正常关机。最终电源切断需等待系统关机或完成只读文件系统策略；初期通过系统shutdown后再拔电。

物理针脚参考：[Raspberry Pi官方GPIO文档](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio)。
