def isphonenumber(n):
    if(len(n)!=12):
        return print("it is not a phone number")
    for i in range(0,3):
        if not n[i].isdecimal():
            return print("it is not a phone number")
    if n[3] and n[7]!= '-':
        return print("it is not a phone number")
    for i in range(4,7):
        if not n[i].isdecimal():
            return print("it is not a phone number")
    for i in range(8,12):
        if not n[i].isdecimal():
            return print("it is not a phone number")
    return print(" given input is a phone number")
        

n=input("Entre the phne number:")
isphonenumber(n)
    
