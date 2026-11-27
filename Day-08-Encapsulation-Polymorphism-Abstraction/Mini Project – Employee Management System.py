from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_salary(self):
        print("Salary:", self.__salary)

    @abstractmethod
    def calculate_bouns(self):
        pass

class Developer(Employee):
    def calculate_bouns(self):
        print("Developer bouns:", 5000)

class Tester(Employee):
    def calculate_bouns(self):
        print("Tester bouns:", 3000)

developer = Developer("Keerti", 30000)
tester = Tester("Raj", 25000)

developer.show_salary()
developer.calculate_bouns()

tester.show_salary()
tester.calculate_bouns()