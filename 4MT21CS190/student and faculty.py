class Student:
    def __init__(self):
        self.name=" "
        self.reg= " "
        self.dept=" "
        self.year=0
    def getvalue(self):
        self.name=input("Enter the Student name:")
        self.reg=input("Enter the registeration id:")
        self.dept=input("Enter the department")
        self.year=int(input("Enter the semester of student:"))
        
    def showvalue(self):
        print("Name of the student:",self.name)
        print("Registeration id:",self.reg)
        print("Department:",self.dept)
        print("Semester of student:",self.year)
        print("======================*****************==============")

class Faculty:
    def __init__(self):
        self.fname=" "
        self.fid= " "
        self.sub=" "
        self.year=0
    def getvalue(self):
        self.fname=input("Enter the faculty name:")
        self.fid=input("Enter the faculty id:")
        self.sub=input("Enter the subject taken")
        self.year=int(input("Enter the semester taken classes:"))
    def showvalue(self):
        print("*************************************************")
        print("Name of the faculty:",self.fname)
        print("faculty id:",self.fid)
        print("subject:",self.sub)
        print("Semester of taken classes:",self.year)

g1=Student()
g2=Faculty()

g1.getvalue()
g2.getvalue()

g1.showvalue()
g2.showvalue()
