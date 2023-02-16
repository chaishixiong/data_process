data_dict = dict()
with open(r"X:\数据库\taobao\{taobao_look-data_tmall}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.split(",")
        goods = data[0]
        sales = data[3]
        hdata = data_dict.get(goods)
        if hdata:
            if int(sales)>int(hdata[3]):
                data_dict[goods]=data
        else:
            data_dict[goods] = data
with open(r"X:\数据库\taobao\{taobao_look-data_tmall_quchong}[goods,seller_id,price,sales,name,cid,score,url].txt","w",encoding="utf-8") as f:
    for i in data_dict.values():
        f.write(",".join(i))