class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am studying {self.course}.")


class Student1(Student):

    def __init__(self, name, age, course):
        super().__init__(name, age, course)


# First student
name1 = input("Enter first student name: ")
age1 = int(input("Enter first student age: "))
course1 = input("Enter first student course: ")

student1 = Student(name1, age1, course1)

# Second student
name2 = input("\nEnter second student name: ")
age2 = int(input("Enter second student age: "))
course2 = input("Enter second student course: ")

student2 = Student1(name2, age2, course2)

# Display details
print("\n--- First Student ---")
student1.display_details()
student1.introduce()

print("\n--- Second Student ---")
student2.display_details()
student2.introduce()