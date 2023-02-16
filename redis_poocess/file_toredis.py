import redis
class redis_process():
    def __init__(self,host,port,password=None,db=0):
        self.server = redis.Redis(host=host, port=port,password=password,db=db)

    def file_toredis(self,file_name,key,type="set"):
        with open(file_name,"r",encoding="utf-8") as f:
            for data in f:
                data = data.strip()
                if type=="set":
                    self.server.sadd(key,data)
                elif type=="list":
                    self.server.lpush(key,data)


if __name__=="__main__":
    file_name = "X:\数据库\速卖通\{速卖通_商品其他1}[卖家id,商品id].txt_拆分\_(1-5000000).txt"
    host = "192.168.0.226"
    port = "5208"
    key = "smt_comment:start_url"
    process = redis_process(host=host,port=port)
    # process.file_toredis(file_name,key,"set")