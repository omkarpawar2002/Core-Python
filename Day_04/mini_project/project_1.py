"""

Project 1: Basic Calculator

Difficulty: Beginner

Objective

Create a calculator that performs basic arithmetic operations.

Concepts Used
Arithmetic operators
Assignment
Expressions
input()
print()

Functional Requirements
Accept two numbers from the user.
Display:
Addition
Subtraction
Multiplication
Division
Floor Division
Modulus
Exponentiation

"""

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print("========================================================")
print(f"Addition of {num1} and {num2} is {num1 + num2}")
print(f"Subtraction of {num1} and {num2} is {num1 - num2}")
print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
print(f"Division of {num1} and {num2} is {num1 / num2}")
print(f"Floor Division of {num1} and {num2} is {num1 // num2}")
print(f"Modulus of {num1} and {num2} is {num1 % num2}")
print(f"Exponent of {num1} and {num2} is {num1**num2}")
print("========================================================")
