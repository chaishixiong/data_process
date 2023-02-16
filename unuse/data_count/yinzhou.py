# coding=gbk
import pandas as pd
from sqlalchemy import create_engine
from copy import deepcopy
pingtai = ["jd"]
column = 'shop_id,company,company_address,shop_name,company_tel,main_sale'

condition = 'where city like "%%温州%%"'
host_228 = '192.168.0.228'
smt_database = "ec_cross_border"
jd_database = 'oridata_jd'
ori_database = 'oridata'
a1688_database = 'oridata_1688'
host_227 = '192.168.0.227'
keys = 'Data227or8Dev715#'
user = 'dev'
engine_str = 'mysql+pymysql://{user}:{pw}@{host}/{db}?charset=utf8'
engine_228 = create_engine(engine_str.format(user=user,pw=keys,host=host_228,db='e_commerce'),encoding='utf-8')
engine_1688 = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=a1688_database),encoding='utf-8')
engine_ori = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=ori_database),encoding='utf-8')
engine_jd = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=jd_database),encoding='utf-8')
engine_smt = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=smt_database),encoding='utf-8')


def get_year_shop():
    company_mouth = pd.DataFrame()
    company_last_year = pd.DataFrame()
    company_last_mouths = pd.DataFrame()
    company_mouths = pd.DataFrame()
    company_year = pd.DataFrame()

    mouth_now = 202006
    last_mouths = list(range(201901,mouth_now-100+1))
    last_year = list(range(201901,201913))
    mouths = deepcopy(last_year)
    now_mouths = list(range(202001,mouth_now+1))
    mouths.extend(now_mouths)
    # mouths.extend([202001, 202002, 202003, 202004,202005])
    for mouth in mouths:
        for pt in pingtai:
            if pt == 'jd':
                sql = "select {0},sales_money/3.5 as sales_money,'{1}'as pingtai from {1}_shopinfo_{2} {3}".format(column,pt,mouth,condition)
                data = pd.read_sql(sql,con=engine_228)
                data = data.drop_duplicates('shop_id',keep='last')
            else:
                sql = "select {0},sales_money+0 as sales_money,'{1}' as pingtai from {1}_shopinfo_{2} {3} ".format(column,pt,mouth,condition)
                data = pd.read_sql(sql,con=engine_228)
                data = data.drop_duplicates('shop_id',keep='last')
            print(len(data))
            if mouth == mouth_now:
                company_mouth = company_mouth.append(data)
            if mouth in last_year:
                company_last_year = company_last_year.append(data)
            if mouth in last_mouths:
                company_last_mouths= company_last_mouths.append(data)
            if mouth in now_mouths:
                company_mouths = company_mouths.append(data)
            company_year = company_year.append(data)
    return company_mouth,company_last_year,company_last_mouths,company_mouths,company_year
company_mouth,company_last_year,company_last_mouths,company_mouths,company_year = get_year_shop()
company_mouth = company_mouth.groupby(['shop_id'])[['sales_money']].sum().reset_index()#group by
company_last_year = company_last_year.groupby(['shop_id'])[['sales_money']].sum().reset_index()#group by
company_last_mouths = company_last_mouths.groupby(['shop_id'])[['sales_money']].sum().reset_index()#group by
company_mouths = company_mouths.groupby(['shop_id'])[['sales_money']].sum().reset_index()#group by
company_year = company_year.drop_duplicates('shop_id',keep='last')

# company_year1 = company_year.groupby(['shop_id'])[['sales_money']].sum().reset_index()#去重

company_year = pd.merge(company_year,company_mouth,on ='shop_id',suffixes =('','1'),how='left')#合并
company_year = pd.merge(company_year,company_last_year,on ='shop_id',suffixes =('','1'),how='left')#
company_year = pd.merge(company_year,company_last_mouths,on ='shop_id',suffixes =('','1'),how='left')#合并
company_year = pd.merge(company_year,company_mouths,on ='shop_id',suffixes =('','1'),how='left')#合并



# company_data.sort_values(by = ['sales_money'],ascending=[False],inplace=True)
# company1 = company_data.head(20)
company_year.to_excel(r'C:\Users\Administrator\Desktop\温州—jd.xlsx',index=False)
