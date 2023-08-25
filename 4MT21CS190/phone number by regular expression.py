import re
txt=input("enter the phone number:")
p1=re.compile(r'\d{3}-\d{3}-\d{4}')
p2 = p1.search(txt)
print(p2.groups(1))
if(txt==p2.group()):
    print("It is phone number")
else:
    print("It is not phone number")
