import redis, pymysql, datetime, re
from tqdm import tqdm


def updata_goods():
    year_list = ['202108', '202112', '202211']
    data_dict = dict()
    new_goods = open("X:\数据库\ebay数据采集\ebayinfo_goods-data_new.txt", "w", encoding="utf-8")
    connect = pymysql.connect(host='192.168.1.4', port=3306, database='ec_cross_border', user='update_all',
                                   password='123456',
                                   charset='utf8', use_unicode=True)
    cursor = connect.cursor()
    for year in year_list:
        cursor.execute("""SELECT * FROM `ebay_goodsinfo_{}`""".format(year))
        all_data = cursor.fetchall()
        connect.commit()
        for all_data_1 in all_data:
            goods_id_1 = all_data_1[0]
            data_dict[goods_id_1] = all_data_1
    with open(r'X:\数据库\ebay数据采集\ebayinfo_goods-data_合并.txt', "r", encoding="utf-8") as goods_2:
        for godds_data in goods_2:
            godds_data_list = godds_data.strip().split(',')
            goodsid_2 = godds_data_list[0]
            goods_data = data_dict.get(goodsid_2)
            if goods_data != None:
                godds_data_list[1] = goods_data[1]
                godds_data_list[2] = goods_data[2]
                godds_data_list[3] = goods_data[3]
                godds_data_list[4] = goods_data[4]
                godds_data_list[5] = goods_data[5]
                godds_data_list[6] = goods_data[6]
                godds_data_list[8] = goods_data[8]
                godds_data_list[9] = goods_data[9]
                godds_data_list[10] = goods_data[10]
                godds_data_list[11] = goods_data[11]
                godds_data_list[12] = goods_data[12]
                godds_data_list[13] = goods_data[13]
            new_goods.write(','.join(godds_data_list) + '\n')
            new_goods.flush()
        new_goods.close()


if __name__ == '__main__':
    updata_goods()









