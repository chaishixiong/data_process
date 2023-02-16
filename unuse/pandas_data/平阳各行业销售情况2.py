import pandas as pd
from sqlalchemy import create_engine

import sys
path = r"D:\PythonProject"
sys.path.append(path)

host_228 = '192.168.0.228'
tmall_database = 'oridata_tmall'
ori_database = 'oridata'
host_227 = '192.168.0.227'
keys = 'Data227or8Dev715#'
user = 'dev'
engine_str = 'mysql+pymysql://{user}:{pw}@{host}/{db}?charset=utf8'
engine_228 = create_engine(engine_str.format(user=user,pw=keys,host=host_228,db='e_commerce'),encoding='utf-8')
engine_ori = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=ori_database),encoding='utf-8')
engine_tmall = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=tmall_database),encoding='utf-8')

def get_shop():
    shop = pd.DataFrame()
    shop = pd.read_csv('pingyang_shop_id.csv')
    shop['shop_id'] = shop['shop_id'].astype('str')
    return shop

def get_goods():
    goods = pd.DataFrame()
    for i in range(9,8,-1):
        print(i)
        term = pd.read_sql("select goods_id,goods_name,shop_id,cid,sales_month,discount_price from tmall_goodsmobile_2019{0}".format("%02d" % i),con=engine_tmall)
        print(len(term))
        term = term.loc[term.shop_id.isin(shop.shop_id)]
        print(len(term))
        goods = goods.append(term)
    return goods

shop = get_shop()

goods = get_goods()

goods.to_csv('tmall_goods_table2019.csv',index=False)
