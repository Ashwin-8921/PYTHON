'''Add 'science': 93 to 'Simran''s marks in the nested dictionary.
'''

students = {
    'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
    'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
}

students['Simran']['marks']['science'] = 93

print(students['Simran']['marks'])
