#Input a number and find its smallest divisor greater than 1 (using only loops).

n=int(input("n:"))

for i in range(2,n+1):
    if n%i==0:
        break
print(i)
