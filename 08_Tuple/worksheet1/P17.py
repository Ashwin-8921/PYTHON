'''
Description: Count how many times a particular value occurs in a tuple.
Element frequency counting is useful for analytics and validation tasks.
Input: t = (1, 2, 3, 2, 2, 4), Count: 2
Output: 3
'''
import ast
inp=input("enter tuple:")

t=ast.literal_eval(inp)

c=int(input("count:"))

print("output:",t.count(c))