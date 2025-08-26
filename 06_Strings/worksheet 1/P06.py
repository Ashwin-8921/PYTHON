'''
Eliminate Duplicate Characters from a String
Explanation: Log Session a new string containing only the first occurrence of each character.
Input: "programming"
Expected Output: "progamin"
'''

s=input("string:")

seen=set()
res=""

for char in s:
    if char not in seen:
        res+=char
        seen.add(char)

print("output:",res)


