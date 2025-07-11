#Question: Write a function greet_person(name, greeting) that prints a personalized 
# message like "Hello, John!" using the arguments.
#Sample data: greet_person("John", "Hi")
#OUTPUT:Hi, John!

def greet_person(name,greet):
    print(f"{greet}, {name}!")



name=input("enter string1:")
greet=input("enter string2:")
greet_person(name,greet)

