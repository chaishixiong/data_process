# coding=gbk
import pandas as pd
from sqlalchemy import create_engine
from copy import deepcopy
pingtai = ["a1688"]
column = 'company'
condition = r'''where company in ("苍南县众信宠物用品厂","苍南县龙港琬瑞鞋厂","温州旭美包装有限公司","温州森匠鞋业有限公司","苍南县圣亿包装制品厂","苍南县龙港奇格纸塑制品厂","苍南县欣梦魅影鞋厂","温州旗凯制衣有限公司","苍南安晴工艺礼品有限公司","温州市阡陌文具礼品有限公司","苍南县西蜜服装厂","温州八宝鹿服饰有限公司","浙江汇中包装科技有限公司","苍南县欣一佳内衣加工厂","温州她画工艺品有限公司","苍南县希博来服饰有限公司","温州领科实业有限公司","苍南县约瑟服装厂","温州香嬷嬷日用品有限公司","温州市源本办公用品有限公司","苍南县鸿源纸塑制品厂","苍南县龙港爱晨纸制品厂","苍南县筱筱服装厂","苍南县博冉服装厂","苍南县妙印包装制品厂","苍南县龙港镇乐帅服装厂","苍南县俊驰服饰有限公司","苍南县喜冠制衣厂","温州妙秀服饰有限公司","浙江麦嘉文化用品有限公司","苍南县晟凯包装材料有限公司","温州鑫泰新材料股份有限公司","苍南县安迪鞋业有限公司","苍南县本色内衣厂","苍南县金乡金工标牌厂","苍南县唯麦服装厂","苍南县御泉服装厂","苍南臻静包装有限公司","温州市康妮制衣有限公司","苍南县八福鼠服饰有限公司","苍南雨奇文具有限公司","温州市君腾工艺品有限公司","苍南县佳笙鞋厂","温州圣驰汽配科技有限公司","苍南艺婷服饰有限公司","苍南县夫车马帽饰厂","浙江源敏科技有限公司","温州市申士文具用品有限公司","温州亚航工艺品有限公司","苍南县海联印务有限公司","苍南县永多制衣厂","苍南县娇娜服饰有限公司","苍南县帆顺服饰有限公司","苍南富腾服饰有限公司","苍南县龙港伊朵夏荷制衣厂","温州市欧圣服饰有限公司","温州际途服装有限公司","苍南县宸瑜服饰有限公司","苍南县雯捷贝制衣厂","苍南县英范贸易有限公司","温州力诚鞋业有限公司","苍南县吉奥商贸有限公司","苍南县翔成服饰有限公司","温州爱康服饰有限公司","苍南县雷君服饰有限公司","苍南县品墨轩文具用品厂","苍南县鼎恒鞋业有限公司","苍南县美琳达皮鞋厂","苍南县宜山佳思吉制衣厂","温州恒茂服装有限公司","苍南县祥衣阁制衣厂","苍南县蓝马服饰加工厂","苍南县长颈鹿服饰厂","温州三叶文具有限公司","苍南县万兴标牌有限公司","温州市芝依服饰有限公司","苍南金汇胶粘制品有限公司","苍南县宏丰装饰材料有限公司","温州市锦远文具有限公司","温州双禾包装有限公司","苍南佰欧尼奥服饰有限公司","苍南海之佳水产品有限公司","温州展风服饰有限公司","温州腾辉文具有限公司","苍南县彤心服饰有限公司","温州市小白兔洁具有限公司","温州双金卫浴有限公司","温州百浩洁具有限公司","温州经济技术开发区海城舒亿达卫浴洁具加工厂","浙江华潮实业有限公司","温州市凯勒卫浴洁具有限公司","温州经济技术开发区海城深信卫浴洁具加工厂","温州沐光文具礼品有限公司","浙江贝乐卫浴科技有限公司","温州美居智能科技有限公司","温州经济技术开发区滨海博达开关厂","温州勒希电器有限公司","温州市哈博筷子有限公司","浙江朗威电器科技有限公司","温州祉妤服饰有限公司","温州奔的智能电器有限公司","温州初念木业有限公司","乐清市稚子童心服饰有限公司","乐清古燕电器有限公司","乐清市美超继电器插座厂","乐清市欧科电气有限公司","乐清市亚洲美甲用品有限公司","乐清市星展美容用品有限公司","浙江康力迪医疗用品有限公司","浙江光大通信设备有限公司","乐清市锐思搏体育用品有限公司","温州潇博科技有限公司","乐清市亚比雅摩配有限公司","温州金好家居用品有限公司","温州市彩诺工艺礼品有限公司","龙港市友尼纸制品厂","温州市棉花兔日用品有限公司","温州市迪鸿工艺品有限公司","温州市爱雅无纺布有限公司","温州佳多乐儿童用品有限公司","苍南县贝司塑料制品有限公司","温州际友工艺品有限公司","浙江晴耕雨读实业有限公司","苍南县龙港亿绵纸塑制品厂","温州星德包装科技有限公司","温州晴诗工艺品有限公司","温州鼎龙包装有限公司","温州荣腾印业有限公司","浙江奥奇医用敷料有限公司","浙江穗印科技有限公司","温州康倩服饰有限公司","温州澜宇实业有限公司","温州华冰冰袋有限公司","龙港市格调纸塑制品厂","龙港市高鼎工艺品有限公司","温州中锐包装科技有限公司","温州绿森服饰有限公司","温州路克箱包有限公司","温州华诺印业有限公司","温州蒙可工艺品有限公司","浙江格利亚电器科技有限公司","温州市格致诚正文化用品有限公司","龙港市嘉智纸制品厂","温州贝丽欧母婴用品有限公司","浙江欧奔智能科技有限公司","温州赛康电器有限公司","浙江康尔美鞋业有限公司","浙江卡特五金有限公司","温州莎扬鞋业有限公司","浙江争亚箱包有限公司","温州哈博科技有限公司","温州市曾泰眼镜厂","温州海纳进出口有限公司","温州尔沫卫浴有限公司","浙江味意食品有限公司","浙江百特电器有限公司","温州市南方立邦印刷实业有限公司","温州市法尚鞋业有限公司","温州经济技术开发区沙城时泰电器厂","温州市巨莉莱鞋业有限公司","温州市利德仕五金有限公司","温州丁巴美业智能科技有限公司","温州市陌上彩鞋业有限公司","温州市町栀鞋业有限公司","浙江日峰电器有限公司","温州市鹿城区仰义诗塔莎皮鞋加工厂","温州市及时雨服饰有限公司","温州忠麒鞋业有限公司","温州宝奢珠宝科技有限公司","温州市千意鞋业有限公司","温州厚瀚鞋业有限公司","温州苛妃尔商贸有限公司","温州瑞朗电器有限公司","温州红贯电器有限公司","温州菲莱拉服饰有限公司","温州市辰帆贸易有限公司","温州民辉国际贸易有限公司","温州市源荣鞋业有限公司","温州润成鞋业有限公司","温州博工电力设备有限公司","温州市龙池鞋业有限公司","温州市中联针服有限公司","温州原驰鞋业有限公司","温州市瓯海娄桥达麦上童鞋厂","温州市金东烟具厂","温州火火工艺品有限公司","温州市中邦烟具制造有限公司","温州市创意精灵服饰有限公司","温州市乔帅鞋业有限公司","浙江香香莉鞋业有限公司","温州市正当时鞋业有限公司","温州市瓯海郭溪舒亿皮鞋厂","温州市鹿城华跃打火机厂","温州市瓯海仙岩倩琦鞋厂","温州康家智能锁业有限公司","温州市瓯海郭溪帝斯康足皮鞋厂","温州市骏丰鸟鞋业有限公司","温州金璇服饰有限公司","温州九鼎鞋业有限公司","温州市祥林工贸有限公司","温州嘉凡服饰有限公司","温州朴恩鞋业有限公司","温州爱比你鞋业有限公司","温州市康益鞋业有限公司","温州市瓯海潘桥银邦皮鞋厂","温州市八达光学有限公司","浙江硕而博科技股份有限公司","温州市康恒鞋业有限公司","温州市瓯海鑫丝漫鞋业有限公司","温州市经纬眼镜厂","温州市万顺眼镜有限公司","浙江百诚烟具有限公司","温州市拉丁公羊鞋业有限公司","温州盛裕眼镜制造有限公司","温州德克家居装饰材料有限公司","温州市嘉洋眼镜有限公司","温州市瓯海鸿星鞋业有限公司","温州市勤鑫鞋业有限公司","温州市领派鞋业有限公司","温州鱼言鱼服饰有限公司","温州市菲迪服饰有限公司","温州市兽邦鞋业有限公司","温州百奇众创电子商务有限公司","温州市宏升鞋业有限公司","温州施乐康医疗器械有限公司","浙江布鲁金眼镜有限公司","温州市瓯海潘桥巨晶鞋厂","温州萌星服饰有限公司","温州裕博鞋业有限公司","温州厚德鞋业有限公司","温州市丁丁猫鞋业有限公司","温州市翔宇食品有限公司","温州飞宏眼镜有限公司","浙江百珍堂食品有限公司","温州滴滴猫鞋业有限公司","温州恒资眼镜有限公司","温州市耐锐鞋业有限公司","浙江美琳诗鞋业有限公司","温州市博恒光学有限公司","温州市成业眼镜有限公司","温州市爱腾鞋业科技有限公司","温州市金烈马鞋业有限公司","浙江宏顺鞋业有限公司","温州创宇眼镜有限公司","温州市牛霸鞋业有限公司","温州轩宇童鞋有限公司","温州郅泰科技有限公司","瑞安市峻菲电子商务有限公司","温州云中鹤鞋业有限公司","温州迈启鞋业有限公司","温州雄锐鞋业有限公司","温州市瓯海潘桥玛佐利服装厂","平阳县佳贝工艺品厂","温州坤禾包装有限公司","平阳县燕燕纸制品厂","苍南县龙港燕燕制袋厂","龙港市敏洁工艺品有限公司","温州创颖日用品有限公司","温州兴航塑料制品有限公司","温州贝巧母婴用品有限公司","平阳县瑞腾文具厂","平阳县富红制袋厂","温州录帮新材料科技有限公司","平阳县溪湾文具厂","温州邦领文具有限公司","平阳县芙尔芮服装厂","平阳县缀泰皮具有限公司","温州瑞威电子有限公司","平阳县依晨无纺布制品有限公司","温州均溢服装有限公司","温州市慧聪电子科技有限公司","温州市子丹保罗贸易有限公司","平阳县钱仓华帛服装厂","平阳县涵乔电子厂","平阳鸿途电子商务有限公司","浙江速能电子科技有限公司","平阳县霄鸿工艺品厂","平阳县兴盛皮件有限公司","平阳县冰凌皮具有限公司","平阳培勇电子科技有限公司","平阳铭度电子商务有限公司","温州曼歌乳胶科技有限公司","温州久扬文具有限公司","浙江青扬电子科技有限公司","温州腾雄文具用品有限公司","平阳县崇堂服装厂","浙江众寻电子科技有限公司","温州市仁爱工艺礼品制造有限公司","平阳美萱工艺品厂","温州迈泰家居有限公司","温州振东皮业有限公司","温州明莱乳胶制品有限公司","温州胜浩家纺有限公司","温州佳盛乳胶制品有限公司","温州金本文具有限公司","平阳县三正工艺品厂","温州易马电子有限公司","温州双卡工艺品有限公司","平阳县振泽工艺品厂","平阳纳百川贸易有限公司","温州鑫远日用品有限公司","温州自主日用品有限公司","温州嘉博乳胶制品有限公司","温州三顺金属制品有限公司","温州大信科技有限公司","平阳县发达塑料制品有限公司","温州乐曼特科技有限公司","温州英久科技有限公司","温州绮豪文具有限公司","佩蒂动物营养科技股份有限公司","平阳县安顺皮具厂","平阳县博誉文具有限公司","温州巨达文具有限公司","平阳县艾维克按摩器材有限公司","瑞安市美秋服饰有限公司","浙江蓝雨伞业有限公司","瑞安市神邦家居用品有限公司","温州市丰宝鞋业有限公司","温州市范哲希服饰有限公司","瑞安市竞酷鞋业有限公司","瑞安市百耀贸易有限公司","瑞安市雅哈鞋业有限公司","瑞安市杰童鞋服有限公司","瑞安市碧康针织有限公司","瑞安市徐忠好服装加工厂","浙江深奥科技有限公司","浙江比迪比鞋业有限公司","瑞安市如森箱包有限公司","瑞安市鸿泰皮具有限公司","瑞安市奥雅服饰有限公司","温州皓邦鞋业有限公司","瑞安市润悦鞋业有限公司","瑞安市金刚狼服装厂","瑞安市南唯莎日用品有限公司","温州鸿渐商贸有限公司","瑞安市天鹿鞋业有限公司","瑞安市顾佳家日用品厂","瑞安市白鹿鞋业有限公司","瑞安市酷客鞋厂","浙江环球鞋业有限公司","瑞安市网乐鞋厂","温州峰尚鞋业有限公司","浙江新纪元鞋业有限公司","瑞安市凌爵鞋业有限公司","瑞安市千艺鸟鞋厂","瑞安市安斯瑞鞋厂","瑞安市达人鞋业有限公司","温州顶鹿服饰有限公司","瑞安市潮荣鞋厂","瑞安市爱尚美鞋厂","浙江天宏卓不凡鞋业有限公司","瑞安市令升鞋厂","瑞安市宝达鞋业有限公司","瑞安市凯瑞家居用品厂","瑞安市诗婷鞋厂","瑞安市佳乐迪鞋业有限公司","温州久发鞋材有限公司","温州聚悦鞋业有限公司","瑞安市飞神鞋厂","浙江升豪鞋业有限公司","浙江远波鞋业有限公司","光裕集团有限公司","苍南县颐新服装厂","瑞安市兆尚电子有限公司","永嘉县群星美容工具有限公司","温州绿辰鞋业有限公司","永嘉县豫见鞋厂","温州潮王鞋业有限公司","温州辰辰服饰有限公司","永嘉县瓯北街道东达鞋厂","永嘉唯美佳足鞋业有限公司","永嘉县晨风教玩具有限公司","温州两情悦鞋业有限公司","温州帮宝智成游乐设备有限公司","永嘉县童宝服装有限公司")'''

# condition = 'where county like "%%鄞州%%"'
host_228 = '192.168.0.228'
smt_database = "ec_cross_border"
jd_database = 'oridata_jd'
ori_database = 'oridata'
a1688_database = 'oridata_1688'
tmall_database = 'oridata_tmall'
host_227 = '192.168.0.227'
keys = 'Data227or8Dev715#'
user = 'dev'
engine_str = 'mysql+pymysql://{user}:{pw}@{host}/{db}?charset=utf8'

engine_228 = create_engine(engine_str.format(user=user,pw=keys,host=host_228,db='e_commerce'),encoding='utf-8')
engine_1688 = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=a1688_database),encoding='utf-8')
engine_ori = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=ori_database),encoding='utf-8')
engine_jd = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=jd_database),encoding='utf-8')
engine_smt = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=smt_database),encoding='utf-8')
engine_tmall = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=tmall_database),encoding='utf-8')


def get_year_shop():
    # company_mouth = pd.DataFrame()
    company_last_year = pd.DataFrame()
    # company_last_mouths = pd.DataFrame()
    company_mouths = pd.DataFrame()
    company_year = pd.DataFrame()

    mouth_now = 202007
    # last_mouths = list(range(201901,mouth_now-100+1))
    last_year = list(range(201901,201913))
    mouths = deepcopy(last_year)
    now_mouths = list(range(202001,mouth_now+1))
    mouths.extend(now_mouths)
    # mouths.extend([202001, 202002, 202003, 202004,202005])
    for mouth in mouths:
        for pt in pingtai:
            if pt =="taobao_qiye"or pt== "tmall":
                column_t = "shop_id,company_boss ,company_tel,"
            elif pt =="a1688":
                column_t= "seller_id_en as shop_id,contacts as company_boss,phone1 as company_tel,"
            else:
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
            # if mouth == mouth_now:
            #     company_mouth = company_mouth.append(data)
            if mouth in last_year:
                company_last_year = company_last_year.append(data)
            # if mouth in last_mouths:
            #     company_last_mouths= company_last_mouths.append(data)
            if mouth in now_mouths:
                company_mouths = company_mouths.append(data)
            company_year = company_year.append(data)
    # return company_mouth,company_last_year,company_last_mouths,company_mouths,company_year
    return company_last_year,company_mouths,company_year

company_last_year,company_mouths,company_year = get_year_shop()
# company_mouth = company_mouth.groupby(['shop_id'])[['sales_money']].sum().reset_index()#group by
company_last_year = company_last_year.groupby(['company'])[['sales_money']].sum().reset_index()#group by
# company_last_mouths = company_last_mouths.groupby(['shop_id'])[['sales_money']].sum().reset_index()#group by
company_mouths = company_mouths.groupby(['company'])[['sales_money']].sum().reset_index()#group by
company_year = company_year.drop_duplicates('shop_id',keep='last')

# company_year1 = company_year.groupby(['shop_id'])[['sales_money']].sum().reset_index()#去重

# company_year = pd.merge(company_year,company_mouth,on ='shop_id',suffixes =('','1'),how='left')#合并
company_year = pd.merge(company_year,company_last_year,on ='company',suffixes =('','1'),how='left')#
# company_year = pd.merge(company_year,company_last_mouths,on ='shop_id',suffixes =('','1'),how='left')#合并
company_year = pd.merge(company_year,company_mouths,on ='company',suffixes =('','1'),how='left')#合并



# company_data.sort_values(by = ['sales_money'],ascending=[False],inplace=True)
# company1 = company_data.head(20)
company_year.to_excel(r'C:\Users\Administrator\Desktop\a1688.xlsx',index=False)
