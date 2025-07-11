'''
Swap Commas and Dots in a String
Explanation: Replace commas with dots and dots with commas.
Input: "23,45.89,78.90"
Expected Output: "23.45,89.78,90"
'''


s = input("enter string:")

s = s.replace(',', '#')
s = s.replace('.', ',')
s = s.replace('#', '.')

print(s)
