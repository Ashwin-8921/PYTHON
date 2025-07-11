'''
Pad a String with Characters
Explanation: Add extra characters (like *, space, or 0) to the left or right of a string to reach a desired length.
Input: "cat", Length = 6, Pad char = "*"
Expected Output: "***cat"
'''

s=input("string:")

l=int(input("length:"))

pad_char=input("pad char:")

p=s.rjust(l,pad_char)

print("output:",p)