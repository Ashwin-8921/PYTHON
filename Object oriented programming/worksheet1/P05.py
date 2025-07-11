'''
5. One for All: The Magic of Class Attributes
Scenario:
All students in a school belong to the same institution. How can you ensure this is reflected in every student object?

What you’ll learn:
Class (static) attributes: properties shared by all instances
When and why to use them

Task:
Define a Student class where every student has the same school_name.

Example:
If you create two students and print their school_name:

Expected Output:
Central High School Central High School
'''

class Student:
    school="central high school"

    def data(self,name):
        self.name=name


s1=Student()
s2=Student()

s1.data("Ashwin")
s2.data("Akash")

print("school:",s1.school,"name:",s1.name)
print("school:",s2.school,"name:",s2.name)