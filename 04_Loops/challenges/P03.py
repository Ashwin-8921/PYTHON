#Find all numbers less than 1000 which equal the sum of the factorials of their digits.
#Valid Example: 145: 1! + 4! + 5! = 1 + 24 + 120 = 145 (valid)
#Invalid Example: 123: 1! + 2! + 3! = 1 + 2 + 6 = 9 (not valid)

for i in range(1,1000):
    a=i
    sum=0
    while a>0:
        b=a%10
        f=1
        for j in range(1,b+1):
            f*=j
        sum+=f
        a=a//10
    if sum==i:
      print(i)
        