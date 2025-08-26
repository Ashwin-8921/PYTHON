'''
Print the Middle Character of a String
Explanation: Display the character(s) at the center of the string.
Input: "python"
Expected Output: Middle character: 't' and 'h'

'''

s = input("string:")
l = len(s)
mid_index = l // 2

if l % 2 == 0:
    print("Middle characters:")
    print(s[mid_index - 1])
    print(s[mid_index])
else:
    print("Middle character:")
    print(s[mid_index])
