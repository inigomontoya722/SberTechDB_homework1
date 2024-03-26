import redis
import json
import time

f = open('generated.json')
data = json.load(f)

r = redis.StrictRedis(host='localhost', port=6379, db=1)

print('Время на запись в строку:')
start_time = time.time()
for id in range(len(data)):
  r.set(f'large-file-string:{id}', str(data[id]))
print("--- %s seconds ---" % (time.time() - start_time))

print('Время на чтение строки:')
start_time = time.time()
for id in range(len(data)):
  r.get(f'large-file-string:{id}')
print("--- %s seconds ---" % (time.time() - start_time))

for id in range(len(data)):
  r.delete(f'large-file-string:{id}')  

print('Время на запись в hset:')
start_time = time.time()
for id in range(len(data)):
  r.hset(f'large-file-hset:{id}', mapping=data[id])
print("--- %s seconds ---" % (time.time() - start_time))

print('Время на чтение hset:')
start_time = time.time()
for id in range(len(data)):
  r.hgetall(f'large-file-hset:{id}')
print("--- %s seconds ---" % (time.time() - start_time))

for id in range(len(data)):
  r.delete(f'large-file-hset:{id}')  

print('Время на запись в zset:')
start_time = time.time()
r.zadd('ages', {user['_id']: user['age'] for user in data})
print("--- %s seconds ---" % (time.time() - start_time))

print('Время на чтение zset:')
start_time = time.time()
r.zrange('ages', 20, 40)
print("--- %s seconds ---" % (time.time() - start_time))

r.delete('ages')

print('Время на запись в list:')
start_time = time.time()
for id in range(len(data)):
  r.lpush('names', data[id]['name'])
print("--- %s seconds ---" % (time.time() - start_time))

print('Время на чтение list:')
start_time = time.time()
r.lrange('names', 0, len(data))
print("--- %s seconds ---" % (time.time() - start_time))

r.delete('names')


