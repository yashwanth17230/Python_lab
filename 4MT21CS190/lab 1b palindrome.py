x=int(input("enter the number="))
count=x
t=0
while(x>0):
    rem=x%10
    t=t*10+rem
    x=x//10
if(t==count):
    print("palindrome")
else:
    print("not palindrome")

def palindrome(x1):
     while(x1>0):
         rem=x1%10
         print(rem,"no of occurances")
         x2.count(str(rem))
         x1=x//10
     palindrome(x)
         
