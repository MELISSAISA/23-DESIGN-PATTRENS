import random

class Car:
    def __init__(self):
        self.generator = random.Random()

    def accelerate(self):
        speed = self.generator.randint(50, 100)
        print(f"The speed of the car is {speed} mph")

    def apply_brakes(self):
        speed = self.generator.randint(20, 40)
        print(f"The speed of the car is {speed} mph after applying the brakes")

    def assign_driver(self, driver_name):
        print(f"{driver_name} is driving the car")


