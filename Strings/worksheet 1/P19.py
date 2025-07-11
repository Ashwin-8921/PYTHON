'''Convert Integer to String and Vice Versa
Explanation: Change a number to a string, and a string of digits to an integer.
Input: Integer = 123, String = "456"
Expected Output:
Integer to string: '123'
String to integer: 456'''

i = int(input("integer: "))
s = input("string: ")

int_to_str = str(i)
str_to_int = int(s)

print("Integer to string:", int_to_str)
print("String to integer:", str_to_int)
