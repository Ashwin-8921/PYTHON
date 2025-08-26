#Use the Ternary Operator to Find the Minimum of Two Numbers
#Use a single expression to find the smaller of two numbers.
#Sample Input: a = 20, b = 13

a=(int(input("a:")))
b=(int(input("b:")))

res=a if a<b else b

print("min:",res)
