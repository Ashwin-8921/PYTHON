'''
8. The Cafe’s Popular Menu
Every order is tracked in a list. Can you build a menu board that 
shows how many times each item was ordered today?
Input: orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
Expected Output: {'latte': 3, 'espresso': 2, 'tea': 1}
'''
import ast
inp=input("input1:")

orders=ast.literal_eval(inp)

freq={}

for order in orders:
    if order in freq:
        freq[order]+=1
    else:
        freq[order]=1

print(freq)