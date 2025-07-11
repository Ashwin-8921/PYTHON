'''
Description: Find all unique elements present in a tuple of tuples using set logic.
This teaches set operations and how to process nested iterable structures.
Input: t = ((1, 2), (2, 3), (4, 5))
Output: {1, 2, 3, 4, 5}
'''
import ast
inp=input("enter tuple:")

t=ast.literal_eval(inp)

unique_elements = set(x for sub in t for x in sub)

print(unique_elements)

