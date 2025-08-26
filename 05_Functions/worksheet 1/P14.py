'''
Question: Write a recursive function reverse_string(s) that returns the reversed string.
Sample data:print(reverse_string("python"))
output:nohtyp
'''

def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])


s=input("enter string:")

print("output:",reverse_string(s))