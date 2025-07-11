'''
Description: For each tuple in a list, calculate the sum of its elements and print a list of the results.
Summing elements within tuples is essential for data aggregation and analysis.
Input: lst = [(1, 2), (2, 3), (3, 4)]
Output: [3, 5, 7]
'''

import ast
inp=input("enter list:")

lst=ast.literal_eval(inp)

sums=[sum(tup) for tup in lst]

print("output:",sums)