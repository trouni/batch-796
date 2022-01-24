from datetime import date


class Car:
    # class attribute
    brand = "Toyota"

    # constructor
    def __init__(self, color, age):
        # STATE / attributes of the instance
        self.color = color  # str
        self.age = age
        self.engine_started = False

    # BEHAVIOUR
    # instance methods
    def start_engine(self):
        self.engine_started = True

    def paint_car(self, new_color):
        self.color = new_color

    # class methods
    @classmethod
    def from_make_year(cls, color, make_year):
        age = date.today().year - make_year
        # returns a car
        return cls(color, age)
