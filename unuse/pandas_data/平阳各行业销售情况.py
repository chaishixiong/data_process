import pandas as pd
from sqlalchemy import create_engine

import sys
path = r"C:\Users\admin\Desktop"
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

def get_cid():
    cidlist = pd.DataFrame()
    cidlist = pd.read_csv('pingyang_pet_cid.csv')
    cidlist['cid'] = cidlist['cid'].astype('str')
    return cidlist

def get_goods():
    goods = pd.DataFrame()
    for i in range(10,8,-1):
        print(i)
        term = pd.read_sql("select goods_id,goods_name,shop_id,cid,sales_month,discount_price from tmall_goodsmobile_2019{0}".format("%02d" % i),con=engine_tmall)
        print(len(term))
        term = term.loc[term.cid.isin(cidlist.cid)]
        print(len(term))
        goods = goods.append(term)
    return goods

cidlist = get_cid()

goods = get_goods()

goods.to_csv('tmall_goods_table2019.csv',index=False)