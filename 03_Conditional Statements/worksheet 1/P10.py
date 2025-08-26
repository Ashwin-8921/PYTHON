#Given three sensor readings, print "Majority High" if at least two readings 
# are above a threshold (e.g., 50), otherwise "Majority Low".
#Input: 40, 65, 70
#Output: Majority High

a=int(input("sensor1:"))
b=int(input("sensor2:"))
c=int(input("sensor3:"))

'''if a > 50 and b > 50 and  c > 50 :
    print("Majority high")
elif a > 50 and b >50:
    print("Majority high")
elif a > 50 and c > 50:
    print("Majority high")
elif b > 50 and c >50:
    print("Majority high")
else:
    print("Majority Low")'''

count = (a > 50) + (b > 50) + (c > 50)

if count == 2:
    print("Majority high")
else:
    print("Majority Low")
    