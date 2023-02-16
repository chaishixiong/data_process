from tools.tools_d.tools_process import tools_file
def commend4_1():
    path = r"X:\数据库\taobao"
    file_name1 = "{taobao_shopid_other1}[shop_id,seller_id].txt"
    data_input = "{3_6_淘宝卖家ID}[KEY,卖家ID].txt"
    file_namew = "{taobao_shopid_zhejiang1}[shop_id,seller_id].txt"
    data_tool = tools_file()
    data_tool.file_write_inset(path,file_name1,data_input,file_namew,num_seed=0,num_data=0,inornot=False)
commend4_1()