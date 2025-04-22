import os

import numpy

def test():print("hello")


x=1
y =   3

z=x+y

print(z)

name = "John"
print("hello, {} ".format(name))
print(id(name))

def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


example_function(name="Alice", age=30, city="New York")

def example_function2(*args):
     for arg in args:
         print(arg)

example_function2(1, "hello", 3.14)

print( 14 // 3)
print( 14 % 3)
print( 2 ** 3)
print(True + True)
print(1000 > 500)

print('######################################################')

a = 1
b = 1
c = 3
d = a
print( a is b)
print( a is not c)
print( a is d)

nothing = None
print(nothing)
print(nothing is None)

print('######################################################')
#logical operator
a = 1
b = 1
print(not a == b)
print(a != b)

print('######################################################')

age = 150

if not 0 < age < 120:
    print("wired age!!!")