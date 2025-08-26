#Given the code
#What is the value of y and why?

x = [1, 2, 3]
y = x
x = [4, 5, 6]
print(y)

'''After y = x, both x and y point to [1, 2, 3].

But when x is reassigned to [4, 5, 6], it now points to a new list.

y still points to the original list [1, 2, 3].'''