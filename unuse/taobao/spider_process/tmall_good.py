file_name = r"X:\数据库\飞猪\{feizhu_goodsmobile_202008}[采集时间,商品ID,近似销量,月销量,评论数,总库存,收藏量,发货地址,类目ID,品牌ID,平台,商品名称,卖家ID,店铺ID,促销名称,促销价,定金,定金描述,原价名称,原价,配送费用,商品保证,网店推广,推广描述,商品积分,主图,商品属性,区间价格].txt"
write_name = r"X:\数据库\飞猪\{feizhu_goodsmobile_202008_w}[采集时间,商品ID,近似销量,月销量,评论数,总库存,收藏量,发货地址,类目ID,品牌ID,平台,商品名称,卖家ID,店铺ID,促销名称,促销价,定金,定金描述,原价名称,原价,配送费用,商品保证,网店推广,推广描述,商品积分,主图,商品属性,区间价格].txt"
write_file = open(write_name, "w", encoding="utf-8")
with open(file_name, "r", encoding="utf-8") as f:
    for i in f:
        data = i.split(",")
        if "万" in data[3]:
            sales = data[3].replace("万", "")
            sales = sales.replace("+", "")
            sales_real = str(int(float(sales) * 10000))
            data[3] = sales_real
            write_file.write(",".join(data))
        elif "+" in data[3]:
            sales = data[3].replace("+", "")
            data[3] = sales
            write_file.write(",".join(data))
        else:
            write_file.write(i)
write_file.close()