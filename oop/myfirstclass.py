class Person(object):
    
     num_legs = 2
     count = 0


    # constructor
     def __init__(self, name, age, gender):
          self.name = name
          self.age = age
          self.gender = gender
          Person.count += 1

     def walk(self):
          print(f"{self.name} is walking... with {Person.num_legs} legs!!!")

     def run(self):
          print(f"{self.name} is running")

john = Person("John", 28, 'male')
print(Person.count)
taro = Person("Taro", 18, 'male')
print(Person.count)
emma = Person("Emma", 40, 'female')
print(Person.count)

# instance variable
print(john.name)
print(taro.age)
print(emma.gender)

print(f"before modification: {john.age}")
john.age = 29
print(f"after modification: {john.age}")

# instance method
john.walk()
emma.walk()
john.run()

print(john.num_legs)
print(taro.num_legs)
print(Person.num_legs)
print("Person.num_legs = 3")
Person.num_legs = 3
print(john.num_legs)
print(taro.num_legs)
print(Person.num_legs)
print("john.num_legs = 4")
john.num_legs = 4
print(john.num_legs)
print(taro.num_legs)
print(Person.num_legs)


'''
class Car(object):

    def __init__(self, model_name, mileage, manufacturer):
         self.modelname = model_name
         self.mileage = mileage
         self.manufacturer = manufacturer
    
    def gas(self):
         print(f"{self.modelname} gas")
    
    def breakes(self):
         print(f"{self.modelname} breakes")         

if __name__ == "__main__":
    prius_2014 = Car("prius", 50, "Toyota")
    corolla_2014 = Car("corolla", 30, "Toyota")
    corolla_2024 = Car("corolla", 28, "Toyota")
    print(prius_2014.modelname)

'''