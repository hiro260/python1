import time
from re import search

print(dir())








quit()


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper
    

@my_decorator
def say_hello(name):
    print(f"Hello!, {name}")

say_hello("Alice")

import sys

print(sys.path)
import numpy as np
print("\n")
print(np.__file__)

print("\n")

import time
print(time.time()/(60*60*24*365))
print(time.ctime())
localtime = time.localtime()
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
print(localtime.tm_hour)
print(localtime.tm_min)

sec = 10
#time.sleep(sec)


print(dir(__builtins__))