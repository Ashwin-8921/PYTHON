#Find the Largest of Three Numbers Using Only Expressions
#Without using if, elif, or any function, write an expression to find the largest of three given numbers.
#Sample Input: a = 14, b = 27, c = 19

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

res= a if a>b and a>c else b if b>c else c
print(res)