def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def calculator():
    print("Welcome to the Calculator!")
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        
        operation = input("Enter operation (+, -, *, /): ").strip()
        
        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            raise ValueError("Invalid operation!")
        
        print(f"The result is: {result}")
    
    except ValueError as e:
        print(f"Error: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()


