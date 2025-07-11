'''
Replace Multiple Words at Once
Explanation: Simultaneously replace several different words in a string with new ones.
Input: String = "I like apples and bananas.", Replace: {"apples": "oranges", "bananas": "grapes"}
Expected Output: "I like oranges and grapes.
'''

s = input("enter string:")
replacements = {"apples": "oranges", "bananas": "grapes"}

for old, new in replacements.items():
    s = s.replace(old, new)

print(s)
