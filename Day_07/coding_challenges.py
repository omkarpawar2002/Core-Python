# Reverse a number (using loops)
number = int(input("Enter any number : "))
print("Number = ",number)
num = number
reverse_number = ""
while num != 0:
    last_digit = num % 10
    reverse_number += str(last_digit)
    num //= 10
print("Reverse Number = ",int(reverse_number))

# Count even and odd digits in a number
number = int(input("Enter any number : "))
even = odd = 0
num = number
while num != 0:
    last_digit = num % 10
    if(last_digit % 2 == 0):
        even += 1
    else:
        odd += 1
    num //= 10
print("Even Count = ",even)
print("Odd Count = ",odd)

# Print all factors of a number
num = int(input("Enter any number : "))
print(f"Factors of number {num} : ")
for i in range(1,num+1):
    if(num % i == 0):
        print(" - ",i)

# Check whether a number is prime
number = int(input("Enter any number : "))
if(number < 0):
    print("Invalid Number")
elif(number == 1):
    print("Not Prime")
else:
    for i in range(2,number):
        if(number % i == 0):
            print("Not Prime")
            break
    else:
        print("Prime")

# Find the GCD of two numbers
first_num = int(input("Enter first number : "))
second_num = int(input("Enter second number : "))
highes_gcd = 0
for i in range(1,first_num + 1):
    if(((first_num % i == 0) and (second_num % i == 0)) and ( i > highes_gcd)):
        highes_gcd = i
print(highes_gcd)

# Find the LCM of two numbers
first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
count = 0
for i in range(1,11):
    num1 = first_number * i
    for i in range(1,11):
        num2 = second_number * i
        if(num1 == num2):
            count += 1
            print(f"LCM = {num2}")
    if(count != 0):
        break
            
# Print all prime numbers from 1 to n
number = int(input("Enter any number : "))
for i in range(1,number+1):
    if(i == 1):
        print(f"{i} = Not Prime")
    else:
        for j in range(2,i):
            if(i % j == 0):
                print(f"{i} = Not Prime")
                break
        else:
            print(f"{i} = Prime")

# Print Fibonacci series up to n terms
num1 = 0
num2 = 1
number = int(input("How many Fibonacci Number Want To Generate : "))
count = 0
print(num1,num2,end=" ")
while count < (number - 2):
    temp = num1 + num2
    print(temp,end=" ")
    num1 = num2
    num2 = temp
    count += 1

# Print different star patterns using nested loops
rows = int(input("Enter rows = "))
for i in range(rows):
    for j in range(rows):
        print(" * ",end="")
    print()
print()
for i in range(1,rows + 1):
    for j in range(1,i+1):
        print(" * ",end="")
    print()
print()
for i in range(rows,0,-1):
    for j in range(i):
        print(" * ",end="")
    print()

# Create a number pyramid pattern
rows = int(input("Enter rows : "))
for i in range(1,rows + 1):
    for j in range(rows - i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()