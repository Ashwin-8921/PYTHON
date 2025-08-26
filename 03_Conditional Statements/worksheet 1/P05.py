#If a sensor value is outside the range 100–900, print "Sensor Fault". If within, print "Sensor OK".
#Input: 950
#Output: Sensor Fault

a=int(input("a:"))

if 100 <= a <= 900:
    print("Sensor OK")
else:
    print("Sensor Fault")