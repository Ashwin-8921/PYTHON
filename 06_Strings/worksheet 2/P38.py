'''
Reverse Sort a String
Explanation: Sort the characters of the string in descending order.
Input: "python"
Expected Output: "ytponh"
'''

s=input("string:")

r=''.join(sorted(s,reverse=True))

print("output:",r)