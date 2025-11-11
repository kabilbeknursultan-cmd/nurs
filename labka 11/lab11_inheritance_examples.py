"""
lab11_inheritance_examples.py
Содержит 5 отдельных примеров (работ) по наследованию и полиморфизму.
"""

from abc import ABC, abstractmethod

# === Example 1 ===
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print(f"{self.name} writes code. Salary: {self.salary}$")

class Designer(Employee):
    def work(self):
        print(f"{self.name} designs UI/UX. Salary: {self.salary}$")

class Manager(Employee):
    def work(self):
        print(f"{self.name} manages team. Salary: {self.salary}$")


def run_example1():
    workers = [Developer("Aruzhan", 2000), Designer("Dias", 1800), Manager("Nursultan", 3000)]
    for w in workers:
        w.work()


# === Example 2 ===
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes some sound")

class Lion(Animal):
    def sound(self):
        super().sound()
        print("The lion roars!")

class Snake(Animal):
    def sound(self):
        super().sound()
        print("The snake hisses!")


def run_example2():
    animals = [Lion("Simba"), Snake("Kaa")]
    for a in animals:
        a.sound()


# === Example 3 ===
class SaleMixin:
    def apply_discount(self, percent):
        new_price = self.price - (self.price * percent / 100)
        print(f"Discount applied! New price: {new_price}")

class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def info(self):
        print(f"Product: {self.title}, Price: {self.price}")

class Phone(Product, SaleMixin):
    pass


def run_example3():
    iphone = Phone("iPhone 15", 1200)
    iphone.info()
    iphone.apply_discount(10)


# === Example 4 ===
class Transport(ABC):
    @abstractmethod
    def trip_cost(self, km):
        pass

class Taxi(Transport):
    def trip_cost(self, km):
        return km * 200

class Scooter(Transport):
    def trip_cost(self, km):
        return 100 + km * 50


def run_example4():
    vehicles = [("Taxi", Taxi()), ("Scooter", Scooter())]
    distance = 10
    for name, v in vehicles:
        print(f"{name} trip for {distance} km: {v.trip_cost(distance)}")


# === Example 5 ===
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching students")

class Professor(Teacher):
    def research(self):
        print(f"{self.name} is doing scientific research")


def run_example5():
    p = Professor("Dr. Adil")
    p.teach()
    p.research()


if __name__ == "__main__":
    run_example1()
    run_example2()
    run_example3()
    run_example4()
    run_example5()
