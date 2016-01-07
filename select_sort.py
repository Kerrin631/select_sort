import random
import datetime

before = datetime.datetime.now()

arr = []
for x in range(100):
 arr.append(random.randint(0,10000))
for i in range(0, len(arr) -1):
 minimum = i
 for j in range(i+1, len(arr)):
   if arr[j] < arr[minimum]:
     minimum = j
 if minimum != i:
   arr[i], arr[minimum] = arr[minimum], arr[i]

after = datetime.datetime.now()
time = after - before

print arr
print time