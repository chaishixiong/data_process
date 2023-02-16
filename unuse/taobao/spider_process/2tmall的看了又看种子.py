from tools.tools_d.tools_base import tools_file_b
data_tools = tools_file_b()
platerm = input("请输入平台:")
data_base = "taobao"
if platerm == "飞猪":
    data_base = "飞猪"
file_name_w = r"X:\数据库\{}\{{5_8_1_ALL商品ID_{}去重_种子}}[key].txt".format(data_base,platerm)
if platerm == "天猫" or platerm == "飞猪":
    file = open(file_name_w, "w", encoding="utf-8")
    for i in data_tools.get_yield(r"X:\数据库\{}\{{5_8_1_ALL商品ID_{}去重}}[商品ID,卖家ID,店铺ID].txt".format(data_base,platerm)):
        data = i.strip().split(",")
        str_data = "itemId={}&sellerId={}&shopId={}&".format(data[0],data[1],data[2])
        file.write(str_data+"\n")
    file.close()
elif platerm == "浙江淘宝":
    file = open(file_name_w, "w", encoding="utf-8")
    for i in data_tools.get_yield(r"X:\数据库\{}\{{5_8_1_ALL商品ID_{}去重}}[商品ID,卖家ID,店铺ID].txt".format(data_base,platerm)):
        data = i.strip().split(",")
        str_data = "seller_id={}&shop_id={}&item_ids={}".format(data[1],data[2],data[0])
        file.write(str_data+"\n")
    file.close()
else:
    print("输入平台错误")
