"""

Project – Student Result Management System
Objective

Determine a student's result and grade based on marks.

Concepts Used
Input
Comparison Operators
Logical Operators
if-elif-else
Functional Requirements

Ask for the student's name.
Ask for marks in three subjects.
Calculate:
Total
Average
Display:
Grade
Pass/Fail
Print an appropriate message based on the result.

"""

name = input("Enter your name : ")
phy = int(input("Enter physics marks : "))
maths = int(input("Enter maths marks : "))
biology = int(input("Enter biology marks : "))
total = phy + maths + biology
avg = total / 3
print()
print("Student Name : ",name)
print("Physics = ",phy)
print("Maths = ",maths)
print("Biology = ",biology)
print("------------------------------")
print("Total Marks = ",total)
print("Average = ",avg)
grade = ""
if(avg >= 90):
    grade += "A"
elif(avg >= 70):
    grade += "B"
elif(avg >= 50):
    grade += "C"
elif(avg >= 35):
    grade += "D"
else:
    grade += "F"
print("Grade = ",grade)
if(grade != "F"):
    print("Result = Pass")
else:
    print("Result = Fail")