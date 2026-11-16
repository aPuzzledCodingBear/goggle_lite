# Mechanical design inputs

## English

The design validates separate display, compute, and energy modules. This directory will hold source CAD, STL/STEP exports, and printing parameters. No manufacturing dimensions are inferred from missing source images.

For sustained wear, minimize the complete head-borne assembly, not only the optics. Record installed mass/balance, protrusion, plug/cable envelope, and each retained component's necessity. Support cable weight independently. Do not sacrifice eye clearance, adjustment travel or strength for smaller dimensions. Compare against unmodified eyewear in staged wear trials; see [wearability rationale](../docs/wearability.md).

- goggles_mount: retain the original optics/FPC assembly; allow vertical, lateral, depth, and angle adjustment, then lock it.
- driver_enclosure: place the HDMI driver near the frame/headband connection with connector clearance and strain relief.
- pendant: Zero and CCPA form the compute module; power electronics and the future battery form the energy module. Keep separable interfaces, even if initially partitioned within one enclosure. Keep the battery away from heat and sharp edges.
- controls: print the EC11-compatible wheel, button caps, guides, and travel stops.
- cable_retainer: use gentle bends and strain relief; cables must release when the neck strap breaks away.

Measure mounting holes, maximum component heights, connector/plug envelopes, goggle depth, and eye clearances before enclosure design. Approximately 80×50×30mm is a target, not a final dimension. PETG provides rigid structures; TPU provides cushioning. Test printed fits before assembly.

The optical assembly must not contact the eye during slipping or impact. Reversible modification does not preserve the goggle's original impact certification. Initial validation is stationary in a controlled environment.

---

# 中文 · 结构设计输入

结构用于验证显示、运算与能源模块分离；模块接口需可识别和拆换。

本目录后续存放源CAD、导出STL/STEP及打印参数。当前没有依据缺失原图虚构可制造尺寸。

为长期佩戴，减重缩小的对象是完整头部装配，而非仅光机。记录安装后的重量／平衡、突出尺寸、插头线缆包络，以及每个本地部件保留的必要性。独立支撑线缆重量，不能牺牲眼部间隙、调节行程或强度来缩壳。与原眼镜对比逐级试戴，见[佩戴需求论证](../docs/wearability.md)。

- goggles_mount：保留原厂光学组件和FPC整体；上下、左右、前后及角度可调，调整后锁定。
- driver_enclosure：沿镜框/头带连接处布置HDMI板，留插拔空间和应力释放。
- pendant：Zero和CCPA构成运算模块，电源板和后续电池构成能源模块；接口可分离，可先同仓分区固定，电池远离热源及锐边。
- controls：EC11轴配合滚轮、按键帽、导向和限位均自行打印。
- cable_retainer：线束缓弯、抗拉固定；挂绳脱离时线缆也需释放。

先测量板孔、最高器件、连接器及插头包络、风镜净深和眼部间隙，再设计壳体。目标约80×50×30mm不是定稿尺寸。PETG做硬结构，TPU做缓冲，测试打印配合后再总装。

光机不得在佩戴滑动或受冲击时接触眼部；可逆改装不代表保留风镜原有防冲击认证。首次验证在静止受控环境进行。
