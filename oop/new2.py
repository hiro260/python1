a = None
print(a is None)

if a is None:
    print("a is None!!")
else:
    print("a has value!!!")

if not a:
    print("a is None")
else:
    print("a has value!!!")

'''
age = int(input("how old are you?"))

if age >= 18:
    print("please come in")
else:
    print("sorry, you cannot come in")
'''
print("""
aaaaaa      
bbbbbb
cccccc
""")

print("hello world"[3])

fruits = ['apple', 'peach', 'melon', 'grapes']
print(fruits)
fruits.append('banana')
print(fruits)
fruits.insert(3, 'lemon')
print(fruits)
fruits.remove('peach')
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
print(len(fruits))

#slicing
even = [2, 4, 6, 8, 10, 12]
print(even[1:4])
print(even[:4])
print(even[3:-1])
print(even[:])

text = "hello world"
print(text[2:10:2])
print(text[::-1])

print([1, 2, 3] + [4, 5, 6])
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
a += b
print(a)

#join
print("**".join(["Hi", "My", "name", "is", "John"]))

print("Hi My name is John".split(" "))

fruits = ['apple', 'peach', 'melon', 'grapes']

print('apple' in fruits)

y = "jet"

if y:
    print("yes")
else:
    print("no")

fruits = ['apple', 'peach', 'melon', 'grapes']
for fruit in fruits:
    print(f"I love {fruit}!!")