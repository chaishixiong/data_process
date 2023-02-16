from tools.tools_d.tools_process import tools_file
def commend2():
    path = r"X:\数据库\taobao"
    file_name_seed = r"{taobao_newshopid}[店铺ID,卖家ID].txt"
    file_name2 = r"{5_3_asyn取商品ID_其他各省淘宝}[商品ID,KEY,商品名称,价格,月销量].txt"
    file_namew = r"{5_3_asyn取商品ID_其他各省淘宝_new}[商品ID,KEY,商品名称,价格,月销量].txt"
    # file_namew = file_name2.replace("}","zhejiang")
    data_tool = tools_file()
    data_tool.file_write_inset(path,file_name_seed,file_name2,file_namew,num_seed=1,num_data=1,inornot=True)

def commend3():
    path = r"X:\数据库\taobao"
    file_name_seed = r"{taobao_newshopid}[店铺ID,卖家ID].txt"
    file_name2 = r"{5_2_asyn取商品ID_浙江淘宝}[商品ID,KEY,商品名称,价格,月销量].txt"
    file_namew = r"{5_2_asyn取商品ID_浙江淘宝_new}[商品ID,KEY,商品名称,价格,月销量].txt"
    # file_namew = file_name2.replace("}","zhejiang")
    data_tool = tools_file()
    data_tool.file_write_inset(path,file_name_seed,file_name2,file_namew,num_seed=1,num_data=1,inornot=True)
commend3()