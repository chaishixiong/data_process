#生成dif表
import pymysql
from tqdm import tqdm

def get_data(sql_prame,sql):
    connect = pymysql.connect(host=sql_prame.get("host"), port=3306, db=sql_prame.get("db"),
                               user=sql_prame.get("user"), password=sql_prame.get("password"), charset="utf8",
                               use_unicode=True, cursorclass=pymysql.cursors.Cursor)
    cursor = connect.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connect.close()
    return data
def get_addict(sql_prame,table_ad):
    sql_ad = '''select company,company_address,province,city,county
    from {}'''.format(table_ad)
    data = get_data(sql_prame,sql_ad)
    dict_ad = {}
    for i in data:
        dict_ad[i[0]] = i[1:]
    return dict_ad
def insert_con(sql_prame,dif_table):
    connect = pymysql.connect(host=sql_prame.get("host"), port=3306, db=sql_prame.get("db"),
                              user=sql_prame.get("user"), password=sql_prame.get("password"), charset="utf8",
                              use_unicode=True, cursorclass=pymysql.cursors.Cursor)
    cursor = connect.cursor()
    creat_table = '''CREATE TABLE  IF NOT EXISTS `{}` (
      `formername` varchar(255) DEFAULT NULL,
      `companyname` varchar(255) DEFAULT NULL,
      `address` varchar(255) DEFAULT NULL,
      `province` varchar(255) DEFAULT NULL,
      `city` varchar(255) DEFAULT NULL,
      `contry` varchar(255) DEFAULT NULL
    ) ENGINE=MyISAM DEFAULT CHARSET=utf8;'''.format(dif_table)
    cursor.execute(creat_table)
    return cursor

if __name__=="__main__":
    table_ad = "company_ad_20200704"
    sql_prame = {
        "host": "192.168.0.227",
        "db": "oridata",
        "user": "dev",
        "password": "Data227or8Dev715#"
    }
    table_qichacha = "company_qichacha_202006_add"
    dif_table = "company_ad_diff_20200706"

    sql_ad = '''select company,`曾用名`
    from {} where `曾用名` !="" and `曾用名` is not null and `曾用名` !="nan"'''.format(table_qichacha)
    dict_ad = get_addict(sql_prame,table_ad)#获取地址dict
    print("地址dict生成")
    dif_data = get_data(sql_prame,sql_ad)
    cursor = insert_con(sql_prame,dif_table)

    for i in tqdm(dif_data):
        dif_list = i[1].split("；")
        company = i[0]
        for j in dif_list:
            sql_insert = '''insert into {} (formername,companyname,address,province,city,contry) values ({})'''.format(dif_table,",".join(["'{}'"] * 6))
            info = dict_ad.get(company, ("", "", "", ""))
            sql_insert = sql_insert.format(j.strip(),company,info[0],info[1],info[2],info[3])
            try:
                cursor.execute(sql_insert)
            except Exception as e:
                print(e)
                print(sql_insert)