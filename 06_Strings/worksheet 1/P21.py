'''
Convert a List or Tuple of Characters to a String
Explanation: Combine list/tuple elements into a single string.
Input: ['p', 'y', 't', 'h', 'o', 'n']
Expected Output: "python"
'''

s = input("Enter char separated by commas: ")  # e.g., a,b,c
char_tuple = tuple(s.split(","))
print("Tuple:", char_tuple)

result = ''.join(char_tuple)
print("output string:", result)
