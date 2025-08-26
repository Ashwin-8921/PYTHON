
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

diff = (a if a > b and a > c else b if b > c else c) - (a if a < b and a < c else b if b < c else c)

print(diff)