
class address_pipei():

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