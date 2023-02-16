#tmall
a = input("天猫还是淘宝浙江？：")
if a== "天猫":
    file_name = r"X:\数据库\taobao\{taobao_look-data_tmall}[goods,seller_id,price,sales,name,cid,score,url].txt"
elif a=="淘宝浙江":
    file_name = r"X:\数据库\taobao\{taobao_look-data_zhejiang}[goods,seller_id,price,sales,name,cid,score,url].txt"
else:
    raise("输入错误")
data_dict = dict()
with open(r"X:\数据库\taobao\taobao_tm_look-data_合并.txt","r",encoding="utf-8") as f:
    for i in f:
        try:
            data = i.split(",")
            goods = data[0]
            sales = data[3]
            # if int(sales)>0:#taobao其他地区数据筛选大于0
            hdata = data_dict.get(goods)
            if hdata:
                if int(sales)>int(hdata[3]):
                    data_dict[goods]=data
            else:
                data_dict[goods] = data
        except Exception as e:
            pass
with open(file_name,"w",encoding="utf-8") as f:
    for i in data_dict.values():
        f.write(",".join(i))
