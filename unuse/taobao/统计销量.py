from pathlib import PureWindowsPath, Path
from collections import defaultdict

path = r"W:\徐超\新建文件夹"
file_name1 = "{9_2_天猫_商品计算销量}[卖家ID,商品ID,月销量,促销价].txt"
shuchu_name = r"20卖家id.txt"
path_name = Path(path)

file_path1 = path_name / file_name1
file_path2 = path_name / shuchu_name
num_shuliang = 0
with open(file_path1, "r", encoding="utf-8") as f:
    seller_dict = defaultdict(list)
    seller1_dict = defaultdict(list)
    for i in f:
        if i:
            num_shuliang+=1
            data_list = i.strip().split(",")
            sellerid = data_list[0]
            goodid = data_list[1]
            sale_num = int(data_list[2] if data_list[2] else 0)
            prime = float(data_list[3] if data_list[2] else 0)
            if prime<100000:
                sale_money = sale_num * prime
                seller_dict[sellerid].append(sale_money)
list1 = []

for i in seller_dict:
    num = len(seller_dict[i])
    sum_money = sum(seller_dict[i])
    list1.append((i,num,sum_money))
list1.sort(key = lambda x: x[2],reverse=True)
num_s = 0
with open(file_path2, "w", encoding="utf-8") as f1:
    for i in list1:
        num_s += i[1]
        if num_s < num_shuliang*0.2:
            f1.write("{},{},{}".format(i[0],i[1],i[2])+"\n")