class Emp:
    def __init__(self):
        self.ename=" "
        self.empid=" "
        self.deptid=" "
        self.salary= 0
    def getvalue(self):
        self.ename=input("Enter the name of employee:")
        self.empid=input("Enter the employee id:")
        self.deptid=input("Enter the employee department id:")
        self.salary=float(input("Enter the salary of employee:"))
    def showvalue(self):
        print("*************************************************")
        print("Name of the employee:",self.ename)
        print("Employee id:",self.empid)
        print("Department id:",self.deptid)
        print("Employee salary:",self.salary)

e1=Emp()
e1.getvalue()
e1.showvalue()
