n=int(input("enter the number "))
a=0
b=1
c=0
print(a,end=" ")
print(b,end=" ")
for i in range(n):
    c=a+b
    print(c)
    a=b
    b=c
