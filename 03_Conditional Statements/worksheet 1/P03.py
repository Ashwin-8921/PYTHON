#Enter a temperature and print "Overheat" (>75°C), "Normal" (25-75°C), or "Low Temp" (<25°C).
#Input: 18
#Output: Low Temp

t=int(input("temperature:"))

if 25<= t <=75:
    print("Normal")
elif t>75:
    print("Overheat")
else:
    print("Low Temp")
 
