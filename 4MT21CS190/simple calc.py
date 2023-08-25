def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mult(x,y):
    return(x*y)
def square(x,y):
    return(x**y)
def div(x,y):
    return(x//y)
def mod(x,y):
    return(x%y)

a=float(input("enter the number:"))
b=float(input("enter the number:"))

print("addition of two numbers",add(a,b))
print("subration of two numbers",sub(a,b))
print("multiplication of two numbers",mult(a,b))
print("square of two numbers",square(a,b))
print("divison of two numbers",div(a,b))
print("modulus of two numbers",mod(a,b))
