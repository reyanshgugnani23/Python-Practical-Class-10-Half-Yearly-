num = int(input("Enter a number: "))
rev = 0
num_str = str(num)
for i in range(len(num_str)):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed number:", rev)
