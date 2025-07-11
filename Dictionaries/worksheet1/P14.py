#Add a key 'status' with value 'active' to user = {'name': 'Riya'} only if it doesn’t exist.


import ast

inp=input("enter dict:")

user=ast.literal_eval(inp)

if 'status' not in user:
    user['status']='active'

print(user)