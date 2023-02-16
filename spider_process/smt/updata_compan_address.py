data_w = open(r'X:\数据库\速卖通\{速卖通牌照信息_本月}[店铺ID,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区].txt', 'w', encoding='utf-8')
company_cross_dict = {}
with open(r'X:\数据库\速卖通\{company_cross}[公司名称,省,市,区].txt', 'r', encoding='utf-8') as company_cross_r:
    for company in company_cross_r:
        company_list = company.strip('\n').split(',')
        company_cross_dict[company_list[0]] = company_list
with open(r'X:\数据库\速卖通\{速卖通牌照信息_本月_备份}[店铺ID,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区].txt', 'r', encoding='utf-8') as data_r:
    for data in data_r:
        data_list = data.split(',')
        company_name = data_list[1]
        company_data = company_cross_dict.get(company_name)
        if company_data:
            data_list[9] = company_data[1]
            data_list[10] = company_data[2]
            data_list[11] = company_data[3]
            data_w.write(','.join(data_list) + '\n')
        else:
            data_w.write(data)
            data_w.flush()
    data_w.close()
