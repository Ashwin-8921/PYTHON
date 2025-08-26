'''
Find the Location of a Word in a String
Explanation: Find the index where a word first appears in the string.
Input: String = "welcome to python", Word = "python"
Expected Output: Position: 11
'''


text = input("Enter the string: ")
word = input("Enter the word to find: ")

position = text.find(word)

if position != -1:
    print("Position:", position)
else:
    print("Word not found.")
