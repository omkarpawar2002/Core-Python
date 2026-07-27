# input() function :
"""
1.To take input from user input() function has been provided by python.
2.By default input always return them as a string.
3.Syntax :  input(prompt)
"""

name = input("Enter your name : ")
print("Name :", name)


# print() function :
"""
print() function is used to display the message/output on screen.
"""
favourite_number = input("Enter your favourite number :")
print("Favourite Number : ", favourite_number)
print(type(favourite_number))


# Type casting :
"""
Type casting is a process of converting one data type into another data type.
There are two types of type casting :
    1.Implicit type casting
    2.Explicit type casting
"""

# Why we required type casting concept :
"""
1.Here we print favourite_number but when i add 2 in it so it shows TypeError.
2.So before adding value in it i need to convert the data type of favourite_number from string to int.
3.So for that python provided different function :
    1.int()             5.list()
    2.float()           6.tuple()
    3.complex()         7.set()
    4.bool()            8.dict()
"""
favourite_number = input("Enter your favourite number :")
print("Favourite Number : ", favourite_number)
print(type(favourite_number))
print("Favourite Number : ", int(favourite_number), type(int(favourite_number)))


# 1.Implicit type casting :
"""
1.Implicit type casting is a process of converting one data type into another automatically.
2.Python automatically converts compatible data types when needed.
"""
num1 = 10
num2 = 34.50
print(num1 + num2)  # Here automatically conversion from int to float so result is float


# Explicit type conversion
"""
1.In explicit type conversion developer manually converted one data type into another.
2.Here we perform explicit type conversion by using some built-in functions :
    1.int()             5.list()
    2.float()           6.tuple()
    3.complex()         7.set()
    4.bool()            8.dict()
"""
favourite_number = input("Enter your favourite number :")
print("Favourite Number : ", favourite_number)
print(type(favourite_number))
print("Favourite Number : ", int(favourite_number), type(int(favourite_number)))
