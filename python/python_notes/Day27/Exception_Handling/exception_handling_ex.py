def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a / b
        else:
            raise ValueError("Invalid operation")
    except ValueError as e:
        print("Value Error:", e)
    except ZeroDivisionError as e:
        print("Math Error:", e)
    else:
        print("Result:", result)
    finally:
        print("Calculator execution completed")
calculator()