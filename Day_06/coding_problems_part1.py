# write a program to print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

# write a program to print numbers from 10 to 1 in reverse order using a for loop.
for i in range(10, 0, -1):
    print(i)

# write a program to print all even numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# write a program to print all odd numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# write a program to print the square of numbers from 1 to 10.
for i in range(1, 11):
    print(i**2)

# write a program to print the cube of numbers from 1 to 10.
for i in range(1, 11):
    print(i**3)

# write a program to calculate and print the sum of numbers from 1 to 10.
total = 0
for i in range(1, 11):
    total += i
print("Total =", total)

# write a program to calculate and print the sum of all even numbers from 1 to 100.
even_total = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_total += i
print("Even Total =", even_total)

# write a program to print numbers from 1 to 20 using a while loop.
i = 1
while i < 21:
    print(i)
    i += 1

# write a program to print numbers from 20 to 1 in reverse order using a while loop.
i = 20
while i > 0:
    print(i)
    i -= 1

# write a program to print the first 10 multiples of 5.
count = 0
for i in range(1, 101):
    if i % 5 == 0:
        print(i)
        count += 1
        if count == 10:
            break

# write a program to print the multiplication table of a number entered by the user.
num = int(input("Enter any number : "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# write a program to print numbers from 1 to 10, but skip the number 5 using the continue statement.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# write a program to print numbers from 1 to 10, but stop the loop when the number becomes 6 using the break statement.
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# write a program that uses the pass statement inside a loop and prints "Loop Completed" after the loop ends.
for i in range(1, 11):
    pass
print("Loop Completed")

# write a program to search for the number 16 in the list [4, 8, 15, 16, 23, 42] using a loop and break.
li = [4, 8, 15, 16, 23, 42]
num = 16
for i in li:
    if i == 16:
        print("Number Found =", num)
        break

# write a program to print only the positive numbers from the list [5, 10, -3, 7, -1, 12] using the continue statement.
li = [5, 10, -3, 7, -1, 12]
for i in li:
    if i > 0:
        print(i)
    else:
        continue

# write a program to search for the number 7 in the range 1 to 10 using a loop and loop else.
for i in range(1, 11):
    if i == 7:
        print("Found")
        break
else:
    print("Number found 7")


# writea program to count the number of digits in an integer entered by the user using a while loop.
num = int(input("Enter any number : "))
count = 0
while num != 0:
    last_digit = num % 10
    count += 1
    num = num // 10
print("Count : ", count)

# writea program to calculate the sum of the digits of an integer entered by the user using a while loop.
num = int(input("Enter any number : "))
sum_of_digits = 0
while num != 0:
    last_digit = num % 10
    sum_of_digits += last_digit
    num = num // 10
print("Sum of all digits =", sum_of_digits)
