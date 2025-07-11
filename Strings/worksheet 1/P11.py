'''
Check If a String is a Binary String
Explanation: Test if the string contains only '0' and '1'.
Input: "101101"
Expected Output: Is binary string: Yes
'''

s=input("input:")
flag=0
for char in s:
    if char != '0' and char !='1':
        flag=1
        break

print(f"is binary: {'yes' if flag==0 else 'no'}")