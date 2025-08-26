'''
Find the Maximum Frequency Character
Explanation: Determine which character appears most frequently in the string.
Input: "banana"
Expected Output: Maximum frequency character: 'a'
'''

s=input("string:")

freq={}

for char in s:
    freq[char]=freq.get(char,0)+1

max=max(freq.values())

for char in s:
    if max==freq[char]:
        print("max frequency char:",char)
        break