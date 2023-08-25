import math
class shape:
    def __init__(self):
        self.area=0
        self.name=" "
    def display(self):
        print("area of ",self.name,"is:",self.area)
class circle(shape):
    def __init__(self,rad):
        self.area=0
        self.name="circle"
        self.rad=rad
    def calcArea(self):
        self.area=self.rad*self.rad*math.pi
class triangle(shape):
    def __init__(self,base,height):
        self.area=0
        self.name="triangle"
        self.base=base
        self.height=height

    def calcArea(self):
        self.area=0.5*self.base*self.height

class rectangle(shape):

    def __init__(self,length,breadth):
        self.area=0
        self.name="rectangle"
        self.length=length
        self.breadth=breadth
    def calcArea(self):
        self.area=self.length*self.breadth

c1= circle(5)
c1.calcArea()
c1.display()

t1=triangle(3,4)
t1.calcArea()
t1.display()

r1=rectangle(5,4)
r1.calcArea()
r1.display()
