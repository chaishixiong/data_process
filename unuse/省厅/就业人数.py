#coding:utf-8
import pymysql


class PersonNum():
    def __init__(self):
        self.conn_2020 = pymysql.connect(host='192.168.0.125', port=3306, db='bizdep_platform', user='nriat_dev', password='Dev530#')
        self.conn_2019 = pymysql.connect(host='192.168.0.125', port=3306, db='bizdep_platform_20200319', user='nriat_dev', password='Dev530#')
        self.conn_2016 = pymysql.connect(host='192.168.0.125', port=3306, db='elecbplatform_20190418', user='nriat_dev', password='Dev530#')

    def sheng_person(self, data):
        '''
        省就业人数
        2020.6月以后
        sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county WHERE date='{}' and province = '浙江省'".format(i)
        20201-5月
        sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county_磐安划分前 WHERE date='{}' and province = '浙江省'".format(i)
        2019年及以前
        sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county WHERE date='{}' and province = '浙江省'".format(i)
        :return:
        '''
        rateRandom = 2.48 + 0.5 * 0.3

        # 2020
        # cursor = self.conn_2020.cursor()
        cursor = self.conn_2016.cursor()
        for i in data:
            print(i)
            # 2020.06以后
            # sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county WHERE date='{}' and province = '浙江省'".format(i)
            # 2020.01-2020.05
            # sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county_磐安划分前 WHERE date='{}' and province = '浙江省'".format(i)
            sql1 = "SELECT (sum(tb_shop_count)*1.5 +sum(tmall_shop_count)*4 +sum(jd_shop_count)*3 +sum(shop_count))+(sum(tb_shop_count)*1.5 +sum(tmall_shop_count)*4 +sum(jd_shop_count)*3 +sum(shop_count))*0.0225  from elecsales WHERE count_time='{}' and province = '浙江省'".format(i)

            cursor.execute(sql1)
            res = cursor.fetchall()
            print(round(res[0][0]), round(int(res[0][0])*rateRandom))

        # 2019
        # cursor = self.conn_2019.cursor()
        # for i in data:
        #     print(i)
        #     sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county WHERE date='{}' and province = '浙江省'".format(i)
        #     cursor.execute(sql1)
        #     res = cursor.fetchall()
        #     print(round(res[0][0]), round(int(res[0][0]) * rateRandom))

    def city_people(self, data, city):
        '''
        城市就业人数
        2020.06以后
        sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county WHERE date='{}' and city = '{}'".format(i, n)
        20201-5月
        sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county_磐安划分前 WHERE date='{}' and city = '{}'".format(i, n)
        2019年及以前
        sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county WHERE date='{}' and city = '{}'".format(i, n)
        :param data: 时间列表
        :param city: 城市列表
        :return:
        '''
        rateRandom = 2.48 + 0.5 * 0.3

        # 2020
        # cursor = self.conn_2020.cursor()
        # for n in city:
        #     for i in data:
        #
        #         # 2020.06以后
        #         # sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county WHERE date='{}' and city = '{}';".format(i, n)
        #         # 2020.1-5
        #         sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county_磐安划分前 WHERE date='{}' and city = '{}'".format(i, n)
        #
        #         cursor.execute(sql1)
        #         res = cursor.fetchall()
        #         print(n, i, round(res[0][0]), round(int(res[0][0]) * rateRandom))

        # 2019
        # cursor = self.conn_2019.cursor()
        # 2016
        cursor = self.conn_2016.cursor()
        for n in city:
            print(n)
            for i in data:
                # print(i)
                # sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from elecsales WHERE date='{}' and city = '{}'".format(i, n)
                sql1 = "SELECT (sum(tb_shop_count)*1.5 +sum(tmall_shop_count)*4 +sum(jd_shop_count)*3 +sum(shop_count))+(sum(tb_shop_count)*1.5 +sum(tmall_shop_count)*4 +sum(jd_shop_count)*3 +sum(shop_count))*0.0225  from elecsales WHERE count_time='{}' and city = '{}'".format(i, n)

                # i = i.split('.')[0] + '年'
                cursor.execute(sql1)
                res = cursor.fetchall()
                print(round(res[0][0]), round(int(res[0][0]) * rateRandom))

    def county_people(self, data, county):
        '''

        :param data:
        :param county:
        :return:
        '''
        rateRandom = 2.48 + 0.5 * 0.3
        # 2020
        # cursor = self.conn_2020.cursor()
        # for i in data:
        #     print(i)
        #     for n in county:
        #
        #         # sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county WHERE date='{}' and county = '{}'".format(i, n)
        #         sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county_磐安划分前 WHERE date='{}' and county = '{}'".format(i, n)
        #
        #         # i = i.split('.')[0] + '年'
        #         cursor.execute(sql1)
        #         res = cursor.fetchall()
        #         print(round(res[0][0]), round(int(res[0][0]) * rateRandom))

        # 2019
        # cursor = self.conn_2019.cursor()
        # 2016
        cursor = self.conn_2016.cursor()
        for i in data:
            print('----------%s-----------' % i)
            for n in county:
                # print(n)
                # sql1 = "SELECT (sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))+(sum(taobao_act_shop_cnt)*1.5 +sum(tmall_act_shop_cnt)*4 +sum(jd_act_shop_cnt)*3 +sum(sum_act_shop_cnt))*0.0225  from ec_city_county WHERE date='{}' and county = '{}'".format(i, n)
                sql1 = "SELECT (sum(tb_shop_count)*1.5 +sum(tmall_shop_count)*4 +sum(jd_shop_count)*3 +sum(shop_count))+(sum(tb_shop_count)*1.5 +sum(tmall_shop_count)*4 +sum(jd_shop_count)*3 +sum(shop_count))*0.0225  from elecsales WHERE count_time='{}' and county = '{}'".format(i, n)

                # i = i.split('.')[0] + '年'
                cursor.execute(sql1)
                res = cursor.fetchall()
                print(round(res[0][0]), round(int(res[0][0]) * rateRandom))
if __name__ == '__main__':
    person = PersonNum()
    # 省级就业人口
    # person.sheng_person(['2020.05','2020.04','2020.03','2020.02'])
    # person.sheng_person(['2019.12','2019.11','2019.10','2019.09','2019.08','2019.07','2019.06','2019.05','2019.04','2019.03','2019.02'])
    # person.sheng_person(['2018.12','2018.11','2018.10','2018.09','2018.08','2018.07','2018.06','2018.05','2018.04','2018.03','2018.02'])
    # person.sheng_person(['2017.12','2017.11','2017.10','2017.09','2017.08','2017.07','2017.06','2017.05','2017.04','2017.03','2017.02','2017.01'])
    # person.sheng_person(['2016.11','2016.10','2016.09','2016.08','2016.07','2016.06','2016.05','2016.04','2016.03','2016.02','2016.01'])

    # 市级就业人口
    # person.city_people(['2020.06'], ['杭州市','宁波市','温州市','湖州市','嘉兴市','绍兴市','金华市','衢州市','舟山市','台州市', '丽水市'])
    # person.city_people(['2020.05','2020.04','2020.03','2020.02',], ['杭州市','宁波市','温州市','湖州市','嘉兴市','绍兴市','金华市','衢州市','舟山市','台州市', '丽水市'])
    # person.city_people(['2019.12','2019.11','2019.10','2019.09','2019.08','2019.07','2019.06','2019.05','2019.04','2019.03','2019.02'], ['杭州市','宁波市','温州市','湖州市','嘉兴市','绍兴市','金华市','衢州市','舟山市','台州市', '丽水市'])
    # person.city_people(['2018.12','2018.11','2018.10','2018.09','2018.08','2018.07','2018.06','2018.05','2018.04','2018.03','2018.02'], ['杭州市','宁波市','温州市','湖州市','嘉兴市','绍兴市','金华市','衢州市','舟山市','台州市', '丽水市'])
    # person.city_people(['2017.12','2017.11','2017.10','2017.09','2017.08','2017.07','2017.06','2017.05','2017.04','2017.03','2017.02','2017.01'], ['杭州市','宁波市','温州市','湖州市','嘉兴市','绍兴市','金华市','衢州市','舟山市','台州市', '丽水市'])
    # person.city_people(['2016.11','2016.10','2016.09','2016.08','2016.07','2016.06','2016.05','2016.04','2016.03','2016.02','2016.01'], ['杭州市','宁波市','温州市','湖州市','嘉兴市','绍兴市','金华市','衢州市','舟山市','台州市', '丽水市'])

    # 区就业人口   ,'玉环县'
    # person.county_people(['2020.06'], ['上城区', '下城区', '江干区', '拱墅区', '西湖区', '滨江区', '萧山区', '余杭区', '桐庐县', '淳安县', '建德市', '富阳区', '临安区', '海曙区', '江北区', '镇海区', '北仑区', '鄞州区', '奉化区', '余姚市', '慈溪市', '宁海县', '象山县', '鹿城区', '龙湾区', '瓯海区', '洞头区', '乐清市', '瑞安市', '永嘉县', '文成县', '平阳县', '泰顺县', '苍南县', '龙港市', '吴兴区', '南浔区', '德清县', '长兴县', '安吉县', '南湖区', '秀洲区', '嘉善县', '平湖市', '海盐县', '海宁市', '桐乡市', '越城区', '柯桥区', '诸暨市', '上虞区', '嵊州市', '新昌县', '婺城区', '金东区', '兰溪市', '东阳市', '义乌市', '永康市', '浦江县', '武义县', '磐安县', '柯城区', '衢江区', '龙游县', '江山市', '常山县', '开化县', '定海区', '普陀区', '岱山县', '嵊泗县', '椒江区', '黄岩区', '路桥区', '临海市', '温岭市', '玉环市', '天台县', '仙居县', '三门县', '莲都区', '龙泉市', '青田县', '云和县', '庆元县', '缙云县', '遂昌县', '松阳县', '景宁县'])
    # person.county_people(['2020.05','2020.04','2020.03','2020.02'], ['上城区', '下城区', '江干区', '拱墅区', '西湖区', '滨江区', '萧山区', '余杭区', '桐庐县', '淳安县', '建德市', '富阳区', '临安区', '海曙区', '江北区', '镇海区', '北仑区', '鄞州区', '奉化区', '余姚市', '慈溪市', '宁海县', '象山县', '鹿城区', '龙湾区', '瓯海区', '洞头区', '乐清市', '瑞安市', '永嘉县', '文成县', '平阳县', '泰顺县', '苍南县', '龙港市', '吴兴区', '南浔区', '德清县', '长兴县', '安吉县', '南湖区', '秀洲区', '嘉善县', '平湖市', '海盐县', '海宁市', '桐乡市', '越城区', '柯桥区', '诸暨市', '上虞区', '嵊州市', '新昌县', '婺城区', '金东区', '兰溪市', '东阳市', '义乌市', '永康市', '浦江县', '武义县', '磐安县', '柯城区', '衢江区', '龙游县', '江山市', '常山县', '开化县', '定海区', '普陀区', '岱山县', '嵊泗县', '椒江区', '黄岩区', '路桥区', '临海市', '温岭市', '玉环市', '天台县', '仙居县', '三门县', '莲都区', '龙泉市', '青田县', '云和县', '庆元县', '缙云县', '遂昌县', '松阳县', '景宁县'])
    # person.county_people(['2019.12','2019.11','2019.10','2019.09','2019.08','2019.07','2019.06','2019.05','2019.04','2019.03','2019.02', '2018.12','2018.11','2018.10','2018.09','2018.08','2018.07','2018.06','2018.05','2018.04','2018.03','2018.02', '2017.12','2017.11','2017.10','2017.09','2017.08','2017.07','2017.06','2017.05','2017.04','2017.03','2017.02','2017.01', '2016.12'], ['上城区', '下城区', '江干区', '拱墅区', '西湖区', '滨江区', '萧山区', '余杭区', '桐庐县', '淳安县', '建德市', '富阳区', '临安区', '海曙区', '江北区', '镇海区', '北仑区', '鄞州区', '奉化区', '余姚市', '慈溪市', '宁海县', '象山县', '鹿城区', '龙湾区', '瓯海区', '洞头区', '乐清市', '瑞安市', '永嘉县', '文成县', '平阳县', '泰顺县', '苍南县',  '吴兴区', '南浔区', '德清县', '长兴县', '安吉县', '南湖区', '秀洲区', '嘉善县', '平湖市', '海盐县', '海宁市', '桐乡市', '越城区', '柯桥区', '诸暨市', '上虞区', '嵊州市', '新昌县', '婺城区', '金东区', '兰溪市', '东阳市', '义乌市', '永康市', '浦江县', '武义县', '磐安县', '柯城区', '衢江区', '龙游县', '江山市', '常山县', '开化县', '定海区', '普陀区', '岱山县', '嵊泗县', '椒江区', '黄岩区', '路桥区', '临海市', '温岭市', '玉环市', '天台县', '仙居县', '三门县', '莲都区', '龙泉市', '青田县', '云和县', '庆元县', '缙云县', '遂昌县', '松阳县', '景宁县'])
    # person.county_people(['2016.11','2016.10','2016.09','2016.08','2016.07','2016.06','2016.05','2016.04','2016.03','2016.02','2016.01'], ['上城区', '下城区', '江干区', '拱墅区', '西湖区', '滨江区', '萧山区', '余杭区', '桐庐县', '淳安县', '建德市', '富阳区', '临安区', '海曙区', '江东区', '江北区', '镇海区', '北仑区', '鄞州区', '奉化区', '余姚市', '慈溪市', '宁海县', '象山县', '鹿城区', '龙湾区', '瓯海区', '洞头区', '乐清市', '瑞安市', '永嘉县', '文成县', '平阳县', '泰顺县', '苍南县', '吴兴区', '南浔区', '德清县', '长兴县', '安吉县', '南湖区', '秀洲区', '嘉善县', '平湖市', '海盐县', '海宁市', '桐乡市', '越城区', '柯桥区', '诸暨市', '上虞区', '嵊州市', '新昌县', '婺城区', '金东区', '兰溪市', '东阳市', '义乌市', '永康市', '浦江县', '武义县', '磐安县', '柯城区', '衢江区', '龙游县', '江山市', '常山县', '开化县', '定海区', '普陀区', '岱山县', '嵊泗县', '椒江区', '黄岩区', '路桥区', '临海市', '温岭市',  '天台县', '仙居县', '三门县', '莲都区', '龙泉市', '青田县', '云和县', '庆元县', '缙云县', '遂昌县', '松阳县', '景宁县'])
    person.county_people(['2016.11','2016.10','2016.09','2016.08','2016.07','2016.06','2016.05','2016.04','2016.03','2016.02','2016.01'], ['玉环市'])