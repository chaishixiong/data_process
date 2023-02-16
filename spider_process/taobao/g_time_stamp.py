from tools.tools_d.tools_process import tools_file
from tools.tools_d.tools_base import tools_file_b
import time
def commend1():
    path_xinyong = r"X:\数据库\taobao"
    file_name1 = "{5_6_3_淘宝看了又看_浙江淘宝}[商品ID].txt"
    file_name2 = r"{5_5_2_tuiasyn_浙江淘宝去重}[商品ID].txt"
    file_namew = file_name1.replace("}","_新增}")
    data_tool = tools_file()
    data_tool.two_data_p(path_xinyong,file_name1,file_name2,file_namew,num=0,num1=0)
def commend2():
    path_xinyong = r"X:\数据库\taobao"
    file_name1 = "{5_6_1_天猫看了又看_天猫}[good_id].txt"
    file_name2 = r"{5_5_0_tuiasyn_天猫去重}[商品ID].txt"
    file_namew = file_name1.replace("}","_新增}")
    data_tool = tools_file()
    data_tool.two_data_p(path_xinyong,file_name1,file_name2,file_namew,num=0,num1=0)
def commend3():
    path_xinyong = r"X:\数据库\飞猪"
    file_name1 = "{5_6_2_天猫看了又看_飞猪}[good_id].txt"
    file_name2 = r"{5_5_1_tuiasyn_飞猪去重}[商品ID].txt"
    file_namew = file_name1.replace("}","_新增}")
    data_tool = tools_file()
    data_tool.two_data_p(path_xinyong,file_name1,file_name2,file_namew,num=0,num1=0)
def commend4():
    path_xinyong = r"X:\数据库\taobao"
    file_name1 = "{5_6_1_天猫看了又看_天猫}[good_id].txt"
    file_name2 = r"{5_5_0_tuiasyn_天猫去重}[商品ID].txt"
    file_namew = file_name1.replace("}","_新增}")
    data_tool = tools_file()
    data_tool.two_data_p(path_xinyong,file_name1,file_name2,file_namew,num=0,num1=0)
def commend5():
    path = r"X:\数据库\taobao"
    file_name1 = "{3_4_1天猫卖家ID去重}[KEY,卖家ID].txt"
    file_name2 = "{3_4_1天猫卖家ID去重_加错误}[KEY,卖家ID].txt"
    file_namew = "{3_4_1天猫卖家ID去重_差值}[KEY,卖家ID].txt"
    data_tool = tools_file()
    data_tool.file_write_inset(path,file_name1,file_name2,file_namew,num_seed=0,num_data=0,inornot=False)

def time_stamp():
    file = r"X:\数据库\taobao\{8_0_1_天猫店铺补充信息_time}[店铺ID,开店时间].txt"
    data_tools = tools_file_b()
    with open(r"X:\数据库\taobao\{8_0_1_天猫店铺补充信息_时间}[店铺ID,开店时间].txt","w",encoding="utf-8") as f:
        for i in data_tools.get_yield(file):
            data = i.strip().split(",")
            if data[1]:
                l_time = time.localtime(int(data[1][:-3]))
                s_time = time.strftime("%Y-%m-%d %H:%M:%S",l_time)
                f.write("{},{}".format(data[0],s_time)+"\n")
def saoid():
    data_tools = tools_file()
    data_tools.saomiao(r"X:\数据库\taobao\扫描遗漏", )#扫描查漏
def commend6():
    path_xinyong = r"X:\数据库\taobao"
    file_name1 = "{淘宝天猫店铺ID}[店铺ID,状态].txt"
    file_name2 = r"{(20210116-023718)采集_淘宝店铺ID_手机店铺信用}[KEY].txt"#修改名称
    file_namew = file_name1.replace("}","_差值}")
    data_tool = tools_file()
    data_tool.two_data_p(path_xinyong,file_name1,file_name2,file_namew,num=0)

time_stamp()