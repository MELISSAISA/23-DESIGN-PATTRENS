# Abstract Factory
from abc import ABC, abstractmethod
class VehicleFactory(ABC):
    def create_car(self):
        pass

    def create_motorcycle(self):
        pass

# Concrete Factory for Mercedes
class MercedesFactory(VehicleFactory):
    def create_car(self):
        return MercedesCar()

    def create_motorcycle(self):
        return MercedesMotorcycle()

# Concrete Factory for BMW
class BMWFactory(VehicleFactory):
    def create_car(self):
        return BMWCar()

    def create_motorcycle(self):
        return BMWMotorcycle()

# Abstract Products
class Car:
    def drive(self):
        pass

class Motorcycle:
    def ride(self):
        pass

# Concrete Products for Mercedes
class MercedesCar(Car):
    def drive(self):
        return "Mercedes car is driving."

class MercedesMotorcycle(Motorcycle):
    def ride(self):
        return "Mercedes motorcycle is riding."

# Concrete Products for BMW
class BMWCar(Car):
    def drive(self):
        return "BMW car is driving."

class BMWMotorcycle(Motorcycle):
    def ride(self):
        return "BMW motorcycle is riding."

# Client Code
def create_vehicle(factory):
    car = factory.create_car()
    motorcycle = factory.create_motorcycle()
    return car, motorcycle

# Testing the Abstract Factory
mercedes_factory = MercedesFactory()
bmw_factory = BMWFactory()

mercedes_car, mercedes_motorcycle = create_vehicle(mercedes_factory)
bmw_car, bmw_motorcycle = create_vehicle(bmw_factory)

print(mercedes_car.drive())         # Output: Mercedes car is driving.
print(mercedes_motorcycle.ride())   # Output: Mercedes motorcycle is riding.
print(bmw_car.drive())              # Output: BMW car is driving.
print(bmw_motorcycle.ride())        # Output: BMW motorcycle is riding.

