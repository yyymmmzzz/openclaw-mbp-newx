#!/usr/bin/env python3
import psycopg2
from datetime import datetime, timedelta

conn = psycopg2.connect(host='127.0.0.1', port='5432', database='frepple0', user='frepple', password='frepple')
conn.autocommit = True
cur = conn.cursor()
now = '2026-04-01 00:00:00'
today = datetime(2026, 4, 1)

def ts(days=0, hours=0):
    d = today + timedelta(days=days, hours=hours)
    return d

def iv(seconds):
    return f"{seconds} seconds"

print("Loading Locations...")
locations = [
    ("WH-RAW-01","原材料仓库A区-钢材","warehouse"),("WH-RAW-02","原材料仓库B区-塑料","warehouse"),
    ("WH-RAW-03","原材料仓库C区-电子元件","warehouse"),("WH-RAW-04","原材料仓库D区-包装","warehouse"),
    ("WH-SEM-01","半成品仓库-机箱区","warehouse"),("WH-SEM-02","半成品仓库-PCBA区","warehouse"),("WH-SEM-03","半成品仓库-电机区","warehouse"),
    ("WH-FG-01","成品仓库A区-A系列","warehouse"),("WH-FG-02","成品仓库B区-B系列","warehouse"),
    ("WH-FG-03","成品仓库C区-C/D系列","warehouse"),("WH-FG-04","成品仓库D区-配件区","warehouse"),
    ("LINE-STL-01","产线-钢材加工","production"),("LINE-STL-02","产线-钣金成型","production"),
    ("LINE-PCK-01","产线-PCB贴装","production"),("LINE-PCK-02","产线-PCB焊接","production"),
    ("LINE-ASM-01","产线-装配线A","production"),("LINE-ASM-02","产线-装配线B","production"),("LINE-ASM-03","产线-装配线C","production"),
    ("LINE-TST-01","产线-测试线","production"),("LINE-PKG-01","产线-包装线","production"),
    ("QC-01","质检中心-原材料检验","quality"),("QC-02","质检中心-过程检验","quality"),("QC-03","质检中心-成品检验","quality"),
    ("OFF-RD-01","研发中心","office"),("OFF-RD-02","设计室","office"),("OFF-MGT-01","管理办公区","office"),
    ("LOG-IN-01","收货区","logistics"),("LOG-OUT-01","出货区","logistics"),("LOG-RET-01","退货处理区","logistics"),("LOG-STG-01","暂存区","logistics"),
    ("CUST-CN-01","客户现场-华南区","customer"),("CUST-CN-02","客户现场-华东区","customer"),("CUST-CN-03","客户现场-华北区","customer"),
]
for name,desc,cat in locations:
    cur.execute("INSERT INTO location (name,description,category,owner_id,lastmodified) VALUES (%s,%s,%s,NULL,%s) ON CONFLICT (name) DO NOTHING",(name,desc,cat,now))
print(f"  Locations: {len(locations)}")

print("Loading Suppliers...")
suppliers = [
    ("SUP-STL-001","宝钢供应链","supplier"),("SUP-STL-002","鞍钢材料贸易","supplier"),
    ("SUP-STL-003","沙钢集团采购","supplier"),("SUP-STL-004","华菱钢铁","supplier"),
    ("SUP-PLT-001","中石化塑料分销","supplier"),("SUP-PLT-002","金发科技","supplier"),("SUP-PLT-003","道恩高分子","supplier"),
    ("SUP-CMP-001","村田电子贸易","supplier"),("SUP-CMP-002","三星电机中国","supplier"),
    ("SUP-CMP-003","风华高科","supplier"),("SUP-CMP-004","顺络电子","supplier"),("SUP-CMP-005","PCB极速打样","supplier"),
    ("SUP-PKG-001","合兴包装材料","supplier"),("SUP-PKG-002","荣成环科纸业","supplier"),("SUP-PKG-003","众喜泡沫制品","supplier"),
    ("SUP-MOT-001","卧龙电气集团","supplier"),("SUP-MOT-002","威灵电机制造","supplier"),("SUP-MOT-003","松下电机中国","supplier"),
    ("SUP-PSU-001","台达电子技术","supplier"),("SUP-PSU-002","明纬电源股份","supplier"),("SUP-PSU-003","航嘉驰源电气","supplier"),
    ("SUP-IC-001","德州仪器中国","supplier"),("SUP-IC-002","意法半导体中国","supplier"),("SUP-IC-003","微芯科技股份","supplier"),
    ("SUP-MTL-001","螺丝螺母标准件","supplier"),("SUP-MTL-002","电线电缆","supplier"),
    ("SUP-MTL-003","润滑油清洗剂","supplier"),("SUP-MTL-004","工具耗材","supplier"),("SUP-MTL-005","办公用品","supplier"),
    ("SUP-LOG-001","顺丰速运企业","supplier"),("SUP-LOG-002","德邦物流股份","supplier"),
]
for name,desc,cat in suppliers:
    cur.execute("INSERT INTO supplier (name,description,category,owner_id,lastmodified) VALUES (%s,%s,%s,NULL,%s) ON CONFLICT (name) DO NOTHING",(name,desc,cat,now))
print(f"  Suppliers: {len(suppliers)}")

print("Loading Customers...")
customers = [
    ("CUST-GD-001","美的集团采购","customer"),("CUST-GD-002","格力电器股份","customer"),
    ("CUST-GD-003","TCL海外事业部","customer"),("CUST-GD-004","海信集团","customer"),
    ("CUST-GD-005","创维RGB电子","customer"),("CUST-GD-006","华为技术采购","customer"),("CUST-GD-007","中兴通讯采购","customer"),
    ("CUST-SH-001","上海电气集团","customer"),("CUST-SH-002","海尔智家股份","customer"),
    ("CUST-SH-003","比亚迪汽车工业","customer"),("CUST-SH-004","蔚来汽车采购","customer"),
    ("CUST-SH-005","小鹏汽车科技","customer"),("CUST-SH-006","理想汽车","customer"),
    ("CUST-SH-007","上海汽车集团","customer"),("CUST-SH-008","吉利控股集团","customer"),
    ("CUST-BJ-001","小米科技","customer"),("CUST-BJ-002","京东零售采购","customer"),
    ("CUST-BJ-003","百度在线网络","customer"),("CUST-BJ-004","字节跳动采购","customer"),
    ("CUST-BJ-005","中国移动采购","customer"),("CUST-BJ-006","中国电信集团","customer"),
    ("CUST-OT-001","格力电器(重庆)","customer"),("CUST-OT-002","美的武汉制冷","customer"),
    ("CUST-OT-003","海尔电器(胶州)","customer"),("CUST-OT-004","海信(山东)空调","customer"),
    ("CUST-OT-005","长虹电器股份","customer"),("CUST-OT-006","康佳集团股份","customer"),
    ("CUST-AB-001","Samsung Electronics VN","customer"),("CUST-AB-002","LG Electronics VN","customer"),
    ("CUST-AB-003","Panasonic Asia Pacific","customer"),("CUST-AB-004","Sharp Corporation Japan","customer"),
    ("CUST-AB-005","Sony Electronics Asia","customer"),
]
for name,desc,cat in customers:
    cur.execute("INSERT INTO customer (name,description,category,owner_id,lastmodified) VALUES (%s,%s,%s,NULL,%s) ON CONFLICT (name) DO NOTHING",(name,desc,cat,now))
print(f"  Customers: {len(customers)}")

print("Loading Resources...")
resources = [
    ("RES-CNC-001","数控激光切割机#1","resource",True,1,100),("RES-CNC-002","数控激光切割机#2","resource",True,1,100),
    ("RES-CNC-003","数控折弯机#1","resource",True,1,80),("RES-CNC-004","数控折弯机#2","resource",True,1,80),
    ("RES-CNC-005","焊接机器人#1","resource",True,1,60),("RES-CNC-006","焊接机器人#2","resource",True,1,60),
    ("RES-SMT-001","SMT贴片机#1","resource",True,1,120),("RES-SMT-002","SMT贴片机#2","resource",True,1,120),
    ("RES-SMT-003","回流焊炉#1","resource",True,1,100),("RES-SMT-004","AOI自动光学检测仪","resource",True,1,40),
    ("RES-ASM-001","装配工位A#1-5","resource",True,5,50),("RES-ASM-002","装配工位B#1-5","resource",True,5,50),
    ("RES-ASM-003","装配工位C#1-5","resource",True,5,50),("RES-ASM-004","流水线A#1-3","resource",True,3,80),
    ("RES-ASM-005","流水线B#1-3","resource",True,3,80),
    ("RES-TST-001","ICT测试仪#1","resource",True,1,30),("RES-TST-002","ICT测试仪#2","resource",True,1,30),
    ("RES-TST-003","功能测试台#1","resource",True,1,40),("RES-TST-004","功能测试台#2","resource",True,1,40),
    ("RES-TST-005","老化测试室","resource",True,1,200),
    ("RES-PKG-001","包装线#1","resource",True,1,60),("RES-PKG-002","包装线#2","resource",True,1,60),
    ("RES-PKG-003","打包机#1","resource",True,1,30),
    ("RES-WHS-001","叉车A#1-2","resource",True,2,50),("RES-WHS-002","叉车B#1-2","resource",True,2,50),
    ("RES-WHS-003","堆垛机#1","resource",True,1,40),("RES-WHS-004","传送带系统","resource",True,1,150),
    ("RES-QC-001","三坐标测量仪","resource",True,1,20),("RES-QC-002","硬度测试仪","resource",True,1,15),
    ("RES-QC-003","光谱分析仪","resource",True,1,15),
    ("RES-MLD-001","冲压模具组#1","resource",True,1,0),("RES-MLD-002","注塑模具组#1-3","resource",True,3,0),
]
for name,desc,rtype,constrained,maximum,cost in resources:
    cur.execute("INSERT INTO resource (name,description,type,constrained,maximum,cost,location_id,owner_id,lastmodified) VALUES (%s,%s,%s,%s,%s,%s,NULL,NULL,%s) ON CONFLICT (name) DO NOTHING",(name,desc,rtype,constrained,maximum,cost,now))
print(f"  Resources: {len(resources)}")

print("Loading Operations...")
operations = [
    ("PUR-STL-001","采购钢材","WH-RAW-01",iv(86400)),
    ("PUR-STL-002","采购塑料粒子","WH-RAW-02",iv(86400)),
    ("PUR-CMP-001","采购电子元件","WH-RAW-03",iv(172800)),
    ("PUR-CMP-002","采购PCB板","WH-RAW-03",iv(172800)),
    ("PUR-PKG-001","采购包装材料","WH-RAW-04",iv(43200)),
    ("PUR-MOT-001","采购电机","WH-SEM-03",iv(172800)),
    ("PUR-PSU-001","采购电源模块","WH-SEM-03",iv(172800)),
    ("MFG-STL-CUT","钢材切割下料","LINE-STL-01",iv(7200)),
    ("MFG-STL-BND","钢材折弯成型","LINE-STL-02",iv(10800)),
    ("MFG-STL-WLD","钢材焊接","LINE-STL-02",iv(14400)),
    ("MFG-PLT-INJ","塑料注塑成型","LINE-STL-01",iv(3600)),
    ("MFG-PCK-SMT","SMT贴装","LINE-PCK-01",iv(1800)),
    ("MFG-PCK-REF","回流焊接","LINE-PCK-02",iv(1200)),
    ("MFG-PCK-AOI","AOI光学检测","LINE-PCK-02",iv(600)),
    ("MFG-PCK-THR","通孔焊接","LINE-PCK-02",iv(2400)),
    ("ASM-CAB-FRM","机箱框架组装","LINE-ASM-01",iv(3600)),
    ("ASM-CAB-PNL","机箱面板装配","LINE-ASM-01",iv(2400)),
    ("ASM-MOT-001","电机组件装配","LINE-ASM-02",iv(4800)),
    ("ASM-PSU-001","电源模块装配","LINE-ASM-02",iv(3600)),
    ("ASM-FG-A1","装配产品A1","LINE-ASM-01",iv(7200)),
    ("ASM-FG-A2","装配产品A2","LINE-ASM-01",iv(9000)),
    ("ASM-FG-B1","装配产品B1","LINE-ASM-02",iv(7200)),
    ("ASM-FG-B2","装配产品B2","LINE-ASM-02",iv(9000)),
    ("ASM-FG-C1","装配产品C1","LINE-ASM-03",iv(5400)),
    ("ASM-FG-C2","装配产品C2","LINE-ASM-03",iv(7200)),
    ("ASM-FG-D1","装配产品D1","LINE-ASM-03",iv(10800)),
    ("TST-ICT-001","ICT在线测试","LINE-TST-01",iv(600)),
    ("TST-FUNC-001","功能测试","LINE-TST-01",iv(1800)),
    ("TST-AGING","老化测试","LINE-TST-01",iv(28800)),
    ("TST-FINAL","最终检验","LINE-TST-01",iv(1200)),
    ("PKG-FINAL","成品包装","LINE-PKG-01",iv(2400)),
    ("PKG-STORAGE","入库上架","WH-FG-01",iv(1200)),
    ("LOG-SHIP","出库发货","LOG-OUT-01",iv(1800)),
]
for name,desc,loc,dur in operations:
    cur.execute("INSERT INTO operation (name,description,type,location_id,duration,item_id,owner_id,lastmodified) VALUES (%s,%s,'operation',%s,%s,NULL,NULL,%s) ON CONFLICT (name) DO NOTHING",(name,desc,loc,dur,now))
print(f"  Operations: {len(operations)}")

print("Loading BOMs...")
boms = [
    ("ASM-FG-A1","FG-PROD-A1","end",1),("ASM-FG-A1","SEM-CAB-001","start",1),
    ("ASM-FG-A1","SEM-PCK-001","start",1),("ASM-FG-A1","SEM-MOT-001","start",1),("ASM-FG-A1","SEM-PSU-001","start",1),
    ("ASM-FG-A2","FG-PROD-A2","end",1),("ASM-FG-A2","SEM-CAB-002","start",1),
    ("ASM-FG-A2","SEM-PCK-001","start",1),("ASM-FG-A2","SEM-MOT-001","start",2),("ASM-FG-A2","SEM-PSU-001","start",1),
    ("ASM-FG-B1","FG-PROD-B1","end",1),("ASM-FG-B1","SEM-CAB-001","start",1),("ASM-FG-B1","SEM-PCK-001","start",1),("ASM-FG-B1","SEM-MOT-001","start",1),
    ("ASM-FG-B2","FG-PROD-B2","end",1),("ASM-FG-B2","SEM-CAB-002","start",1),
    ("ASM-FG-B2","SEM-PCK-001","start",2),("ASM-FG-B2","SEM-MOT-001","start",2),("ASM-FG-B2","SEM-PSU-001","start",2),
    ("ASM-FG-C1","FG-PROD-C1","end",1),("ASM-FG-C1","SEM-CAB-001","start",1),("ASM-FG-C1","SEM-PCK-001","start",1),
    ("ASM-FG-C2","FG-PROD-C2","end",1),("ASM-FG-C2","SEM-CAB-002","start",1),
    ("ASM-FG-C2","SEM-PCK-001","start",1),("ASM-FG-C2","SEM-MOT-001","start",1),("ASM-FG-C2","SEM-PSU-001","start",1),
    ("ASM-FG-D1","FG-PROD-D1","end",1),("ASM-FG-D1","SEM-CAB-002","start",1),
    ("ASM-FG-D1","SEM-PCK-001","start",2),("ASM-FG-D1","SEM-MOT-001","start",3),("ASM-FG-D1","SEM-PSU-001","start",2),
    ("ASM-CAB-FRM","SEM-CAB-001","end",1),("ASM-CAB-FRM","RAW-STL-001","start",5),("ASM-CAB-FRM","RAW-PKG-001","start",2),
    ("ASM-CAB-PNL","SEM-CAB-002","end",1),("ASM-CAB-PNL","RAW-STL-002","start",3),("ASM-CAB-PNL","RAW-CMP-004","start",1),
    ("MFG-PCK-SMT","SEM-PCK-001","end",1),("MFG-PCK-SMT","RAW-CMP-001","start",20),
    ("MFG-PCK-SMT","RAW-CMP-002","start",20),("MFG-PCK-SMT","RAW-CMP-003","start",5),("MFG-PCK-SMT","RAW-CMP-004","start",1),
    ("ASM-MOT-001","SEM-MOT-001","end",1),("ASM-MOT-001","RAW-STL-003","start",2),("ASM-MOT-001","RAW-PLT-001","start",1),
    ("ASM-PSU-001","SEM-PSU-001","end",1),("ASM-PSU-001","RAW-CMP-003","start",3),
    ("ASM-PSU-001","RAW-CMP-001","start",10),("ASM-PSU-001","RAW-CMP-002","start",10),
]
for op,item,btype,qty in boms:
    cur.execute("INSERT INTO operationmaterial (operation_id,item_id,type,quantity,lastmodified) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",(op,item,btype,qty,now))
print(f"  BOMs: {len(boms)}")

print("Loading Sales Orders...")
sales_orders = [
    ("SO-GD-001","FG-PROD-A1","WH-FG-01","CUST-GD-001",50,ts(7),5),
    ("SO-GD-002","FG-PROD-A2","WH-FG-01","CUST-GD-001",30,ts(10),5),
    ("SO-GD-003","FG-PROD-B1","WH-FG-02","CUST-GD-002",80,ts(5),5),
    ("SO-GD-004","FG-PROD-B2","WH-FG-02","CUST-GD-003",45,ts(8),5),
    ("SO-GD-005","FG-PROD-C1","WH-FG-03","CUST-GD-004",100,ts(3),5),
    ("SO-GD-006","FG-PROD-C2","WH-FG-03","CUST-GD-005",60,ts(6),5),
    ("SO-GD-007","FG-PROD-D1","WH-FG-03","CUST-GD-006",25,ts(12),5),
    ("SO-GD-008","FG-PROD-A1","WH-FG-01","CUST-GD-007",40,ts(9),5),
    ("SO-SH-001","FG-PROD-A1","WH-FG-01","CUST-SH-001",70,ts(5),5),
    ("SO-SH-002","FG-PROD-B1","WH-FG-02","CUST-SH-002",55,ts(7),5),
    ("SO-SH-003","FG-PROD-B2","WH-FG-02","CUST-SH-003",35,ts(10),5),
    ("SO-SH-004","FG-PROD-C1","WH-FG-03","CUST-SH-004",90,ts(4),5),
    ("SO-SH-005","FG-PROD-C2","WH-FG-03","CUST-SH-005",40,ts(8),5),
    ("SO-SH-006","FG-PROD-D1","WH-FG-03","CUST-SH-006",20,ts(14),5),
    ("SO-SH-007","FG-PROD-A2","WH-FG-01","CUST-SH-007",50,ts(6),5),
    ("SO-SH-008","FG-PROD-B1","WH-FG-02","CUST-SH-008",65,ts(5),5),
    ("SO-BJ-001","FG-PROD-A1","WH-FG-01","CUST-BJ-001",85,ts(4),5),
    ("SO-BJ-002","FG-PROD-A2","WH-FG-01","CUST-BJ-002",100,ts(3),5),
    ("SO-BJ-003","FG-PROD-B1","WH-FG-02","CUST-BJ-003",45,ts(6),5),
    ("SO-BJ-004","FG-PROD-B2","WH-FG-02","CUST-BJ-004",55,ts(7),5),
    ("SO-BJ-005","FG-PROD-C1","WH-FG-03","CUST-BJ-005",75,ts(5),5),
    ("SO-BJ-006","FG-PROD-C2","WH-FG-03","CUST-BJ-006",35,ts(9),5),
    ("SO-OT-001","FG-PROD-A1","WH-FG-01","CUST-OT-001",30,ts(8),5),
    ("SO-OT-002","FG-PROD-B1","WH-FG-02","CUST-OT-002",40,ts(6),5),
    ("SO-OT-003","FG-PROD-C1","WH-FG-03","CUST-OT-003",60,ts(4),5),
    ("SO-OT-004","FG-PROD-C2","WH-FG-03","CUST-OT-004",25,ts(10),5),
    ("SO-OT-005","FG-PROD-D1","WH-FG-03","CUST-OT-005",15,ts(12),5),
    ("SO-AB-001","FG-PROD-A1","WH-FG-01","CUST-AB-001",200,ts(20),3),
    ("SO-AB-002","FG-PROD-B1","WH-FG-02","CUST-AB-002",150,ts(18),3),
    ("SO-AB-003","FG-PROD-C1","WH-FG-03","CUST-AB-003",120,ts(15),3),
    ("SO-AB-004","FG-PROD-D1","WH-FG-03","CUST-AB-004",80,ts(25),3),
    ("SO-AB-005","FG-PROD-A2","WH-FG-01","CUST-AB-005",100,ts(22),3),
]
for name,item,loc,cust,qty,due,pri in sales_orders:
    cur.execute("INSERT INTO demand (name,item_id,location_id,customer_id,quantity,due,priority,status,lastmodified) VALUES (%s,%s,%s,%s,%s,%s,%s,'quote',%s) ON CONFLICT (name) DO NOTHING",(name,item,loc,cust,qty,due,pri,now))
print(f"  Sales Orders: {len(sales_orders)}")

print("Loading ItemSuppliers...")
itemsuppliers = [
    ("RAW-STL-001","SUP-STL-001","WH-RAW-01",iv(86400*3)),
    ("RAW-STL-002","SUP-STL-002","WH-RAW-01",iv(86400*4)),
    ("RAW-STL-003","SUP-STL-003","WH-RAW-01",iv(86400*5)),
    ("RAW-STL-001","SUP-STL-004","WH-RAW-01",iv(86400*6)),
    ("RAW-PLT-001","SUP-PLT-001","WH-RAW-02",iv(86400*2)),
    ("RAW-PLT-002","SUP-PLT-002","WH-RAW-02",iv(86400*3)),
    ("RAW-PLT-003","SUP-PLT-003","WH-RAW-02",iv(86400*4)),
    ("RAW-CMP-001","SUP-CMP-001","WH-RAW-03",iv(86400*5)),
    ("RAW-CMP-002","SUP-CMP-002","WH-RAW-03",iv(86400*5)),
    ("RAW-CMP-003","SUP-CMP-003","WH-RAW-03",iv(86400*7)),
    ("RAW-CMP-004","SUP-CMP-004","WH-RAW-03",iv(86400*6)),
    ("RAW-CMP-004","SUP-CMP-005","WH-RAW-03",iv(86400*4)),
    ("RAW-PKG-001","SUP-PKG-001","WH-RAW-04",iv(43200*2)),
    ("RAW-PKG-002","SUP-PKG-002","WH-RAW-04",iv(43200*2)),
    ("RAW-PKG-003","SUP-PKG-003","WH-RAW-04",iv(43200*3)),
    ("SEM-MOT-001","SUP-MOT-001","WH-SEM-03",iv(86400*7)),
    ("SEM-MOT-001","SUP-MOT-002","WH-SEM-03",iv(86400*8)),
    ("SEM-MOT-001","SUP-MOT-003","WH-SEM-03",iv(86400*10)),
    ("SEM-PSU-001","SUP-PSU-001","WH-SEM-03",iv(86400*6)),
    ("SEM-PSU-001","SUP-PSU-002","WH-SEM-03",iv(86400*7)),
    ("SEM-PSU-001","SUP-PSU-003","WH-SEM-03",iv(86400*8)),
    ("RAW-CMP-003","SUP-IC-001","WH-RAW-03",iv(86400*10)),
    ("RAW-CMP-003","SUP-IC-002","WH-RAW-03",iv(86400*12)),
    ("RAW-CMP-003","SUP-IC-003","WH-RAW-03",iv(86400*14)),
    ("RAW-STL-001","SUP-MTL-001","WH-RAW-01",iv(86400*2)),
    ("RAW-PLT-001","SUP-MTL-002","WH-RAW-02",iv(86400*3)),
    ("RAW-CMP-001","SUP-MTL-003","WH-RAW-03",iv(86400*2)),
    ("RAW-STL-002","SUP-MTL-004","WH-RAW-01",iv(86400*1)),
    ("RAW-PKG-001","SUP-MTL-005","WH-RAW-04",iv(86400*2)),
    ("RAW-STL-001","SUP-STL-001","WH-RAW-01",iv(86400*5)),
    ("RAW-PLT-001","SUP-PLT-001","WH-RAW-02",iv(86400*4)),
    ("RAW-CMP-001","SUP-CMP-001","WH-RAW-03",iv(86400*6)),
]
for item,sup,loc,lead in itemsuppliers:
    cur.execute("INSERT INTO itemsupplier (item_id,supplier_id,location_id,leadtime,lastmodified) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",(item,sup,loc,lead,now))
print(f"  ItemSuppliers: {len(itemsuppliers)}")

print("Loading Buffers...")
buffers = [
    ("RAW-STL-001","WH-RAW-01",500,100),("RAW-STL-002","WH-RAW-01",300,80),("RAW-STL-003","WH-RAW-01",150,50),
    ("RAW-PLT-001","WH-RAW-02",800,200),("RAW-PLT-002","WH-RAW-02",600,150),("RAW-PLT-003","WH-RAW-02",400,100),
    ("RAW-CMP-001","WH-RAW-03",3000,500),("RAW-CMP-002","WH-RAW-03",3000,500),
    ("RAW-CMP-003","WH-RAW-03",800,200),("RAW-CMP-004","WH-RAW-03",400,100),
    ("RAW-PKG-001","WH-RAW-04",1500,300),("RAW-PKG-002","WH-RAW-04",1000,200),("RAW-PKG-003","WH-RAW-04",200,50),
    ("SEM-CAB-001","WH-SEM-01",50,20),("SEM-CAB-002","WH-SEM-01",30,10),
    ("SEM-PCK-001","WH-SEM-02",80,30),("SEM-MOT-001","WH-SEM-03",60,20),("SEM-PSU-001","WH-SEM-03",40,15),
    ("FG-PROD-A1","WH-FG-01",100,30),("FG-PROD-A2","WH-FG-01",50,15),
    ("FG-PROD-B1","WH-FG-02",80,25),("FG-PROD-B2","WH-FG-02",40,10),
    ("FG-PROD-C1","WH-FG-03",120,40),("FG-PROD-C2","WH-FG-03",60,20),("FG-PROD-D1","WH-FG-03",20,5),
    ("FG-ACC-001","WH-FG-04",200,50),("FG-ACC-002","WH-FG-04",300,80),("FG-ACC-003","WH-FG-04",150,40),
    ("FG-ACC-004","WH-FG-04",500,100),("FG-ACC-005","WH-FG-04",400,100),
    ("FG-SUB-001","WH-SEM-02",30,10),
]
for item,loc,onhand,minimum in buffers:
    try:
        cur.execute("INSERT INTO buffer (item_id,location_id,onhand,minimum,lastmodified) VALUES (%s,%s,%s,%s,%s) ON CONFLICT (item_id,location_id,batch) DO UPDATE SET onhand=EXCLUDED.onhand,minimum=EXCLUDED.minimum",(item,loc,onhand,minimum,now))
    except Exception as e:
        pass
print(f"  Buffers: {len(buffers)}")

print("\nSummary:")
for table,name in [("item","Items"),("location","Locations"),("supplier","Suppliers"),("customer","Customers"),("resource","Resources"),("operation","Operations"),("operationmaterial","BOMs"),("demand","Sales Orders"),("itemsupplier","Item Suppliers"),("buffer","Buffers")]:
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    print(f"  {name}: {cur.fetchone()[0]}")
conn.close()
print("\nAll done!")
