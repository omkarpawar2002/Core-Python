# Print "Hello, Python!".
print("Hello, Python!")

# Create a variable name and print it.
name = "Kirti"
print("Name : ", name)

# Create variables for your age and city, then print both.
age = 23
city = "Mumbai"
print("My Age Is", age)
print("I Live In", city)

# Assign three variables in one line and print them.
a, b, c = 101, 201, 301
print(a, b, c)

# Assign the same value to three variables.
a = b = c = 111
print(a, b, c)

# Swap the values of two variables without using a temporary variable.
a, b = 101, 201
print(a, b)
a, b = b, a
print(a, b)

# Create a constant PI and print it.
PI = 3.14
print(PI)

# Write a program with two comments explaining the code.
age = 23  # Here we defined a variable age and store 23
name = "Naitik"  # Here we defined variable name and store Naitik
print("My Name Is", name, "And Age", age)

# Add a docstring to a simple program.
"""
    1.Person Joined Course In Pune
    2.Course Name Is FUll Stack Python
"""
city = "pune"
course_name = "full stack python"

# Print the type of an integer.
age = 23
print(type(age))

# Print the type of a string.
name = "jinesh"
print(type(name))

# Print the type of a decimal number.
marks = 78.34
print(type(marks))

# Create variables with meaningful names following snake_case.
student_marks = 90.32
student_name = "vishal"
print(student_marks)
print(student_name)

# Try using a keyword as a variable name and observe the error.
"""
if = 23   
print(if)

It will show syntax error
"""

# Create two variables with different letter cases (for example, age and Age) and print both.
age = 23
Age = 29
print(age, Age)

# Print the id() of two different variables.
age = 23
Age = 29
print(id(age), id(Age))

# Reassign a variable from an integer to a string and print its type before and after.
name = "kiran"
print(type(name))
name = 23
print(type(name))

# Write a program that stores your favorite book, author, and publication year in variables and prints them.
favourite_book = "python with beginner"
author_name = "Guido Van Rossum"
publication_year = 1991
print("Favourite Book =", favourite_book)
print("Author Name =", author_name)
print("Publication Year =", publication_year)

# Create three constants (MAX_USERS, DEFAULT_PORT, PI) and print them.
MAX_USERS = 5
DEFAULT_PORT = 4000
PI = 3.14
print(MAX_USERS, DEFAULT_PORT, PI)

# Write a short program that demonstrates good variable naming, comments, and proper indentation.
age = 19  # Valid variable name
if age >= 18:
    print("Eligible To Vote!")  # Proper Indentation
