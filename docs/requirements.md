# Requirements baseline · 2026-11-16

## English

This is an engineering prototype to validate separation of **display, compute, and energy modules**. CarPlay is the current test workload for video, interaction, and wireless connectivity; it is not the final product definition. Each module needs documented interfaces, measurements, and a replacement path. Start with a centralized 5V bench supply, then validate a separate energy module powering the system through the harness. Logical separation does not mean three physical enclosures have already been designed.

The user-supplied conversation ends with the FastCarPlay route. Earlier dedicated receiver PCBA, Pico, and LIVI routes are outside V1.

### Sustained-wear design requirement

The head-worn module must be as light, small, and simple as practical because the glasses support it throughout prolonged wear, including idle periods. Minimize complete installed mass, protrusion and local functions, while preserving optical adjustment, eye clearance and secure mounting. Keep compute, energy and controls off-head; justify every component retained on the frame. The ≤30g added-mass goal is a provisional ceiling, not a comfort threshold. See [rationale and wear trials](wearability.md).

### Decisions

- iPhone runs navigation, applications, location, and UI generation.
- The existing Raspberry Pi Zero 2 W runs FastCarPlay with a CPC200-CCPA wireless AutoKit USB adapter.
- The display module uses OL23 monocular full-color see-through optics and an HDMI driver, not the AV version.
- A bare EC11 push encoder and two back/blanking buttons connect directly to GPIO. Finger-contact mechanical parts are printed.
- Breadboard first, soldered flying wires later; no custom PCB. The existing Pico 1 is unused.
- The chest compute module receives and decodes video. The energy module supplies power; it may initially share the chest location, with separable interfaces. The neck harness carries HDMI and separate power; no head-mounted battery.
- Energy is supplied by a finished USB power bank at 5V. No custom battery pack, charger or boost board is developed or purchased for V1.
- PETG/TPU enclosures and mounts use reversible attachment where possible.

### Conversation-reported specifications — not independently verified

| Part | Reported specification | Verification needed |
|---|---|---|
| OL23 | ECX336CN, 640×400, 60Hz, approximately 12g | Model and whether weight includes cables |
| Optics | FOV 21.2°×13.26°, eyebox 10.8×5.4mm, eye relief 15mm | Original datasheet and assembly drawing |
| Brightness | 0–400nits at eye; 3000nits panel | Do not equate them; outdoor measurement needed |
| Envelope | Approximately 60.74×37.03×24.37mm | Original image missing; not a manufacturing CAD input |
| HDMI board | 40.5×12.5mm, DC3.5–5V | Connector, timings, power, polarity, BRT ADJ |
| External power | Reportedly requires removing a specified 0Ω resistor | Obtain original instructions before modifying |

### V1 engineering targets — unmeasured

Monocular full-color 640×400; chest assembly approximately 80×50×30mm and ≤150g; added goggle mass ≤30g; runtime ≥2h; removable and repairable modules. Stable bench operation and readability take priority over size, which must be reassessed after measurement.

Audio and microphone hardware are outside the current purchasing baseline. A normal monitor supports bench work; the final navigation/Siri audio path must be defined separately. Do not assume direct phone audio or Bluetooth headphones will work automatically.

Source: [shared discussion](https://chatgpt.com/share/6afac55f-4244-83e8-bf40-7b98fdae869a), supplied as text by the user; original uploaded images are missing.

---

# 中文 · 需求基线

依据用户粘贴的分享正文，以末尾确认的 FastCarPlay 方案为准；早期的专用接收 PCBA、Pico 和 LIVI 方案不进入 V1。

## 项目定位

本项目是验证显示、运算及能源模块分离的工程原型。CarPlay只是现阶段用于验证视频、交互和无线连接的负载，不是项目最终产品定义。显示模块、运算模块和能源模块分别定义接口、测量和替换路径。先用集中5V台架供电，再验证独立能源模块经线束供电；逻辑分离不等于已经完成物理三仓设计。

## 长期佩戴设计要求

头部模块必须在可行范围内尽量轻、小、简单，因为长时间使用及显示空闲期间，眼镜始终承担其负载。减少完整安装后的重量、突出尺寸和本地功能数量，同时保留光学调节、眼部间隙和可靠固定。运算、能源及控件移出头部，每个留在镜框上的部件都需说明理由。新增重量≤30g是暂定上限，不是舒适性阈值，见[论证与试戴方法](wearability.md)。

## 已决定

- iPhone 负责导航、应用、定位和界面生成。
- 已有 Raspberry Pi Zero 2 W 运行 FastCarPlay，配 CPC200-CCPA 无线 AutoKit USB 适配器。
- 显示为 OL23 全彩单目透视模组，选择 HDMI 驱动套件，不选 AV 版。
- EC11 带按压裸编码器 + 返回/黑屏两个按键，GPIO 直连；机械手指接触件自行打印。
- 面包板验证、飞线总装，无定制 PCB；Pico 1 本版闲置。
- 胸前运算模块接收、解码；能源模块负责供电，初期可同处胸前但需保持可分离接口；挂脖线束承载 HDMI 和独立供电；头部无电池。
- 能源固定为成品充电宝经USB输出5V；V1不自制或采购裸电池组、充电板及升压管理板。
- 外壳及支架 PETG / TPU 打印，优先可逆固定。

## 对话转述的参数（未独立核验）

| 部件 | 参数 | 需复核 |
|---|---|---|
| OL23 | ECX336CN，640×400，60Hz，约12g | 型号、总重是否包含线材 |
| 光学 | FOV 21.2°×13.26°，Eyebox 10.8×5.4mm，出瞳15mm | 原规格书和装配图 |
| 亮度 | 入眼0–400nits；面板3000nits | 两者不可混用，需户外实测 |
| 包络 | 约60.74×37.03×24.37mm | 原图未取得，不能直接据此定稿CAD |
| HDMI板 | 40.5×12.5mm，DC3.5–5V | 插座、时序、功耗、极性、BRT ADJ |
| 外接供电 | 据称需移除指定0Ω电阻 | 未有原图，不据转述执行焊改 |

## V1 工程目标（未实测）

单目全彩640×400；胸前约80×50×30mm、≤150g；风镜新增≤30g；续航≥2h；可拆卸维修。以桌面稳定链路和可读性为先，尺寸需待实测重新评估。

音频和麦克风不在当前采购基线内：普通显示器可用于桌面验证，最终语音导航/Siri 的音频路径需另行定义，不默认原生手机或蓝牙耳机自动可用。

来源：https://chatgpt.com/share/6afac55f-4244-83e8-bf40-7b98fdae869a （用户提供正文，原图缺失）。
