class MyError(Exception):
    pass

response = input("y/n? ")
if response != "y" and response != "n":
    raise MyError("my error occurred")