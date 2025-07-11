'''
3. The Unique Collector’s Auction
You’re at a collector’s auction. Each lot number is a key, and the value is the type of collectible. 
Auctioneers want to quickly know how many unique collectibles are being auctioned, 
not just the number of lots. Can you wow them with an instant count?
Input: auction = {'lot1': 'coin', 'lot2': 'stamp', 'lot3': 'coin', 'lot4': 'comic'}
Expected Output: Unique collectibles: ['coin', 'stamp', 'comic']
'''
import ast

inp=input("input:")

dict1=ast.literal_eval(inp)

uniq=list(set(dict1.values()))

print(uniq)

