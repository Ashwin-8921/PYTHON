'''Check if a String is a Palindrome or Symmetrical
Explanation: A palindrome reads the same forwards and backwards (e.g., "madam"). A symmetrical string has matching halves.
Input: "madam"
Expected Output:
Palindrome: Yes
Symmetrical: Yes'''

s=input("enter string:")
length = len(s)
half = length // 2

pal = s == s[::-1]

if length % 2 == 0:
    sym = s[:half] == s[half:][::-1]
else:
    sym = s[:half] == s[half+1:][::-1]

print("Palindrome: Yes" if pal else "Palindrome: No")
print("Symmetrical: Yes" if sym else "Symmetrical: No")
