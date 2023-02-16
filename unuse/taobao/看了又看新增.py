from tools.tools_d import tools_file

def commend1():
    path_xinyong = r"X:\数据库\taobao"
    file_name1 = "{5_6_1_天猫看了又看_天猫}[good_id].txt"
    file_name2 = r"{5_5_0_tuiasyn_天猫去重}[商品ID].txt"
    file_namew = file_name1.replace("}","_新增}")
    data_tool = tools_file()
    data_tool.two_data_p(path_xinyong,file_name1,file_name2,file_namew,num=0,num1=0)

def commend2():
    path_xinyong = r"X:\数据库\taobao"
    file_name1 = "浙江有销量shopid.txt"
    file_name2 = r"{6_4_3_字典_淘宝_月统计等大于0_浙江_1}[店铺ID].txt"
    file_namew = "{浙江12月有销量少}[shop_id].txt"#file_name1.replace(".","新增.")
    data_tool = tools_file()
    data_tool.two_data_p(path_xinyong,file_name1,file_name2,file_namew,num=0,num1=0)
commend1()