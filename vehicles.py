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

class Motorcycle:
    def __init__(self):
        self.generator = random.Random()

    def rev_throttle(self):
        speed = self.generator.randint(50, 100)
        print(f"The speed of the motorcycle is {speed} mph")

    def pull_brake_lever(self):
        speed = self.generator.randint(20, 40)
        print(f"The speed of the motorcycle is {speed} mph after applying the brakes")

    def assign_rider(self, rider_name):
        print(f"{rider_name} is riding the motorcycle")
