n=int(input("enter the number"))
def dectobin(n1):
    if(n1>=1):
        dectobin(n1//2)
        print(n1%2)

dectobin(n)
    
