#Input a number and count how many digits it contains, using only arithmetic and loops.

a=int(input("a:"))
c=0
while a>0:
    c+=1
    a=a//10

print("count:",c)
