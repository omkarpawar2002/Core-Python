"""

Project 4: Multiplication Table Generator
Objective

Generate multiplication tables for one or more numbers.

Concepts Used
for loops
Nested loops
User input

Functional Requirements
Ask the user for:
Starting number
Ending number
Print the multiplication table (1–10) for every number in the given range.
Display each table with a clear heading.

"""

start_num = int(input("Enter starting number : "))
end_num = int(input("Enter ending number : "))
for i in range(start_num, end_num + 1):
    print(f"Multiplication Table Of Number {i}.")
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()
