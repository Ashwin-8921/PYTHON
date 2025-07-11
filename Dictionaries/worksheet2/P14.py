'''
14. Value to Key Reverse Find
You know a value, but not which key owns it. Trace back and report the key for a given value!
Input: d = {'x': 100, 'y': 200}, value = 200
Expected Output: Key for value 200: 'y'
'''


import ast

d=ast.literal_eval(input("dict:"))

v=int(input("value:"))

for key in d:
    if d[key]==v:
        print(f"key for value {v}: {key} ")
        break
else:
 print("key not found")