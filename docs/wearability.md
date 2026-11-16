# Why the head-worn module must be light, small, and simple

## English

### The requirement comes from sustained glasses wear

The intended use is sustained wearing of glasses, not just briefly holding a display in front of an eye. The head-worn assembly therefore has to remain acceptable during ordinary wear, including periods when no image is needed. **As light, as small, and as simple as practical** is a primary architectural requirement, subject to optical performance, secure mounting, eye clearance, and electrical safety. It is not a cosmetic objective or a claim that comfort has already been demonstrated.

### Light: minimize the load that stays on the head

Every added gram is carried through the frame, nose/ear contacts or headband for the entire session. Placement matters as well as mass: a front-heavy or one-sided addition creates a moment about the supports, and head movement adds inertial loads. These can require more retention force or repeated fit adjustment. Increasing battery capacity on the frame also increases the load carried continuously, even when the display is idle.

Move application processing, video reception/decoding, energy storage and user controls off the head. Account for the complete head-borne addition: optics, driver if retained, enclosure, mounts, fasteners, connectors and the cable portion supported by the frame. Track total eyewear mass and balance as well as the added mass. Cable drag can undo savings in electronics weight, so support the harness independently and test it during head turns.

### Small: minimize protrusion and the worn envelope

A light but bulky module can still obstruct the useful field of view, interfere with the face or other worn equipment, snag, or sit far from its support and increase the moment arm. Measure its installed envelope, not only the bare optical engine. Include plug bodies, cable bends, adjustment travel and eye clearance.

Place components close to the support where optics permit. Shrinking the housing must not reduce the eyebox adjustment range, place hard parts closer to the eye, force sharp cable bends, weaken the mount or obstruct necessary ventilation.

### Simple: keep only functions required at the display

The head module should contain only the optical/display chain and the minimum local circuitry and mechanical protection required for it to work. Battery charging, wireless reception, general-purpose compute, storage and physical controls belong in off-head modules. Fewer local boards, interconnects and functions reduce the local packaging, assembly and service burden and avoid placing their power dissipation on the frame. This moves complexity elsewhere; it does not eliminate system complexity.

For V1, the OL23 HDMI driver may remain on the frame because of the factory FPC and verified interface limits. Moving it off-head is a later option only after signal integrity and cable feasibility are demonstrated; do not extend raw RGB/FPC merely to reduce head weight. Every retained component needs a reason it cannot reasonably be moved off-head.

### Design priorities and verification

1. Keep optical alignment, eye clearance, mounting strength and power integrity as constraints.
2. Within those constraints, minimize total head-borne mass, protrusion and local functional complexity. Prefer relocating a function off-head when two options provide equivalent display performance.
3. Treat the current **≤30g added mass as a provisional V1 ceiling, not an optimum or a comfort threshold**. Continue reducing it when practical. No universal size limit is asserted before the actual eyewear and optical assembly are measured.
4. Compare the unmodified eyewear and the assembled prototype in stationary sessions of 15, 30 and 60 minutes, progressing only while acceptable to the wearer. These are proposed test checkpoints, not demonstrated all-day wear times. Record actual duration, pressure/discomfort reports, slipping, readjustments, image loss, head-turn cable pull, mass/balance, installed dimensions and local temperature. Stop at discomfort or unstable fit, document the cause, and revise.
5. A working image and a passed weight target do not establish long-duration comfort. Retain observations and unsuccessful trials alongside successful results; longer intended sessions need separate evaluation.

This is an engineering rationale based on the user's sustained-wear requirement and basic load/packaging considerations. It is not a medical conclusion or a completed ergonomic study. The modular validation succeeds only if moving compute and energy off-head produces a useful wearable arrangement rather than merely relocating boxes in a diagram.

---

# 中文 · 为什么头部模块必须尽量轻、小、简单

## 需求来自长期佩戴眼镜的现实

预期使用方式是持续佩戴眼镜，而不是短暂把显示器举到眼前。即使暂时不显示内容，头部组件也需要能够被接受地持续佩戴。因此，**在可行范围内越轻越好、越小越好、越简单越好**是首要架构需求，前提是满足光学效果、固定可靠性、眼部间隙和电气安全。它不是外观偏好，也不代表已经验证了佩戴舒适性。

## 轻：减少持续留在头上的负担

每增加一克重量，整个佩戴期间都要通过镜框、鼻部／耳部接触点或头带承受。重量分布同样重要：前端或单侧偏重会对支撑位置产生力矩，转头还会带来惯性载荷，可能需要更强的固定力或反复调整佩戴位置。把更大电池装到镜框上，也会在显示关闭时持续增加负担。

因此将应用处理、视频接收／解码、储能和操作控件移出头部。重量统计必须包括全部头部新增件：光学组件、保留在头部的驱动板、外壳、支架、紧固件、连接器，以及由镜框承受的那部分线缆。除新增重量外，还记录整副眼镜的重量和重心平衡。线缆牵拉可能抵消电子部分减重的收益，因此线束应独立支撑，并在转头时验证。

## 小：减少突出和佩戴包络

轻但体积大的模块仍可能遮挡有效视野、干涉面部或其他佩戴装备、发生钩挂，或因离支点更远而增大力臂。应测量安装后的完整包络，而不只是裸光机尺寸；插头、线缆弯曲空间、调节行程和眼部间隙都要计入。

在光学允许的前提下尽量靠近支撑位置。不能为了缩壳而缩减Eyebox调节范围、让硬件更靠近眼睛、强折线缆、削弱支架或阻碍必要散热。

## 简单：头部只保留显示必需功能

头部模块只保留光学／显示链路，以及维持其工作所必需的最少本地电路和机械保护。电池充电、无线接收、通用运算、存储和实体交互放在头部以外。减少本地板卡、互连和功能，有助于降低局部封装、装配与维护负担，也避免将这些功能的耗散功率放在镜框上。这是在转移复杂度，并不意味着系统总复杂度消失。

V1中，OL23 HDMI驱动板可以因原厂FPC及已验证接口的限制保留在镜框上。只有确认信号完整性和线束可行性后，才考虑将其移出头部；不能为了减重而直接延长未经验证的RGB／FPC。每个留在头部的部件都应说明为何不能合理外移。

## 设计取舍与验证

1. 将光学对准、眼部间隙、固定强度和供电可靠性作为约束。
2. 在这些约束内，尽量减少完整头部负载、突出尺寸及本地功能复杂度；两种方案显示能力相当时，优先将功能外移。
3. 当前**新增重量≤30g只是V1暂定上限，不是最佳值，更不是舒适性阈值**；有条件仍应继续减重。未测量实际镜体和光学组件前，不虚设通用尺寸上限。
4. 对比原眼镜与改装原型，在静止环境按15、30、60分钟逐级试戴，仅在佩戴者能够接受时进入下一阶段。这些是拟定检查点，不代表已实现全天佩戴。记录实际时长、压迫／不适反馈、滑移、调整次数、画面丢失、转头时线缆牵拉、重量／平衡、安装包络及局部温度；出现不适或固定不稳即停止，记录原因并改进。
5. 能显示画面、满足重量目标，都不能直接证明长时间舒适。保留失败和成功试验记录；更长的目标佩戴时长需要另行验证。

这是依据用户持续佩戴需求及基础受力、封装因素提出的工程论证，不是医学结论或已完成的人体工学研究。模块分离的验证结果应体现为可用的佩戴形态，而不仅是框图上把几个盒子分开。
