import redis

try:
    r = redis.StrictRedis(host='192.168.12.23', port=6379,db=0, password="123456")
    print(r.get("py1809"),type(r.get("py1809")))
    #得到字节类型数据
    print(r.get("py1809").decode("utf8"),type(r.get("py1809").decode("utf8")))
    resulr=r.hget("hashobj","key2")
    r.hset("hashobj","key3",'hello world')
    resulr1 = r.hget("hashobj", "key3")
    print(resulr)
    print(resulr1)
except Exception as e:
    print(e)
