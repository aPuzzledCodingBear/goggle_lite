# Wiring plan — not bench-tested

English first; Chinese follows. These connections implement a detachable display module, compute module and energy module. CarPlay is the demonstration workload, not the architecture boundary.

GPIO numbers are BCM. Connect passive switches/encoder contacts only between input and ground, with internal pull-ups; never connect these inputs to 5V.

| Function | BCM GPIO | Physical pin |
|---|---:|---:|
| EC11 A | 17 | 11 |
| EC11 B | 27 | 13 |
| Encoder press | 22 | 15 |
| Back | 23 | 16 |
| Blank display | 24 | 18 |
| Display load-switch enable, optional | 25 | 22 |
| Common ground | GND | 9 |

Connect encoder common to GND. The push switch has separate contacts. Confirm the actual EC11 pinout with a meter. Fit headers to an unpopulated Zero first; do not route battery/high-current power through breadboard rails.

B05 uses a four-pin SPST-NO momentary tactile switch: identify the two internally joined pairs with a meter. Connect one distinct pair to GND and the other to GPIO23 or GPIO24. Using two contacts from the same pair grounds the input permanently.

## Module interfaces

- **Compute:** Zero 2 W + CCPA + GPIO controls; CCPA connects through a USB-A female OTG cable to Zero's data port. The other Micro USB port powers Zero.
- **Display:** OL23 + HDMI driver; retain the factory FPC between driver and optics. Extend verified HDMI, not raw RGB/FPC. Zero uses **Mini HDMI Type C**, not Micro Type D; confirm the OL23 connector before ordering.
- **Energy:** external regulated 5V source with separate branches to compute and display. Use a finished power bank through USB 5V for the detachable energy module; no custom battery/charger. Verify total output, low-load auto-off and cable voltage drop. Do not request higher USB PD/QC voltage for the 5V branches. Record branch current, board-end voltage, connector polarity and power-off behavior.

## Power and shutdown

Follow the original vendor drawing for display supply and common ground. Any removal of a 0Ω resistor requires the original modification diagram, not a reconstruction from chat text.

Do not parallel two active 5V outputs. GPIO drives a logic enable only, not the display load. A load switch controls the display branch; HDMI has additional powered/signaling paths, so test backfeed, actual blanking and EDID recovery after power restoration.

A mechanical switch does not shut Linux down cleanly. Use normal shutdown before disconnecting compute power until a shutdown/readonly-filesystem strategy has been verified. Detachable means removable after an appropriate shutdown, not guaranteed hot-swappable.

Pin reference: [Raspberry Pi GPIO documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio).

---

# 接线规划 · 尚未实测

GPIO 编号为 BCM。仅无源编码器/开关接输入与GND，启用内部上拉，不接5V。

| 功能 | BCM GPIO | 40针物理位置 |
|---|---:|---:|
| EC11 A | 17 | 11 |
| EC11 B | 27 | 13 |
| 编码器按压 | 22 | 15 |
| 返回 | 23 | 16 |
| 黑屏 | 24 | 18 |
| 显示负载开关使能（后续） | 25 | 22 |
| 公共地 | GND | 9 |

编码器公共端接GND；按压开关另外两脚为按键接点。EC11各家针位可能不同，先用万用表确认，不依据外观猜测。Zero若无排针先焊接排针，面包板阶段不把电池大电流走面包板轨道。

B05采用常开自复位四脚轻触开关，四脚分为两组内部相连触点。先用万用表识别两组；一组接GND，另一组接GPIO23或GPIO24。不能把同一组内两脚分别接GPIO和GND，否则输入会常低。

## USB与HDMI

- CCPA → USB-A母 OTG → Zero 的 USB 数据口；Zero另一Micro USB接口用于供电。
- Zero为 **Mini HDMI（Type C）**，不是 Micro HDMI（Type D）。OL23端接口未确认，先获取实际插座照片。
- 光机到驱动板使用原厂FPC；长距离仅延长已经验证的HDMI，不自行延长RGB/FPC。

## 电源

第一阶段用可靠5V电源；显示板供电按原厂图接线，共地。驱动板外接供电是否要移除0Ω电阻必须依据原图复核后执行。

不要把两个有源5V输出直接并联；负载开关仅控制显示支路，GPIO不能直接供电给显示板。HDMI存在5V/DDC等连接，切断显示独立电源后是否仍反向供电、是否真正变暗，需要实测。恢复供电后还要验证EDID和画面恢复。

机械拨动开关不是Linux正常关机。最终电源切断需等待系统关机或完成只读文件系统策略；初期通过系统shutdown后再拔电。

物理针脚参考：[Raspberry Pi官方GPIO文档](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio)。

模块边界：计算模块含Zero、CCPA及交互；显示模块含OL23及驱动板；能源模块为可拆离5V电源。独立能源模块固定为成品充电宝经USB输出5V，不自制电池或充电板；验证总输出、低负载自动关断及线缆压降，5V支路不请求USB PD/QC高压。记录各支路电流、板端电压、极性和断电行为。可拆离指正常关机后可拆，不代表支持热插拔。
