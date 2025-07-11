#Take a number as input and calculate its factorial using loops (no recursion).
a=int(input("a:"))
res=1
for i in range(1,a+1):
    res=res*i
print("factorial:",res)

