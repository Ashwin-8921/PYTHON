'''
Question: Write a function grade(score) that returns 'A' if score ≥ 90, 'B' if 80 ≤ score < 90, 
'C' if 70 ≤ score < 80, and 'F' for anything less.
Sample data:
print(grade(85))
print(grade(72))
print(grade(50))
output:
B
C
F
'''

def grade(score):
    if score >=90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'
    

score=int(input("enter score:"))

print("grade:",grade(score))