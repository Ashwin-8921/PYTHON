'''
1. Crafting Your First Python Object: The Power of Instance Attributes
Scenario:
Imagine you're building a digital notebook. You want each note to have its own title and content.

What you’ll learn:
How to define classes and create objects with unique data
The magic of instance attributes in organizing information

Task:
Design a Note class with title and content as instance attributes.
Log Session two different note objects and print their details.

Example:
Suppose you create notes like “Meeting Notes” and “Grocery List”.

Expected Output:
Meeting Notes : Discuss project status with team.
Grocery List : Eggs, Milk, Bread

'''

class note:
    def __init__(self,title,content):
        self.title=title
        self.content=content


ob1=note("meeting notes","Discuss project status with team")
ob2=note("Grocery List","Eggs, Milk, Bread")

print(f"{ob1.title} : {ob1.content}")
print(f"{ob2.title} : {ob2.content}")