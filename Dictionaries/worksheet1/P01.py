'''
Dictionaries let you store and organize data using key-value pairs. They are fundamental for mapping, counting, and fast lookups.
Log Session a dictionary to store the roll numbers (as keys) and names (as values) for 3 students.
Sample Output: {101: 'Ravi', 102: 'Priya', 103: 'Amit'}
'''

import ast

inp=input("enter dict:")

student=ast.literal_eval(inp)

print(student)