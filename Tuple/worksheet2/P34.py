'''
Description: Sort a tuple of (string, float) pairs by the float value in descending order.
Sorting by a specific field is essential in data analysis and organization, especially when dealing with mixed data types.
Input: t = (('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'))
Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
'''
import ast
inp=input("enter t:")

t=ast.literal_eval(inp)
sorted_list = sorted(t, key=lambda x: float(x[1]), reverse=True)

print(sorted_list)