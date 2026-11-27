#Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:",self.__balance)

account = BankAccount(10000)

account.deposit(2000)

account.show_balance()


#polymorphism
class Dog:
    def sound(self):
        print("Dog braks.")

class Cat:
    def sound(self):
        print("Cat meows.")

class Cow:
    def sound(self):
        print("Cow moos.")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()


#abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")

car = Car()
bike = Bike()
car.start()
bike.start()
