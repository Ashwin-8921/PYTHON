'''
Generate All Permutations of a String
Explanation: List all possible ways to rearrange the characters.
Input: "abc"
Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
'''



import itertools

s = input("string:")
perms = itertools.permutations(s)

result = [''.join(p) for p in perms]

print(result)
