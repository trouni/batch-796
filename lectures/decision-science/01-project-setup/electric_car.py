from car import Car

# class ChildClass(ParentClass)
class ElectricCar(Car):
    brand = "Tesla"
    power_source = "electric"

    def __init__(self, color, age, battery_capacity):
        super().__init__(self, color, age)
        self.battery_capacity = battery_capacity
