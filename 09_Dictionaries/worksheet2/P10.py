'''
10. Pairing the Guest List
You have two lists: guest names and their seat numbers. 
Match each guest to their seat for the dinner plan!
Input: names = ['Alice', 'Bob', 'Eve'], seats = [5, 12, 8]
Expected Output: {'Alice': 5, 'Bob': 12, 'Eve': 8}
'''

import ast
inp=input("input1:")

names=ast.literal_eval(inp)

inp=input("input2:")

seats=ast.literal_eval(inp)

seating=dict(zip(names,seats))

print(seating)
