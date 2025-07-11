'''
Access and print the english marks of 'Rahul' in:

        students = {

          'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},

          'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}

        }
        
Expected Output: 88
'''

students = {
    'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
    'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
}

print(students['Rahul']['marks']['english'])
