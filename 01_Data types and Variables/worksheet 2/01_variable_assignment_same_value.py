#Given the assignment a = b = 10, what happens if you later 
# set b = 20? What is the value of a? Explain why.

a=b=10

print(a,b)

b=20

print(a,b)

#initially a and b are pointing to same object but when bi modified it points to the new object this doesnt affect a