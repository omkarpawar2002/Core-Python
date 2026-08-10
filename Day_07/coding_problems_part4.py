# Write a program to print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i,end=" ")

# Write a program to print numbers from 10 to 1 using a while loop.
i = 10
while i > 0:
    print(i,end=" ")
    i -= 1

# Write a program to print the multiplication table of a given number.
num = int(input("Enter number : "))
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

# Write a program to calculate the sum of numbers from 1 to n.
num = int(input("Enter number : "))
total = 0
for i in range(1,num+1):
    total += i
print(f"Total = {total}")

# Write a program to calculate the factorial of a number.
num = int(input("Enter any number : "))
fact = 1
for i in range(1,num+1):
    fact *= i
print(f"Factorial of {num} = {fact}")

# Write a program to count the number of digits in an integer.
num = int(input("Enter any number : "))
if(num == 0):
    print("Count = 1")
count = 0
while num != 0:
    count += 1
    num //= 10
print(f"Count of digit = {count}")

# Write a program to print all even numbers between 1 and 100.
for i in range(1,101):
    if(i % 2 == 0):
        print(i,end=" ")

# Write a program to print a right-angled triangle star (*) pattern using nested loops.
size = int(input("Enter size : "))
for row in range(size):
    for col in range(row + 1):
        print("*", end=" ")
    print()

# Write a program to demonstrate the use of both break and continue in a loop.
for i in range(1, 11):
    if i == 2:
        break
    print(i)

for i in range(1, 11):
    if i == 5:
        continue
    print(i,end=" ")

# Write a program to repeatedly ask the user for a password until the correct password is entered using a while loop.
password = "admin@123"
while True:
    user_password = input("Enter password : ")
    if(user_password == "q"):
        break
    elif(password == user_password):
        print("Correct Password")
        break
    else:
        print("Incorrect Password")