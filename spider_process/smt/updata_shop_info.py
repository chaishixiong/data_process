shop_pf_dict = dict()
smt_compan_dict = dict()
smt_sales_money_dict = dict()

with open(r'X:\数据库\速卖通\{3_1_1_字典_速卖通_月统计}[店铺id,sum(销量 米 商品价格_较高值),sum(销量)].txt', 'r', encoding='utf-8') as smt_shop_sm:
    for shop_sm in smt_shop_sm:
        shop_sn_list = shop_sm.strip('\n').split(',')
        smt_sales_money_dict[shop_sn_list[0]] = shop_sn_list

with open(r'X:\数据库\速卖通\202211\{2_1_速卖通_有效_店铺评分}[店铺ID,卖家ID,店铺名称,粉丝数,店铺地址,开店时间].txt', 'r', encoding='utf-8') as smt_shop_pf:
    for shop_pf in smt_shop_pf:
        shop_pf_list = shop_pf.strip('\n').split(',')
        shop_pf_dict[shop_pf_list[0]] = shop_pf_list


with open(r'X:\数据库\速卖通\{速卖通牌照信息_上月}[店铺ID,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区].txt', 'r', encoding='utf-8') as smt_compan_sy:
    for sy_compan in smt_compan_sy:
        compan_sy_list = sy_compan.strip('\n').split(',')
        smt_compan_dict[compan_sy_list[0]] = compan_sy_list


with open(r'X:\数据库\速卖通\{速卖通牌照信息_本月}[店铺ID,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区].txt', 'r', encoding='utf-8') as smt_compan_by:
    for by_compan in smt_compan_by:
        compan_by_list = by_compan.strip('\n').split(',')
        smt_compan_dict[compan_by_list[0]] = compan_by_list


shopinfo_w = open(r'X:\数据库\速卖通\{smt_shopinfo_202301}[店铺ID,卖家ID,店铺名称,营业地址,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区,销量,销售额,粉丝数,店铺地址,开店时间,浙江地区当月销量].txt', 'w', encoding='utf-8')

with open(r'X:\数据库\速卖通\{smt_shopinfo_202301_备份}[店铺ID,卖家ID,店铺名称,营业地址,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区,销量,销售额,粉丝数,店铺地址,开店时间,浙江地区当月销量].txt', 'r', encoding='utf-8') as smt_shopinfo_bf:
    for shopinfo in smt_shopinfo_bf:
        shopinfo_list = shopinfo.strip('\n').split(',')
        shop_id = shopinfo_list[0]
        shop_pf = shop_pf_dict.get(shop_id, ['', '', '', '', '', ''])
        shop__sm = smt_sales_money_dict.get(shop_id, ['', '', ''])
        shop_compan = smt_compan_dict.get(shop_id, ['', '', '', '' '', '', '' '', '', '', '', '', '' '', '', '' '', '', ''])
        shopinfo_list[-1] = shop__sm[1]
        shopinfo_list[-5] = shop__sm[1]
        shopinfo_list[-6] = shop__sm[2]
        shopinfo_list[2] = shop_pf[2]
        shopinfo_list[17] = shop_pf[3]
        shopinfo_list[18] = shop_pf[4]
        shopinfo_list[19] = shop_pf[5]
        shopinfo_list[5] = shop_compan[2]
        shopinfo_list[6] = shop_compan[3]
        shopinfo_list[7] = shop_compan[4]
        shopinfo_list[8] = shop_compan[5]
        shopinfo_list[9] = shop_compan[6]
        shopinfo_list[10] = shop_compan[7]
        shopinfo_list[11] = shop_compan[8]
        shopinfo_list[12] = shop_compan[9]
        shopinfo_list[13] = shop_compan[10]
        shopinfo_list[14] = shop_compan[11]
        shopinfo_w.write(','.join(shopinfo_list) + '\n')
        shopinfo_w.flush()
    shopinfo_w.close()







