"""

Project 3: Number Analysis Tool
Objective

Analyze a number entered by the user using loops.

Concepts Used
while loop
for loop
if
Iteration
Functional Requirements

Ask the user to enter a number and display:

Number of digits
Sum of digits
Reverse of the number
Whether it is a palindrome
Whether it is a prime number

After displaying the results, ask the user whether they want to analyze another number.

Continue until the user chooses to exit.

"""

while True:
    print("===== Number Analysis Tool =====")
    number = int(input("Enter number : "))

    # Number of digits
    num1 = number
    number_of_digits = 0
    while num1 != 0:
        last_digit = num1 % 10
        number_of_digits += 1
        num1 = num1 // 10
    print(f"Digits : {number_of_digits}")

    # Sum of digits
    num2 = number
    sum_of_digits = 0
    while num2 != 0:
        last_digit = num2 % 10
        sum_of_digits += last_digit
        num2 = num2 // 10
    print(f"Sum : {sum_of_digits}")

    # Reverse of the number
    num3 = number
    reverse_num = ""
    while num3 != 0:
        last_digit = num3 % 10
        reverse_num += str(last_digit)
        num3 = num3 // 10
    print(f"Reverse : {int(reverse_num)}")

    # Whether it is a palindrome
    num4 = number
    reverse_num = ""
    while num4 != 0:
        last_digit = num4 % 10
        reverse_num += str(last_digit)
        num4 = num4 // 10
    if number == int(reverse_num):
        print("Palindrome : Yes")
    else:
        print("Palindrome : No")

    # Whether it is a prime number
    num5 = number
    if num5 < 0:
        print(f"{num5} = Invalid Number")
    elif num5 == 1:
        print("Prime : No")
    else:
        for i in range(2, num5):
            if num5 % i == 0:
                print("Prime : No")
                break
        else:
            print("Prime : Yes")

    print("======================================")
    ch = input("Do you want to exit : [yes / no] ")
    if ch == "yes":
        break
