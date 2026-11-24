#module created for calculator functions
#done in calculator.py
# and imported in main.py


#different ways to import modules
#method 1: import the complete module
import math
print(math.sqrt(25))  # Output: 4.0

#method 2: import specific functions from a module
from math import sqrt
print(sqrt(36))  # Output: 6.0

#method 3: import a module with an alias
import math as m
print(m.sqrt(49))  # Output: 7.0


#writing into a file
file = open("my_learning.txt", "w")
file.write("I am learning Python.\n")
file.write("My goal is to become a GenAI Engineer.")
file.close()

#reading from a file
file = open("my_learning.txt", "r")
content = file.read()
print(content)
file.close()

#A Better way: "with open() as file" automatically closes the file after the block of code is executed
with open("my_learning.txt", "w") as file:
    file.write("I am learning Python.\n")
    file.write("My goal is to become a GenAI Engineer.")

with open("my_learning.txt", "r") as file:
    content = file.read()
    print(content)