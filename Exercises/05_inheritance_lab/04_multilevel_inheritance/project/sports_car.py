from project.car import Car


class SportsCar(Car):
    def race(self):
        return "racing..."

# https://judge.softuni.org/Contests/Practice/Index/1940#4

# 4.	Multilevel Inheritance
# In a folder called project create three files: vehicle.py and car.py, and sports_car.py.
# In each file, create its corresponding class - Vehicle, Car, and SportsCar:
# •	Vehicle with a single method move() that returns: "moving..."
# •	Car with a single method drive() that returns: "driving..."
# •	SportsCar with a single method race() that returns: "racing...".
# SportsCar should inherit from Car and Car should inherit from Vehicle.
# Submit in Judge a zip file of the folder project.