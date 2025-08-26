#Print all 3-digit numbers such that the sum of the cubes of their digits equals the number itself.
#Example: 153 → 1³ + 5³ + 3³ = 153

for i in range(100,1000):
    a=i//100
    b=(i//10)%10
    c=i%10
    res=a**3 + b**3 + c**3
    if(i==res):
     print(i)


