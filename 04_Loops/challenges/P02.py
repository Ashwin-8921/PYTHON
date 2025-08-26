#For n between 100 and 999, print all numbers where the sum of their 
# digits raised to their own position is equal to the number.
#Valid Example: 135: 1¹ + 3² + 5³ = 1 + 9 + 125 = 135 (valid)
#Invalid Example: 123: 1¹ + 2² + 3³ = 1 + 4 + 27 = 32 (not valid)

for i in range (100,1000):
    a=i%10
    b=(i//10)%10
    c=(i//100)
    sum=(a**3)+(b**2)+(c**1)
    if sum==i:
        print(i)