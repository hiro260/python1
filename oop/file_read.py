#with open("New.txt") as f:
#    for line in f:
#        print(line, end="")

with open("New.txt") as f:
    print(f.read())

#.readaline
with open("New.txt") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()
    
with open("New.txt") as f:
    lines = f.readlines()
    print(lines)