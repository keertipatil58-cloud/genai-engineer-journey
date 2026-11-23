#1. Function 
#code without function
print("Hello Keerti!")
print("Welcome to GenAI!")
print("Keep Learning Python!")

print("Hello Raj!")
print("Welcome to GenAI!")
print("Keep Learning Python!")

#code with function
def welcome():
    print("Hello!")
    print("Welcome to GenAI!")
    print("Keep Learning Python!")

welcome()
welcome()

#function with parameters
def greet(name):
    print(f"Hello {name}!")
    print("Welcome to your GenAI journey!")

greet("Keerti")
greet("Raj")
greet("Karunya")

#multiple parameters
def student_profile(name, course, age):
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"Age: {age}")

student_profile("Keerti", "GenAI Engineering", 21)

#return statement
def add(a, b):
    result = a + b
    return result

answer = add(10, 20)
print(answer)

#another example
def multiply(x, y):
    return x * y

result = multiply(5, 6)
print(result)

#functions with lists
def display_skills(skills):
    for skill in skills:
        print(skill)

my_skills = ["Python", "SQL", "HTML", "GenAI"]
display_skills(my_skills)