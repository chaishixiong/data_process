# coding=utf-8

import random

# 获取浮点数格式的销售额

def get_float_sale(sale):
    try:
        sale = float(sale)
    except:
        return 0.0

    if sale <= 0:
        return 0.0

    return sale

# 获取四舍五入后整数形式的销售额
# 京东销售额除以3.5，若结果大于0小于1返回1，否则四舍五入


def get_ec_round_sale(ec, sale):
    try:
        sale = float(sale)
    except:
        return 0

    if sale <= 0:
        return 0

    # 处理京东销售数据
    if ec == 'jd':
        sale /= 3.5
        if sale < 1:
            return 1

    return round(sale)


# 计算两个list的pearson相关系数


def get_lists_pearson(x_list, y_list):
    n = len(x_list)
    xsum = sum(x_list)
    ysum = sum(y_list)
    sqxsum = sum([pow(xi, 2) for xi in x_list])
    sqysum = sum([pow(yi, 2) for yi in y_list])
    psum = sum([xi * yi for xi, yi in zip(x_list, y_list)])
    num = psum - (xsum * ysum / n)
    den = pow((sqxsum - pow(xsum, 2) / n) * (sqysum - pow(ysum, 2) / n), 0.5)

    if den == 0:
        return 0
    return num / den


# 总数量按p列表中的数值比例分配
def distributed_by_prop(n_sum, p_list):
    n = len(p_list)
    p_sum = sum(p_list)
    if p_sum == 0:
        p_list = [1 / n for p in p_list]
    else:
        p_list = [p / p_sum for p in p_list]

    n_list = [0 for p in p_list]
    while n_sum != sum(n_list):
        n_list = [n_sum * p for p in p_list]
        n_list = [int(n) + 1
                  if random.random() < (n - int(n))
                  else int(n) for n in n_list]
    return n_list

'''def distributed_by_prop(n_sum, p_list):
    n = len(p_list)
    p_sum = sum(p_list)
    if p_sum == 0:
        p_list = [1 / n for p in p_list]
    else:
        p_list = [p / p_sum for p in p_list]

    n_float_list = [n_sum * p for p in p_list]
    n_list = [int(n) for n in n_float_list]
    n_res_list = [n - int(n) for n in n_float_list]
    n_sum_res = n_sum - sum(n_list)

    sorted_index = sorted(range(len(n_res_list)), key=lambda k: n_res_list[k], reverse=True)

    for i in range(n_sum_res):
        n_list[sorted_index[i]] += 1

    return n_list'''


# 判断mysql中的表格是否存在
def mysql_table_exist(curs, table_name):
    sql_query = 'show tables like "' + table_name + '"'
    curs.execute(sql_query)
    tables = curs.fetchall()
    if len(tables) != 0:
        return True
    return False

arab2chn_dict = {0: '零', 1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九', 10: '十'}

def arab2chn(n):
    n_str = str(n)
    if len(n_str) > 2:
        print('暂不支持三位数字转换')
        return None
    if len(n_str) == 1:
        return arab2chn_dict[n]
    if n_str == '10':
        return '十'
    if n_str[0] == '1':
        return '{}{}'.format('十', arab2chn(int(n_str[1])))
    if n_str[1] == '0':
        return '{}{}'.format(arab2chn(int(n_str[0])), '十')

    return '{}十{}'.format(arab2chn(int(n_str[0])), arab2chn(int(n_str[1])))


























