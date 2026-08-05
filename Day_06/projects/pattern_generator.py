"""

Project 2: Pattern Generator
Objective

Create a menu-driven program that prints different patterns based on the user's choice.

Concepts Used
Nested loops
while loop
break
if-elif-else
Functional Requirements

Display a menu like:

1. Square Pattern
2. Right Triangle
3. Inverted Triangle
4. Number Triangle
5. Exit
Ask the user to choose an option.
Ask for the pattern size (number of rows).
Print the selected pattern.
Keep showing the menu until the user chooses Exit.

"""

while True:
    choice = int(
        input(
            "==========================="
            "\n 1. Square Pattern "
            "\n 2. Right Triangle "
            "\n 3. Inverted Triangle "
            "\n 4. Number Triangle "
            "\n 5. Exit "
            "\n==========================="
            "\n Enter your choice :- "
        )
    )
    if choice == 1:
        rows = int(input("Enter rows : "))
        if rows >= 1:
            for row in range(rows):
                for column in range(rows):
                    print("*", end=" ")
                print()
        else:
            print("Rows Should Be Greater Than 0")
    elif choice == 2:
        rows = int(input("Enter rows : "))
        if rows >= 1:
            for row in range(1, rows + 1):
                for column in range(1, row + 1):
                    print("*", end=" ")
                print()
        else:
            print("Rows Should Be Greater Than 0")
    elif choice == 3:
        rows = int(input("Enter rows : "))
        if rows >= 1:
            for row in range(rows, 0, -1):
                for col in range(1, row + 1):
                    print("*", end=" ")
                print()
        else:
            print("Rows Should Be Greater Than 0")
    elif choice == 4:
        rows = int(input("Enter rows : "))
        if rows >= 1:
            for row in range(1, rows + 1):
                for col in range(1, row + 1):
                    print(col, end=" ")
                print()
        else:
            print("Rows Should Be Greater Than 0")
    elif choice == 5:
        print("Thank you for using the application.")
        break
    else:
        print("Incorrect Choice")
