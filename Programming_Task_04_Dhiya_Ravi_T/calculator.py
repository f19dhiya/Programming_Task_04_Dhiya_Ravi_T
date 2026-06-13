def addition(a, b):
    
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! You cannot divide by zero."
    return a / b


print("=== Simple Calculator ===\n")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nEnter Choice: "))

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == 1:
    result = addition(num1, num2)
elif choice == 2:
    result = subtraction(num1, num2)
elif choice == 3:
    result = multiplication(num1, num2)
elif choice == 4:
    result = division(num1, num2)
else:
    result = "Invalid choice! Please enter a number between 1 and 4."

print(f"\nResult: {result}")