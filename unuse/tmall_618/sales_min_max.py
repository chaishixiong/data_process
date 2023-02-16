import os
from collections import defaultdict
path = r"X:\数据库\双十一\sales"
file_names = os.listdir(path)
sales_dict = defaultdict(list)
seed_file = r"X:\数据库\双十一\sales\{taobao_look-data_zhejiang_jieguo3}[goods,min_sales,max_sales,cha_sales].txt"
data_file = r"X:\数据库\双十一\sales\{taobao_look-data_zhejiang_5}[goods,sales].txt"
write_file = r"X:\数据库\双十一\sales\{taobao_look-data_zhejiang_jieguo4}[goods,min_sales,max_sales,cha_sales].txt"

jieguo_dict = dict()
if "jieguo" in seed_file:
    sales_dict = defaultdict(list)
    with open(seed_file,"r",encoding="utf-8") as f:
        for i in f:
            data = i.strip().split(",")
            goodsid = data[0]
            min_sales = data[1]
            max_sales = data[2]
            sales_dict[goodsid].append((min_sales,max_sales))
    with open(data_file,"r",encoding="utf-8") as f:
        for i in f:
            data = i.strip().split(",")
            goodsid = data[0]
            sales = data[1]
            sales_dict[goodsid].append(int(sales) if sales else 0)
    with open(write_file,"w",encoding="utf-8") as f:
        for i,y in sales_dict.items():
            if len(y)==2:
                if y[0][1]:
                    if y[1]>int(y[0][1]):
                        min_sales = y[0][0]
                        max_sales = y[1]
                    else:
                        min_sales = y[0][0]
                        max_sales = y[0][1]
                else:
                    if y[1]>int(y[0][0]):
                        min_sales = y[0][0]
                        max_sales = y[1]
                    else:
                        min_sales = y[1]
                        max_sales = ""
            else:
                if isinstance(y[0],tuple):
                    min_sales = y[0][0]
                    max_sales = y[0][1]
                else:
                    min_sales = y[0]
                    max_sales = ""
            if max_sales:
                cha = int(max_sales)-int(min_sales)
            else:
                cha = ""
            f.write("{},{},{},{}\n".format(i,min_sales,max_sales,cha))
else:
    sales_dict = defaultdict(list)
    with open(seed_file, "r", encoding="utf-8") as f:
        for i in f:
            data = i.strip().split(",")
            goodsid = data[0]
            sales = data[1]
            sales_dict[goodsid].append(int(sales) if sales else 0)
    with open(data_file,"r",encoding="utf-8") as f:
        for i in f:
            data = i.strip().split(",")
            goodsid = data[0]
            sales = data[1]
            sales_dict[goodsid].append(int(sales) if sales else 0)
    with open(write_file,"w",encoding="utf-8") as f:
        for i,y in sales_dict.items():
            if len(y)==2:
                if y[1]-y[0]>0:
                    min_sales = y[0]
                    max_sales = y[1]
                else:
                    min_sales = min(y[0],y[1])
                    max_sales = ""
            else:
                min_sales = y[0]
                max_sales = ""
            f.write("{},{},{}\n".format(i,min_sales,max_sales))







