with open("writing_file.txt", mode='w') as f:
    f.write("you can write contents here\nuse 'backslssh' to break the row")
    f.write("new write() does not break row")

    print("you can add a new row using 'file' parameter", file=f, end="\n")
    print("new print() method breaks the row for you!!", file=f, end="\n")