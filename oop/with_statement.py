
#print(f)
#print(type(f))

try:
    f = open("New.txt")
    for line in f:
        print(line, end="")
finally:
    f.close()


print("hello", end="\n")
print("world", end="\n")
print("hello", end="")
print("world", end="")

#f.close

# with statement
with open("New.txt") as f:
    for line in f:
        print(line, end="")

