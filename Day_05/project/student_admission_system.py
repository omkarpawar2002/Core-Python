"""
🟢 Project 1 – Student Admission System
🎯 Objective

Create a system that decides whether a student is eligible for admission.

📚 Concepts Used
if
elif
Nested if
Boolean variables
✅ Functional Requirements

Ask the user for:

Student Name
Age
Percentage
Entrance Exam Qualified (True/False)

Rules:

Age must be at least 17.
Percentage must be at least 60%.
If age and percentage are valid, check the entrance exam result.

Display:
Admission Approved
Admission Rejected
Reason for rejection
⭐ Challenge

Add different departments based on percentage:

90+ → Computer Science
80–89 → IT
70–79 → Electronics
60–69 → Mechanical
"""

name = input("Enter your name : ")
age = int(input("Enter your age : "))
percentage = float(input("Enter your percentage : "))
enterance_qualify = input("Have you qualify enterance exam [yes/no]: ")

if age >= 17:
    if percentage >= 60:
        if enterance_qualify == "yes":
            print("Admission Approved")
            dept = ""
            if percentage >= 90:
                dept = "Computer Science"
            elif percentage >= 80:
                dept = "IT"
            elif percentage >= 70:
                dept = "Electronics"
            elif percentage >= 60:
                dept = "Mechanical"

            print(
                "============================================"
                " \n *** Admission Approved *** "
                f"\n Student Name : {name}"
                f"\n Student Age : {age}"
                f"\n Student Percentage : {percentage}"
                f"\n Enterrance Exam Pass : {enterance_qualify}"
                f"\n Department : {dept}\n"
                "============================================"
            )
        else:
            print("Admission Rejected Due To Failed Enterance Exam")
    else:
        print("Minimum Percentage Required 60 or more.")
else:
    print("Below 17 Not Eligible")
