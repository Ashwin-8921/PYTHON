'''
Question: Write a function min_max(numbers) 
that returns both the smallest and largest number in a list (use returning multiple values).
sample data:
small, large = min_max([8, 3, 5, 2, 10])
print("Smallest:", small)
print("Largest:", large)

output:
Smallest: 2
Largest: 10

'''

def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
            
    return smallest, largest

numbers = [8, 3, 5, 2, 10]

small, large = min_max(numbers)

print("Smallest:", small)
print("Largest:", large)
