'''
17. Flip Nested Dictionary
Given a nested dictionary, swap the outer and inner keys. Who becomes the new outer boss?
Input: d = {'x': {'p': 1}, 'y': {'q': 2}}
Expected Output: {'p': {'x': 1}, 'q': {'y': 2}}
'''
import ast

d = ast.literal_eval(input("dict: "))

flipped = {}

for outer_key, inner_dict in d.items():
    for inner_key, value in inner_dict.items():
        if inner_key not in flipped:
            flipped[inner_key] = {}
        flipped[inner_key][outer_key] = value

print(flipped)
