class Person(object):

    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        print("get_age called!!")
        return self._age

    @age.setter
    def age(self, age):
        print("set_age called!!")
        if age <0:
            print("please input more than 0")
        else:
            self._age = age

    #age =property(get_age, set_age)


john = Person("John", 10)
emma = Person("Emma", 40)

#print(john)
print(john.age)
john.age = -10
print(john.age)