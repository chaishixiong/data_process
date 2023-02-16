# coding=utf-8

import os
import pymysql
import xlsxwriter
from utility_ecpt import *
from utility_addr import *
from utility_cate import *
from utility_excp import *
from utility_func import *
from utility_date import *

print('提示:假如统计2020年3月的，输入 202003 即可')
date_time = str(input('请输入日期:'))



def run(date_time):
    pr_list = ['浙江省']
    ym_list = cdate.get_ym_list(date_time)
    all_ec_list = cecpt.all_ec_list.copy()
    ec_list = cecpt.new_ec_list.copy()
    b2c_list = cecpt.new_b2c_list.copy()
    old_b2c_list = b2c_list.copy()
    old_b2c_list.remove('taobao_qiye')

    taobao_geti = 'taobao_geti'
    taobao_qiye = 'taobao_qiye'
    taobao_list = [taobao_geti, taobao_qiye]

    ts = '月销售额'
    ta = '活跃店铺数'
    tr = '注册店铺数'
    st_list = [ta, tr, ts]
    qj = '旗舰店店铺数'
    zy = '专营店店铺数'
    zm = '专卖店店铺数'
    tmall_st_list = [ta, tr, ts, qj, zy, zm]
    conn = pymysql.connect(
        host='192.168.0.228',
        user='dev',
        passwd='Data227or8Dev715#',
        port=3306,
        charset='utf8',
        cursorclass=pymysql.cursors.SSCursor
    )
    curs = conn.cursor()

    for pr in pr_list:
        for ym in ym_list:
            ec_city = {}
            for ec in ec_list:
                ec_city[ec] = {}
                for city in caddr.prov_city[pr]:
                    ec_city[ec][city] = {}
                    if ec == 'tmall':
                        for st in tmall_st_list:
                            ec_city[ec][city][st] = 0
                    else:
                        for st in st_list:
                            ec_city[ec][city][st] = 0

            ec_city_cate = {}
            for ec in ec_list:
                ec_city_cate[ec] = {}
                for city in caddr.prov_city[pr]:
                    ec_city_cate[ec][city] = {}
                    for cate in ccate.cate_list:
                        ec_city_cate[ec][city][cate] = {}
                        for st in st_list:
                            ec_city_cate[ec][city][cate][st] = 0

            ec_city_cnty = {}
            for ec in ec_list:
                ec_city_cnty[ec] = {}
                for city in caddr.prov_city[pr]:
                    ec_city_cnty[ec][city] = {}
                    for cnty in caddr.prov_city_cnty[pr][city]:
                        ec_city_cnty[ec][city][cnty] = {}
                        if ec == 'tmall':
                            for st in tmall_st_list:
                                ec_city_cnty[ec][city][cnty][st] = 0
                        else:
                            for st in st_list:
                                ec_city_cnty[ec][city][cnty][st] = 0

            ec_city_cnty_cate = {}
            for ec in ec_list:
                ec_city_cnty_cate[ec] = {}
                for city in caddr.prov_city[pr]:
                    ec_city_cnty_cate[ec][city] = {}
                    for cnty in caddr.prov_city_cnty[pr][city]:
                        ec_city_cnty_cate[ec][city][cnty] = {}
                        for cate in ccate.cate_list:
                            ec_city_cnty_cate[ec][city][cnty][cate] = {}
                            for st in st_list:
                                ec_city_cnty_cate[ec][city][cnty][cate][st] = 0

            # 读取的mysql数据库
            database = 'e_commerce'

            qiye_sid_set = set()
            ec = 'taobao_qiye'
            print('提取淘宝企业店信息')

            table = '{}.{}_shopinfo_{}'.format(database, ec, ym)
            sql_select = 'select shop_id, main_sale, sales_money, '
            sql_select += 'province, city, county from {} group by shop_id'
            sql_select = sql_select.format(table)

            curs.execute(sql_select)
            for shop_infos in curs:
                shop_id, cate, sale, prov_ori, city_ori, cnty_ori = shop_infos
                if prov_ori in caddr.prov_simple_dict.keys():
                    prov_ori = caddr.prov_simple_dict[prov_ori]
                prov, city, cnty = caddr.get_b2c_prov_city_cnty(prov_ori, city_ori, cnty_ori)
                sale = get_ec_round_sale(ec, sale)
                cate = ccate.get_ec_cate_norm(ec, cate)

                if not cexcp.shop_is_valid(ec, shop_id, prov, city, cnty):
                    prov, city, cnty = caddr.get_b2c_munipalicity_norm(prov_ori, city_ori, cnty_ori)

                if not cexcp.shop_is_valid(ec, shop_id, prov, city, cnty):
                    if prov_ori != '' and prov_ori is not None:
                        print('     无效网店：', ec, ym, shop_infos)
                else:
                    qiye_sid_set.add(shop_id)

            ec = 'taobao'
            print('统计{}数据：'.format(cecpt.en_cn[taobao_geti]), ym, ec)
            table = '{}.{}_shopinfo_{}'.format(database, ec, ym)
            sql_select = 'select shop_id, address, main_sale, sales_money from {} group by shop_id '
            sql_select = sql_select.format(table)

            curs.execute(sql_select)
            for shop_infos in curs:
                shop_id, addr, cate, sale = shop_infos

                if shop_id not in qiye_sid_set:
                    prov, city = caddr.get_tb_norm_prov_city(addr)
                    sale = get_ec_round_sale(ec, sale)
                    cate = ccate.get_ec_cate_norm(ec, cate)

                    if prov == pr:
                        if not cexcp.shop_is_valid(ec, shop_id, prov, city):
                            print('     无效网店：', shop_id, sale, cate, prov, city)
                        else:
                            ec_city[taobao_geti][city][tr] += 1
                            ec_city_cate[taobao_geti][city][cate][tr] += 1

                            if sale > 0:
                                ec_city[taobao_geti][city][ta] += 1
                                ec_city_cate[taobao_geti][city][cate][ta] += 1

                                ec_city[taobao_geti][city][ts] += sale
                                ec_city_cate[taobao_geti][city][cate][ts] += sale

            for ec in b2c_list:
                print('统计{}数据：'.format(cecpt.en_cn[ec]), pr, ym, ec)
                if ec == 'tmall':
                    sql_select = 'select shop_id, main_sale, sales_money,tmall_shop_type3,'
                else:
                    sql_select = 'select shop_id, main_sale, sales_money, '
                table = '{}.{}_shopinfo_{}'.format(database, ec, ym)
                sql_select += 'province, city, county '
                sql_select += 'from {} where province = "{}" group by shop_id '
                sql_select = sql_select.format(table, pr)

                curs.execute(sql_select)
                for shop_infos in curs:
                    if ec == 'tmall':
                        shop_id, cate, sale, tmall_shop_type3, prov, city, cnty, = shop_infos
                    else:
                        shop_id, cate, sale, prov, city, cnty = shop_infos
                    prov, city, cnty = caddr.get_b2c_prov_city_cnty(prov, city, cnty)
                    sale = get_ec_round_sale(ec, sale)
                    cate = ccate.get_ec_cate_norm(ec, cate)
                    if not cexcp.shop_is_valid(ec, shop_id, prov, city, cnty):
                        print('     无效网店：', shop_id, sale, cate, prov, city, cnty)
                    else:
                        ec_city[ec][city][tr] += 1
                        ec_city_cate[ec][city][cate][tr] += 1
                        ec_city_cnty[ec][city][cnty][tr] += 1
                        ec_city_cnty_cate[ec][city][cnty][cate][tr] += 1
                        # 判断活跃店铺,销售额大于0的则为活跃店铺
                        if sale > 0:
                            ec_city[ec][city][ta] += 1
                            ec_city_cate[ec][city][cate][ta] += 1
                            ec_city_cnty[ec][city][cnty][ta] += 1
                            ec_city_cnty_cate[ec][city][cnty][cate][ta] += 1

                            ec_city[ec][city][ts] += sale
                            ec_city_cate[ec][city][cate][ts] += sale
                            ec_city_cnty[ec][city][cnty][ts] += sale
                            ec_city_cnty_cate[ec][city][cnty][cate][ts] += sale
                        if ec == 'tmall':
                            # 统计天猫不同类型店铺数量
                            if tmall_shop_type3 == '旗舰店':
                                ec_city[ec][city][qj] += 1
                                ec_city_cnty[ec][city][cnty][qj] += 1
                            elif tmall_shop_type3 == '专营店':
                                ec_city[ec][city][zy] += 1
                                ec_city_cnty[ec][city][cnty][zy] += 1
                            elif tmall_shop_type3 == '专卖店':
                                ec_city[ec][city][zm] += 1
                                ec_city_cnty[ec][city][cnty][zm] += 1

            # 根据淘宝地市级销售额与其他B2C平台的相关性计算淘宝区县级销售额
            print('根据B2C平台区县级销售划分淘宝个人店销售额到区县级')

            fst = ta
            c2c = 'taobao_geti'
            city_list = caddr.prov_city[pr]

            #  计算淘宝与其它平台地市级活跃店铺数的相关性权重
            c2c_city = [ec_city[c2c][city][fst] for city in city_list]
            b2c_city = {}
            for b2c in b2c_list:
                b2c_city[b2c] = [ec_city[b2c][city][fst] for city in city_list]

            cor_lst = [get_lists_pearson(c2c_city, b2c_city[b2c]) for b2c in b2c_list]
            cor_lst = [cor if cor >= 0 else 0 for cor in cor_lst]
            cor_sum = sum(cor_lst)
            cor_wgt = [cor / cor_sum
                       if cor_sum > 0
                       else 1 / len(cor_lst)
                       for cor in cor_lst]

            # 计算各B2C平台活跃店铺数量权重
            num_lst = [sum(ec_city[b2c][city][fst] for city in city_list)
                       for b2c in b2c_list]
            num_sum = sum(num_lst)
            num_wgt = [num / num_sum
                       if num_sum > 0
                       else 1 / len(num_lst)
                       for num in num_lst]

            # 计算相关性和活跃店铺数量的混合权重
            mix_lst = [cor * num for cor, num in zip(cor_wgt, num_wgt)]
            mix_sum = sum(mix_lst)
            mix_wgt = [mix / mix_sum
                       if mix_sum > 0
                       else 1 / len(mix_lst)
                       for mix in mix_lst]

            # 根据权重把淘宝地市级销售额及店铺数量分配到各个区县
            random.seed(int(ym))
            for city in city_list:
                cnty_list = caddr.prov_city_cnty[pr][city]

                b2c_prop = []
                for cnty in cnty_list:
                    b2c_cnty_fst = [ec_city_cnty[b2c][city][cnty][fst] / ec_city[b2c][city][fst]
                                    if ec_city[b2c][city][fst] > 0
                                    else 1 / len(cnty_list)
                                    for b2c in b2c_list]
                    b2c_prop.append(sum(w * e for w, e in zip(mix_wgt, b2c_cnty_fst)))

                for st in st_list:
                    c2c_sum = ec_city[c2c][city][st]
                    c2c_list = distributed_by_prop(c2c_sum, b2c_prop)
                    c2c_dict = dict(zip(cnty_list, c2c_list))

                    for cnty in cnty_list:
                        ec_city_cnty[c2c][city][cnty][st] = c2c_dict[cnty]

            # ------------------------------------分地区统计-------------------------------------------------
            # ---------------------------------各地市统计----------------------------------------------
            # 生成统计报表
            dw_top = './输出结果/浙江省商务厅电商统计报表（{0}）/{1}{0}电商数据统计'.format(cdate.get_ym_cn(ym), pr)
            if not os.path.exists(dw_top):
                os.makedirs(dw_top)

            dw = '{}/分地区统计'.format(dw_top)
            if not os.path.exists(dw):
                os.makedirs(dw)

            fw_name = '{}/各地市统计({}).xlsx'.format(dw, cdate.get_ym_cn(ym))

            # 表头
            workbook = xlsxwriter.Workbook(fw_name)
            merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
            worksheet = workbook.add_worksheet('各地市统计')

            worksheet.merge_range(0, 0, 2, 0, '地市', merge_format)

            row = 0
            col = 1
            ec = 'taobao'
            worksheet.merge_range(row, col, row, col + 5, cecpt.en_cn[ec], merge_format)

            col = 1
            for ec in taobao_list:
                row = 1
                worksheet.merge_range(row, col, row, col + 2, cecpt.en_cn[ec], merge_format)
                row = 2
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                col += 3

            col = 7
            for ec in old_b2c_list:
                row = 0
                if ec == 'tmall':
                    worksheet.merge_range(row, col, row + 1, col + 5, cecpt.en_cn[ec], merge_format)
                else:
                    worksheet.merge_range(row, col, row + 1, col + 2, cecpt.en_cn[ec], merge_format)
                row = 2
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                if ec == 'tmall':
                    worksheet.write(row, col + 3, '旗舰店店铺数')
                    worksheet.write(row, col + 4, '专营店店铺数')
                    worksheet.write(row, col + 5, '专卖店店铺数')
                    col += 3
                col += 3
            row = 0
            worksheet.merge_range(row, col, row + 1, col + 2, '汇总', merge_format)
            row = 2
            for st in st_list:
                worksheet.write(row, col, st)
                col += 1

            # 表内容

            row = 3
            col = 0
            for city in caddr.prov_city[pr]:
                worksheet.write(row, col, city)
                col += 1
                for ec in ec_list:
                    if ec == 'tmall':
                        for st in tmall_st_list:
                            worksheet.write(row, col, ec_city[ec][city][st])
                            col += 1
                    else:
                        for st in st_list:
                            worksheet.write(row, col, ec_city[ec][city][st])
                            col += 1

                # 汇总各个地市全平台数据
                for st in st_list:
                    city_st_sum = sum(ec_city[ec][city][st] for ec in ec_list)
                    worksheet.write(row, col, city_st_sum)
                    col += 1

                row += 1
                col = 0

            # 汇总各个平台全省数据
            worksheet.write(row, col, '汇总')
            col = 1
            # 遍历平台
            for ec in ec_list:
                if ec == 'tmall':
                    for st in tmall_st_list:
                        ec_st_sum = sum(ec_city[ec][city][st]
                                        for city in caddr.prov_city[pr])
                        worksheet.write(row, col, ec_st_sum)
                        col += 1
                else:
                    for st in st_list:
                        ec_st_sum = sum(ec_city[ec][city][st]
                                        for city in caddr.prov_city[pr])
                        worksheet.write(row, col, ec_st_sum)
                        col += 1

            # 总汇总
            for st in st_list:
                st_sum = sum(ec_city[ec][city][st] for ec in ec_list for city in caddr.prov_city[pr])
                worksheet.write(row, col, st_sum)
                col += 1

            workbook.close()

            # ------------------------------------各地市分区县统计------------------------------------
            fw_name = '{}/各地市分区县统计({}).xlsx'.format(dw, cdate.get_ym_cn(ym))

            # 表头
            workbook = xlsxwriter.Workbook(fw_name)
            merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
            worksheet = workbook.add_worksheet('各地市分区县统计')

            worksheet.merge_range(0, 0, 2, 0, '地市', merge_format)
            worksheet.merge_range(0, 1, 2, 1, '区县', merge_format)

            row = 0
            col = 2
            ec = 'taobao'
            worksheet.merge_range(row, col, row, col + 5, cecpt.en_cn[ec], merge_format)

            col = 2
            for ec in taobao_list:
                row = 1
                worksheet.merge_range(row, col, row, col + 2, cecpt.en_cn[ec], merge_format)
                row = 2
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                col += 3

            col = 8
            for ec in old_b2c_list:
                row = 0
                if ec == 'tmall':
                    worksheet.merge_range(row, col, row + 1, col + 5, cecpt.en_cn[ec], merge_format)
                else:
                    worksheet.merge_range(row, col, row + 1, col + 2, cecpt.en_cn[ec], merge_format)
                row = 2
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                if ec == 'tmall':
                    worksheet.write(row, col + 3, '旗舰店店铺数')
                    worksheet.write(row, col + 4, '专营店店铺数')
                    worksheet.write(row, col + 5, '专卖店店铺数')
                    col += 3
                col += 3
            row = 0
            worksheet.merge_range(row, col, row + 1, col + 2, '汇总', merge_format)
            row = 2
            for st in st_list:
                worksheet.write(row, col, st)
                col += 1

            # 表内容

            row = 3
            col = 0

            for city in caddr.prov_city[pr]:
                for cnty in caddr.prov_city_cnty[pr][city]:
                    worksheet.write(row, col, city)
                    worksheet.write(row, col + 1, cnty)
                    col += 2
                    for ec in ec_list:
                        if ec == 'tmall':
                            for st in tmall_st_list:
                                worksheet.write(row, col, ec_city_cnty[ec][city][cnty][st])
                                col += 1
                        else:
                            for st in st_list:
                                worksheet.write(row, col, ec_city_cnty[ec][city][cnty][st])
                                col += 1

                    # 汇总各个区县全平台数据
                    for st in st_list:
                        cnty_st_sum = sum(ec_city_cnty[ec][city][cnty][st] for ec in ec_list)
                        worksheet.write(row, col, cnty_st_sum)
                        col += 1

                    row += 1
                    col = 0

            # 汇总各个平台全省数据
            worksheet.merge_range(row, col, row, col + 1, '汇总', merge_format)
            col = 2
            for ec in ec_list:
                if ec == 'tmall':
                    for st in tmall_st_list:
                        ec_st_sum = sum(ec_city_cnty[ec][city][cnty][st]
                                        for city in caddr.prov_city[pr]
                                        for cnty in caddr.prov_city_cnty[pr][city])
                        worksheet.write(row, col, ec_st_sum)
                        col += 1
                else:
                    for st in st_list:
                        ec_st_sum = sum(ec_city_cnty[ec][city][cnty][st]
                                        for city in caddr.prov_city[pr]
                                        for cnty in caddr.prov_city_cnty[pr][city])
                        worksheet.write(row, col, ec_st_sum)
                        col += 1

            # 总汇总
            for st in st_list:
                st_sum = sum(ec_city_cnty[ec][city][cnty][st]
                             for ec in ec_list
                             for city in caddr.prov_city[pr]
                             for cnty in caddr.prov_city_cnty[pr][city])
                worksheet.write(row, col, st_sum)
                col += 1

            workbook.close()

            # ---------------------------------分行业统计------------------------------------------------------------
            # ---------------------------------各行业统计--------------------------------------
            dw = '{}/分行业统计'.format(dw_top)
            if not os.path.exists(dw):
                os.makedirs(dw)

            fw_name = '{}/各行业统计({}).xlsx'.format(dw, cdate.get_ym_cn(ym))

            # 表头
            workbook = xlsxwriter.Workbook(fw_name)
            merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
            worksheet = workbook.add_worksheet('各行业统计')

            worksheet.merge_range(0, 0, 2, 0, '行业', merge_format)

            row = 0
            col = 1
            ec = 'taobao'
            worksheet.merge_range(row, col, row, col + 5, cecpt.en_cn[ec], merge_format)

            col = 1
            for ec in taobao_list:
                row = 1
                worksheet.merge_range(row, col, row, col + 2, cecpt.en_cn[ec], merge_format)
                row = 2
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                col += 3

            col = 7
            for ec in old_b2c_list:
                row = 0
                worksheet.merge_range(row, col, row + 1, col + 2, cecpt.en_cn[ec], merge_format)
                row = 2
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                col += 3
            row = 0
            worksheet.merge_range(row, col, row + 1, col + 2, '汇总', merge_format)
            row = 2
            for st in st_list:
                worksheet.write(row, col, st)
                col += 1

            # 表内容

            row = 3
            col = 0

            for cate in ccate.cate_list:
                worksheet.write(row, col, cate)
                col += 1
                for ec in ec_list:
                    for st in st_list:
                        cate_st_sum = sum(ec_city_cate[ec][city][cate][st]
                                          for city in caddr.prov_city[pr])
                        worksheet.write(row, col, cate_st_sum)
                        col += 1

                # 汇总各个行业全平台数据
                for st in st_list:
                    cate_st_sum = sum(ec_city_cate[ec][city][cate][st]
                                      for ec in ec_list
                                      for city in caddr.prov_city[pr])
                    worksheet.write(row, col, cate_st_sum)
                    col += 1

                row += 1
                col = 0

            # 汇总各个平台全行业数据
            worksheet.write(row, col, '汇总')
            col = 1
            for ec in ec_list:
                for st in st_list:
                    ec_st_sum = sum(ec_city_cate[ec][city][cate][st]
                                    for city in caddr.prov_city[pr]
                                    for cate in ccate.cate_list)
                    worksheet.write(row, col, ec_st_sum)
                    col += 1

            # 总汇总
            for st in st_list:
                st_sum = sum(ec_city_cate[ec][city][cate][st]
                             for ec in ec_list
                             for city in caddr.prov_city[pr]
                             for cate in ccate.cate_list)
                worksheet.write(row, col, st_sum)
                col += 1

            workbook.close()

            # ---------------------------------各地市分行业统计--------------------------------------
            fw_name = '{}/各地市分行业统计({}).xlsx'.format(dw, cdate.get_ym_cn(ym))

            # 表头
            workbook = xlsxwriter.Workbook(fw_name)
            merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
            worksheet = workbook.add_worksheet('各地市分行业统计')

            worksheet.merge_range(0, 0, 2, 0, '地市', merge_format)
            worksheet.merge_range(0, 1, 2, 1, '行业', merge_format)

            row = 0
            col = 2
            ec = 'taobao'
            worksheet.merge_range(row, col, row, col + 5, cecpt.en_cn[ec], merge_format)

            col = 2
            for ec in taobao_list:
                row = 1
                worksheet.merge_range(row, col, row, col + 2, cecpt.en_cn[ec], merge_format)
                row = 2
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                col += 3

            col = 8
            for ec in old_b2c_list:
                row = 0
                worksheet.merge_range(row, col, row + 1, col + 2, cecpt.en_cn[ec], merge_format)
                row = 2
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                col += 3
            row = 0
            worksheet.merge_range(row, col, row + 1, col + 2, '汇总', merge_format)
            row = 2
            for st in st_list:
                worksheet.write(row, col, st)
                col += 1

            row = 3
            col = 0

            for city in caddr.prov_city[pr]:
                for cate in ccate.cate_list:
                    worksheet.write(row, col, city)
                    worksheet.write(row, col + 1, cate)
                    col += 2
                    for ec in ec_list:
                        for st in st_list:
                            worksheet.write(row, col, ec_city_cate[ec][city][cate][st])
                            col += 1

                    # 汇总各个行业全平台数据
                    for st in st_list:
                        cate_st_sum = sum(ec_city_cate[ec][city][cate][st] for ec in ec_list)
                        worksheet.write(row, col, cate_st_sum)
                        col += 1

                    row += 1
                    col = 0

            # 汇总各个平台全省数据
            worksheet.merge_range(row, col, row, col + 1, '汇总', merge_format)
            col = 2
            for ec in ec_list:
                for st in st_list:
                    ec_st_sum = sum(ec_city_cate[ec][city][cate][st]
                                    for city in caddr.prov_city[pr]
                                    for cate in ccate.cate_list)
                    worksheet.write(row, col, ec_st_sum)
                    col += 1

            # 总汇总
            for st in st_list:
                st_sum = sum(ec_city_cate[ec][city][cate][st]
                             for ec in ec_list
                             for city in caddr.prov_city[pr]
                             for cate in ccate.cate_list)
                worksheet.write(row, col, st_sum)
                col += 1

            workbook.close()
            # ---------------------------------各行业分地市统计--------------------------------------
            fw_name = '{}/各行业分地市统计({}).xlsx'.format(dw, cdate.get_ym_cn(ym))

            # 表头
            workbook = xlsxwriter.Workbook(fw_name)
            merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
            worksheet = workbook.add_worksheet('各行业分地市统计')

            worksheet.merge_range(0, 0, 2, 0, '行业', merge_format)
            worksheet.merge_range(0, 1, 2, 1, '地市', merge_format)

            row = 0
            col = 2
            ec = 'taobao'
            worksheet.merge_range(row, col, row, col + 5, cecpt.en_cn[ec], merge_format)

            col = 2
            for ec in taobao_list:
                row = 1
                worksheet.merge_range(row, col, row, col + 2, cecpt.en_cn[ec], merge_format)
                row = 2
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                col += 3

            col = 8
            for ec in old_b2c_list:
                row = 0
                worksheet.merge_range(row, col, row + 1, col + 2, cecpt.en_cn[ec], merge_format)
                row = 2
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                col += 3
            row = 0
            worksheet.merge_range(row, col, row + 1, col + 2, '汇总', merge_format)
            row = 2
            for st in st_list:
                worksheet.write(row, col, st)
                col += 1

            row = 3
            col = 0

            for cate in ccate.cate_list:
                for city in caddr.prov_city[pr]:
                    worksheet.write(row, col, cate)
                    worksheet.write(row, col + 1, city)
                    col += 2
                    for ec in ec_list:
                        for st in st_list:
                            worksheet.write(row, col, ec_city_cate[ec][city][cate][st])
                            col += 1

                    # 汇总各个行业全平台数据
                    for st in st_list:
                        cate_st_sum = sum(ec_city_cate[ec][city][cate][st] for ec in ec_list)
                        worksheet.write(row, col, cate_st_sum)
                        col += 1

                    row += 1
                    col = 0

            # 汇总各个平台全省数据
            worksheet.merge_range(row, col, row, col + 1, '汇总', merge_format)
            col = 2
            for ec in ec_list:
                for st in st_list:
                    ec_st_sum = sum(ec_city_cate[ec][city][cate][st]
                                    for city in caddr.prov_city[pr]
                                    for cate in ccate.cate_list)
                    worksheet.write(row, col, ec_st_sum)
                    col += 1

            # 总汇总
            for st in st_list:
                st_sum = sum(ec_city_cate[ec][city][cate][st]
                             for ec in ec_list
                             for city in caddr.prov_city[pr]
                             for cate in ccate.cate_list)
                worksheet.write(row, col, st_sum)
                col += 1

            workbook.close()
            # ----------------------------------各区县分行业统计----------------------------------
            fw_name = '{}/各区县分行业统计({}).xlsx'.format(dw, cdate.get_ym_cn(ym))

            # 表头
            workbook = xlsxwriter.Workbook(fw_name)
            merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
            worksheet = workbook.add_worksheet('各区县分行业统计')

            worksheet.merge_range(0, 0, 1, 0, '地市', merge_format)
            worksheet.merge_range(0, 1, 1, 1, '区县', merge_format)
            worksheet.merge_range(0, 2, 1, 2, '行业', merge_format)

            col = 3
            for ec in b2c_list:
                row = 0
                worksheet.merge_range(row, col, row, col + 2, cecpt.en_cn[ec], merge_format)
                row = 1
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                col += 3
            row = 0
            worksheet.merge_range(row, col, row, col + 2, '汇总', merge_format)
            row = 1
            for st in st_list:
                worksheet.write(row, col, st)
                col += 1

            row = 2
            col = 0

            for city in caddr.prov_city[pr]:
                for cnty in caddr.prov_city_cnty[pr][city]:
                    for cate in ccate.cate_list:
                        worksheet.write(row, col, city)
                        worksheet.write(row, col + 1, cnty)
                        worksheet.write(row, col + 2, cate)
                        col += 3
                        for ec in b2c_list:
                            for st in st_list:
                                worksheet.write(row, col, ec_city_cnty_cate[ec][city][cnty][cate][st])
                                col += 1

                        # 汇总各个行业全平台数据
                        for st in st_list:
                            cate_st_sum = sum(ec_city_cnty_cate[ec][city][cnty][cate][st]
                                              for ec in b2c_list)
                            worksheet.write(row, col, cate_st_sum)
                            col += 1

                        row += 1
                        col = 0

            # 汇总各个平台全省数据
            worksheet.merge_range(row, col, row, col + 2, '汇总', merge_format)
            col = 3
            for ec in b2c_list:
                for st in st_list:
                    ec_st_sum = sum(ec_city_cnty_cate[ec][city][cnty][cate][st]
                                    for city in caddr.prov_city[pr]
                                    for cnty in caddr.prov_city_cnty[pr][city]
                                    for cate in ccate.cate_list)
                    worksheet.write(row, col, ec_st_sum)
                    col += 1

            # 总汇总
            for st in st_list:
                st_sum = sum(ec_city_cnty_cate[ec][city][cnty][cate][st]
                             for ec in b2c_list
                             for city in caddr.prov_city[pr]
                             for cnty in caddr.prov_city_cnty[pr][city]
                             for cate in ccate.cate_list)
                worksheet.write(row, col, st_sum)
                col += 1

            workbook.close()
            # ---------------------------------各行业分区县统计---------------------------------

            fw_name = '{}/各行业分区县统计({}).xlsx'.format(dw, cdate.get_ym_cn(ym))
            # 表头
            workbook = xlsxwriter.Workbook(fw_name)
            merge_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
            worksheet = workbook.add_worksheet('各行业分区县统计')

            worksheet.merge_range(0, 0, 1, 0, '行业', merge_format)
            worksheet.merge_range(0, 1, 1, 1, '地市', merge_format)
            worksheet.merge_range(0, 2, 1, 2, '区县', merge_format)

            col = 3
            for ec in b2c_list:
                row = 0
                worksheet.merge_range(row, col, row, col + 2, cecpt.en_cn[ec], merge_format)
                row = 1
                worksheet.write(row, col, ta)
                worksheet.write(row, col + 1, tr)
                worksheet.write(row, col + 2, cecpt.ec_ps[ec])
                col += 3
            row = 0
            worksheet.merge_range(row, col, row, col + 2, '汇总', merge_format)
            row = 1

            for st in st_list:
                worksheet.write(row, col, st)
                col += 1

            row = 2
            col = 0

            for cate in ccate.cate_list:
                for city in caddr.prov_city[pr]:
                    for cnty in caddr.prov_city_cnty[pr][city]:
                        worksheet.write(row, col, cate)
                        worksheet.write(row, col + 1, city)
                        worksheet.write(row, col + 2, cnty)
                        col += 3
                        for ec in b2c_list:
                            for st in st_list:
                                worksheet.write(row, col, ec_city_cnty_cate[ec][city][cnty][cate][st])
                                col += 1

                        # 汇总各个行业全平台数据
                        for st in st_list:
                            cate_st_sum = sum(ec_city_cnty_cate[ec][city][cnty][cate][st]
                                              for ec in b2c_list)
                            worksheet.write(row, col, cate_st_sum)
                            col += 1

                        row += 1
                        col = 0

            # 汇总各个平台全省数据
            worksheet.merge_range(row, col, row, col + 2, '汇总', merge_format)
            col = 3
            for ec in b2c_list:
                for st in st_list:
                    ec_st_sum = sum(ec_city_cnty_cate[ec][city][cnty][cate][st]
                                    for city in caddr.prov_city[pr]
                                    for cnty in caddr.prov_city_cnty[pr][city]
                                    for cate in ccate.cate_list)
                    worksheet.write(row, col, ec_st_sum)
                    col += 1

            # 总汇总
            for st in st_list:
                st_sum = sum(ec_city_cnty_cate[ec][city][cnty][cate][st]
                             for ec in b2c_list
                             for city in caddr.prov_city[pr]
                             for cnty in caddr.prov_city_cnty[pr][city]
                             for cate in ccate.cate_list)
                worksheet.write(row, col, st_sum)
                col += 1

            workbook.close()

    curs.close()
    conn.close()

    print('统计完成，生成报表在如下目录中：{}'.format(dw_top))


run(date_time)
