#
def tamll_updata():
    b_name = {}
    with open(r"X:\数据库\taobao\updata\tmall_goodsmobile_618_202102.txt", "r", encoding="utf-8") as f_f:
        b_num = 0
        for i_i in f_f:
            b_num += 1
            if b_num % 1000000 == 0:
                print(b_num)
            data_1 = i_i.strip().split(",")
            b_name_id = data_1[1]
            b_name[b_name_id] = data_1


    file_write = open(r"X:\数据库\taobao\updata\goods_tmall_202106_new.txt", "a", encoding="utf-8")
    with open(r"X:\数据库\taobao\updata\{tmall_goodsmobile_202106}[采集时间,商品ID,近似销量,月销量,评论数,总库存,收藏量,发货地址,类目ID,品牌ID,平台,商品名称,卖家ID,店铺ID,促销名称,促销价,定金,定金描述,原价名称,原价,配送费用,商品保证,网店推广,推广描述,商品积分,主图,商品属性].txt", "r", encoding="utf-8") as f:
        b_type = "B"
        goods_list = {}
        num = 0
        for i in f:
            try:
                num += 1
                data = i.strip().split(",")
                goods_id = data[1]
                zhuangtai = b_name.get(goods_id)
                write_data = [""] * 27
                write_data[1] = data[0]
                write_data[1] = data[1]  # goods_id 商品ID
                write_data[2] = data[2]  # veges_month 销量
                write_data[3] = data[3]  # sales_month 销量
                write_data[4] = data[4]  # comment_count
                write_data[5] = data[5]  # inventory
                write_data[6] = data[6]  # collect_num
                write_data[7] = data[7]  # address 发货地址
                write_data[8] = data[8]  # cid 天猫类目ID
                write_data[9] = data[9]  # bid 天猫品牌ID
                write_data[10] = data[10]  # bc_type 平台
                write_data[11] = data[11]  # goods_name 天猫商品名称
                write_data[12] = data[12]  # seller_id 卖家ID
                write_data[13] = data[13]  # shop_id 店铺ID
                write_data[14] = data[14]  # discount_price 折扣价
                if zhuangtai != None:
                    if float(zhuangtai[13]) > float(data[15]):
                        write_data[15] = data[15]  # real_price 真实扣价
                        goods_list[goods_id] = 'T'
                    elif float(zhuangtai[13]) < float(data[15]):
                        write_data[15] = zhuangtai[13]
                        goods_list[goods_id] = 'T'
                    elif float(zhuangtai[13]) == float(data[15]):
                        write_data[15] = data[15]
                        goods_list[goods_id] = 'T'
                else:
                    write_data[15] = data[15]
                write_data[16] = data[16]  # price_area 区间价格
                write_data[17] = data[17]  # price
                write_data[18] = data[18]  # image_url
                write_data[19] = data[19]  # mark 双十一标识
                write_data[20] = data[20]  # mark2 跨店
                write_data[21] = data[21]  # obtained 是否下架
                write_data[22] = data[22]  # c_name1 类别
                write_data[23] = data[23]  # c_name2 类别2TypeError: sequence item 24: expected str instance, NoneType found
                write_data[24] = data[24]  # b_name 品牌name
                write_data[25] = data[25]  # sales_cha 销量差值
                write_data[26] = data[26]  # sales_money 销售额
                if write_data[15] == '':
                    print(goods_id)
                file_write.write(",".join(write_data)+"\n")
                if num % 1000000 == 0:
                    print(num)
                    file_write.flush()
            except Exception as e:
                print(e)

    for data_b_name in b_name.keys():
        id = data_b_name
        l_x = goods_list.get(id)
        if l_x == None:
            num_2 = 0
            try:
                num_2 += 1
                data = b_name[data_b_name]
                write_data_2 = [""] * 27
                '''
                update_date,goods_id,sales_month,comment_count,inventory, collect_num,address,cid,bid,bc_type,goods_name,seller_id,shop_id,discount_price,price_area,price,image_url
                0              1            2       3             4           5         6       7  8     9        10         11        12     13            14         15     16
                '''
                write_data_2[0] = data[0]  # update_date
                write_data_2[1] = data[1]  # goods_id
                write_data_2[2] = ''  # sales_vague
                write_data_2[3] = data[2]  # sales_month
                write_data_2[4] = data[3]  # comment_count
                write_data_2[5] = data[4]  # inventory
                write_data_2[6] = data[5]  # collect_num
                write_data_2[7] = data[6]  # address
                write_data_2[8] = data[7]  # cid
                write_data_2[9] = data[8]  # bid
                write_data_2[10] = data[9]  # bc_type
                write_data_2[11] = data[10]  # goods_name
                write_data_2[12] = data[11]  # seller_id
                write_data_2[13] = data[12]  # shop_id
                write_data_2[14] = ''  # advertising
                write_data_2[15] = data[13]  # discount_price
                write_data_2[16] = ''  # earnest
                write_data_2[17] = ''  # earnest_desc
                write_data_2[18] = ''  # price_name
                write_data_2[19] = ''  # price
                write_data_2[20] = ''  # ship_cost
                write_data_2[21] = ''  # assurance
                write_data_2[22] = ''  # promotion
                write_data_2[23] = ''  # promotion_desc
                write_data_2[24] = ''  # rewards
                write_data_2[25] = data[16]  # image_url
                write_data_2[26] = ''  # goods_info
                file_write.write(",".join(write_data_2) + "\n")
                if num_2 % 1000000 == 0:
                    print(num_2)
                    file_write.flush()
                if write_data_2[26] == '':
                    print(id)
            except Exception as e:
                print(e)
# shop_data = {}
# with open(r"X:\数据库\taobao\updata\tmall_shopinfo_202105_cp.txt", "r", encoding="utf-8") as f_f:
#     b_num = 0
#     for i_i in f_f:
#         b_num += 1
#         if b_num % 1000000 == 0:
#             print(b_num)
#         data_1 = i_i.strip().split(",")
#         b_name_id = data_1[0]
#         shop_data[b_name_id] = data_1
def smt_updta():
    shop_data = {}
    with open(r"W:\scrapy_chai\smt\smt_goodsinfo_202106_duoyu.txt", "r", encoding="utf-8") as f_f:
        b_num = 0
        for i_i in f_f:
            b_num += 1
            if b_num % 1000000 == 0:
                print(b_num)
            data_1 = i_i.strip().split(",")
            goods_id_id = data_1[3]
            shop_data[goods_id_id] = data_1
    file_write = open(r"W:\scrapy_chai\smt_goodsinfo_202106_new.txt", "a", encoding="utf-8")
    with open(r"W:\scrapy_chai\smt\smt_goodsinfo_202106_quchong.txt", "r", encoding="utf-8") as f:
        num = 0
        for i in f:
            try:
                num += 1
                data = i.strip().split(",")
                goods_id = data[3]
                quchong_data = shop_data.get(goods_id)
                if quchong_data is not None:
                    file_write.write(",".join(quchong_data) + "\n")
                else:
                    file_write.write(",".join(data) + "\n")
                if num % 1000000 == 0:
                    print(num)
                    file_write.flush()
            except Exception as e:
                print(e)

if __name__ == "__main__":
    smt_updta()
