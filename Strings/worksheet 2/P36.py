'''
Check if Two Strings are Rotationally Equivalent
Explanation: Check if one string can be rotated (circularly shifted) to match the other.
Input: "abcde", "cdeab"
Expected Output: Rotationally equivalent: Yes
'''

s1=input("string1:")
s2=input("string2:")

if len(s1) != len(s2):
    print("rotationally equivalent: No")
elif s2 in s1 + s1:
    print("rotationally equivalent: Yes")
else:
    print("rotationally equivalent: No")