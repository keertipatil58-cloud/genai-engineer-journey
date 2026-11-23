# Day 4 – Python Functions

## 📌 Overview
On Day 4 of my GenAI Engineer learning journey, I learned about Python functions and how to organize code into reusable blocks.

## 📚 Topics Covered

- What are functions?
- Creating functions using `def`
- Calling functions
- Parameters and arguments
- Multiple parameters
- `return` statement
- Difference between `print()` and `return`
- Default parameters
- Functions with lists

## 💻 Practical Project: My Skill Calculator

Created a Python program called `day4_my_skill_calculator.py`.

### Project Features
- Accepts three numbers from the user.
- Passes the numbers to a function.
- Calculates their total.
- Returns the result using the `return` statement.
- Displays the final result.

### Code Example

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
- How to create and call functions.
- How to pass information using parameters and arguments.
- How to return values from functions.
- Why reusable functions make programs easier to maintain.
- Difference between displaying a value and returning a value.

## 🤖 Connection to GenAI
Functions are important in GenAI applications because they help organize tasks such as:
- Processing user prompts.
- Calling AI models.
- Processing API responses.
- Handling document information.
- Reusing code in AI applications.

## 📈 Learning Progress
**Day 4: Completed ✅**