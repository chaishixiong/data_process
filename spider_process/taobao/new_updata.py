#  618 数据和当月数据合并
def tmall_618tmall():
    b_name = {}
    with open(
            r"X:\数据库\taobao\updata\{tmall_goodsmobile_202106}[采集时间,商品ID,近似销量,月销量,评论数,总库存,收藏量,发货地址,类目ID,品牌ID,平台,商品名称,卖家ID,店铺ID,促销名称,促销价,定金,定金描述,原价名称,原价,配送费用,商品保证,网店推广,推广描述,商品积分,主图,商品属性].txt",
            "r", encoding="utf-8") as f_f:
        b_num = 0
        for i_i in f_f:
            b_num += 1
            if b_num % 1000000 == 0:
                print(b_num)
            data_1 = i_i.strip().split(",")
            b_name_id = data_1[1]
            b_name[b_name_id] = '2'

    file_write = open(r"X:\数据库\taobao\updata\goods_tmall_202106_new_new.txt", "a", encoding="utf-8")
    with open(r"X:\数据库\taobao\updata\tmall_goodsmobile_618_202102.txt", "r", encoding="utf-8") as f:
        b_type = "B"
        goods_list = {}
        num = 0
        for i in f:
            try:
                num += 1
                data = i.strip().split(",")
                goods_id = data[1]
                zhuangtai = b_name.get(goods_id)
                if zhuangtai == None:
                    write_data_2 = [""] * 27
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
                    if num % 1000000 == 0:
                        print(num)
                        file_write.flush()
                    if write_data_2[15] == '':
                        print(id)
                        file_write.flush()
            except Exception as e:
                print(e)


#  更新天猫店铺信息

def tmall_shopinfo_updata():
    shop_data = {}
    with open(r"X:\数据库\taobao\updata\tmall_shopinfo_202105.txt", "r", encoding="utf-8") as f_f:
        b_num = 0
        for i_i in f_f:
            b_num += 1
            if b_num % 1000000 == 0:
                print(b_num)
            data_1 = i_i.strip().split(",")
            b_name_id = data_1[0]
            shop_data[b_name_id] = data_1


    file_write = open(r"X:\数据库\taobao\updata\tmall_shopinfo_202106_new_new.txt", "a", encoding="utf-8")
    with open(r"X:\数据库\taobao\{tmall_shopinfo_202106_new}[店铺ID,卖家ID,平台,主营,公司名称,月销售量,月销售额,发货地址,卖家用户名,卖家等级,店铺好评率,店铺名称,微淘ID,店铺粉丝,开店时间,商品数量,上新数量,关注人数,保证金,店铺图片,金牌店铺,店铺类型,店铺URL,天猫省,天猫市,客服电话,电话分机,店铺类型2,店铺年龄,店铺类型3,加密旺旺,工商xid].txt", "r", encoding="utf-8") as f:
        b_type = "B"
        goods_list = []
        num = 0
        for i in f:
            try:
                num += 1
                data = i.strip().split(",")
                goods_id = data[0]
                zhuangtai = shop_data.get(goods_id)
                if zhuangtai != None:
                    write_data = [""] * 32
                    write_data[0] = data[0] # shop_id
                    write_data[1] = data[1]  # seller_id
                    write_data[2] = data[2]  # bc_type
                    write_data[3] = data[3]  # main_sale
                    write_data[4] = data[4]  # company
                    write_data[5] = data[5]  # sales_count
                    write_data[6] = data[6]  # sales_money
                    write_data[7] = data[7]  # address
                    write_data[8] = zhuangtai[8]  # seller_name
                    write_data[9] = zhuangtai[9]  # seller_lv
                    write_data[10] = zhuangtai[10]  # shop_hpl
                    write_data[11] = zhuangtai[11]  # shop_name
                    write_data[12] = data[12]  # weitao_id
                    write_data[13] = zhuangtai[13]  # shop_fans_num
                    write_data[14] = zhuangtai[14]  # open_shop_date
                    write_data[16] = zhuangtai[15]  # goods_num
                    '''seller_name,seller_lv,shop_hpl,shop_name,shop_fans_num,open_shop_date,goods_num,
                    new_goods_num,shop_url,tmall_province,tmall_city,tmall_shop_type2,shop_age,tmall_shop_type3,ww_jm,xid'''
                    write_data[16] = zhuangtai[16]  # new_goods_num
                    write_data[17] = data[17]  # guanzhu_num
                    write_data[18] = data[18]  # shop_money
                    write_data[19] = zhuangtai[19]  # shop_iocn
                    write_data[20] = data[20]  # gold_shop
                    write_data[21] = data[21]  # shop_type
                    write_data[22] = zhuangtai[22]  # shop_url
                    write_data[23] = zhuangtai[23]  # tmall_province
                    write_data[24] = zhuangtai[24]  # tmall_city
                    write_data[25] = data[25]  # phone
                    write_data[26] = data[26]  # tel
                    write_data[27] = zhuangtai[26]  # shop_type2
                    write_data[28] = zhuangtai[27]  # shop_age
                    write_data[29] = zhuangtai[28]  # tmall_shop_type3
                    write_data[30] = zhuangtai[29]  # ww_jm
                    write_data[31] = zhuangtai[30]  # xid
                    file_write.write(",".join(write_data)+"\n")
                else:
                    file_write.write(",".join(data) + "\n")
                if num % 1000000 == 0:
                    print(num)
                    file_write.flush()
            except Exception as e:
                print(e)

def updata_smt_shop_name():
    shop_data = {}
    with open(r"X:\数据库\速卖通\new_goods\smt_shopinfo_202104.txt", "r", encoding="utf-8") as f_f:
        b_num = 0
        for i_i in f_f:
            b_num += 1
            if b_num % 1000000 == 0:
                print(b_num)
            data_1 = i_i.strip().split(",")
            b_name_id = data_1[0]
            shop_data[b_name_id] = data_1[1]
    num = 0
    file_write = open(r"X:\数据库\速卖通\new_goods\smt_shopinfo_202106_new.txt", "a", encoding="utf-8")
    with open(r"X:\数据库\速卖通\new_goods\{smt_shopinfo_202106}[店铺ID,卖家ID,店铺名称,营业地址,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区,销量,销售额,粉丝数,店铺地址,开店时间,浙江地区当月销量].txt", "r", encoding="utf-8") as f:
        for i in f:
            try:
                num += 1
                data = i.strip().split(",")
                new_shop_name = data[0]
                shop_name = shop_data.get(new_shop_name)
                if shop_name != None:
                    data[2] = shop_name
                    file_write.write(",".join(data) + "\n")
                else:
                    file_write.write(",".join(data) + "\n")
                if num % 1000000 == 0:
                    print(num)
                    file_write.flush()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    updata_smt_shop_name()
