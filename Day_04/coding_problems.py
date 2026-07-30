# 1. Write a program to add two numbers and print the result.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(f"Addition of {n1} and {n2} = {n1 + n2}")

# 2. Write a program to subtract two numbers.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(f"Subtraction of {n1} and {n2} = {n1 - n2}")

# 3. Write a program to multiply two numbers.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(f"Multiply of {n1} and {n2} = {n1 * n2}")

# 4. Write a program to divide two numbers using /.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(f"Division of {n1} and {n2} = {n1 / n2}")

# 5. Write a program to find the remainder when 25 is divided by 4.
print(25 % 4)

# 6. Write a program to find the floor division of 25 by 4.
print(25 // 4)

# 7. Write a program to calculate 3 raised to the power 4.
print(3**4)

# 8. Create a variable x = 15. Increase it by 10 using a compound assignment operator.
x = 15
x += 10
print(x)

# 9. Create a variable balance = 1000. Decrease it by 250 using a compound assignment operator.
balance = 1000
balance -= 250
print(balance)

# 10. Create a variable count = 6. Multiply it by 5 using a compound assignment operator.
count = 6
count *= 5
print(count)

# 11. Check whether 15 is greater than 8.
print(15 > 8)

# 12. Check whether 20 is equal to 25.
print(20 == 25)

# 13. Check whether 18 is not equal to 12.
print(18 != 12)

# 14. Check whether a number stored in age is between 18 and 60 using a chained comparison.
age = 24
print(18 < age < 60)

# 15. Check whether marks is greater than or equal to 40 and attendance is at least 75.
marks = 73
attendance = 65
print(marks >= 40 and attendance >= 75)

# 16. Check whether a person is eligible if they are either "admin" or "manager".
person = "admin"
print(person == "admin" or person == "manager")

# 17. Use the not operator to reverse a Boolean value.
is_loggin = True
print(not is_loggin)

# 18. Check whether "p" exists in "python".
print("p" in "python")

# 19. Check whether "z" does not exist in "python".
print("z" not in "python")

# 20. Create two variables referring to the same object and check them using is.
a = b = 10
print(a is b)

# 21. Create two different string variables with the same text. Compare them using both == and is.
first_name = "ankit"
last_name = "ankit"
print(first_name == last_name)
print(first_name is last_name)

"""
22.
    Evaluate the expression:
    25 + 5 * 2
    Store and print the result.
"""
result = 25 + 5 * 2
print(result)

"""
23. 
Evaluate:

(25 + 5) * 2
"""
print((25 + 5) * 2)

"""
24. 
Calculate:

50 // 6 + 3
"""
print(50 // 6 + 3)

"""
25. 
Calculate:

18 % 5 + 2 ** 3
"""
print(18 % 5 + 2**3)

"""
26. 
Check whether:

5 < 10 < 20
"""
print(5 < 10 < 20)

"""
27. 
Check whether:

True or False and False
"""
print(True or False and False)

"""
28. 
Check whether:

not True or False
"""
print(not True or False)

# 29. Create a program that checks whether "@gmail.com" exists in an email address.
email = "welcome@gmail.com"
print("@gmail.com" in email)

# 30. Write a simple calculator that performs addition, subtraction, multiplication, division, floor division, modulus, and exponentiation on two numbers entered by the user.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(f"Addition of {n1} and {n2} is {n1 + n2}")
print(f"Subtraction of {n1} and {n2} is {n1 - n2}")
print(f"Multiplication of {n1} and {n2} is {n1 * n2}")
print(f"Division of {n1} and {n2} is {n1 / n2}")
print(f"Floor Division of {n1} and {n2} is {n1 // n2}")
print(f"Modulus of {n1} and {n2} is {n1 % n2}")
print(f"Exponent of {n1} and {n2} is {n1**n2}")
