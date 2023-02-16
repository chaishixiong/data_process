import redis
from scrapy_redis import picklecompat

serializer = picklecompat

rediscli = redis.StrictRedis(host='127.0.0.1', port=5208,  db=0)
# num = rediscli.zcard("amazon_ph:requests")
a = rediscli.lrange('allegro_goodlist:requests',0,-1)
obj = serializer.loads(a[0])
url = obj.get("url")

print(a)