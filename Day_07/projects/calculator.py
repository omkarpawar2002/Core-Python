"""

Project – Basic Calculator ⭐ (Mandatory)
Objective

Create a calculator that performs basic arithmetic operations based on the user's choice.

Concepts Used
Variables
Input/Output
Type Conversion
Arithmetic Operators
if-elif-else

Functional Requirements
Display a menu:
Addition
Subtraction
Multiplication
Division
Exit
Accept the user's choice.
Ask for two numbers.
Perform the selected operation.
Display the result.
Handle division by zero.
Display an "Invalid Choice" message for incorrect menu options.

Challenge (Optional):

Keep showing the menu until the user chooses Exit.

"""

while True:
    print("===========================================")
    choice = int(
        input(
            "\n -------- Calculator --------"
            "\n 1.Addition "
            "\n 2.Subtraction "
            "\n 3.Multiplication "
            "\n 4.Division "
            "\n 5.Exit "
            "\n Enter your choice : "
        )
    )
    if(choice == 1):
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(f"Addition of {num1} + {num2} = {num1 + num2}")
    elif(choice == 2):
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(f"Subtraction of {num1} - {num2} = {num1 - num2}")
    elif(choice == 3):
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(f"Multiplication of {num1} * {num2} = {num1 * num2}")
    elif(choice == 4):
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        if(num2 == 0):
            print("Can not divide by 0")
        else:
            print(f"Division of {num1} / {num2} = {num1 / num2}")
    elif(choice == 5):
        print("===========================================")
        print("Thank you for using this application")
        break
    else:
        print("Incorrect Choice")