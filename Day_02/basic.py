# Syntax
"""
1.Syntax is the set of rules that tells us how to write Python programs correctly.
2.If we are not follow the syntax then python throws an error called as SyntaxError.
"""

# Indentation
"""
1.Indentation means adding some spaces [4 space] before the code block.
2.In other programming language to define a block of code we used curly braces {}. But here we used indenation. 
"""
if True:
    print("Hello World")


# Keywords
"""
1.Keywords are the reserved words in python.
2.We can not used them as a variable name because they have a special meaning in python programming.
3.All the keywords are in lowercase except [True,False,None].
4.For example : if , else , elif , True , for , while , not , and , or ......
"""

# Identifiers
"""
Identifiers are names used to identify variables, functions, classes, or modules.
For Example : a = 20 ------> Here a is a valid identifier
"""

# Variables
"""
1.Variable is a container which used to store or hold a value in computer memory so we can used it later.
or
2.Variable is a name reffered to objects in memory.
3.For Example : 
                name = "ketan" ---> Here "ketan" is a value and name is a variable name 
"""
name = "ketan"
print(name)

# We can also declare multiple variable in single line
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

# Variable naming rules
"""
1.Variable name can contain alphanumeric characters.
2.Variable name can start with letter and underscore but not with number.
3.Among all the special character only underscore is allowed.
4.Variable name are case sensitive.
5.Reserved keywords can not be used as a variable name.
"""

# Constants
"""
1.Constant is a value if we assign to variable so that value never change throught the program in other programming languages.
2.But here in python there is no any way to make a constant variable.
3.But if you want to take a feel then try to make a variable in uppercase letter, so it's a hint to other developer try to not modify its value.
4.Example : PI = 3.14
"""

PI = 3.14
print(PI)

# Comments
"""
1.Comments are notes written for humans. Python ignores them while executing the program.
2.Comments are useful while debugging the code.
3.There are 2 types of comments in python 
    a.Single line comment : 
            Single line comment is denoted by hash [#] symbol.
    
    b.Multi-line comment :
            Multi-line comment is denoted by single/double triple quotes [''' '''] or [""" """].
"""

# Documentation strings (docstrings)
"""
A docstring is the first string inside a module, function, class, or method that describes its purpose.
"""

# Naming conventions
"""
Here we need to follow proper naming conventions instead of a , b we can used proper name like name , age.
"""
a = "Abhishek"
b = 23
print(a, b)  # It's valid but not recommended

name = "Abhishek"
age = 23
print(name, age)  # Recommended

# Multiple assignment
a = b = c = 100
print(a)
print(b)
print(c)

# Dynamic typing
"""
1.Python is a dynamically typed programming language.
2.So we no need to define the data type of variable before declaring a variable like other programming c,c++ or java.
"""
name = "Naitik"

# type()
"""
type() function is used to return the type of object.
"""
marks = 78.34
print(type(marks))

# id()
"""
id() function is used to return unique identifier of an object.
or in cpython it return the memory address of varible.
"""
age = 23
print(id(23))
