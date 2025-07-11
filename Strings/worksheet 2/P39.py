'''
Validate a Password String
Explanation: Check if a password meets certain conditions (length, special characters, etc.).
Input: "MyPass123@"
Expected Output: Valid password: Yes
'''
import string

pas=input("password:")

upper=any(c.isupper() for c in pas)
lower=any(c.islower() for c in pas)
digit=any(c.isdigit() for c in pas)
special=any(c in string.punctuation  for c in pas)
len= len(pas) >= 8

if upper and lower and digit and special and len:
    print("valid password: Yes")
else:
    print("valid password: No")