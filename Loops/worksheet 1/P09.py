#Take an integer and, using only loops, sum its digits repeatedly until only a single digit remains.
#Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2

n=int(input("n:"))

sum=n
b=0
while n >= 10:
    sum=0
    while n>0:
        sum=sum+(n%10)
        n=n//10
    n=sum
print(n)