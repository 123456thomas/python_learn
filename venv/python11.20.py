import redis
r = redis.StrictRedis(host='192.168.12.23', port=6379,
                 db=0, password="123456")

r.hset("hai_1","key1",23)
result=r.hget("hai_1","key1")
print(result)
r.setex("str1",200,"wer")

r.lpush("list123","34","2","3","4","67")
#有很多
r.lpop("list123")
result1=r.lrange("list123",0,3)
print(result1)

t=r.llen("list123")
print(t,type(t))

r.sadd("set234","34","12")
t1=r.scard("set234")
print(t1)