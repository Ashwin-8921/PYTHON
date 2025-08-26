#Swap Two Numbers Without Using a Third Variable
#Swap two variables’ values using a single line of code.
#Sample Input: a = 15, b = 8

a=int(input("a:"))
b=int(input("b:"))
print("before:",a," ",b)

a,b=b,a

print("after:",a," ",b)

