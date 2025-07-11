'''
Show what happens when you do b = a with a = {'x': [1, 2]}
 and then modify b['x']. What happens to a?
'''

import ast

inp=input("enter dict:")

a=ast.literal_eval(inp)

b=a
print("a before :",a)
print("b before :",b)

b['x'].append(3)

print("a after :",a)
print("b after :",b)

