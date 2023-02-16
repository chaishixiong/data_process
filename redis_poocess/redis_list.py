import redis
import time
while True:
    server = redis.Redis(host='192.168.1.4', port=6776)
    while True:
        a = server.rpoplpush("smt_goodsid_order:error_url", "smt_goodsid_order:requests")
        if not a:
            break
    print("完成")
    time.sleep(5)

