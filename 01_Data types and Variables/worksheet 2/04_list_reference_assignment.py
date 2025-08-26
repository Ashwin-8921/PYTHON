#Given x = [1, 2, 3] and y = x, then x[0] = 9.
#  What are the values of x and y? Explain the behavior.

x=[1,2,3]

y=x

x[0]=9

print(x)
print(y)

#x is a list, which is mutable.

#y = x does not copy the list, it just creates another reference to the same list object in memory.

#So when you modify x[0], you're changing the shared list — y sees that change too.