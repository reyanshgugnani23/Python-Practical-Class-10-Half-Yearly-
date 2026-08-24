# CBSE Python reference: lists, indexing and slicing; tuples

numbers = [23, 12, 5, 9, 65, 44]

# Indexing
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:4])
print(numbers[2:])
print(numbers[:-2])
print(numbers[:])
print(numbers[::-1])

# Common list operations
numbers.append(100)
numbers.extend([7, 8])
numbers.remove(5)
print(numbers)
print(len(numbers))

# Tuple
t = (10, 20, 30, 40)
print(t[1])
print(t[1:3])

# Tuples cannot be changed after creation.
# del t removes the complete tuple.
