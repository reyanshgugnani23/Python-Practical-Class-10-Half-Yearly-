def vote():
    age = int(input("Enter Your Age: "))
    if age >= 18:
        print("Go Ahead, Vote!!.")
    else:
        print("Fallback to Safe Zone.")
#vote()

def gnum2():
    num1 = int(input("num1??: "))
    num2 = int(input("num2??: "))

    if num1 > num2:
        print("num 1 is greater")
    elif num2 > num1:
        print("num 2 is greater")
    else:
        print("Both Num Are same")
#gnum2()

def pnz():
    n = int(input("enter a num: "))

    if n > 0:
        print("+ve")
    elif n < 0:
        print("-ve")
    else:
        print("num is 0")
#pnz()

def grade():
    n = int(input("Enter marks: "))
    if n >= 90:
        print("A+")
    elif n >= 75:
        print("B+")
    elif n >= 50:
        print("C+")
    else:
        print("D+")
#grade()

def gnum3():
    n1 = int(input("Enter a num1: "))
    n2 = int(input("Enter a num2: "))
    n3 = int(input("Enter a num3: "))

    if n1 > n2 and n1 > n3:
        print("n1")
    elif n2 > n1 and n2 > n3:
        print("n2")
    elif n3 > n1 and n3 > n2:
        print("n3")
    elif n1 == n2 == n3:
        print("all numbers are same")
    else:
        pass
#gnum3()

def week():
    week = int(input("Enter a num between(1-7): "))
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if 1 <= week <= 7:
        print(days[week-1])
    else:
        print("invalid num")
#week()

def n10():
    for i in range(1,11):
        print(i)

    print()

    l = 1
    while 10 >= l:
        print(l)
        l += 1
#n10()

def odd10():
    for i in range(1,21,2):
        print(i)

    print()

    l = 1
    while l <= 19:
        print(l)
        l += 2
#odd10()

def even10():
    for i in range(2,21,2):
        print(i)

    print()

    l = 2
    while l <= 21:
        print (l)
        l += 2
#even10()

def total():
    total = 0
    for i in range(1, 11):
        total += i
    print("Sum:", total)

    totall = 0
    il = 1
    while il <= 10:
        totall += il
        il += 1
    print("Sum:", totall)
#total()

def fact():
    n = int(input("enter a num: "))
    fact = 1

    for i in range(1,n+1):
        fact *= i

    print(fact)
#fact()

def sd():
    n = int(input("Enter a num: "))
    sum = 0
    for digit in str(n):
        sum += int(digit)
    print(sum)

    print()

    nn = int(input("Enter a Numm: "))
    summ = 0
    while nn > 0:
        aa = nn%10
        summ = summ + aa
        nn = nn // 10
    print(summ)
#sd()

def rev():
    n = int(input("Enter a num: "))
    rev = 0
    for i in range(len(str(n))):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    print(rev)

    print()

    num = int(input("Enter A Num: "))
    sum = 0
    while num > 0:
        a = num % 10
        sum = sum * 10 + a
        num = num // 10
    print(sum)
#rev()

def table():
    n = int(input("enter a num: "))
    for i in range(1,11):
        p = n*i
        print(n, " x ", i, ' = ',p)

    print()

    n = int(input("enter a num: "))
    i=1
    while i <= 10:
        p=i*n
        print(n, " x ", i, ' = ',p)
        i+=1
#table()

def fib():
    n = int(input("enter a num: "))
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        a,b=b,b+a

    print()

    n = int(input("enter a num: "))
    a=0
    b=1
    count = 0
    while count <=n:
        print(count)
        a=b
        b = count
        count = a+b

fib()
