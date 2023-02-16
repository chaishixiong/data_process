import redis, pymysql, datetime, re
from tqdm import tqdm

class Add_redis_data():
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port='5208', db=14, decode_responses=True)
        self.r1 = redis.Redis(host='127.0.0.1', port='5208', db=1, decode_responses=True)
        # self.connect = pymysql.connect(host='192.168.0.226', port=3306, database='oridata', user='dev',
        #                                password='Data227or8Dev715#',
        #                                charset='utf8', use_unicode=True)
        self.connect = pymysql.connect(host='192.168.0.227', port=9227, database='oridata', user='update',
                                       password='change227NRIAT!#$',
                                       charset='utf8', use_unicode=True)
        self.cursor = self.connect.cursor()
        all_task_name = self.r.keys()
        self.r1.delete('gs_adress')
        self.r1.delete('not_spider_address')
        for i in all_task_name:
            TaskName = re.match('company_info', i)
            cache_queue = re.match('gs_cache_queque', i)
            if TaskName != None:
                self.r.delete(i)
            if cache_queue != None:
                self.r.delete(i)

    def get_company_addr(self, table):
        # self.cursor.execute("""SELECT  company,company_address from {} GROUP BY company,company_address""".format(table))        #前：工商地址库

        self.cursor.execute("""SELECT  company,company_address from {} where 法定代表人 !='' GROUP BY company,company_address""".format(table))    # 后：欧洲亚马逊处理
        all_data = self.cursor.fetchall()
        self.connect.commit()
        return all_data

    def check__table(self):
        self.count = self.cursor.execute("""show tables""")
        all_shopinfo = self.cursor.fetchall()
        self.connect.commit()
        all_shopinfo_list = []
        for i in all_shopinfo:
            all_shopinfo_list.append(i[0])
        return all_shopinfo_list

    def run(self):
        table = input('请输入数据库表名:')  # 一：上个月表：company_qichacha_202007     二：新增表：company_qichacha_202007_add
        all_table = self.check__table()
        if table in all_table:
            start_time = datetime.datetime.now()
            company_info_list = self.get_company_addr(table)
            end_time = datetime.datetime.now() - start_time
            print('查询所有公司名称所用时间：{}'.format(end_time))
            for i in tqdm(range(len(company_info_list))):
                try:
                    company = company_info_list[i][0]
                except:
                    company = ''
                try:
                    company_addr = company_info_list[i][1]
                except:
                    company_addr = ''
                if company_addr != '':
                    company_addr = company_addr.replace('——', '')
                    company_info = company + '——' + company_addr
                    self.r.sadd('company_info', company_info)
            data_num = self.r.scard('company_info')
            print('工商地址库参数-任务生成完毕,任务数量为：{}'.format(data_num))
        else:
            print("'{}'表不存在，请确认表名后重新运行程序".format(table))

run = Add_redis_data()
run.run()
