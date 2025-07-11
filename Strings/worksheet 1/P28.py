'''
Rotate a String by k Positions
Explanation: Shift characters in the string to the right by k positions.
Input: String = "hello", k = 2
Expected Output: "lohel"

'''

s=input("enter string:")
k=int(input("k:"))

k=k % len(s)

res=s[-k:] + s[:-k]

print("output:",res)