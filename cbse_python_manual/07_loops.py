# CBSE Python reference: for and while loops

# Syntax of for loop:
# for val in sequence:
#     body

numbers = [6, 5, 3, 8, 4]
total = 0
for value in numbers:
    total = total + value
print("The sum is", total)

# range() is useful for repeated numeric iterations
for i in range(1, 6):
    print(i)

# Syntax of while loop:
# while test_expression:
#     body

n = 10
total = 0
i = 1
while i <= n:
    total = total + i
    i = i + 1
print("The sum is", total)

# Always update the counter in a counter-controlled while loop.
