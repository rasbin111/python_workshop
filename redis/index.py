import redis

pool = redis.ConnectionPool(host="localhost", port=6379, db=0)

r = redis.Redis(connection_pool=pool)


print(r.dbsize())

r.set("animal", "leopard")

animal = r.get("animal").decode("utf-8")
animal_b = r.get("animal")

print(type(animal)) # string 
print(type(animal_b)) # bytes

r.delete('furst')
r.delete("frust")
r.delete("_kombu.binary.celery")
r.delete("celery")

print(r.exists("animal"))
# r.expire("animal", 30) # expires in 30 seconds

r.set("count", 1)
# r.persist("animal")
r.incr("count")

print(r.keys('*'))
