

# # 1. write a python program to calculate roots of a quadratic equation




a = int(input("enter the values of a :"))
b = int(input("enter the values of b :"))
c = int(input("enter the values of c :"))
d = (b*b)-(4*a*c)
deno = 2*a
if(d>0):
    print("Real Roots")
    root1 = (-b + d**0.5)/deno
    root2 = (-b - d**0.5)/deno
    print("Root1 =",root1,"\tRoot2 =",root2)
elif(d==0):
    print("Eual Roots")
    root = -b/deno
    print("Root1 and Root2 =",root)
else:
    print("Imaginary Roots")



# # 2. Write a program to enter a numberr and then calculate the sum of its digits




sumOfDigits = 0
num = int(input("Enter the number:"))
while(num!=0):
    temp = num % 10
    sumOfDigits = sumOfDigits + temp
    num = num // 10

print("The sum of digits is :",sumOfDigits)


# # 3.write a program using for loop to calculate factorial of a number




num = int(input("Enter the number"))
if(num==0):
    fact =1
else:
    fact=1
    for i in range(1,num+1):
        fact = fact * i
print("Factorial of ",num, "is",fact)


# # 4. Write a program to find the sum of given two numbers using lambda function




a = int(input("Enter the first number:"))
b = int(input("Enter the second number"))
sum = lambda x,y:x+y
print("sum of given two numbers",sum(a,b))


# # 5. write a program to swap two numbers using fucntions




def swap(a,b):
    a,b = b,a
    print("After swaping :")
    print("First Number :",a)
    print("Second Number :", b)

a= int(input("Enter the first number:"))
b = int(input("Enter the Second number :"))
print("Before swaping:")
print("First Number :",a)
print("Second Number :", b)
swap(a,b)


# # 6. Write a python program calculate the sum of A1 to A5 cell in excel sheet and add the sum in A7 cell




# import openpyxl module
import openpyxl

# Call a Workbook() function of openpyxl
# to create a new blank Workbook object
wb = openpyxl.Workbook()

# Get workbook active sheet
# from the active attribute.
sheet = wb.active

# writing to the cell of an excel sheet
sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = 400
sheet['A4'] = 500
sheet['A5'] = 600

# The value in cell A7 is set to a formula
# that sums the values in A1, A2, A3, A4, A5 .
sheet['A7'] = '= SUM(A1:A5)'

# save the file
wb.save("sum.xlsx")


# # 7. Write a python program to create the json from dictionary 

import json

# Data to be written
dictionary = {
	"name": "sathiyajith",
	"rollno": 56,
	"cgpa": 8.6,
	"phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
	outfile.write(json_object)


# Opening JSON file
with open('sample.json', 'r') as openfile:

	# Reading from json file
	json_object = json.load(openfile)

print(json_object)
print(type(json_object))






