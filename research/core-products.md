# Core procurement verification / 核心采购核验

## English

Checked: 2026-11-16 (Asia/Shanghai). Demonstration path: iPhone → CPC200-CCPA wireless AutoKit → existing Zero 2 W / FastCarPlay → HDMI → OL23 display kit. No seller was contacted and no purchase was made.

### Link list and verification level

| Item | Link | Verified evidence | Price / availability |
| --- | --- | --- | --- |
| OL23 kit, original Taobao lead | [User-provided short link](https://e.tb.cn/h.jOTlUi1g4QEw6bB?tk=CqNr6V12DcF) | Not expanded: web tool returned a non-retryable error on repeat checks. Title, seller, item ID and SKU remain unverified. | Unknown |
| ECX336CN component reference | [Aoshite component page](https://www.aoshite.net/productView503_1073.html) | Page lists ECX336CN, 0.23 inch, 640 × 400, **MIPI**. This is a component reference, not verification of the OL23 HDMI kit. | Quote required; stock unverified |
| CPC200-CCPA manufacturer reference | [CarlinKit CCPA](https://www.carlinkit.com/ccpa) | Model CPC200-CCPA, AutoKit for aftermarket Android head units; wired/wireless connections; USB male/female ports; 5V ± 0.2V, 1A input. | No verified retail quote or stock |
| CPC200-CCPA alternative retail channel | [Carlinkit Carplay Store product page](https://carlinkitcarplay.com/products/carlinkit-wirless-adapter-for-android-head-unit-support-carplay-and-android-auto) | Accessible product page for the AutoKit CCPA adapter. Several variants are listed, including CCPA and CCPA-MIC. This is not Taobao. | Page displays USD 65 and “Notify Me When Available”; do not treat as confirmed stock, delivered price or a quote for every variant. |

The target OL23 specification — ECX336CN full-colour waveguide with a 40.5 × 12.5 mm HDMI board — comes from the user’s plan, not an independently verified listing. A bare MIPI ECX336CN cannot be assumed to accept HDMI.

Exact-model searches restricted to item.taobao.com and detail.tmall.com returned no verifiable CCPA listing. OL23/ECX336CN/HDMI searches likewise produced no verified matching Taobao detail page. Earlier browser inventory was empty and Safari access timed out; no login or risk-control screen was observed, so those causes are not established. Search pages are not presented as product pages.

### FastCarPlay upstream check

The [upstream Raspberry Pi setup wiki](https://github.com/niellun/FastCarPlay/wiki/Raspbery-Pi-Setup), prerequisites, explicitly names **CPC200-CCPA AutoKit**, Zero 2 W, USB OTG and a reliable 5V/2.5A supply. This supports the chosen architecture. The [README](https://github.com/niellun/FastCarPlay) uses broader Carlinkit/CCPM wording and requires checking actual USB VID/PID with `lsusb` and configuring permissions/settings accordingly. Neither source guarantees every current retail firmware batch. The manufacturer page itself describes Android + AutoKit, not Linux support.

### Before ordering

- OL23: obtain the full item ID and exact HDMI-kit SKU; verify waveguide, display, driver board and flex cables are included; board dimensions, connector direction, HDMI modes/EDID, supply current, brightness controls, eye side/eye relief, cable bend limits, price, stock and return/dead-pixel terms.
- CCPA: obtain label/photos, exact CCPA versus CCPA-MIC SKU, firmware version, AutoKit USB protocol compatibility and return terms. Ordinary U2W/2air/CP2A wired-to-wireless adapters and the earlier 16-pin PCBA are excluded.
- Test one complete set before wearable integration: USB enumeration and power stability, wireless phone pairing, FastCarPlay video/control, and HDMI negotiation on the actual OL23 driver.

## 中文（完整对应）

实查日期：2026-11-16（上海时区）。演示链路：iPhone → CPC200-CCPA 无线 AutoKit → 已有 Zero 2 W / FastCarPlay → HDMI → OL23 显示套件。未联系商家，未购买。

### 链接清单与验证程度

| 项目 | 链接 | 已验证依据 | 价格 / 可购买状态 |
| --- | --- | --- | --- |
| OL23 套件，原淘宝线索 | [用户提供的短链](https://e.tb.cn/h.jOTlUi1g4QEw6bB?tk=CqNr6V12DcF) | 重复检查仍无法展开，网页工具返回不可重试错误。标题、店铺、商品 ID、SKU 均未核实。 | 未知 |
| ECX336CN 元件参考 | [奥视特元件页](https://www.aoshite.net/productView503_1073.html) | 页面列出 ECX336CN、0.23 英寸、640 × 400、**MIPI**。仅为元件参考，不能证明 OL23 HDMI 套件规格。 | 需询价；库存未验证 |
| CPC200-CCPA 厂家参考 | [CarlinKit CCPA 官方页](https://www.carlinkit.com/ccpa) | 型号 CPC200-CCPA；用于后装安卓车机的 AutoKit；有线/无线连接；USB 公母口；输入 5V ± 0.2V、1A。 | 无已核实的零售报价或库存 |
| CPC200-CCPA 替代零售渠道 | [Carlinkit Carplay Store 商品页](https://carlinkitcarplay.com/products/carlinkit-wirless-adapter-for-android-head-unit-support-carplay-and-android-auto) | 可访问的 AutoKit CCPA 商品详情页，列出 CCPA、CCPA-MIC 等版本。不是淘宝。 | 页面显示 65 美元和到货通知按钮；不能认定为现货、到手价或所有版本的报价。 |

OL23 目标规格“ECX336CN 全彩光波导 + 40.5 × 12.5 mm HDMI 板”来自用户方案，未获独立商品页验证。裸 MIPI ECX336CN 不能被当作可直接接 HDMI 的产品。

限定 item.taobao.com、detail.tmall.com 搜索精确 CCPA 型号，未找到可核实商品；OL23/ECX336CN/HDMI 搜索也未取得匹配淘宝详情页。此前浏览器列表为空，Safari 访问超时；没有看到登录或风控页面，不能断言是这些原因。未将搜索入口充作商品详情页。

### FastCarPlay 上游核对

[上游树莓派配置 Wiki](https://github.com/niellun/FastCarPlay/wiki/Raspbery-Pi-Setup)的前置硬件明确列出 **CPC200-CCPA AutoKit**、Zero 2 W、USB OTG 和可靠的 5V/2.5A 电源，因此支持所选架构。[README](https://github.com/niellun/FastCarPlay)使用较宽泛的 Carlinkit/CCPM 表述，并要求用 `lsusb` 检查实际 USB VID/PID、配置权限和设置。两者均不能保证当前所有零售固件批次可用。厂家页面本身说明的是安卓 + AutoKit，并未承诺 Linux 支持。

### 下单前确认

- OL23：取得完整商品 ID、准确 HDMI 套件 SKU；核实包含光波导、显示屏、驱动板和排线；确认板尺寸、接口朝向、HDMI 模式/EDID、供电电流、亮度控制、左右眼/出瞳距离、线缆弯折限制、价格、现货及退换/坏点条件。
- CCPA：取得标签和实物照片、CCPA 或 CCPA-MIC 的准确 SKU、固件版本、AutoKit USB 协议兼容性与退换条件。排除普通 U2W/2air/CP2A 有线转无线适配器和此前 16 针 PCBA。
- 穿戴集成前先测试一整套：USB 枚举与供电稳定性、手机无线配对、FastCarPlay 视频/控制、实际 OL23 驱动板的 HDMI 协商。
