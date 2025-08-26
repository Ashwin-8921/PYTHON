#Ask for two numbers and compute their Greatest Common Divisor (GCD)
#  using repeated subtraction or division with loops.

a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))

while a != b:
    if a>b:
        a=a-b
    else:
        b=b-a
print("GCD:",a)
