from tools.tools_d.tools_process import tools_file
from tools.tools_d.tools_base import tools_file_b
import json
import time
def commend1():
    path_xinyong = r"X:\数据库\taobao\上个月过程数据"
    file_name1 = r"{taobao_look-data_tmall}[seller_id].txt_去重.txt"
    file_name2 = r"{3_4_天猫卖家ID}[KEY,卖家ID].txt"
    file_namew = file_name1.replace("}","_add1}")
    data_tool = tools_file()
    data_tool.two_data_p(path_xinyong,file_name1,file_name2,file_namew,num=0,num1=1,dict_name="setdiff1d")
    # intersect1d 交集
    # setdiff1d a-b
    # union1d 并集
    # setxor1d 异或
def commend2():
    path = r"X:\数据库\taobao"
    file_name_seed = r"{taobao_look-data_zhejiang}[goods,seller_id,price,sales,name,cid,score,url].txt"
    file_name2 = r"{taobao_look-data_asynzhejiang}[商品ID,KEY,价格,月销量,商品名称,cid,score,url].txt"
    file_namew = r"{taobao_look-data_asynzhejiang_test}[商品ID,KEY,价格,月销量,商品名称,cid,score,url].txt"
    # file_namew = file_name2.replace("}","zhejiang")
    data_tool = tools_file()
    data_tool.file_write_inset(path,file_name_seed,file_name2,file_namew,num_seed=0,num_data=0,inornot=False)

def commend3():
    data = json.loads('''{"shop_id": "33891732", "seller_id": "46592366", "company": "\u5bb6\u5c45\u7528\u54c1", "main_sale": "", "address": "\u6c5f\u82cf\u5357\u901a", "sales_money": "0", "sales_count": "0", "company_address": "", "province": "", "city": "", "county": "", "street": "", "sales_average": "", "last_sales_average": "", "month_on_month": ""}''')
    headers = [i for i in data]
    data = [[data[i] for i in data]]
    data_tool = tools_file_b()
    data_tool.write_csv(r"C:\Users\admin\Desktop\commend2.txt", headers, data)

def commend4():
    ospath = r"C:\Users\admin\Desktop\test"
    data_tool = tools_file()
    data_tool.file_zip7(ospath,".txt","(.*)")

def commend5():
    path = r"D:\data_process\taobao12过程校验\扫描id\10000"
    data_tool = tools_file()
    data_tool.saomiao(path)


def commend7():
    path = r"X:\数据库\taobao"
    file_name1 = "{3_3_天猫卖家ID_信用错误}[KEY,卖家ID,状态].txt"
    file_namew = "{3_3_天猫卖家ID_信用错误_python}[KEY,卖家ID,状态].txt"
    data_tools = tools_file()
    youxiao = "//.+\.m\.tmall"

    data_tools.file_write_re(path,file_name1,file_namew,youxiao,2)

def time_stamp():
    file = r"X:\数据库\taobao\{8_0_1_天猫店铺补充信息}[店铺ID,开店时间].txt"
    data_tools = tools_file_b()
    with open(r"X:\数据库\taobao\{8_0_1_天猫店铺补充信息_时间}[店铺ID,开店时间].txt","a",encoding="utf-8") as f:
        for i in data_tools.get_yield(file):
            data = i.strip().split(",")
            if data[1]:
                l_time = time.localtime(int(data[1][:-3]))
                s_time = time.strftime("%Y-%m-%d %H:%M:%S",l_time)
                f.write("{},{}".format(data[0],s_time)+"\n")

def commend8():
    file_name = r'X:\数据库\taobao\{taobao_goodsmobile_other2_备份}[近似销量,真实价格].txt'
    data_tools = tools_file()
    sum = data_tools.field_sum(file_name,sales_sum=True)
    print(sum)

commend2()
