n=input("=>")
w,d,u,l=0,0,0,0
l_w=n.split()
print(l_w)
x=len(l_w)
print(x)

for i in n:
    if(i.isdigit()):
        d=d+1
    elif( i.isupper()):
        u=u+1
    elif(i.islower()):
        l=l+1 
print("no of words",x,"no of digits",d,"no of upper case letters",u,"no of lower case letters",l)
s
