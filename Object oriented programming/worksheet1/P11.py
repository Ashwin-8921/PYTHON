'''
11. Meet the Person: Calculate Age from Date of Birth
Scenario:
Log Session a birthday tracker! Determine someone’s age from their date of birth.

What you’ll learn:
Handling dates and calculating with them
Real-world use of classes

Task:
Make a Person class and compute age.

Example:
For a person born on 2000-05-25 (today is 2025-05-25):

Expected Output:
Alice is 25 years old.
'''

class Person:
    def __init__(self,dob):
        self.dob=dob
        print("dob:",dob)
        
    def age(self):
        today=2025
        year=self.dob.split("-")
        year=int(year[0])
        print(f"Alice is {today-year} years old")

p1=Person("2000-05-25")
p1.age()