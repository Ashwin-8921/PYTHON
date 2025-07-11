#Question: Write a function print_details(name, age) that prints a sentence using both parameters.
#Sample data: print_details("Alice", 25)
#Expected output: Name: Alice, Age: 25

def print_details(x,y):
    print(f"Name: {x}, Age: {y}")

x=input("Enter name:")
y=int(input("Enter Age:"))
print_details(x,y)