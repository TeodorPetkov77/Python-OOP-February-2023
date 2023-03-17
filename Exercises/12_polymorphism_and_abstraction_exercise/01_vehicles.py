from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle, ABC):
    ac_consumption = 0.9
    fuel_tank_quality = 1

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumed_fuel = distance * (self.fuel_consumption + self.ac_consumption)
        if self.fuel_quantity >= consumed_fuel:
            self.fuel_quantity -= consumed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.fuel_tank_quality


class Truck(Vehicle, ABC):
    ac_consumption = 1.6
    fuel_tank_quality = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumed_fuel = distance * (self.fuel_consumption + self.ac_consumption)
        if self.fuel_quantity >= consumed_fuel:
            self.fuel_quantity -= consumed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.fuel_tank_quality


# https://judge.softuni.org/Contests/Compete/Index/1943#0

# 1.	Vehicle
# Create an abstract class called Vehicle that should have abstract methods drive and refuel. Create 2 vehicles that inherit the Vehicle class (a Car and a Truck) and simulates driving and refueling them. Car and Truck both receive fuel_quantity and fuel_consumption in liters per km upon initialization. They both can be driven a given distance: drive(distance) and refueled with a given amount of fuel: refuel(fuel). It is summer, so both vehicles use air conditioners, and their fuel consumption per km when driving is increased by 0.9 liters for the car and 1.6 liters for the truck. Also, the Truck has a tiny hole in its tank, and when it is refueled, it keeps only 95% of the given fuel. The car has no problems and adds all the given fuel to its tank. If a vehicle cannot travel the given distance, its fuel does not change.
# Note: Submit all your classes and imports in the judge system
# Examples
# Test Code	Output
# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)	2.299999999999997
# 12.299999999999997
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)	17.0
# 64.5
