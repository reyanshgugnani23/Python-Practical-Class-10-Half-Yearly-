n= int(input("Enter the number of terms="))
a=0
b=1
count=0
while(count<=n):
    print(count)
    a=b
    b=count
    count=a+b
