from collections import defaultdict
import os
# os.rename()
result = defaultdict(set)
f_w = open(r"X:\数据库\taobao\{taobao_look-data_other}[goods,seller_id,price,sales,name,cid,score,url].txt","w",encoding="utf-8")
num = 0
# with open(r"W:\scrapy_xc\taobao_look.txt","r",encoding="utf-8") as f:

with open(r"X:\数据库\taobao\{taobao_look-data_other_all}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as f:
    for i in f:
        num+=1
        if num%100000==0:
            print(num)
            f_w.flush()
        data = i.strip().split(",")
        try:
            goods_id = data[0]
            seller_id = data[1]
            try:
                sales = int(data[3])
            except:
                sales = 0
            goods_list = result.get(seller_id, set())

            if goods_id not in goods_list and (len(goods_list) < 5 or sales > 0):
                f_w.write(i)
                result[seller_id].add(goods_id)
        except:
            pass


