"""

🔵 Project 7 – Hospital Patient Priority System
🎯 Objective

Determine treatment priority.

📚 Concepts Used
elif
Nested if
Branching logic
✅ Functional Requirements

Inputs:

Age
Emergency Level
Critical
Serious
Normal
Insurance Available (True/False)

Rules:

Critical → Immediate Treatment.
Serious → High Priority.
Normal → Regular Queue.
If insurance is unavailable, display a payment reminder.
⭐ Challenge

Give senior citizens higher priority when the emergency level is the same.

"""

age = int(input("Enter patient age : "))
emergency_level = input("Enter emergency level [Critical,Serious,Normal] : ")
insurance_available = input("Is insurance available [yes/no] : ")
if age > 0:
    if emergency_level == "Critical":
        print("Immediate Treatment")
        if age >= 60:
            print("High Priority For Senior Citizen")
        if insurance_available != "yes":
            print("Proceed Payment")
    elif emergency_level == "Serious":
        print("High Priority")
        if age >= 60:
            print("High Priority For Senior Citizen")
        if insurance_available != "yes":
            print("Proceed Payment")
    elif emergency_level == "Normal":
        print("Regular Queue")
        if age >= 60:
            print("High Priority For Senior Citizen")
        if insurance_available != "yes":
            print("Proceed Payment")
    else:
        print("Invalid Emergency Level")
else:
    print("Invalid Age")
