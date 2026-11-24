#exception handling
#code to understand try and except block
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error! You cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

#understanding else and finally block
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Enter valid numbers.")

else:
    print("Result:", result)

finally:
    print("Calculator program finished.")


#common python exceptions
"""
| Error | Meaning |
|---|---|
| `ValueError` | Invalid value |
| `TypeError` | Wrong data type |
| `NameError` | Variable not defined |
| `ZeroDivisionError` | Division by zero |
| `IndexError` | Invalid list index |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | Requested file doesn't exist | 
"""

