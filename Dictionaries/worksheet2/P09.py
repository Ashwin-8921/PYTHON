'''
9. Update the Employee Profile
A nested dictionary holds employee info. An employee changed their phone number. 
Update it without touching the rest of their info.
Input: profile = {'info': {'name': 'Sam', 'phone': '555-1234'}}, new_phone = '555-9999'
Expected Output: {'info': {'name': 'Sam', 'phone': '555-9999'}}
'''
import ast
inp=input("input1:")

profile=ast.literal_eval(inp)

num=input("new_phone:")

profile['info']['phone']=num

print(profile)
