import time

curent_time = time.localtime(time.time())

print(curent_time)

year,month,day,hour,minute = curent_time[0:5]

print(str(day) + '/' + str(month) + '/' + str(year)) 
print(str(hour) + ':' + str(minute))

time.time()
print(time.time())

time.gmtime()
print(time.gmtime())

time.asctime()
time.ctime()

print(time.asctime())
print(time.ctime())

print('Hello')
time.sleep(1)
print('World')
time.sleep(1)

my_time = time.localtime(time.time())

year,month,day =  my_time[0:3]

print(str(year) + '/' + str(month) + '/' + str(day))
