'''
3. Looping Through Lists
Log Session a list of numbers from 1 to 5.
Use a for loop to print each number.
Use a while loop to print each number.
Use list comprehension to create a new list with each number squared.
'''

nums=list(map(int,input("enter list:").split()))
print("using for loop:")
for num in nums:
    print(num,end=" ")

i=0
print("\nusing while loop:")
while i < len(nums):
    print(nums[i],end=" ")
    i+=1

new=[x*x for x in nums]

print("\nnew list:",new)