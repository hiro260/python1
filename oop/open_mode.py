# mode='a'
#with open("writing_file.txt", mode='a') as f:
#    f.write("mode=a appends text")
#print("test")
# mode='r+'
#with open("writing_file.txt", mode='r+') as f:
#     #print(f.read())
#    f.write("you can write and read with r+ mode!!!!!!!!!!!!!!!!!!!\n")
#    f.write("you can write and read with r+ mode#########")
#    f.seek(0)
#    print(f.read())
#    print("test2")

#mode="w+"
#with open("writing_file.txt", mode='w+') as f:
#    print(f.read())
#    f.write("you can write and read with w+ mode#########")

#mode="a+"
with open("writing_file.txt", mode='a+') as f:
    print(f.read())
    f.write("\nyou can write and read with a+ mode?????????")