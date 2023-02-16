# -*- coding:utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

pingtai = ["tmall","taobao_qiye","jd"]
column = 'shop_id,company,company_address,company_boss,company_tel,street,main_sale,shop_name,open_shop_date,goods_num'
# condition = 'shop_id like "110883527" and goods_name like "%%会员%%"'
condition = r'''where company in ("温州畏衫电子商务有限公司","温州市巨康食品有限公司","温州吉派服饰有限公司","温州联腾包装机械有限公司","温州亿蓬电子商务有限公司","温州市强能食品有限公司","温州新足佳鞋业有限公司","温州天瀚金属制品有限公司","温州市瓯海南白象莱顿鞋店","温州市龙安贸易有限公司","温州市金烈马鞋业有限公司","浙江拍普儿服饰有限公司","温州市拓步者户外休闲装备有限公司","温州莫畏电子商务有限公司","温州市瓯海南白象嗳玛服装网店","温州市飞煌机械设备有限公司","温州蓝星电子商务有限公司","温州迅驰贸易有限公司","温州宗晨贸易有限公司","温州市自留地贸易有限公司","温州市仟维意服饰有限公司","温州市坤汉贸易有限公司","温州市瓯海南白象伊微尔鞋服网店","温州市益母百货有限公司","温州市琛和机械设备有限公司","温州市凯驰包装机械有限公司","温州市启昂服饰有限公司","温州市龙溪电子商务有限公司","温州喜璐电子商务有限公司","温州市强聚鞋业有限公司","温州佳伍特商贸有限公司","温州威玛服饰有限公司","温州市德尔机器有限公司","温州市军明眼镜制造有限公司","温州市瓯海南白象圣华家用电器厂","温州市三来光学有限公司","温州麒文电器有限公司","温州市卡美拉鞋业有限公司","温州汶昕迪贸易有限公司","温州中博工艺品有限公司","温州市辉煌五金有限公司","温州容睿贸易有限公司","温州博冠服饰有限公司","温州市大卫摩配有限公司","温州羽泉鞋业有限公司","温州启篇贸易有限公司","温州个性美鞋业有限公司","温州市佳宝禾粮食复制品有限公司","温州市启昂服饰有限公司","温州和平医疗投资管理有限公司","温州市强聚鞋业有限公司","温州市自留地贸易有限公司")'''
# condition = "where county like '%%永嘉%%'"
host_228 = '192.168.0.228'
smt_database = "ec_cross_border"
a1688_database = 'oridata_1688'
jd_database = 'oridata_jd'
ori_database = 'oridata'
tmall_database = 'oridata_tmall'
host_227 = '192.168.0.227'
keys = 'Data227or8Dev715#'
user = 'dev'
engine_str = 'mysql+pymysql://{user}:{pw}@{host}/{db}?charset=utf8'

engine_228 = create_engine(engine_str.format(user=user,pw=keys,host=host_228,db='e_commerce'),encoding='utf-8')
engine_ori = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=ori_database),encoding='utf-8')
engine_jd = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=jd_database),encoding='utf-8')
engine_tmall = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=tmall_database),encoding='utf-8')
engine_1688 = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=a1688_database),encoding='utf-8')
engine_smt = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=smt_database),encoding='utf-8')
def get_year_shop():
    company_year=pd.DataFrame()
    mouths = list(range(202001,202008))
    # mouths.extend([202001, 202002, 202003, 202004,202005,202006])
    for mouth in mouths:
        for pt in pingtai:
            # if pt =="taobao_qiye"or pt== "tmall":
            #     column_t = "shop_id,company_boss ,company_tel,"
            # elif pt =="a1688":
            #     column_t= "seller_id_en as shop_id,contacts as company_boss,phone1 as company_tel,"
            # else:
            column_t=""

            if pt == "smt":
                sql = "select {4}{0},sales_money/3.5 as sales_money,'{1}'as pingtai,'{2}' as date from {1}_shopinfo_{2} {3} ".format(column,pt,mouth,condition,column_t)
                data = pd.read_sql(sql,con=engine_smt)
                data.drop_duplicates('shop_id',keep='last')
            elif pt =="a1688":
                sql = "select {4}{0},month_sales_month+0 as sales_money,'{1}'as pingtai,'{2}' as date from {1}_shopinfo_{2} {3} ".format(column,pt,mouth,condition,column_t)
                data = pd.read_sql(sql,con=engine_1688)
                data.drop_duplicates('shop_id',keep='last')
            elif pt =="jd":
                sql = "select {4}{0},sales_money/3.5 as sales_money,'{1}'as pingtai,'{2}' as date from {1}_shopinfo_{2} {3} ".format(
                    column, pt, mouth, condition,column_t)
                data = pd.read_sql(sql,con=engine_228)
                data.drop_duplicates('shop_id',keep='last')
            else:
                sql = "select {4}{0},sales_money*1 as sales_money,'{1}'as pingtai,'{2}' as date from {1}_shopinfo_{2} {3} ".format(
                    column, pt, mouth, condition,column_t)
                data = pd.read_sql(sql,con=engine_228)
                data.drop_duplicates('shop_id',keep='last')
            print(len(data))
            company_year = company_year.append(data)
    return company_year
company_year = get_year_shop()
company1 = company_year.groupby(['company'])[['sales_money']].sum().reset_index()#group by
# company2 = company_year.groupby(['company','date'])[['sales_money']].sum().reset_index()#group by
#
# # company_year = company_year.drop_duplicates('shop_id',keep='last')#去重
company_data = pd.merge(company_year,company1,on ='company',suffixes =('','1'),how='right')#合并
# company_data = pd.merge(company_data,company2,on ='company',suffixes =('','1'),how='left')#合并

# company_year.sort_values(by = ['sales_money'],ascending=[False],inplace=True)
# shop_sales_top = company_year.head(200)
company_data.to_excel(r'C:\Users\Administrator\Desktop\南白象2.xlsx',index=False)
