class Car(object):
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year

        
class Truck(Car):
    def __init__(self, maker, model, year, current_load, max_load):
        super().__init__(maker=maker, model=model, year=year)
        self.current_load = current_load
        self.max_load = max_load

    def load(self, new_load):
        if self.current_load + new_load > self.max_load:
            print(("overload, but you can overload"))
            self.current_load += new_load
        elif self.current_load + new_load <= 0:
            self.current_load = 0
        else:
            self.current_load += new_load
        print(f"new current load: {self.current_load}")


if __name__ = "__main__":
    truck1 = Truck("Isuzu", "Menards", 2025, 1000, 3000)
    print(truck1.maker)
    print(truck1.model)
    print(truck1.year)
    print(truck1.current_load)
    print(truck1.max_load)

    truck1.load(400)
    truck1.load(4000)
    truck1.load(-5000)
    truck1.load(-1000)
    truck1.load(2000)