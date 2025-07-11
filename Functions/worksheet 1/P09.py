'''
Question: Write a function introduction(name, country='India') that prints a message introducing the person and their country.
Sample data:
introduction("Sara")
introduction("Alex", "USA")

output:
My name is Sara and I am from India.
My name is Alex and I am from USA.
'''

def intro(name,cont='India'):
    print(f"My name is {name} and i am from {cont}")


name=input("enter name:")
cont=input("enter country:")

intro(name)
intro(name,cont)