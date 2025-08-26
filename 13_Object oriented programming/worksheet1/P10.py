'''
10. All About Circles: Area and Perimeter
Scenario:
Designing a map app? You’ll want to know the area covered by a circular pond!

What you’ll learn:
Implementing methods with calculations
Understanding encapsulation

Task:
Build a Circle class with area() and perimeter() methods.

Example:
For a circle of radius 3:

Expected Output:
28.27
18.85
'''

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("area:",3.14 * (self.radius ** 2 ))

    def perimeter(self):
        print("perimeter:",2 * 3.14 * self.radius)

c1=Circle(3)
c1.area()
c1.perimeter()