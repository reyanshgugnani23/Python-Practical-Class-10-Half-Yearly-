# CBSE Python Syntax Cheat Sheet

Based on the Python topics and syntax covered in the CBSE Python Content Manual.

## Variables
```python
variable = value
x, y = 5, 10
x = y = 0
```

## Input / output
```python
print(value)
name = input("Enter name: ")
age = int(input("Enter age: "))
```

## Type conversion
```python
int(value)
float(value)
str(value)
bool(value)
```

## If
```python
if condition:
    statements
```

## If-else
```python
if condition:
    statements
else:
    statements
```

## If-elif-else
```python
if condition1:
    statements
elif condition2:
    statements
else:
    statements
```

## Nested if
```python
if condition1:
    if condition2:
        statements
```

## For loop
```python
for value in sequence:
    statements
```

## While loop
```python
while condition:
    statements
```

## List
```python
my_list = [item1, item2, item3]
my_list[index]
my_list[start:end]
my_list.append(item)
my_list.extend(other_list)
my_list.remove(item)
```

## Tuple
```python
my_tuple = (item1, item2, item3)
my_tuple[index]
```

## Dictionary
```python
student = {"name": "Aarav", "class": 10}
student["name"]
```

## Package import
```python
import numpy
import numpy as np
from numpy import array
from numpy import array as arr
```

## NumPy array
```python
import numpy as np
A = np.array([1, 2, 3])
np.zeros((4, 3))
np.full((3, 4), 6)
np.arange(0, 30, 5)
```

## Important Python rule
Indentation defines the body of `if`, `for`, `while`, and other compound statements. A colon `:` begins the indented block.
