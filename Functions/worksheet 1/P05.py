#Question: Write a function is_negative(number) that returns True if the number is negative, else False.
#Sample data:print(is_negative(-7))
#            print(is_negative(0))

#output: True
#        False

def is_negative(n):
    if n < 0:
        return False
    else:
        return True

n=int(input("enter num:"))

print(is_negative(n))