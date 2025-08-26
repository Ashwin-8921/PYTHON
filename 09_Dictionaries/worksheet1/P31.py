'''
For each student in the above students dictionary, print the name and all subject marks.
'''

students = {
    'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
    'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
}

for name, info in students.items():
    print(f"{name}: {info['marks']}")
