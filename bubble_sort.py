import random
import datetime

# setting beginning time stamp
before = datetime.datetime.now()


arr=[]

# setting arr to have length of 100
for x in range(100):
	# randomly populating arr with values between 0-10000
	arr.append(random.randint(0,10000))

count = len(arr)-1

while count > 0:
	for i in range(0, len(arr)-1):
		if arr[i] > arr[i + 1]:
			temp = arr[i]
			arr[i] = arr[i+1]
			arr [i+1] = temp
	count -= 1

# setting end time stanp
after = datetime.datetime.now()

# calculating total elapsed time
time = after - before

print arr
print time