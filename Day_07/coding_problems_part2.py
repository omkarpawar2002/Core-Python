# Write a program to calculate the area and perimeter of a rectangle.
length = float(input("Enter length : "))
width = float(input("Enter width : "))
print(f"Area : {length * width}")
print(f"Perimeter : {2 * (length + width)}")

# Write a program to calculate the remainder of two numbers.
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(f"Remainder = {num1 % num2}")

# Write a program to calculate the square and cube of a number.
num = int(input("Enter any number : "))
print(f"Square : {num**2}")
print(f"Cube : {num**3}")

# Write a program to check whether a number is even or odd.
num = int(input("Enter any number : "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Write a program to check whether two numbers are equal.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
if n1 == n2:
    print("Equal")
else:
    print("Not Equal")

# Write a program to check whether one number is greater than another.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n2 > n1:
    print(f"{n2} is greater than {n1}")
else:
    print("Both are same")

# Write a program to check whether a number lies between 10 and 50 using a chained comparison.
num = int(input("Enter any number : "))
if 10 <= num <= 50:
    print("Number is in range")
else:
    print("Number is not in range")

# Write a program to check whether a character exists in a string using the membership operator.
language = "Python"
print("P" in language)

# Write a program to demonstrate and, or, and not.
age = int(input("Enter your age : "))
if age >= 18 and age <= 40:
    print("Young")

if age >= 18 or age == 25:
    print("Married Soon")

is_student = True
print(not (is_student))

# Write a program to demonstrate assignment operators (+=, -=, *=, /=).
a = 10
print(a)
a += 5
print(a)
a -= 2
print(a)
a *= 5
print(a)
a /= 5
print(a)
