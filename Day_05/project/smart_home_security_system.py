"""
🟢 Project 3 – Smart Home Security System
🎯 Objective

Simulate a home's security system.

📚 Concepts Used
Nested if
Boolean variables
Branching logic
✅ Functional Requirements

Inputs:

Main Door Locked (True/False)
Motion Detected (True/False)
Owner at Home (True/False)

Rules:

If the door is unlocked:
If motion is detected:
If the owner is not home:
Trigger Alarm.
Else:
Display "Owner Movement Detected".
Else:
Display "Door Open but No Motion".
If the door is locked:
Display "House Secure".
⭐ Challenge

Add a "Call Police" message when the alarm is triggered.
"""

main_door = input("Enter main door lock or not [yes / no]: ")
if main_door == "yes":
    print("House Secure")
else:
    motion_detect = input("Enter Motioned Detected or not [yes / no]: ")
    if motion_detect == "yes":
        owner_at_home = input("Enter owner at home or not [yes / no]: ")
        if owner_at_home == "yes":
            print("Owner moment detected")
        else:
            print("Alarm Trigger")
            print("Call Police")
    else:
        print("Door Open but No Motion")


