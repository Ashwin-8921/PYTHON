'''
2. Adding and Removing Items
Append "orange" to the fruits list.
Insert "mango" at the second position.
Remove "apple" from the list.
Use the pop() method to remove the last item.
Clear the entire list.
'''

inp=input("enter list:")

list1=inp.split()
print("list:",list1)

word=input("enter item to append:")

list1.append(word)
print("list:",list1)

word=input("enter item to add at 2nd pos:")
list1.insert(1,word)
print("list:",list1)


word=input("enter item to remove:")

list1.remove(word)
print("list:",list1)



list1.pop()
print("list:",list1)

list1.clear()

print("list:",list1)

