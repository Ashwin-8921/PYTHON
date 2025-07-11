#Given a voltage reading, print "Under Voltage", "Nominal", or "Over Voltage".
#(Nominal is between 3.0V and 3.3V inclusive.)
#Input: 3.35
#Output: Over Voltage

v=float(input("voltage:"))

if 3.0 <= v <=3.3:
     print("Nominal")
elif v<3:
     print("Under voltage")
else:
     print("Over voltage")

      