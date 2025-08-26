'''
Description: Compute the element-wise sum of multiple tuples of equal length.
This exercise teaches how to combine tuples by adding corresponding elements, often used in mathematical and data processing tasks.
Input: t1 = (1, 2, 3, 4), t2 = (3, 5, 2, 1), t3 = (2, 2, 3, 1)
Output: (6, 9, 8, 6)
'''
import ast
inp=input("enter t1:")

t1=ast.literal_eval(inp)

inp=input("enter t2:")

t2=ast.literal_eval(inp)

inp=input("enter t3:")

t3=ast.literal_eval(inp)

result = tuple(a + b + c for a, b, c in zip(t1, t2, t3))

print(result)