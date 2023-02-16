with open(r"X:\数据库\taobao\备份\{taobao_address_open}[shop_id,address,open_shop_date].txt","r",encoding="utf-8") as f:
    for i in f:
        if i.strip().split(",")[0]=="62336726":
            print(i)
            break