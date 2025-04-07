class MyClass(object):

    classmethod_count = 0

    def mymethod(self):
        print("this is normal method")

    @staticmethod
    def mystaticmethod():
        print("this is staticmethod!!")

    @classmethod
    def myclassmethod(cls):
        cls.classmethod_count += 1
        print(f"This is classmethod and now the count is {cls.classmethod_count}")



c = MyClass()
c.mymethod()

MyClass.mystaticmethod()
#c.mystaticmethod()
MyClass.myclassmethod()
MyClass.myclassmethod()
