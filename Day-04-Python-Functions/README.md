# Day 4 – Python Functions

## 📌 Overview

On Day 4 of my GenAI Engineer learning journey, I learned how to create reusable blocks of code using Python functions. I also practised passing values to functions and returning results.

## 📚 Topics Covered

### 1. Introduction to Functions
- What are Python functions?
- Creating functions using `def`.
- Calling functions.
- Understanding reusable code.

### 2. Parameters and Arguments
- Understanding parameters.
- Understanding arguments.
- Passing multiple arguments to functions.

### 3. Return Statement
- Using the `return` statement.
- Difference between `print()` and `return`.
- Returning calculated values from functions.

### 4. Default Parameters
- Creating functions with default parameter values.
- Understanding how default arguments work.

### 5. Functions with Lists
- Passing lists as function arguments.
- Working with list data inside functions.

## 💻 Practical Project: My Skill Calculator

Created a Python program called `day4_my_skill_calculator.py`.

### Project Features
- Accepts three numbers from the user.
- Passes the numbers to a function.
- Calculates the total using a function.
- Returns the result using `return`.
- Displays the final calculated result.

### Python Code

```python
def calculate_total(num1, num2, num3):
    return num1 + num2 + num3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

total = calculate_total(num1, num2, num3)

print("Total:", total)
```

## 🛠️ Technologies Used
- Python
- VS Code

## 🎯 What I Learned
- How to create and call Python functions.
- Difference between parameters and arguments.
- How to return values from functions.
- Difference between `print()` and `return`.
- How functions make code reusable and organized.

## 🤖 Connection to GenAI

Functions are important in
