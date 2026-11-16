# Accessory sourcing

## English

Checked: **2026-11-16, Asia/Shanghai** (clock: 15:01 UTC / 23:01 local). Recheck sources below was read-only; no order, seller message, or account login was performed.

### Status meanings

- **C — Candidate:** a public source explicitly lists the product URL and relevant item type; the Taobao/Tmall listing, SKU, current price and stock are unverified.
- **L — Lead:** an index suggests a match, but the original product URL or required specification is not established.
- **M — Missing:** no sufficiently matched product-detail URL found. A search/index page is not a verified product listing.

### Candidate links

| Part; quantity | Link; status | Source evidence, rechecked | Required verification |
|---|---|---|---|
| Bare EC11 encoder with push switch; 2 | [Index only](https://tao.hooos.com/goods_523935212921.html); **L** | Index title identifies EC11 rotation and push switch with 12/15/20mm shafts; names 易达通东柏森专卖店. It uses 523935212921 in its filename, but no original merchant URL was exposed. Previously constructed Tmall URL is withdrawn as evidence. | Obtain original listing, bare 5-contact version, momentary push, detents/pulses, shaft dimensions and pinout. Print the wheel. |
| 6×6mm tactile switch; 5 | [Taobao 42823169259](https://item.taobao.com/item.htm?id=42823169259); **C** | [Xiaozhi getting-started guide](https://xiaozhi.me/home/zh/getting-started/) explicitly lists URL under 6×6mm switches; source reconfirmed. | Through-hole normally-open momentary switch; check 2/4-pin variant and actuator height. |
| Dupont jumper wires; 1 set | [Tmall 41254478179](https://detail.tmall.com/item.htm?id=41254478179); **C** | [Course BOM](https://github.com/haohaoalt/rikirobot) explicitly lists 15/30cm male–male, male–female and female–female wires with this URL; reconfirmed. | 2.54mm; male–male for breadboard, female–male from GPIO. Select length/SKU. |
| 2.54mm GPIO header; 1 set | [Tmall 651104320753](https://detail.tmall.com/item.htm?id=651104320753); **L** | [XFish wiring document](https://www.xfishai.com/xfish-lite/welding) reconfirmed URL for **1×4P** straight header. This does not establish availability of a Zero 2 W header. | Need **2×20** header if board has none; obtain correct SKU or a different listing. Do not order the source's 1×4P example as a full Pi header. |
| Micro USB OTG to USB-A female; 1 | [Taobao 527775920057](https://item.taobao.com/item.htm?id=527775920057); **C** | [Buy2you source index](https://m.buy2you.com/en/buy2taobao/item/527775920057.html) search result again explicitly gives original URL and Micro USB OTG/Pi Zero title; full source reopen returned Cache miss. | Host-mode data adapter, Micro USB male and USB-A female; check clearance. Exclude charge-only and Mini USB versions. |
| 30AWG silicone signal wire; 1 set | [Taobao 658475245663](https://item.taobao.com/item.htm?id=658475245663); **C** | [DFRobot community project](https://mc.dfrobot.com.cn/article-380515.html) source explicitly labels URL as 30AWG silicone wire; reconfirmed. | Actual gauge, stranded conductor and insulation diameter. Power wire gauge must be selected separately using measured current/voltage drop. |

All merchant prices, shipping, stock, shop identity and SKU are unverified. Historical index prices are deliberately omitted.

### Remaining sourcing

| Item | Status and useful lead | Purchase gate |
|---|---|---|
| 400-contact solderless breadboard; 1 | **M**. [Xiaozhi source](https://xiaozhi.me/home/zh/getting-started/) recommends this type but gives search terms rather than a matching original product URL. [ZY-60 index](https://www.taouq.com/id-eMyJqgdhDtdJog4qz0c8BKUzt0-d8ZBBDFnZ6Medbdsd/) is an unverified lead; reopen failed. | Search “400孔 免焊面包板 2.54”. Exclude soldered perfboard. |
| Mini HDMI bench cable; 1 | **M**. Searches returned unrelated DisplayPort converters, capture cards and display kits; none accepted. | Pi end: Mini HDMI Type C. Confirm OL23 socket Type A/C/D before selecting the other end. No inferred connector match. |
| Full-frame goggles; 1 | **M**. Rejected helmet/sunglasses results and a mismatched agent-index page. A [2014 historical bookmark](https://api.duitang.com/blog/?id=145392386) names desert-locust goggles and links [38974401349](https://item.taobao.com/item.htm?id=38974401349), but is too old and lacks fit specifications to qualify as a purchase candidate. | Measure internal depth and OL23 clearance; verify replaceable clear/grey lens and mounting space. Historical title does not establish current stock or protection. |
| Hollow lanyard plus breakaway; 1 set | **M** for complete requirement; **L** for [breakaway lanyard index](https://tao.hooos.com/goods_GA9RW4gf8tYeOyNPZgSYvDCQtJ-rkOPPMu2DN6Vp4VTV.html). Index claims 1.5cm automatic breakaway and names 聆音楼旗舰店, but exposes no original product URL and does not establish hollow construction. | Search “中空 编织 挂绳 安全脱离扣”. Confirm cable passage and complete cable release; a cable bypassing the breakaway defeats it. |
| 26AWG power wire; 1 set | **M** | Select from measured current, voltage drop and temperature. |
| 60–80cm flexible HDMI; 1 | **M**, phase-two purchase | Both connectors, bend direction, length and strain relief need confirmation. Do not assume FPC tolerates repeated sharp folding. |

### Access record

The earlier original Taobao/Tmall opens returned inaccessible or non-retryable errors. This does not prove a listing was removed or requires login. Source rechecks establish provenance only. All items still require merchant-page inspection before procurement; the incomplete list must not be reported as fully verified.

## 中文

核查日期：**2026-11-16，Asia/Shanghai**（时钟15:01 UTC／本地23:01）。以下复查仅为读取，未下单、联系商家或登录账户。

### 状态说明

- **C — 候选：**公开来源明确列出商品URL与相关品类，但淘宝／天猫原站详情、SKU、现价及库存未核实。
- **L — 线索：**索引提示可能匹配，但原始商品URL或所需规格尚未确定。
- **M — 缺失：**未找到足够匹配的商品详情URL。搜索／索引页不视为已核实商品页。

### 候选链接

| 配件；数量 | 链接；状态 | 复核的来源证据 | 待确认事项 |
|---|---|---|---|
| 带按压裸EC11编码器；2个 | [仅商品索引](https://tao.hooos.com/goods_523935212921.html)；**L** | 索引标题提到EC11旋转、按键、12/15/20mm轴，店名易达通东柏森专卖店。文件名含523935212921，但未暴露原商家URL。撤回此前按该ID构造的天猫URL作为证据。 | 获取原商品页，确认裸5触点、瞬时按压、段落／脉冲数、轴尺寸与引脚；滚轮自行打印。 |
| 6×6mm轻触开关；5个 | [淘宝42823169259](https://item.taobao.com/item.htm?id=42823169259)；**C** | [小智入门文档](https://xiaozhi.me/home/zh/getting-started/)在6×6mm按键小节明确列出此URL，本次再次确认。 | 直插、常开、瞬时回弹；核对2／4脚版本及按钮高度。 |
| 杜邦线；1套 | [天猫41254478179](https://detail.tmall.com/item.htm?id=41254478179)；**C** | [课程BOM](https://github.com/haohaoalt/rikirobot)明确列出15／30cm、公公／公母／母母线与此URL，本次再次确认。 | 2.54mm；面包板公公，GPIO至面包板公母；选择长度与SKU。 |
| 2.54mm GPIO排针；1套 | [天猫651104320753](https://detail.tmall.com/item.htm?id=651104320753)；**L** | [小鱼焊接文档](https://www.xfishai.com/xfish-lite/welding)再次确认URL，但示例为**1×4P**直排针，不能证明有Zero 2 W所需排针。 | 板上未焊排针时需**2×20**；获取正确SKU或另找链接。不能按来源的1×4P示例当作完整树莓派排针购买。 |
| Micro USB OTG转USB-A母；1根 | [淘宝527775920057](https://item.taobao.com/item.htm?id=527775920057)；**C** | [Buy2you索引](https://m.buy2you.com/en/buy2taobao/item/527775920057.html)搜索结果再次明确给出原URL和Micro USB OTG／Pi Zero标题；完整重开来源页返回Cache miss。 | 主机模式数据转接，Micro USB公头及USB-A母头，核对插头空间；排除仅充电与Mini USB版本。 |
| 30AWG硅胶信号飞线；1套 | [淘宝658475245663](https://item.taobao.com/item.htm?id=658475245663)；**C** | [DF创客项目](https://mc.dfrobot.com.cn/article-380515.html)明确将URL标为30AWG硅胶线，本次再次确认。 | 实际线规、多股导体及绝缘外径；电源线需另按实测电流／压降选型。 |

所有商家现价、运费、库存、现店铺及SKU均未验证，未引用索引历史价格。

### 待补采购链接

| 配件 | 状态与有效线索 | 下单条件 |
|---|---|---|
| 400孔免焊面包板；1块 | **M**。[小智来源](https://xiaozhi.me/home/zh/getting-started/)推荐此品类，但给出搜索词而非对应原商品URL。[ZY-60索引](https://www.taouq.com/id-eMyJqgdhDtdJog4qz0c8BKUzt0-d8ZBBDFnZ6Medbdsd/)仅为未验证线索，重开失败。 | 搜索“400孔 免焊面包板 2.54”；排除需要焊接的洞洞板。 |
| Mini HDMI台架线；1根 | **M**。结果主要为无关DP转换器、采集卡和屏幕套件，均未采用。 | 树莓派端为Mini HDMI Type C；先确认OL23端Type A／C／D再选另一端，不推断匹配。 |
| 全包围风镜；1副 | **M**。已排除头盔／太阳镜结果和内容错配的代购索引。[2014历史书签](https://api.duitang.com/blog/?id=145392386)提到沙漠蝗虫风镜并链接[38974401349](https://item.taobao.com/item.htm?id=38974401349)，但过旧且缺少安装尺寸，不列作可采购候选。 | 测量内腔深度及OL23间隙，确认可换透明／灰色镜片与安装空间；历史标题不能证明在售或防护能力。 |
| 中空挂绳＋安全脱离件；1套 | 完整需求为**M**；[可脱离挂绳索引](https://tao.hooos.com/goods_GA9RW4gf8tYeOyNPZgSYvDCQtJ-rkOPPMu2DN6Vp4VTV.html)为**L**。索引称1.5cm受力自动断开，店名聆音楼旗舰店，但未暴露原URL，也未证明中空。 | 搜索“中空 编织 挂绳 安全脱离扣”；确认穿线后线束仍可完整脱离，不能由线缆绕过脱离件形成拉索。 |
| 26AWG电源飞线；1套 | **M** | 按实测电流、压降及温升选型。 |
| 60–80cm柔性HDMI；1根 | **M**，第二批采购 | 确认两端、弯头方向、长度及应力释放；不假定FPC可反复锐角折叠。 |

### 访问记录

此前打开淘宝／天猫原站返回不可访问或不可重试错误，不能据此认定下架或要求登录。本次来源复查只确认出处。采购前仍须检查商家页面，不能将这份不完整清单报告为全部已核实。
