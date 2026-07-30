"""

Project 2: Student Eligibility Checker

Difficulty: Beginner

Objective

Determine whether a student passes based on marks and attendance.

Concepts Used
Comparison operators
Logical operators
Boolean values

Functional Requirements
Ask for marks.
Ask for attendance.
A student passes only if:
Marks ≥ 40
Attendance ≥ 75
Display the final result.

"""

marks = float(input("Enter your marks : "))
attendance = int(input("Enter your attendance : "))
result = (marks >= 40) and (attendance >= 75)
print("Student Pass :", result)
