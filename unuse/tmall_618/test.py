# file_tmall_zhejiang = open(r"X:\数据库\taobao\{tmall_shopid_zhejiang}[shop_id,seller_id].txt","r",encoding="utf-8")
# tmall_set = {i.strip().split(",")[1]for i in file_tmall_zhejiang.readlines()}
# file_tmall_zhejiang.close()

#
# with open(r"X:\数据库\taobao\上个月过程数据\{taobao_look-data_zhejiang}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as f:
#     num = 0
#     for i in f:
#         data = i.strip().split(",")
#         if data[2] and data[3] and float(data[2]) < 100000:
#             num += float(data[2])*int(data[3])
#     print(num)
# file = open(r"X:\数据库\taobao\{5_2_asyn取商品ID_浙江淘宝_test}[商品ID,KEY,商品名称,价格,月销量].txt","w",encoding="utf-8")
with open(r"X:\数据库\taobao\{5_2_asyn取商品ID_浙江淘宝}[商品ID,KEY,商品名称,价格,月销量].txt","r",encoding="utf-8") as f:
    num = 0
    for i in f:
        data = i.strip().split(",")
        try:
            if data[3] and data[4] and float(data[3])<100000:
                num+=float(data[3])*int(data[4])
                # file.write(i)
        except:
            pass
    print(num)
#
# with open(r"X:\数据库\taobao\{6_4_1_字典_天猫_月统计}[seller_id,sum(sales 米 price),sum(sales)].txt","r",encoding="utf-8") as f:
#     num = 0
#     for i in f:
#         data = i.strip().split(",")
#         if data[1]:
#             num+=float(data[1])
#     print(num)
