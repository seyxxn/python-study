# 경과 시간 측정
 
import time
from datetime import timedelta

start_time = time.time()

for i in range(5):
    print(i)
    time.sleep(2)


end_time = time.time()
elapsed_time = end_time - start_time  # 경과시간
print("%s seconds" % (elapsed_time))

str(timedelta(seconds = 12345))

# List의 append() vs insert()
num = 40000

start_time = time.time()

data = []
for i in range(1, num + 1):
    data.append(i)
    
end_time = time.time()
elapsed_time = end_time - start_time  # 경과시간
print("append() x %d 경과시간 %s" % (num, str(timedelta(seconds = elapsed_time))))

start_time = time.time()

data = []
for i in range(num, 0, -1):
    data.insert(0, i)
    
end_time = time.time()
elapsed_time = end_time - start_time  # 경과시간
print("insert() x %d 경과시간 %s" % (num, str(timedelta(seconds = elapsed_time))))

# 문자열 연결하기
# str에서의  + VS append() 

"hello" + "Python"
num = 5000000
start_time = time.time()

data = ""
for i in range(num):
    data += "a"
end_time = time.time()

elapsed_time = end_time - start_time  # 경과 시간
print('str(+) x %d 경과시간 %s' % (num, str(timedelta(seconds = elapsed_time))))

start_time = time.time()

data = []
for i in range(num):
    data.append("a")
data = "".join(data)
    
end_time = time.time()
elapsed_time = end_time - start_time  # 경과시간
print("append() x %d 경과시간 %s" % (num, str(timedelta(seconds = elapsed_time))))

