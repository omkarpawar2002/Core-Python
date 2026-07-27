# Data Types
"""
Data type represents what kind of data a variable holds.

There are different kinds of data types in python :
    1.Numeric data types :
        a.int
        b.float
        c.complex
    2.String data type
    3.Boolean data type
    4.None data type
    5.Collective data type :
        a.List
        b.Tuple
        c.Set
        d.Dictionary
"""

# Numeric data types :
"""
Numeric data types are used to store numbers

1.int data type: 
    1.int data type are used to store whole numbers[without decimal parts].
    2.So to store roll_number , emp_id we used int data type.
"""
roll_no = 101
print("Roll Number :", roll_no)
print(type(roll_no))


"""
2.float data type :
    1.float data type are used to store decimal values.
    2.We used floating data type when we want to store price , salary , height etc..,
"""
temperature = 45.75
print(temperature)
print(type(temperature))


"""
3.complex data type :
    1.complex data type are used to store special numbers.
    2.It contain 1 real part and another is imaginary part.
    3.we used complex data type in electrical engineering,scientific calculations.
"""
data = 1 + 2j
print(data)
print(type(data))


"""
4.String data type :
    1.String is a sequence of characters.
    2.Anything which kept together inside single quotes or double quotes are treated as string.
    3.We used string to store textual data like name , address , ifsc_code etc.,...
"""
name = "kiran"
print(name)
print(type(name))


"""
5.None data type :
    1.None data type represents the absence of a value.
    2.We used this when we does not provide intensionally data to variable.
"""
data = None
print(data)
print(type(data))


"""
5.Collective data types :
    1.We used collective data types to store multiple values.
    2.We learn them in detail later.
"""
