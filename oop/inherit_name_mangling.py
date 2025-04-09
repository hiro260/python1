class Person(object):
    def __init__(self, name):
        self.name = name
        self.__mymethod()

    def mymethod(self):
        print("Person method is called")

    __mymethod = mymethod


class Baby(Person):
    def mymethod(self):
        print("Baby method is called")
    #def __init__(self, name):
    #    super.__init__(name)
    pass

taro_baby = Baby("Taro")
taro_person = Person("Taro")
taro_person.mymethod()

print(taro_baby.name)
taro_baby.mymethod()
print(dir(taro_baby))