import os


path1 = r"C:\Users\hsand\OneDrive"
path2 = r"Desktop\python1"
path3 = "README.md"

total_path = os.path.join(path1, path2, path3)

with open(total_path, "r") as file:
    contents = file.read()
    print(contents)


class Car(object):
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.model} is running")

class Truck(Car):
    def __init__(self, maker, model, year, max_load):
        super().__init__(maker, model, year)
        self.max_load = max_load

Hiro_car = Car("Toyota", "Prius", 2014)
Hiro_car.drive()

Naoko_truck = Truck("Toyota", "Tundra", 2023, 500)
print(Naoko_truck.max_load)

import pandas as pd

df = pd.DataFrame({
    'age': [22, 25, 30, 28, 24],
    'income': [40000, 50000, 60000, 55000, 45000]
})

medians = df.median()
print(medians)
print(type(medians))