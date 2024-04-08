import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return x ** y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")
print("6. Power")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")

choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

if choice in ['1', '2', '3', '4', '6', '7', '8', '9']:

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero!"
        return x / y

def calculator():
    print("Welcome to the calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting the calculator.")
            break
        
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please try again.")
            continue
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid input. Please try again.")
            continue

calculator()