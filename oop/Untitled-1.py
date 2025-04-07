import time

time1 = time.localtime()
print(time1.tm_mon)
print(time1.tm_mday)
print(time1.tm_year)
print(time1.tm_hour)
print(time1.tm_min)
print(time1.tm_sec)

print((1, 4, 5) < (1, 4, 6))

print(0 + True)
print(0 + False)