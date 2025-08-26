#Check if the input number reads the same backward as forward, using only loops and arithmetic.

a=int(input("a:"))
b=a
c=0

while b>0:
    c=(c*10)+(b%10)
    b=b//10
if a==c:
    print("yes")
else:
  print("no")
