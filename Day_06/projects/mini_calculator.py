"""

Project 7: Mini Calculator with Loop
Objective

Create a simple calculator that runs continuously until the user exits.

Concepts Used
while loop
break
if-elif-else
User input
Functional Requirements

Display a menu:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Ask for two numbers.
Perform the selected operation.
Display the result.
Repeat until the user chooses Exit.

"""

while True:
    print("====================================")
    choice = int(
        input(
            "\n *** MENU ***"
            "\n 1.ADDITION "
            "\n 2.SUBTRACTION "
            "\n 3.MULTIPLICATION "
            "\n 4.DIVISION "
            "\n 5.EXIT "
            "\n Enter Your Choice :- "
        )
    )
    print()
    if choice == 1:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print(f"Addition of {num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print(f"Subtraction of {num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print(f"Multiplication of {num1} * {num2} = {num1 * num2}")
    elif choice == 4:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        if num2 == 0:
            print("Can't divide by zero")
        else:
            print(f"Division of {num1} / {num2} = {num1 / num2}")
    elif choice == 5:
        print("====================================")
        print("Thank You For Using This Application")
        print("====================================")
        break
    else:
        print("Incorrect Choice")
