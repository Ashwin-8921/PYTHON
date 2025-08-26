'''
Check if a String Contains Special Characters
Explanation: Check if the string contains characters other than letters or numbers.
Input: "Hello@123"
Expected Output: Contains special character: Yes
'''

s=input("string:")
flag=False
for char in s:
    if not char.isalnum():
        flag=True
        break

print("Contains special character:", "Yes" if flag else "No")

