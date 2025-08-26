#Input an integer and count how many times 0 appears in it (no strings or lists).

n=int(input("n:"))
c=0
while n>0:
    a=n%10
    if a==0:
        c+=1
    n=n//10

print("count:",c)