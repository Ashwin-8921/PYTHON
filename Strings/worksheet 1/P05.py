'''
Count Vowels in a String Using Sets
Explanation: Find how many vowels (a, e, i, o, u) are in the string, using sets for efficiency.
Input: "education"
Expected Output: Vowels Count: 5
'''

def count_vowels(s):
    vowel={"a","e","i","o","u","A","E","I","O","U"}
    c=0
    for char in s:
        if char in vowel:
             c+=1
    return c

s=input("string:")

print("vowel count:",count_vowels(s))

