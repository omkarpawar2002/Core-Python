# Write a program to print a square pattern of * with 5 rows and 5 columns using nested loops.
for row in range(5):
    for column in range(5):
        print("*", end=" ")
    print()

# Write a program to print a right triangle pattern of * with 5 rows.
for row in range(5):
    for column in range(row + 1):
        print("*", end=" ")
    print()

# Write a program to print an inverted right triangle pattern of * with 5 rows.
for row in range(5, 0, -1):
    for column in range(row):
        print("*", end=" ")
    print()

# Write a program to print the following number pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()

# Write a program to print the following pattern:
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
for row in range(5, 0, -1):
    for col in range(5, row - 1, -1):
        print(col, end=" ")
    print()

# Write a program to print the multiplication tables from 1 to 5 using nested loops.
for num in range(1, 6):
    print("Multiplication Table Of Number", num)
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
    print()

# Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# Write a program to calculate the factorial of a number entered by the user using a loop.
num = int(input("Enter any number : "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial Of {num} = {fact}")

# Write a program to check whether a number entered by the user is a prime number.
num = int(input("Enter any number : "))
if num < 0:
    print("Invalid Number")
elif num == 1:
    print("1 is not prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "Is Not Prime Number")
            break
    else:
        print(num, "Is Prime Number")

# Write a program to print all prime numbers between 1 and 100.
for i in range(1, 101):
    if i == 1:
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, "= Prime Number")

# Write a program to print the first 10 terms of the Fibonacci series.
num1 = 0
print(num1, end=" ")
num2 = 1
print(num2, end=" ")
i = 1
while i <= (10 - 2):
    temp = num1 + num2
    print(temp, end=" ")
    num1 = num2
    num2 = temp
    i += 1

# Write a program to print the Fibonacci series up to a limit entered by the user.
num = int(input("Enter any number : "))
print(f"User Want Fibonacci Series Upto {num} Numbers")
i = 1
num1 = 0
print(num1, end=" ")
num2 = 1
print(num2, end=" ")
while i <= (num - 2):
    temp = num1 + num2
    print(temp, end=" ")
    num1 = num2
    num2 = temp
    i += 1

# Write a program to reverse a number entered by the user using a while loop.
num = int(input("Enter any number : "))
print(f"User Enter Number = {num}")
reverse_number = ""
while num != 0:
    last_digit = num % 10
    reverse_number += str(last_digit)
    num = num // 10
print(f"Reversed Number = {int(reverse_number)}")

# Write a program to check whether a number entered by the user is a palindrome.
num = int(input("Enter any number : "))
number = num
reverse_num = ""
while number != 0:
    last_digit = number % 10
    reverse_num += str(last_digit)
    number = number // 10
if num == int(reverse_num):
    print("palindrome number")
else:
    print("Not palindrome")

# Write a program to print all Armstrong numbers between 1 and 1000.
for i in range(1, 1001):
    number = i
    num = number

    # Calculate Length
    count = 0
    while num != 0:
        last_digit = num % 10
        count += 1
        num = num // 10

    # Calculate sum of each number
    new_num = number
    total = 0
    while new_num != 0:
        last_digit = new_num % 10
        total += last_digit**count
        new_num = new_num // 10

    if number == total:
        print(f"{number} is an Armstrong number")

# Write a program to repeatedly ask the user to enter a positive number. Stop only when a positive number is entered.
num = int(input("Enter positive number : "))
while num < 0:
    print("User Enter =", num)
    if num > 0:
        break
    num = int(input("Enter positive number : "))

# Write a program to create a simple menu using a while loop that keeps running until the user chooses to exit.
while True:
    ch = int(
        input(
            "Enter Your Choice "
            "\n 1.print number from 1 to 5 both included "
            "\n 2.exit :- "
        )
    )
    if ch == 1:
        for i in range(1, 6):
            print(i, end=" ")
        print()
    elif ch == 2:
        break
    else:
        print("Incorrect Choice")

# Write a program to print all numbers from 1 to 50, skipping numbers divisible by 4 using the continue statement.
for i in range(1, 51):
    if i % 4 == 0:
        continue
    print(i)

# Write a program to search for a number entered by the user in the list [12, 25, 37, 48, 59, 63]. If found, stop searching using break; otherwise, display a message using loop else.
num = int(input("Enter any number : "))
print("User Enter Number :", num)
li = [12, 25, 37, 48, 59, 63]
print("List =", li)
for i in li:
    if num == i:
        print("Number Found", i)
        break
else:
    print("Number Not Found In List")

# Write a program that combines nested loops and break to stop printing the inner loop when a specific condition is met.
for row in range(5):
    for col in range(5):
        if col == 3:
            break
        print(row, col)
    print()
