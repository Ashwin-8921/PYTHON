'''
13. The Shape Family: Hierarchies for Area and Perimeter
Scenario:
Simulate a graphics editor: various shapes with their own formulas.

What you’ll learn:
Creating class hierarchies
Overriding methods for specialized behavior

Task:
Write a Shape base class, then subclasses for Circle, Triangle, and Square, each with its own area/perimeter.

Example:
If you create a Triangle with base 6 and height 4 and call area():

Expected Output:
12.0
'''

class Shape:
    pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("area:",3.14 * (self.radius ** 2))

    def perimeter(self):
        print("perimeter:",2 * 3.14 * self.radius)



class Triangle(Shape):
    def __init__(self,base,height,length):
        self.base=base
        self.height=height
        self.length=length

    def area(self):
        print("area:",0.5 * self.base * self.height)

    def perimeter(self):
        print("perimeter:",self.length + self.base + self.height )

class Square(Shape):
    def __init__(self,side):
        self.side=side
      
    def area(self):
        print("area:",self.side * self.side)

    def perimeter(self):
        print("perimeter:",self.side * 4)



t1=Triangle(6,4,5)

t1.area()