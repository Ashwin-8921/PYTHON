'''
Description: Convert a tuple of positive integers into a single integer by concatenating their values.
This is a common data transformation task, often seen in problems that require generating a unique number from a sequence.
Input: t = (1, 2, 3)
Output: 123
'''
import ast
inp=input("enter t:")

t=ast.literal_eval(inp)

result = int(''.join(str(x) for x in t))

print(result)
