class Animal(object):
    def __init__(self, name):
        self.name = name
        print("Animal init is called")

    def breath(self):
        print(f"{self.name} is breathing")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name=name)
        print("Dog init is called")
    pass




pochi = Dog("pochi")
print(pochi.name)
print("!!!!!!!!!")
pochi.breath()
