"""
Mini Project
Project Name

Simple User Profile Generator

Ask the user for:
Name
Age
City
Height
Convert age and height to appropriate numeric types.
Display the information in a neat, readable format.
Print a friendly closing message such as "Thank you for using the User Profile Generator!"
"""

name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter city name : ")
height = float(input("Enter your height : "))
print("===== Profile Generator! =====")
print("Name :", name)
print("Age :", age)
print("City :", city)
print("Height :", height)
print("===============================")
print("Thank you for using the User Profile Generator!")