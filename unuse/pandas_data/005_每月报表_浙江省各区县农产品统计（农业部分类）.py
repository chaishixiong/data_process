# coding=utf-8

import os
import pymysql
import datetime
import xlsxwriter
from utility_date import *
from utility_addr import *
from utility_excp import *
from utility_ecpt import *

# 提取数据

# 农业部农产品类目集合
print('提示:假如统计2020年3月的，输入 202003 即可')
date_time = int(input('请输入日期:'))

pr = '浙江省'
ec_list = ['tmall', 'taobao']
ym_list = cdate.get_ym_list(202001, date_time)

dr = './输入数据/农产品类目对照表'
fr_name = '农产品类目对照表（农业部）.csv'
fr = open('{}/{}'.format(dr, fr_name))
cid_set = set()
for line in fr:
    cid = line.split(',')[1]
    cid_set.add(cid)
fr.close()

dw = './提取数据/浙江省天猫及淘宝企业店农产品商品数据（按农业部标准）'
for ec in ec_list:
    for ym in ym_list:
        print(ec, ym)
        if ec == 'taobao':
            fw_name = '{}_qiye_farm_goodsinfo_{}.csv'.format(ec, ym)
        else:
            fw_name = '{}_farm_goodsinfo_{}.csv'.format(ec, ym)
        if os.path.exists('{}/{}'.format(dw, fw_name)):
            print('{}/{}文件已存在，如需覆盖，请删除原文件后，再重新运行程序。'.format(dw, fw_name))
        else:
            # 提取浙江省店铺集合
            conn = pymysql.connect(
                host='192.168.0.228',
                user='dev',
                passwd='Data227or8Dev715#',
                port=3306,
                db='e_commerce',
                charset='utf8',
                cursorclass=pymysql.cursors.SSCursor
            )
            curs = conn.cursor()

            if ec == 'taobao':
                database = '{}_qiye_shopinfo_{}'.format(ec, ym)
            else:
                database = '{}_shopinfo_{}'.format(ec, ym)

            sql_query = 'select shop_id, province, city, county from {} where province = "{}" group by shop_id '
            sql_query = sql_query.format(database, pr)
            curs.execute(sql_query)

            sid_addrs = {}
            for shop_infos in curs:
                sid, prov, city, cnty = shop_infos
                prov, city, cnty = caddr.get_b2c_prov_city_cnty(prov, city, cnty)
                if not cexcp.shop_is_valid(ec, sid, prov, city, cnty):
                    print('     无效网店：', sid, prov, city, cnty)
                else:
                    sid_addrs[sid] = [prov, city, cnty]

            curs.close()
            conn.close()

            # 根据店铺集合和农产品类目集合提取农产品商品数据

            conn = pymysql.connect(
                host='192.168.0.227',
                port=3306,
                user='dev',
                password='Data227or8Dev715#',
                charset='utf8',
                db='oridata_{}'.format(ec),
                cursorclass=pymysql.cursors.SSCursor
            )
            curs = conn.cursor()

            start = datetime.datetime.now()

            database = '{}_goodsmobile_{}'.format(ec, ym)

            sql_query = 'select shop_id, cid, discount_price, sales_month from {} group by shop_id '.format(database)
            curs.execute(sql_query)
            fw = open('{}/{}'.format(dw, fw_name), 'w', encoding='utf-8')
            fw.write('shop_id,cid,price,sales_num,province,city,county\n')
            n = 0
            for res in curs:
                if n % 1000000 == 0:
                    print(datetime.datetime.now(), ec, ym,
                          '已处理', n // 10000, '万记录 用时: ',
                          datetime.datetime.now() - start)
                n += 1

                sid, cid, price, sales_num = res
                if (sid in sid_addrs.keys()) and (cid in cid_set):
                    try:
                        price = float(price)
                        sales_num = int(sales_num)
                        prov, city, cnty = sid_addrs[sid]
                        fw.write('{},{},{},{},{},{},{}\n'.format(sid, cid, price, sales_num, prov, city, cnty))
                    except:
                        pass
            fw.close()

            curs.close()
            conn.close()

ts = '单月销售额'
tt = '累计销售额'
ta = '活跃店铺数'
tr = '注册店铺数'
st_list = [ts, tt, ta, tr]
city_list = caddr.prov_city[pr]
ec_list = ['tmall', 'taobao_qiye']

cnty_farm_prod = {}
for ym in ym_list:
    cnty_farm_prod[ym] = {}
    for city in city_list:
        cnty_farm_prod[ym][city] = {}
        for cnty in caddr.prov_city_cnty[pr][city]:
            cnty_farm_prod[ym][city][cnty] = {}
            for st in st_list:
                cnty_farm_prod[ym][city][cnty][st] = 0

dr = './提取数据/浙江省天猫及淘宝企业店农产品商品数据（按农业部标准）'
for ec in ec_list:
    for ym in ym_list:
        print(ym, ec)
        fr_name = '{}_farm_goodsinfo_{}.csv'.format(ec, ym)
        fr = open('{}/{}'.format(dr, fr_name), encoding='utf-8')
        fr.readline()
        for line in fr:
            sid, cid, price, num, prov, city, cnty = line.strip().split(',')
            sales = float(price) * int(num)

            cnty_farm_prod[ym][city][cnty][tr] += 1
            if sales > 0:
                cnty_farm_prod[ym][city][cnty][ts] += sales
                cnty_farm_prod[ym][city][cnty][ta] += 1
        fr.close()



# 计算月累计数据
for city in city_list:
    for cnty in caddr.prov_city_cnty[pr][city]:
        for i in range(len(ym_list)):
            ym = ym_list[i]
            cnty_farm_prod[ym][city][cnty][tt] = sum(cnty_farm_prod[ym][city][cnty][ts]
                                                     for ym in ym_list[: i + 1])

# 生成报表
if len(ym_list) == 1:
    ym_range = cdate.get_ym_cn(ym_list[0])
else:
    ym_begin = cdate.get_ym_cn(ym_list[0])
    ym_end = cdate.get_ym_cn(ym_list[-1])
    ym_range = '{}-{}'.format(ym_begin, ym_end)

dw = './输出结果/浙江省商务厅电商统计报表（{}）/{}{}各区县农产品网络销售统计（农业部分类）'.format(cdate.get_ym_cn(ym), pr, ym_range)
if not os.path.exists(dw):
    os.makedirs(dw)


ec_cn_list = [cecpt.en_cn[ec] for ec in ec_list]
for st in st_list:
    fw_name = '{}/{}各区县农产品{}{}({}).xlsx'
    fw_name = fw_name.format(dw, pr, st, ym_range, '+'.join(ec_cn_list))

    workbook = xlsxwriter.Workbook(fw_name)
    worksheet = workbook.add_worksheet(st)
    percent_format = workbook.add_format({'num_format': '0.00"%"'})

    # 表头
    row = 0
    col = 0
    worksheet.write(row, col, '地市')

    col += 1
    worksheet.write(row, col, '区县')

    for ym in ym_list:
        ym_cn = cdate.get_ym_cn(ym)
        col += 1
        worksheet.write(row, col, ym_cn + st)
        col += 1
        worksheet.write(row, col, ym_cn + st + '全省占比')

    row = 0
    for city in city_list:
        for cnty in caddr.prov_city_cnty[pr][city]:
            row += 1
            col = 0
            worksheet.write(row, col, city)
            col += 1
            worksheet.write(row, col, cnty)

            for ym in ym_list:
                col += 1
                worksheet.write(row, col, cnty_farm_prod[ym][city][cnty][st])
                col += 1
                cnty_sum = sum(cnty_farm_prod[ym][city][cnty][st]
                               for city in city_list
                               for cnty in caddr.prov_city_cnty[pr][city])
                if cnty_sum == 0:
                    cnty_per = 0.00
                else:
                    cnty_per = round(cnty_farm_prod[ym][city][cnty][st]/cnty_sum*100, 2)
                worksheet.write(row, col, cnty_per, percent_format)

    row += 1
    col = 1
    worksheet.write(row, col, '汇总')
    merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
    worksheet.merge_range(row, 0, row, 1, '汇总', merge_format)
    for ym in ym_list:
        col += 1
        ym_sum = sum(cnty_farm_prod[ym][city][cnty][st]
                     for city in city_list
                     for cnty in caddr.prov_city_cnty[pr][city])
        worksheet.write(row, col, ym_sum)
        col += 1
        worksheet.write(row, col, 100, percent_format)

    workbook.close()






















































