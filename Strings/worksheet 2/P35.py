'''
Remove Punctuation from a String
Explanation: Remove all punctuation marks, keeping only letters, digits, and spaces.
Input: "Hello, world! How are you?"
Expected Output: "Hello world How are you"
'''
import string

s=input("string:")

c= ''.join(char for char in s if char not in string.punctuation)

print("output:",c)