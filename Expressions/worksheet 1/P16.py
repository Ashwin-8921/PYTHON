#Find the Sign of a Number as -1, 0, or 1 (Using Only Expressions)
#Write a single expression that gives -1 for negative numbers, 0 for zero, and 1 for positive numbers.
#Sample Input: n = -56

n=int(input("n:"))

a= -1 if n<0 else 0 if n==0 else 1

print(a)