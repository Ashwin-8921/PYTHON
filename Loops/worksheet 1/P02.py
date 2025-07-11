#For a given number, print its multiplication table from 1 to 10, but don’t use the * operator.

a=int(input("input:"))
res=a

for i in range (1,11):
    print(f"{a} x {i} = {res}")
    res+=a