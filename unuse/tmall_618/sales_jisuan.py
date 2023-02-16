import os
from collections import defaultdict
path = r"X:\数据库\双十一\sales"
file_names = os.listdir(path)
sales_dict = defaultdict(list)
num = input("输入次数")
write_file = r"X:\数据库\双十一\{{taobao_look-data{}}}[goods_id,sales_num,sales_money].txt".format(num)
file_num = 0
for i in file_names:
    if i.endswith(".txt"):
        file_num+=1
        with open("{}/{}".format(path,i),"r",encoding="utf-8") as f:
            for j in f:
                data = j.strip().split(",")
                goods_id = data[0]
                sales_num = data[3]
                sales_dict[goods_id].append((file_num,int(sales_num) if sales_num else 0))
print("开始写入")
with open(write_file,"w",encoding="utf-8") as f1:
    sales_all = 0
    for i in sales_dict:
        sales_list = sales_dict.get(i)
        if len(sales_list)==2:
            sales_day = sales_list[1][1]-sales_list[0][1]
            sales_day = sales_day if sales_day>0 else 0
            sales_money = sales_day*float(sales_list[1][2])
            sales_all += sales_money
            f1.write('{},{},{}\n'.format(i,sales_day,sales_money))
print(sales_all)

