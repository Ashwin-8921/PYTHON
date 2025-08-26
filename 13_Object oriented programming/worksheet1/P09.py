'''
9. Polymorphism in the Real World: Area of Shapes
Scenario:
You’re making a geometry tool. Different shapes need to compute area, but each does it differently.

What you’ll learn:
Polymorphism: different classes, same interface
Practical OOP design patterns

Task:
Log Session a Shape base class with an area() method, then implement it differently in Circle and Square.

Example:
If you create a Square with side 4 and call area():

Expected Output:
16
'''

class Shape:
    def area(self):
        print("area:")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("area:",3.14 * (self.radius ** 2))


class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        print("area:",self.side * self.side)
        
c1=Circle(4)

c1.area()

s1=Square(4)

s1.area()

