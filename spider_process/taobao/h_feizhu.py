#"X:\数据库\taobao\{3_7_0_飞猪卖家ID}[KEY,卖家ID,状态,shopUrl天猫,url天猫,飞猪].txt"
from tools.tools_d.tools_process import tools_file
mouth = 202202
def commend1():
    path_xinyong = r"X:\数据库\taobao"
    file_name1 = "{3_7_飞猪卖家ID}[KEY,卖家ID].txt"
    file_name2 = r"{{tmall_shop_xinyong_{}}}[卖家ID,描述_UFB_0高_1_2低,描述评分,描述比同行,服务_UFB_0高_1_2低,服务评分,服务比同行,物流_UFB_0高_1_2低,物流评分,物流比同行,店铺好评率,卖家信用].txt".format(mouth)
    file_namew = file_name2.replace("tmall","feizhu")
    data_tool = tools_file()
    data_tool.file_write_inset(path_xinyong,file_name1,file_name2,file_namew,num_seed=1,num_data=0,inornot=True)

def commend2():
    path_xinyong = r"X:\数据库\taobao"
    file_name1 = "{3_7_飞猪卖家ID}[KEY,卖家ID].txt"
    file_name2 = r"tmall_shopinfo_{}[店铺ID,卖家ID,平台,主营,公司名称,月销售量,月销售额,发货地址,卖家用户名,卖家等级,店铺好评率,店铺名称,微淘ID,店铺粉丝,开店时间,商品数量,上新数量,关注人数,保证金,店铺图片,金牌店铺,店铺类型,店铺URL,天猫省,天猫市,客服电话,电话分机,店铺类型2,店铺年龄,店铺类型3,加密旺旺,工商xid].txt".format(mouth)
    file_namew = file_name2.replace("tmall","feizhu")
    data_tool = tools_file()
    data_tool.file_write_inset(path_xinyong,file_name1,file_name2,file_namew,num_seed=0,num_data=0,inornot=True)

def commend3():
    path_xinyong = r"X:\数据库\taobao"
    file_name1 = "{3_7_飞猪卖家ID}[KEY,卖家ID].txt"
    file_name2 = r"tmall_goodsmobile_202201[采集时间,商品ID,近似销量,月销量,评论数,总库存,收藏量,发货地址,类目ID,品牌ID,平台,商品名称,卖家ID,店铺ID,促销名称,促销价,定金,定金描述,原价名称,原价,配送费用,商品保证,网店推广,推广描述,商品积分,主图,商品属性].txt"
    file_namew = file_name2.replace("tmall","feizhu")
    data_tool = tools_file()
    data_tool.file_write_inset(path_xinyong,file_name1,file_name2,file_namew,num_seed=0,num_data=13,inornot=True)


if __name__ == "__main__":
    commend1()
    # commend2()
    # commend3()