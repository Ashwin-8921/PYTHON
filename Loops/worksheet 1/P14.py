#Check if a given number is a perfect number (sum of divisors excluding itself), using only loops.

n=int(input("n:"))

sum=0

for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("yes")
else:
    print("no")