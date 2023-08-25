m1=int(input("enter the mark of 1="))
m2=int(input("enter the mark of 2="))
m3=int(input("enter the mark of 3="))

if(m1>m2):
    if(m2>m3):
        total=m1+m2
    else:
        total=m1+m3
elif(m2>m1):
         total=m2+m3
print(total)
avg=total/2
print(avg)
    
 
