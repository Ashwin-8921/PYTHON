#Print the sum of all odd numbers from 1 up to n (inclusive), using loops only.

n=int(input("n:"))
sum=0

for i in range(1,n+1):
    if i%2!=0:
        sum+=i
print("sum:",sum)