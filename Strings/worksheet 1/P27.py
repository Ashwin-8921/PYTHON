'''
 Frequency of Consecutive Characters
Explanation: Count how many times each character repeats in sequence.
Input: "aabccddd"
Expected Output: {'a': 2, 'b': 1, 'c': 2, 'd': 3}
'''

s=input("enter string:")

res={}
c=1

for char in s:
    if char in res:
        res[char]+=1
    else:
        res[char]=1

print("output:",res)
    
