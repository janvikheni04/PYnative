#Define a property that must have the same value for every class instance (object)
class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

b1 = Bus("volvo", 100, 21)
print(b1.color, b1.name, "Bus name", "Speed:", b1.max_speed, "mileage:", b1.mileage)

c1 = Car("BMW", 180, 50)
print(c1.color, c1.name, "Name of car", "Speed:", c1.max_speed, "mileage:", c1.mileage)