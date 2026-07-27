# Print your name.
name = input("Enter your name : ")
print("Name :", name)

# Print your age.
age = int(input("Enter your age : "))
print("Age :", age)

# Store your age in a variable and print it.
age = int(input("Enter your age : "))
print("Age :", age)

# Store your height as a float and print it.
height = 5.78
print("Height :", height)

# Create a complex number and print it.
data = 3 + 4j
print(data)

# Create a Boolean variable indicating whether you like Python..
is_like_python = True
print(is_like_python)

# Create a variable with None and print its type.
data = None
print(data, type(data))

# Print three variables using a single print().
num1, num2, num3 = 10, 20, 30
print(num1, num2, num3)

# Ask the user for their name and greet them.
name = input("Enter your name : ")
print("Welcome,", name)

# Ask for the user's city and print it.
city_name = input("Enter city name : ")
print(city_name)

# Ask for the user's age and print its type before conversion.
age = input("Enter your age : ")
print(age, type(age))

# Convert the entered age to an integer and print it.
age = int(input("Enter your age : "))
print(age, type(age))

# Ask for two integers and print their sum.
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print("Sum of 2 numbers :", num1 + num2)

# Ask for two floating-point numbers and print their product.
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
print("Product of 2 numbers :", num1 * num2)

# Convert an integer to a float.
number = 10
print(number, type(number))
number = float(number)
print(number, type(number))

# Convert a float to a string.
number = 10.5
print(number, type(number))
number = str(number)
print(number, type(number))

# Convert a string "100" to an integer.
number = "100"
print(number, type(number))
number = int(number)
print(number, type(number))

# Convert "45.6" to a float.
number = "45.6"
print(number, type(number))
number = float(number)
print(number, type(number))
# Add an integer and a float, then print the result and its type.
n1 = 10
n2 = 5.5
res = n1 + n2
print(res, type(res))

# Calculate the area of a rectangle using user input.
length = float(input("Enter length :"))
width = float(input("Enter width :"))
area = length * width
print("Area of rectangle :", area)

# Calculate the area of a circle using a fixed value of π (for example, 3.14).
radius = float(input("Enter radius : "))
PI = 3.14
area = PI * (radius**2)
print("Area of circle :", area)

# Convert an integer to a complex number and print it.
data = 25
print(data, type(data))
data = complex(data)
print(data, type(data))

# Ask the user for their favorite programming language and display a message using it.
favourite_language = input("Enter favourite programming language :")
print("favourite_language:", favourite_language)

# Store information about a person (name, age, height, student status) and print it clearly.
name = input("Enter your name :")
age = int(input("Enter your age :"))
height = float(input("Enter your height :"))
is_student = True
print("Name :", name)
print("Age :", age)
print("Height :", height)
print("Is Student :", is_student)

# Create a simple program that asks for a user's name, age, and city, then prints a formatted profile.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter your city name : ")
print("==== Profile ====")
print("Name :", name)
print("Age :", age)
print("City Name :", city)
print("=================")