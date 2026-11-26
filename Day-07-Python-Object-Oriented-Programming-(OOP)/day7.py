#oop concepts
#class
class Student:
    name = "Keerti"
    age = 21
    course = "Computer Science"

#object
class Student:
    name = "Keerti"
    age = 21

student1 = Student()

print(student1.name)
print(student1.age)


#_init_ method
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Keerti", 21, "Computer Science")
print(student1.name)
print(student1.age)
print(student1.course)

#self parameter
class Student:
    def __init__(self, name):
        self.name = name

Student1 = Student("Keerti")
Student2 = Student("Raj")

print(Student1.name)
print(Student2.name)

# Methods
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
       print(f"My name is {self.name}")
       print(f"I am learning {self.course}") #or
       print(f"Hello, my name is {self.name} and I am studying {self.course}.")

student1 = Student("Keerti", "GenAI")
student1.introduce()

#Inheritance
class Person:
    def introduce(self):
        print("I am a person.")

class Student(Person):
    def study(self):
        print("I am a studing Python.")

student1 = Student()
student1.introduce()
student1.study()
