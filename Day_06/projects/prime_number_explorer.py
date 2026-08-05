"""

Project 5: Prime Number Explorer
Objective

Work with prime numbers using loops.

Concepts Used
for loop
Nested loops
break
loop else
Functional Requirements

Provide a menu with options such as:

Check if a number is prime.
Print prime numbers within a range.
Count prime numbers within a range.
Exit.

Keep showing the menu until the user exits.

"""

while True:
    print("======================================")
    choice = int(
        input(
            "\n 1.Check if a number is prime."
            "\n 2.Print prime numbers within a range."
            "\n 3.Count prime numbers within a range."
            "\n 4.Exit."
            "\n Enter your choice :- "
        )
    )
    if choice == 1:
        num = int(input("Enter any number : "))
        if num < 0:
            print(f"{num} = Invalid")
        elif num == 1:
            print("1 = Not Prime")
        else:
            for i in range(2, num):
                if num % i == 0:
                    print(f"{num} = Not Prime")
                    break
            else:
                print(f"{num} = Prime")
    elif choice == 2:
        starting_number = int(input("Enter starting number : "))
        ending_number = int(input("Enter ending number : "))
        for num in range(starting_number, ending_number + 1):
            if num < 0:
                print(f"{num} = Invalid")
            elif num == 1:
                continue
            else:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    print(f"{num} = Prime")
    elif choice == 3:
        starting_number = int(input("Enter starting number : "))
        ending_number = int(input("Enter ending number : "))
        count_prime = 0
        for num in range(starting_number, ending_number + 1):
            if num < 0:
                print(f"{num} = Invalid")
            elif num == 1:
                continue
            else:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    count_prime += 1
        print(
            f"Total Prime Numbers Within range {starting_number} to {ending_number} = {count_prime}."
        )
    elif choice == 4:
        print("======================================")
        print("Thank You For Using This Application")
        print("======================================")
        break
    else:
        print("Incorrect Choice")
