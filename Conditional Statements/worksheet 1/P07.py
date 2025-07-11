#Given three boolean flags: `power_on`, `overcurrent`, `overvoltage`, print:
#- "System Safe" if only `power_on` is True.
#- "Shut Down: Overcurrent" if `overcurrent` is True.
#- "Shut Down: Overvoltage" if `overvoltage` is True.
#- "Critical Failure" if both faults are True.
#Input: True, True, False

power_on=input("power:")== "True"
overcurrent=input("overcurrent:")== "True"
overvoltage=input("overvoltage:")== "True"

if power_on and  not overcurrent  and not overvoltage  :
    print("System Safe")
elif overcurrent:
    print("Shut Down: overcurrent")
elif overvoltage:
    print("Shut Down: overvoltage")
elif overcurrent and overvoltage:
    print("Critical Failure")