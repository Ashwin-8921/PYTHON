'''
1. Lost & Found in the Supermarket
You’re managing the stock system for a small supermarket. Each item is a key, and its count is the value. A frantic customer wants to know if “apples” are still available. How will you instantly check if “apples” are on your shelf?
Input: stock = {'apples': 14, 'bananas': 22, 'rice': 12}, query = 'apples'
Expected Output: Yes, apples are in stock!
'''

import ast

inp=input("stock:")

stock=ast.literal_eval(inp)

query=input("query:")

if stock[query] > 0:
    print(f"yes, {query} are in stock")
else:
    print(f"no, {query} are in stock")

