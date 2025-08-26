'''
18. Invert the Nest
Given a nested dictionary of students and their subjects, flip it so 
that subjects are outer keys and students are inside.
Input: d = {'math': {'john': 90, 'jane': 80}, 'science': {'john': 85, 'jane': 95}}
Expected Output: {'john': {'math': 90, 'science': 85}, 'jane': {'math': 80, 'science': 95}}
'''
import ast

d = ast.literal_eval(input("Input dictionary: "))

inverted = {}

for subject, students in d.items():
    for student, score in students.items():
        if student not in inverted:
            inverted[student] = {}
        inverted[student][subject] = score

print(inverted)
