#conditional statements
#A. if statement
age =21
if age >= 18:
    print("You are eligible to vote.")

#another example

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")



#B. if-else statement
marks = 45
if marks >= 35:
    print("You Passed!")
else:
    print("You failed.")

#another example

marks = int(input("Enter your marks: "))
if marks >= 35:
    print("You Passed!")
else:
    print("You failed.")


#C. if-elif-else statement
marks = 85
if marks >= 90:
    print("Excellent")
elif marks >= 70:
    print("Very Good")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

#another example

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Excellent")
elif marks >= 70:
    print("Very Good")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")


#Comparison operators
# ==, !=, >, <, >=, <=
a = 10
b = 20
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True

#Logical operators
# and, or, not
#1 AND operator
age = 21
has_degree = True
if age >= 18 and has_degree:
    print("You are eligible for the job.")

#another example

age = int(input("Enter your age: "))
has_degree = input("Do you have a degree? (yes/no): ").lower() == "yes"
if age >= 18 and has_degree:
    print("You are eligible for the job.")

#2 OR operator
knows_python = True
knows_java = False
if knows_python or knows_java:
    print("You know a programming language.")

#another example

knows_python = input("Do you know Python? (yes/no): ").lower() == "yes"
knows_java = input("Do you know Java? (yes/no): ").lower() == "yes"
if knows_python or knows_java:
    print("You know a programming language.")

#3 NOT operator
is_learning = True
print(not is_learning)  # False

#another example

is_learning = input("Are you learning programming? (yes/no): ").lower() == "yes"
print(not is_learning)  # False if learning, True if not learning

#for loop
for i in range(1, 6):
    print(i)


#another example
skills = ["Python", "SQL", "HTML", "GenAI"]

for skill in skills:
    print(skill)


#while loop
count = 1
while count <= 5:
    print(count)
    count = count + 1

