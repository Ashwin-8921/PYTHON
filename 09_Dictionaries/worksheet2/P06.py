'''
6. Secret Spy Codes
You intercepted a list of coded messages (keys), but your team uses new code names (a mapping). 
How will you quickly rename every code to its new secret label?
Input: codes = {'alpha': 'ok', 'beta': 'wait'}, new_labels = {'alpha': 'red', 'beta': 'blue'}
Expected Output: {'red': 'ok', 'blue': 'wait'}
'''
import ast
inp=input("input1:")

code=ast.literal_eval(inp)

inp=input("input2:")

new=ast.literal_eval(inp)

renamed={new[key]:value for key,value in code.items()}

print(renamed)