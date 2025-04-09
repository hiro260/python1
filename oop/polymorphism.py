class MyClass(object):
    #pass
    def __str__(self):
        return "My class's __str__"
    
def printvalue(arg):
    print(arg +1)

printvalue(1)

quit()
various_types = [1, "1", True, [1, 2, 3], (1,), {'1': 1}, {1}]
for elem in various_types:
    print(elem)