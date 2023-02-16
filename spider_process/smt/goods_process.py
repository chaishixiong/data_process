from tools.tools_s.sql_base import get_data
import os
from tools.tools_d.tools_process import tools_file

def write_lastdata(mouth):
    # mouth = 202210
    sql = '''select shop_id,company,shui_id,yingye_id,address,people,scope,shopCreatedAt,jiguan,province,city,county
    from smt_shopinfo_{}
    where province != ""'''.format(202212)
    sql_prame = {
        "host": "192.168.1.4",
        "db": "ec_cross_border",
        "user": "update_all",
        "password": "123456",
        "port":3306
    }
    data = get_data(sql_prame,sql)
    path = "X:\数据库\速卖通"
    file_name = "/{速卖通牌照信息_上月}[店铺ID,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区].txt"
    with open(path+file_name,"w",encoding="utf-8") as f:
        for i in data:
            f.write(",".join(i)+"\n")
def write_address():
    table = input("表:")
    sql = '''select company,province,city,county
    from {}'''.format(table)
    sql_prame = {
        "host": "192.168.1.4",
        "db": "oridata",
        "port":3306,
        "user": "update_all",
        "password": "123456"
    }
    data = get_data(sql_prame,sql)
    path = "X:/数据库/速卖通"
    file_name = "/{company_cross}[公司名称,省,市,区].txt"
    with open(path+file_name,"w",encoding="utf-8") as f:
        for i in data:
            f.write(",".join(i)+"\n")


def smtgoods_rename(mouth):
    path = "X:/数据库/速卖通"
    old_name = "/smt_goodsid_order.txt_去重.txt"
    goods_name = "/{{smt_goodsinfo_{}}}[店铺id,卖家id,商品数目,商品id,销量,商品价格,商品价格_较高值,产品url,评分,商品名称,评论数量,媒体id,图片链接,标签].txt".format(mouth)
    os.rename(path+old_name,path+goods_name)
# def smtgoods_rename1():
#     path = "X:/数据库/速卖通"
#     old_name = "/smt_comment-data_zhejiang.txt"
#     goods_name = "/{smt_comment_zhejiang}[seller_id,goods_id,current_page,comment_num,comment_distribution,user_name,country,comment_score,comment,time].txt"
#     os.rename(path+old_name,path+goods_name)
def smtgoods_rename2():
    path = "X:/数据库/速卖通"
    old_name = "/smt_comment.txt"
    goods_name = "/{smt_comment_all}[seller_id,goods_id,current_page,comment_num,comment_distribution,user_name,country,comment_score,comment,time].txt"
    os.rename(path+old_name,path+goods_name)
def commend1():#牌照选新id
    path_xinyong = r"X:\数据库\速卖通"
    file_name1 = r"{3_1_1_字典_速卖通_月统计}[店铺id,sum(销量 米 商品价格_较高值),sum(销量)].txt"
    file_name2 = r"{速卖通牌照信息_上月}[店铺ID,公司名称,增值税税号,营业执照注册号,地址,联系人,业务范围,创建时间,登记机关,省,市,区].txt"
    file_namew = "{smt_shopid_new}[shopid].txt"
    data_tool = tools_file()
    data_tool.two_data_p(path_xinyong,file_name1,file_name2,file_namew,num=0,num1=0)


if __name__ == '__main__':
    mouth = 202301
    #爬好商品表
    # smtgoods_rename(mouth)#第一步
    # write_lastdata(mouth)#第一步
    #数据库2统计月销量
    # commend1()#第二步
    # 本地跑本月
    # write_address()
    #评价采集之后
    smtgoods_rename2()