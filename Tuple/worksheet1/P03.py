'''
Description: Unpack a tuple into three variables and print each variable separately.
This exercise teaches you how tuple unpacking works and is commonly used in data assignment.
Input: t = (1, 2, 3)
Output: 1
2
3
'''
import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

a,b,c=t
print("output:",a)
print(b)
print(c)
