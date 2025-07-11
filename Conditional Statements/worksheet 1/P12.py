#Given a voltage and current reading, print "Power OK" if both are in safe ranges, otherwise print specific error:
#- Voltage out of 3.0–3.3V: "Voltage Error"
#- Current out of 10–500mA: "Current Error"
#- Both out: "Power Error"

a = float(input("voltage: "))
b = float(input("current: "))

voltage_ok = 3.0 <= a <= 3.3
current_ok = 10 <= b <= 500

if not voltage_ok and not current_ok:
    print("Power Error")
elif not voltage_ok:
    print("Voltage Error")
elif not current_ok:
    print("Current Error")
else:
    print("Power OK")
