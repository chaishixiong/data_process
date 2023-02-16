import pymysql
# from process_sql.platform_pipei.address_platform import address_pipei


class address_pipei():#获取中国各地区的拼音字段
    @staticmethod
    def address_zhejiang(connect):
        sql_select = '''select * from address_pinyin'''
        cursor = connect.cursor()
        cursor.execute(sql_select)
        data = cursor.fetchall()
        province_list = set()
        city_list = set()
        county_list = set()
        for i in data:
            province_py1 = i.get("province_py1")
            province_py2 = i.get("province_py2")
            city_py1 = i.get("city_py1")
            city_py2 = i.get("city_py2")
            county_py1 = i.get("county_py1")
            county_py2 = i.get("county_py2")
            county_last = ["xian", "shi", "qu"]
            for county_i in county_last:  # 去掉后缀县等
                if county_py1.endswith(county_i):
                    county_py1 = county_py1[:-len(county_i)]
                if county_py2.endswith(county_i):
                    county_py2 = county_py2[:-len(county_i) - 1]
            province = i.get("province")
            city = i.get("city")
            county = i.get("county")
            if province == "浙江":
                province_list.add((province_py1, province))
                province_list.add((province_py2, province))
                city_list.add(((province_py1, province), (city_py1, city)))
                city_list.add(((province_py2, province), (city_py2, city)))
                county_list.add(((province_py1, province), (city_py1, city), (county_py1, county)))
                county_list.add(((province_py2, province), (city_py2, city), (county_py2, county)))
        cursor.close()
        connect.close()
        return province_list,city_list,county_list

    @staticmethod
    def address_quanguo(connect):
        sql_select = '''select * from address_pinyin'''
        cursor = connect.cursor()
        cursor.execute(sql_select)
        data = cursor.fetchall()
        province_list = set()
        city_list = set()
        county_list = set()
        for i in data:
            province_py1 = i.get("province_py1")
            province_py2 = i.get("province_py2")
            city_py1 = i.get("city_py1")
            city_py2 = i.get("city_py2")
            county_py1 = i.get("county_py1")
            county_py2 = i.get("county_py2")
            county_last = ["xian", "shi", "qu"]
            for county_i in county_last:  # 去掉后缀县等
                if county_py1.endswith(county_i):
                    county_py1 = county_py1[:-len(county_i)]
                if county_py2.endswith(county_i):
                    county_py2 = county_py2[:-len(county_i) - 1]
            province = i.get("province")
            city = i.get("city")
            county = i.get("county")
            if city == "厦门":
                city_list.add(((province_py1, province), ("xiamen", city)))
                county_list.add(((province_py1, province), ("xiamen", city), (county_py1, county)))
                county_list.add(((province_py2, province), ("xiamen", city), (county_py2, county)))
            province_list.add((province_py1, province))
            province_list.add((province_py2, province))
            if (len(city_py1) > 4 or city_py1 in ["wuxi"]) and city_py1 not in ["enshi"]:
                city_list.add(((province_py1, province), (city_py1, city)))
                city_list.add(((province_py2, province), (city_py2, city)))
            if (len(county_py1) > 4 or province == "浙江") and county!= "运河区":
                county_list.add(((province_py1, province), (city_py1, city), (county_py1, county)))
                county_list.add(((province_py2, province), (city_py2, city), (county_py2, county)))
        cursor.close()
        connect.close()
        return province_list, city_list, county_list

    @staticmethod
    def address_zhejiang_chinese(connect):
        sql_select = '''select * from address_pinyin'''
        cursor = connect.cursor()
        cursor.execute(sql_select)
        data = cursor.fetchall()
        province_list = set()
        city_list = set()
        county_list = set()
        for i in data:
            province = i.get("province")
            province = province.replace("省","")
            city = i.get("city")
            city = city.replace("市","")
            county = i.get("county")
            county = county.replace("市","")
            county = county.replace("区","")
            county = county.replace("县","")
            if province == "浙江":
                province_list.add((province,))
                city_list.add((province,city))
                county_list.add((province, city, county))
        cursor.close()
        connect.close()
        return province_list, city_list, county_list

class p_pipei():
    def __init__(self):
        self.host = "192.168.0.227"
        self.port = 3306
        self.db = "ec_cross_company"
        self.name = "dev"
        self.password = "Data227or8Dev715#"

    def get_address(self,match_type=""):#中文匹配方式或者英文匹配方式
        if match_type=="浙江":
            self.province_list, self.city_list, self.county_list = address_pipei().address_zhejiang(self.creat_connect())
        elif match_type=="浙江中文":
            self.province_list, self.city_list, self.county_list = address_pipei().address_zhejiang_chinese(self.creat_connect())
        else:
            self.province_list, self.city_list, self.county_list = address_pipei().address_quanguo(self.creat_connect())

    def creat_connect(self):#链接数据库
        connet = pymysql.connect(host=self.host,port=self.port,db=self.db,user=self.name,passwd=self.password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.DictCursor)#get地址信息
        return connet

    def match_detail(self,match_text,match_type=False,judge = 0,state = 0,province_match = "",city_match = "",area_match = "",match_confidence="",province_last=""):#为匹配主要逻辑方法
        province_m = province_match
        city_m = city_match
        if state < 1:#匹配省级规则
            for province in self.province_list:
                if match_type:#为中文规则
                    if province[0] in match_text:
                        judge = 1
                        province_match = province[0]
                        state = 1
                        province_m = province_match
                        break
                else:
                    #if判断中：为匹配的规则所在
                    if match_text.lower().startswith(province[0].lower()) or "|" + province[0].lower() in match_text.lower() or " " + province[0].lower() in match_text.lower() or province[0].lower() + "|" in match_text.lower() or province[0].lower() + " " in match_text.lower():
                        judge = 1
                        province_match = province[1]
                        state = 1
                        province_m = province_match
                        break
        if state < 2:#匹配市级规则
            if not province_last:
                for city in self.city_list:
                    if match_type:
                        if city[1] in match_text:
                            judge = 1
                            province_match = city[0]
                            city_match = city[1]
                            state = 2
                            city_m = city_match
                            break
                    else:
                        if match_text.lower().startswith(city[1][0].lower()) or "|" + city[1][0].lower() in match_text.lower() or " " + city[1][0].lower() in match_text.lower() or city[1][0].lower() + "|" in match_text.lower() or city[1][0].lower() + " " in match_text.lower():
                            judge = 1
                            province_match = city[0][1]
                            city_match = city[1][1]
                            state = 2
                            city_m = city_match
                            break
            else:
                for city in self.city_list:
                    if match_type:
                        if city[1] in match_text and city[0][1] == province_last:
                            judge = 1
                            province_match = city[0]
                            city_match = city[1]
                            state = 2
                            city_m = city_match
                            break
                    else:
                        if (match_text.lower().startswith(city[1][0].lower()) or "|" + city[1][0].lower() in match_text.lower() or " " + city[1][0].lower() in match_text.lower() or city[1][0].lower() + "|" in match_text.lower() or city[1][0].lower() + " " in match_text.lower()) and city[0][1] == province_last:
                            judge = 1
                            province_match = city[0][1]
                            city_match = city[1][1]
                            state = 2
                            city_m = city_match
                            break
        if state < 3:#匹配区级规则
            for county in self.county_list:
                if state == 1:
                    if match_type:
                        if county[2] in match_text and county[0] == province_m:
                            city_match = county[1]
                            area_match = county[2]
                            judge = 1
                            state = 3
                            break
                    else:
                        if (match_text.lower().startswith(county[2][0].lower()) or "|" + county[2][0].lower() in match_text.lower() or " " + county[2][0].lower() in match_text.lower() or county[2][0].lower() + "|" in match_text.lower() or county[2][0].lower() + " " in match_text.lower()) and county[0][1] == province_m:
                            city_match = county[1][1]
                            area_match = county[2][1]
                            judge = 1
                            state = 3
                            break
                elif state == 2:
                    if match_type:
                        if county[2] in match_text and county[1] == city_m:
                            area_match = county[2]
                            judge = 1
                            state = 3
                            break
                    else:
                        if (match_text.lower().startswith(county[2][0].lower()) or "|" + county[2][0].lower() in match_text.lower() or " " + county[2][0].lower() in match_text.lower() or county[2][0].lower() + "|" in match_text.lower() or county[2][0].lower() + " " in match_text.lower()) and county[1][1] == city_m:
                            area_match = county[2][1]
                            judge = 1
                            state = 3
                            break
                else:
                    if match_type:
                        if county[2] in match_text:
                            province_match = county[0]
                            city_match = county[1]
                            area_match = county[2]
                            match_confidence = "1"
                            judge = 1
                            state = 3
                            break
                    else:
                        if match_text.lower().startswith(county[2][0].lower()) or "|" + county[2][0].lower() in match_text.lower() or " " + county[2][0].lower() in match_text.lower() or county[2][0].lower() + "|" in match_text.lower() or county[2][0].lower() + " " in match_text.lower():
                            province_match = county[0][1]
                            city_match = county[1][1]
                            area_match = county[2][1]
                            match_confidence = "1"
                            judge = 1
                            state = 3
                            break
        return judge,state,province_match,city_match,area_match,match_confidence


    def address_match(self,match_text,shop_key,updata_sql,cursor_update,match_text2="",chinese=False):#主要匹配逻辑，match_text为重要字段，match_text2为次重要字段
        if not match_text2:
            judge, state, province_match, city_match, area_match, match_confidence = self.match_detail(match_text,chinese)#true为中文匹配
            if judge == 1:
                update_sqltext = updata_sql.format(province_match,city_match,area_match,match_confidence,shop_key)
                cursor_update.execute(update_sqltext)
        else:
            judge, state, province_match, city_match, area_match, match_confidence = self.match_detail(match_text,chinese)
            if judge == 1:
                judge, state, province_match, city_match, area_match, match_confidence = self.match_detail(match_text2,chinese,judge=judge,state=state,province_match=province_match,city_match=city_match,area_match=area_match,match_confidence=match_confidence,province_last=province_match)
                update_sqltext = updata_sql.format(province_match,city_match,area_match,match_confidence,shop_key)
                cursor_update.execute(update_sqltext)
            else:
                judge, state, province_match, city_match, area_match, match_confidence = self.match_detail(match_text2,chinese)
                if judge == 1:
                    update_sqltext = updata_sql.format(province_match,city_match,area_match,match_confidence,shop_key)
                    cursor_update.execute(update_sqltext)

if __name__ == "__main__":
    match_task = p_pipei()
    match_task.get_address("浙江")#中文address

    connect_get = match_task.creat_connect()
    cursor_get = connect_get.cursor()

    sql_get = 'SELECT location,index_id from lazada_shopinfo_201910 where not (location REGEXP "[u0391-uFFE5]") and location != ""'#选取的sql数据
    sql_update = '''update lazada_shopinfo_201910 set province_match = "{}",city_match = "{}",area_match = "{}",match_confidence="{}" where index_id = "{}";'''#更新语句

    cursor_get.execute(sql_get)
    all_data = cursor_get.fetchall()
    cursor_get.close()
    cursor_update = connect_get.cursor()
    print_num = 0
    for data in all_data:
        if data:
            if print_num % 1000 == 0:
                print(print_num)
            location = data.get("location") if data.get("location") else ""#匹配的字段
            shop_key = data.get("index_id") if data.get("index_id") else ""#sql中的key字段
            match_text = location#可以在各字段中添加|用于分割各字段
            try:
                match_task.address_match(match_text,shop_key,sql_update,cursor_update,chinese=False)#主要代码段
            except Exception as e:
                print(print_num)
                print(e)
        print_num += 1
