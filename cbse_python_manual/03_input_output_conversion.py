# CBSE Python reference: print(), input() and type conversion

# Output
print("Hello, Python!")
print("Total:", 10 + 20)

# User input returns text (string)
name = input("Enter your name: ")
print("Hello", name)

# Explicit conversion
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
print(age, height)

# Common conversion functions
number = 25
print(str(number) + " apples")
print(int(20.8))
print(float(10))
print(bool(5))

# Simple calculation using converted input
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print("Sum =", first + second)
