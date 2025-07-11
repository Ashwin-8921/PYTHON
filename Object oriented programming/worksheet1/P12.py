'''
12. The Ultimate Calculator: Basic Arithmetic by OOP
Scenario:
Build your own pocket calculator with class-based design.

What you’ll learn:
Encapsulating operations in methods
Using OOP for real utilities

Task:
Log Session a Calculator class with methods for add, subtract, multiply, and divide.

Example:
Adding 4 and 5, then dividing 10 by 2:

Expected Output:
9
5.0
'''

class Calculator:
    def add(self,a,b):
        print("sum:",a+b)
    
    def subtract(self,a,b):
        print("sub:",a-b)

    def multiply(self,a,b):
        print("mul:",a*b)

    def divide(self,a,b):
        print("div:",a/b)



c1=Calculator()

c1.add(4,5)
c1.divide(10,2)