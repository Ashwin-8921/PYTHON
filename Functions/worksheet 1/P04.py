#Question: Write a function area_of_circle(radius) that returns the area (πr²) of a circle 
# for the given radius.
#Sample data:print(area_of_circle(3))
# Expected output:28.274333882308138

import math

def area_of_circle(r):
    #return (3.142)*(r**2)
    return math.pi*(r**2)

r=int(input("enter radius:"))

print("output:",area_of_circle(r))

