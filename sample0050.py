print(f"in {__file__} 1")
#print(__file__)

print("before import *")
from module05 import *
print("after import *")

print(f"in {__file__} 2")
hello05(__file__)
hello06(__file__)