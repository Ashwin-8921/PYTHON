'''
Identify the Least Frequent Character in a String
Explanation: Find the character(s) that occur(s) the fewest times in a string.
Input: "statistics"
Expected Output: Least frequent character: 'a'
'''

s=input("string:")

freq={}

for char in s:
    freq[char]=freq.get(char,0)+1

min=min(freq.values())

for char in s:
    if min == freq[char]:
        print("least frequency char:",char)
        break
