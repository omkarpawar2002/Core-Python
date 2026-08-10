# Write a program to check whether a person is eligible to vote.
age = int(input("Enter your age : "))
if(age >= 18):
    print("Eligible to vote")
else:
    print("Minor")

# Write a program to find the largest of two numbers.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
if(n1 > n2):
    print(f"{n1} is greater than {n2}")
elif(n2 > n1):
    print(f"{n2} is greater than {n1}")
else:
    print(f"{n1} or {n2} both are same")

# Write a program to find the largest of three numbers.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
if n1 == n2 and n2 == n3 and n3 == n1:
    print("All are same")
else:
    if n1 > n2 and n1 > n3:
        print(f"{n1} is greater than {n2} or {n3}")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} is greater than {n1} or {n3}")
    else:
        print(f"{n3} is greater than {n2} or {n1}")

# Write a program to determine whether a number is positive, negative, or zero.
num = int(input("Enter any number : "))
if num < 0:
    print("Negative")
elif num > 0:
    print("positive")
else:
    print("Zero")

# Write a program to assign grades based on marks.
marks = int(input("Enter your marks : "))
grade = ""
if marks >= 90:
    grade += "A"
elif marks >= 70:
    grade += "B"
elif marks >= 40:
    grade += "C"
else:
    grade += "F"
print(f"Student Marks : {marks} with Grade {grade}")

# Write a program to check whether a year is a leap year.
year = int(input("Enter year : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes it is a leap year")
        else:
            print("No it's not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")

# Write a program to check whether a number is divisible by both 3 and 5.
num = int(input("Enter any number : "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is not divisible by both 3 and 5")

# Write a program to print the absolute value of a number using a conditional expression.
num = int(input("Enter number : "))
print(num if(num > 0) else (-num))

# Write a program to calculate electricity bill units using if-elif-else (use any reasonable slab rates).
units = int(input("How much units consumed : "))
charge = 0
if(units <= 100):
    charge = units * 5
elif(units <= 200):
    charge = units * 8
else:
    charge = units * 10
print(f"Unit : {units}\nCharges : {charge}")

# Write a program to create a simple menu (1–3) and perform different actions based on the user's choice.
while True:
    choice = int(
        input(
            "\n 1.print number from 1 to 5 both included"
            "\n 2.print number from 5 to 1 both included"
            "\n 3.print square of number from 1 to 5 both included"
            "\n Enter your choice :- "
        )
    )
    if choice == 1:
        for i in range(1, 6):
            print(i, end=" ")
    elif choice == 2:
        for i in range(5, 0, -1):
            print(i,end=" ")
    elif choice == 3:
        for i in range(1, 6):
            print(i**2,end=" ")
    else:
        break