'''
12. Max and Min Detective
Among all your valuables (dictionary values), who owns the largest and smallest? 
Report both the max and min key names.
Input: valuables = {'ring': 5, 'necklace': 9, 'watch': 2}
Expected Output: Max: 'necklace', Min: 'watch'
'''
import ast

valuables = ast.literal_eval(input("Input valuables: "))

max_item = max(valuables, key=valuables.get)
min_item = min(valuables, key=valuables.get)

print("Max:", repr(max_item))
print("Min:", repr(min_item))















