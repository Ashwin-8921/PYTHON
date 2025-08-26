'''
Check for Pangram
Explanation: Verify if a string contains every letter of the alphabet at least once.
Input: "The quick brown fox jumps over the lazy dog"
Expected Output: Is pangram: Yes
'''

import string

s=input("string:").lower()

alpha=set(string.ascii_lowercase)

if set(s) >= alpha:
    print("Is pangram: Yes")
else:
    print("Is pangram: No")