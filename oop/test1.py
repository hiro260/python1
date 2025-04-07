import time

local_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

print("Local Time:", formatted_time)


list1 = ['a', 'b', 'c']

list1.append('d')

print(list1)

list1 = ['a', 'b', 'c']
result = '---'.join(list1)  # Joins with a hyphen (-)
print(result)  
