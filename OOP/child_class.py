#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(Vehicle):
    pass

a = bus("A", 100, 30)
print("Name is", a.name, "speed is", a.max_speed, "ans mileage is", a.mileage)
