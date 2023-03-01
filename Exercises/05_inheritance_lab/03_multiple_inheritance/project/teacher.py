from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


# https://judge.softuni.org/Contests/Practice/Index/1940#2

# 3.	Multiple Inheritance
# In a folder called project create three files: person.py, employee.py, and teacher.py.
# In each file, create its corresponding class - Person, Employee, and Teacher:
# •	Person with a single method sleep() that returns: "sleeping..."
# •	Employee with a single method get_fired() that returns: "fired..."
# •	Teacher with a single method teach() that returns: "teaching...".
# Teacher should inherit from Person and Employee.
# Submit in Judge a zip file of the folder project.