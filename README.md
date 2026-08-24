# Python Practical – Class 10 Half-Yearly

Programs transcribed from **BASICS OF PYTHON PROGRAMMING(1).pdf** used for Python Programming at Amity International School, Sector-46, Gurugram.

## Contents
- `examples/` – Python code examples shown in the introductory sections of the PDF
- `if_else/` – 6 conditional-statement programs
- `loops/for/` – For-loop versions of the practical programs
- `loops/while/` – While-loop versions of the practical programs
- `patterns/` – Pattern-printing programs

The practical-program list in the PDF contains 6 if-else programs and 11 for/while-loop tasks. The code is kept faithful to the PDF, including the apparent source-code behavior/errors in the shown examples.

# AI Practical

## IF-ELSE PROGRAMS

**1. Check if a person can vote**
```python
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

**2. Greatest of two numbers**
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")
```

**3. Positive, negative or zero**
```python
n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```

**4. Grade of student**
```python
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade D")
```

**5. Greatest of three numbers**
```python
x = int(input("Enter first: "))
y = int(input("Enter second: "))
z = int(input("Enter third: "))
if x >= y and x >= z:
    print(x, "is greatest")
elif y >= x and y >= z:
    print(y, "is greatest")
else:
    print(z, "is greatest")
```

**6. Week number to day name**
```python
week = int(input("Enter week number (1-7): "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]
if 1 <= week <= 7:
    print(days[week - 1])
else:
    print("Invalid week number")
```

## LOOP PROGRAMS (for + while, fixed count of 10)

**7. First 10 natural numbers**
```python
for i in range(1, 11):
    print(i, end=" ")

i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
```

**8. First 10 odd numbers**
```python
for i in range(1, 20, 2):
    print(i, end=" ")

i = 1
while i <= 19:
    print(i, end=" ")
    i += 2
```

**9. First 10 even numbers**
```python
for i in range(2, 21, 2):
    print(i, end=" ")

i = 2
while i <= 20:
    print(i, end=" ")
    i += 2
```

**10. Sum of first 10 natural numbers**
```python
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("Sum:", total)
```

**11. Factorial of a number**
```python
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)
```

**12. Sum of digits of a number**
```python
n = int(input("Enter a number: "))
s = 0
for i in str(n):
    s += int(i)
print("Sum of digits:", s)

n = int(input("Enter a number: "))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Sum of digits:", s)
```

**13. Reverse a given number**
```python
n = int(input("Enter a number: "))
rev = 0
temp = n
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reversed:", rev)
```

**14. First 10 numbers in reverse order**
```python
for i in range(10, 0, -1):
    print(i, end=" ")

i = 10
while i >= 1:
    print(i, end=" ")
    i -= 1
```

**15. Fibonacci series**
```python
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

n = int(input("Enter number of terms: "))
a, b = 0, 1
i = 0
while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
```

## TABLES & MATH

**16. Multiplication table (fixed, 10 terms)**
```python
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```

**17. Multiplication table (n terms)**
```python
n = int(input("Enter number: "))
terms = int(input("Enter number of terms: "))
for i in range(1, terms + 1):
    print(n, "x", i, "=", n * i)
```

**18. Simple interest**
```python
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)
```

## LOOPS WITH n AS INPUT

**19. First n natural numbers**
```python
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i, end=" ")
```

**20. First n odd numbers**
```python
n = int(input("Enter n: "))
for i in range(1, 2 * n, 2):
    print(i, end=" ")
```

**21. First n even numbers**
```python
n = int(input("Enter n: "))
for i in range(2, 2 * n + 1, 2):
    print(i, end=" ")
```

**22. Sum of first n natural numbers**
```python
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)
```

## LIST PROGRAMS

**23. Sum of list elements**
```python
lst = [10, 20, 30, 40, 50]
total = 0
for i in lst:
    total += i
print("Sum:", total)
# shortcut
print("Sum:", sum(lst))
```

**24. List operations (append, insert, remove, pop, sort, reverse)**
```python
lst = [10, 30, 20, 50]
lst.append(60)
lst.insert(1, 15)
lst.remove(30)
lst.pop()
lst.sort()
print("Final list:", lst)
lst.reverse()
print("Reversed list:", lst)
```

**25. List indexing**
```python
lst = ["a", "b", "c", "d", "e"]
print("First element:", lst[0])
print("Last element:", lst[-1])
print("Third element:", lst[2])
print("Second last:", lst[-2])
```

**26. Even number list, then convert to odd (+1)**
```python
even_list = []
for i in range(2, 21, 2):
    even_list.append(i)
print("Even list:", even_list)

odd_list = []
for i in even_list:
    odd_list.append(i + 1)
print("Odd list:", odd_list)
```

**27. Extend and sort**
```python
list1 = [10, 40, 20]
list2 = [15, 5, 30]
list1.extend(list2)
list1.sort()
print("Sorted list:", list1)
```

**28. Science quiz list task (remove, append, pop by index)**
```python
children = ["Arjun", "Sonakshi", "Vikram", "Sandhya", "Sonal", "Isha", "Kartik"]
print("Initial list:", children)
children.remove("Vikram")
children.append("Jay")
children.pop(1)
print("Final list:", children)
```

**29. List length and slicing (positive + negative)**
```python
num = [23, 12, 5, 9, 65, 44]
print("Length:", len(num))
print("2nd to 4th (positive index):", num[1:4])
print("3rd to 5th (negative index):", num[-4:-1])
```

## STAR PATTERNS & SHAPES

**30. Right triangle (left-aligned)**
```python
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    print("*" * i)
```

**31. Left triangle (right-aligned)**
```python
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
```

**32. Center (pyramid) triangle**
```python
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

**33. Rectangle**
```python
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
for i in range(rows):
    print("*" * cols)
```

**34. Square**
```python
n = int(input("Enter side: "))
for i in range(n):
    print("*" * n)
```
