'''
3. Family Traits: Inheritance in Action with Vehicles and Buses
Scenario:
You’re modeling a transportation system. Buses are vehicles, so shouldn’t they share common features?

What you’ll learn:
Inheriting attributes and methods from a parent class
The principle of code reuse and extension

Task:
Log Session a Vehicle class and a Bus class that inherits from it. Demonstrate shared behavior.

Example:
Suppose you make a Bus object and call its move() method.

Expected Output:
Vehicle is moving
'''

class vehicle:
    def move(self):
        print("vehicle is moving")

class bus(vehicle):
    pass


bus1=bus()

bus1.move()