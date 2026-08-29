# CBSE Python reference: common data types and collections

integer_value = 42
float_value = 15.6
text = "Python"
boolean_value = True
nothing = None

print(type(integer_value))
print(type(float_value))
print(type(text))
print(type(boolean_value))
print(type(nothing))

# String
name = 'Python'
print(name)

# List: ordered and mutable
numbers = [10, 20, 30, 40]
numbers.append(50)
print(numbers)

# Tuple: ordered and immutable
t = (5, 'program', 2.5)
print(t)

# Set: unordered collection without duplicate entries
values = {1, 2, 2, 3, 3}
print(values)

# Dictionary: key-value pairs
student = {"name": "Aarav", "class": 10}
print(student)
print(student["name"])
