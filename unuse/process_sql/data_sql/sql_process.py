import pymysql
import csv
class process():
    def get_data(self,sql_prame,sql):
        connect = pymysql.connect(host=sql_prame.get("host"), port=3306, db=sql_prame.get("db"),
                                   user=sql_prame.get("user"), password=sql_prame.get("password"), charset="utf8",
                                   use_unicode=True, cursorclass=pymysql.cursors.Cursor)
        cursor = connect.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        connect.close()
        return data

    def get_bigdata(self,sql_prame,sql):
        connect = pymysql.connect(host=sql_prame.get("host"), port=3306, db=sql_prame.get("db"),
                                   user=sql_prame.get("user"), password=sql_prame.get("password"), charset="utf8",
                                   use_unicode=True, cursorclass=pymysql.cursors.SSCursor)
        cursor = connect.cursor()
        cursor.execute(sql)
        while True:
            one = cursor.fetchone()
            if not one:
                break
            yield one

    def write_csv(self,filename, header, data):
        with open(filename, "w", newline="") as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow(header)
            for i in data:
                csvWriter.writerow(i)

    def processing(self):
        sql_prame2 = {
        "host" : "192.168.0.227",
        "db" : "ec_cross_border",
        "user" : "dev",
        "password" : "Data227or8Dev715#"
        }
        sql_prame1 = {
        "host" : "192.168.0.228",
        "db" : "e_commerce",
        "user" : "dev",
        "password" : "Data227or8Dev715#"
        }

        # sql3= "select vendorId from jd_pinggou_shopinfo_201912"
        # data3 = self.get_data(sql_prame2,sql3)
        # data3 = {i[0] for i in data3}
        sql1 = '''select shop_id from dhgate_shopinfo_201912 
where Location like "%zhejiang%" or Location like "%Zhe jiang%"'''
        data = self.get_data(sql_prame2,sql1)
        data = {i[0] for i in data}
        # data_shao = data3&data
        sql2 = '''select shop_id from dhgate_goodsinfo_201912'''
        data2_sql = self.get_data(sql_prame2,sql2)
        num = 0
        for i in data2_sql:
            if i[0] in data:
                num+=1
                if num %10000 == 0:
                    print(num)
        print(num)

if __name__=="__main__":
    a = process()
    a.processing()





