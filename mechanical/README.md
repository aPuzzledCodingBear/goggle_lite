# Mechanical design inputs

## English

The design validates separate display, compute, and energy modules. This directory will hold source CAD, STL/STEP exports, and printing parameters. No manufacturing dimensions are inferred from missing source images.

For sustained wear, minimize the complete head-borne assembly, not only the optics. Record installed mass/balance, protrusion, plug/cable envelope, and each retained component's necessity. Support cable weight independently. Do not sacrifice eye clearance, adjustment travel or strength for smaller dimensions. Compare against unmodified eyewear in staged wear trials; see [wearability rationale](../docs/wearability.md).

- goggles_mount: retain the original optics/FPC assembly; allow vertical, lateral, depth, and angle adjustment, then lock it.
- driver_enclosure: place the HDMI driver near the frame/headband connection with connector clearance and strain relief.
- pendant: Zero and CCPA form the compute module. A finished external USB power bank is the energy module; retain its original enclosure. Provide a detachable USB connection and strain relief, with no custom cell/charger compartment.
- controls: print the EC11-compatible wheel, button caps, guides, and travel stops.
- cable_retainer: use gentle bends and strain relief; cables must release when the neck strap breaks away.

### Power and CarPlay control box

Use a finished external USB power bank as the 5 V source. The box exposes a power input and HDMI output. The iPhone connects wirelessly to the CPC200-CCPA, which sits inside the box and connects to the Pi Zero 2 W over USB OTG. Keep the USB data port and 5 V power input clearly distinct during assembly. Use the existing verified HDMI cable for the first enclosure fit. The two encoders and Back button form a removable control panel. Vehicle electrical integration is outside the project scope.

### OL23 clip-on prototype

Start with a removable, padded clip on an accessible rigid frame edge. A separate carrier supports the OL23 housing on its mechanical surfaces and keeps the optical area and FPC clear. Use a lateral slot and a replaceable wedge shim to try different offsets and angles before fixing the geometry. Anchor the cable to the frame so cable pull does not rotate the carrier. This concept assumes the frame has a suitable clip surface. Measure that edge's thickness, usable length and cross-section, plus the OL23 housing's support surfaces and the worn eye clearance, before making CAD.

Measure mounting holes, maximum component heights, connector/plug envelopes, goggle depth, and eye clearances before enclosure design. Approximately 80×50×30mm is a target, not a final dimension. PETG provides rigid structures; TPU provides cushioning. Test printed fits before assembly.

The optical assembly must not contact the eye during slipping or impact. Reversible modification does not preserve the goggle's original impact certification. Initial validation is stationary in a controlled environment.

---

# 中文 · 结构设计输入

结构用于验证显示、运算与能源模块分离；模块接口需可识别和拆换。

本目录后续存放源CAD、导出STL/STEP及打印参数。当前没有依据缺失原图虚构可制造尺寸。

为长期佩戴，减重缩小的对象是完整头部装配，而非仅光机。记录安装后的重量／平衡、突出尺寸、插头线缆包络，以及每个本地部件保留的必要性。独立支撑线缆重量，不能牺牲眼部间隙、调节行程或强度来缩壳。与原眼镜对比逐级试戴，见[佩戴需求论证](../docs/wearability.md)。

- goggles_mount：保留原厂光学组件和FPC整体；上下、左右、前后及角度可调，调整后锁定。
- driver_enclosure：沿镜框/头带连接处布置HDMI板，留插拔空间和应力释放。
- pendant：Zero和CCPA构成运算模块；成品外置USB充电宝为能源模块，保留原外壳。设计可拆离USB接口及应力释放，不设计裸电芯／充电板仓。
- controls：EC11轴配合滚轮、按键帽、导向和限位均自行打印。
- cable_retainer：线束缓弯、抗拉固定；挂绳脱离时线缆也需释放。

### 供电与 CarPlay 控制盒

成品充电宝在盒外提供 5 V，盒体对外留电源输入和 HDMI 输出。iPhone 无线连接盒内的 CPC200-CCPA，CCPA 经 USB OTG 接 Pi Zero 2 W 的数据口，充电宝接 Pi 的 `PWR IN` 口。首版用现有已验证的 HDMI 线试装。两个旋钮和独立返回键组成可拆控制面板。项目供电范围固定为充电宝。

### OL23 眼镜夹式原型

首版采用可拆软垫夹和独立托座。先按镜框有一段可夹持的硬边考虑，有实物后再定夹位。夹子咬合镜框，托座承托 OL23 外壳的结构面，给光学区和原厂 FPC 留出空间。托座用横向长孔试左右偏移，用可更换的楔形垫片试角度。线缆固定在镜框侧，避免牵拉托座。建模前记录夹位的边缘厚度、可夹长度和截面，OL23 外壳可承托的轮廓，以及佩戴时托座与眼睛的间隙。

先测量板孔、最高器件、连接器及插头包络、风镜净深和眼部间隙，再设计壳体。目标约80×50×30mm不是定稿尺寸。PETG做硬结构，TPU做缓冲，测试打印配合后再总装。

光机不得在佩戴滑动或受冲击时接触眼部；可逆改装不代表保留风镜原有防冲击认证。首次验证在静止受控环境进行。
