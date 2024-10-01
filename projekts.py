def calculator():
    print("Welcome to the Simple Calculator!")

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b == 0:
            print("Error: Cannot divide by zero!")
            return
        result = a / b
    else:
        print("Invalid operation!")
        return

    print("The result is:", result)

# Run the calculator
if __name__ == "__main__":
    calculator()
