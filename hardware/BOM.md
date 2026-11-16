# Bill of materials

[English](#bill-of-materials) | [中文](#采购清单)

Purpose: validate the physical separation of display, compute, and energy modules. CarPlay is the V1 demonstration workload. The energy module starts as an external 5V power bank; only select a custom battery after measuring the system.

All prices below are **planning estimates in CNY**, not verified live offers. Quantities include spares. See [purchasing links](purchasing.md) and [sourcing evidence](../research/taobao.md) before ordering. No purchase has been made by this project.

## Batch 1 — bench and mechanical validation

| ID | Item | Quantity | Estimated subtotal | Purchase gate |
|---|---|---:|---:|---|
| B01 | OL23 optical module + HDMI driver | 1 set | 600–1200 | HDMI, not AV; confirm connector, power and accepted timing |
| B02 | Carlinkit CPC200-CCPA wireless AutoKit adapter | 1 | 150–300 | Confirm exact AutoKit hardware/firmware; ordinary U2W adapters are not substitutes |
| B03 | Full-frame goggles | 1 | 40–100 | Measure internal clearance; select clear/tinted lenses for use case |
| B04 | Bare EC11 encoder with push switch | 2 | 6–16 | One installed, one spare; confirm shaft dimensions for printed wheel |
| B05 | 6×6mm tactile switch | 5 | 2–5 | Two installed, three spares; confirm height |
| B06 | 400-point solderless breadboard | 1 | 5–10 | Bench only |
| B07 | Dupont jumper wires | 1 set | 5–10 | Match male/female ends to headers |
| B08 | 2.54mm GPIO header | 1 | 2–5 | Zero needs 2×20 if not already fitted |
| B09 | Micro USB OTG to USB-A female short cable | 1 | 5–15 | USB host/data capability; connect to Zero data port |
| B10 | Mini HDMI to confirmed OL23 input cable | 1 | 20–50 | Pi end is Type C Mini; OL23 end is unconfirmed |
| B11 | 26/30AWG flexible wire | 1 set | 10–20 | Thin wire for signals; size power wiring from measured voltage drop |
| B12 | 32GB microSD, if missing | 1 | 25–45 | Check existing card first |
| B13 | M2/M2.5 screws and heat-set inserts | 1 set | 10–25 | Select after measuring mounting holes |
| B14 | Heat-shrink and insulation | 1 set | 5–15 | Insulate and restrain soldered wires |
| | **Batch 1 total** | | **885–1816** | Deduct existing parts |

## Batch 2 — after measurements

| ID | Item | Quantity | Estimated subtotal | Purchase gate |
|---|---|---:|---:|---|
| B15 | 60–80cm flexible HDMI harness | 1 | 30–80 | Connector types, bend radius and full-length signal validation |
| B16 | Hollow lanyard and breakaway parts | 1 set | 10–25 | Cable must release along with the strap |
| B17 | Protected 3000mAh Li-ion polymer battery | 1 | 35–70 | Peak current, dimensions, polarity, temperature |
| B18 | USB-C charger and regulated 5V power board | 1 | 25–60 | Output capability, protection and load-sharing if needed |
| B19 | 5V high-side load switch module | 1 | 5–15 | 3.3V logic compatibility, default state and backfeed behavior |
| | **Batch 2 total** | | **105–250** | |
| | **Overall estimate** | | **990–2066** | Excludes shipping, new tools and printing consumables |

## Existing equipment and checks

- Available: Zero 2 W, Pico 1 (unused in V1), 3D printer.
- Check: reliable 5V power bank/supply, microSD, multimeter, soldering tools, PETG/TPU, ordinary HDMI monitor.
- If a USB keyboard and CCPA are needed simultaneously, check for a USB hub; one OTG cable provides only one peripheral port.
- Do not order a separate MFi chip, the earlier 16-pin wired-to-wireless PCBA, or finished wheels/button caps.
- Keep the energy module detachable from the compute enclosure. A custom battery is optional; an external power bank is sufficient to validate this module boundary.

## Questions before buying core parts (not sent to sellers)

OL23: request actual HDMI kit photographs, connector model, accepted input timing/EDID, 5V current, included-part weights, mechanical drawings, brightness-control definition and original external-power modification diagram. Confirm whether 640×400 input is accepted or another input mode is scaled.

CCPA: confirm the CPC200-CCPA wireless model for Android AutoKit, label/hardware/firmware version and USB VID:PID. Linux FastCarPlay support cannot be inferred solely from “wireless CarPlay.” Ask about return terms for incompatible hardware.

---

# 采购清单

所有金额来自用户提供的方案预算，单位人民币，不是实时价格。商品验证见 [淘宝记录](../research/taobao.md)。采购状态均为待购买；已有设备不计价。

## 第一批：桌面及结构验证

| ID | 物品 | 数量 | 预算小计 | 购买条件 |
|---|---|---:|---:|---|
| B01 | OL23 + HDMI 驱动板 | 1套 | 600–1200 | HDMI非AV；确认供电、接口及支持时序 |
| B02 | Carlinkit CPC200-CCPA 无线 AutoKit | 1个 | 150–300 | 确认具体版本支持AutoKit，不买普通U2W转换器 |
| B03 | 全包围式风镜 | 1副 | 40–100 | 需实测内部空间，灰/透明镜片按用途选择 |
| B04 | EC11 带按压裸编码器 | 2个 | 6–16 | 1用1备，确认轴形和轴长以打印滚轮 |
| B05 | 6×6mm 轻触开关 | 5个 | 2–5 | 2用3备，确认高度 |
| B06 | 400孔面包板 | 1块 | 5–10 | 仅验证，不进最终装配 |
| B07 | 杜邦线 | 1套 | 5–10 | 公母组合匹配实际排针 |
| B08 | 2.54mm GPIO 排针 | 1条 | 2–5 | Zero未焊针时需要 |
| B09 | Micro USB OTG → USB-A 母短线 | 1根 | 5–15 | 插Zero数据口，不是仅充电线 |
| B10 | Mini HDMI → OL23对应接口线 | 1根 | 20–50 | Pi端Type C Mini；另一端待确认，不能误买Micro |
| B11 | 26/30AWG 柔性飞线 | 1套 | 10–20 | 细线仅信号；供电线径由压降验证确定 |
| B12 | 32GB microSD（如缺少） | 1张 | 25–45 | 正规渠道，先检查已有卡 |
| B13 | M2/M2.5螺丝及热熔螺母 | 1套 | 10–25 | 测量板孔后选型 |
| B14 | 热缩管、绝缘材料 | 1套 | 5–15 | 飞线固定和隔离 |
| | **第一批小计** | | **885–1816** | B12–B14已有可减免 |

## 第二批：实测后再选

| ID | 物品 | 数量 | 预算小计 | 先决条件 |
|---|---|---:|---:|---|
| B15 | 60–80cm 超柔 HDMI 线束 | 1根 | 30–80 | 两端插座、弯曲半径、全长信号稳定性 |
| B16 | 中空挂绳及安全脱离件 | 1套 | 10–25 | 脱离时线缆不能继续承受牵拉 |
| B17 | 带保护3000mAh锂电池 | 1块 | 35–70 | 峰值电流、尺寸、极性和温升 |
| B18 | USB-C充电 + 5V稳压管理板 | 1块 | 25–60 | 稳定输出、保护、是否支持边充边用需确认 |
| B19 | 5V高边负载开关模组 | 1块 | 5–15 | 3.3V逻辑兼容，电流、默认状态和反灌行为 |
| | **第二批小计** | | **105–250** | |
| | **全部预算** | | **990–2066** | 不含运费及新增工具/打印耗材 |

## 已有与检查项

- 已有：Zero 2 W、Pico 1（本版不用）、3D打印机。
- 检查：稳定5V移动电源、microSD、万用表、电烙铁、PETG/TPU、普通HDMI显示器。
- 装机调试如果需要同时接USB键盘，另检查USB Hub；一根OTG只有一个外设口。
- 不采购：单独MFi芯片、16针有线转无线PCBA、成品旋钮和按键帽。

## 核心件询价问题（未代发）

OL23：请提供HDMI套件实际照片、接口型号、可接受输入时序/EDID、5V输入电流、包含组件重量、机械图、亮度接口定义和外接供电改法原图。请确认输入640×400是否直接支持，或需输入其他时序缩放。

CCPA：请确认是可在安卓主机运行AutoKit的CPC200-CCPA无线版，提供铭牌/硬件版本/固件版本和USB VID:PID。我们以Linux FastCarPlay接入，不能仅以“支持无线CarPlay”判断兼容。询问不匹配时的退换条件。

模块分离约束：能源模块需可从计算模块外壳拆离；独立移动电源即可完成该边界验证，自制电池不是V1前置条件。
