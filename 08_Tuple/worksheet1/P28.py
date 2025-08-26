'''
Description: Given a list of pairs (tuples), separate each position into its own list (unzipping).
Unzipping is key for parallel data processing and converting between row-wise and column-wise formats.
Input: lst = [(1, 'a'), (2, 'b'), (3, 'c')]
Output: [1, 2, 3]
['a', 'b', 'c']
'''

import ast
inp=input("enter list:")

lst=ast.literal_eval(inp)

list1, list2 = zip(*lst)

print(list(list1))
print(list(list2))