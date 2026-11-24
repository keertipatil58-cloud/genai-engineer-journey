try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Choose operation (+, -, *, /): ")

    result = None

    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        result = num1 / num2

    else:
        print("Invalid operation!")

    if result is not None:
        print("Result:", result)

except ZeroDivisionError:
    print("Error! Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")