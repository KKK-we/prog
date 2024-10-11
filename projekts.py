
def dalisana(num1, num2):
    if num2 == 0:
        return "Nevar dalīt ar 0!!!"
    return num1/num2

def reizinasana(num1,num2):
    return num1*num2

def saskaitisana(num1,num2):
    return num1+num2 
    
def atnemsana(num1,num2):
    return num1-num2

def calculator():
    print("Welcome to the Calculator!")

    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    if a.isnumeric() and b.isnumeric():
        a = int(a)
        b = int(b)
        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            result = saskaitisana(a,b)
        elif operation == "-":
            result = atnemsana(a,b)
        elif operation == "*":
            result = reizinasana(a,b)
        elif operation == "/":
            result = dalisana(a,b)
        else:
            print("Error")
            return

        print("The result is:", result)
    else:
        print("Ievadi skaitļus")


answer = "yes"

while answer == "yes":

    
    calculator()
    answer = input("Vai vēlies turpināt? (ievadi 'yes'): ")
    