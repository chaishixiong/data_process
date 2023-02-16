from tools.tools_d import tools_file


def commend1():
    path_xinyong = r"X:\数据库\taobao"
    file_name1 = "{3_0_天猫卖家ID}[KEY,卖家ID,状态,shopUrl,url].txt"
    file_name2 = r"{3_1_天猫卖家ID}[KEY,卖家ID,状态,shopUrl,url].txt"
    file_namew = "{3_0_天猫卖家ID}[KEY].txt"
    data_tool = tools_file()
    data_tool.two_data_p(path_xinyong,file_name1,file_name2,file_namew,num=0,num1=0)
commend1()