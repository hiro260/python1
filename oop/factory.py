import time
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return cls(name=name, age=age)

    @staticmethod
    def create_from_dob2(name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return Person(name=name, age=age)    


class Baby(Person):
    pass

john = Baby('John', 20)
emma = Baby.create_from_dob('Emma', 1989, 4, 3)
emily = Baby.create_from_dob2('Emily', 1999, 12, 3)
print(john.age)
print(emma.name)
print(emma.age)
print(emily.age)

print(type(john))
print(type(emma))
print(type(emily))

#print(john)
#print(emma)
#print(vars(john))
#print(vars(emma))