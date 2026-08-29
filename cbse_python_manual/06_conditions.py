# CBSE Python reference: if, if-else, if-elif-else and nested if

# Syntax:
# if condition:
#     statement(s)

num = 7
if num > 0:
    print("Positive number")

# if-else
age = 16
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# if-elif-else
marks = 82
if marks >= 90:
    grade = "A1"
elif marks >= 80:
    grade = "A2"
elif marks >= 70:
    grade = "B1"
else:
    grade = "B2"
print("Grade:", grade)

# Nested if
n = 0
if n >= 0:
    if n == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
