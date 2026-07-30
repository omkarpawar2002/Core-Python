# 3.Logical Operators :

"""
1.and :
        1.and operator is used to check whether both the conditions are True or not.
        2.If both conditions are True then only it return True or if any one condition if False then it return False.
"""

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(n1 == n2 and n1 > n2)

"""
2.or :
        1.or operator is used to check whether both the condition are True or not.
        2.If both conditions are False then only it return False or if any one condition if True then it return True.
"""

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
print(n1 == n2 or n1 > n2)

"""
3.not :
        1.not operator is used to reverse the result.
        2.If condition is True it return False or if condition is False then it return True.
"""

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
result = n1 == n2
print(result)
print(not result)

print(
    "=================================================================================================="
)

# 4.Assignment operators :

"""
1.Assignment operator [ = ] :
        1.Assignment operator is used to assign the RHS value to the LHS of variable.
"""

name = input("Enter your name : ")
print("Name :", name)

"""
2.Addition Assignment [ += ] :
        Addition Assignment operators are used to evaluates the Addition on RHS and then assign the result to LHS of variable.
"""

n1 = 100
print(n1)
n1 += 50
print(n1)

"""
3.Subtraction Assignment [ -= ] :
        Subtraction Assignment operators are used to evaluates the Subtraction on RHS and then assign the result to LHS of variable.
"""

n1 = 100
print(n1)
n1 -= 50
print(n1)

"""
4.Multiplication Assignment [ *= ] :
        Multiplication Assignment operators are used to evaluates the Multiplication on RHS and then assign the result to LHS of variable.
"""

n1 = 100
print(n1)
n1 *= 5
print(n1)

"""
5.Division Assignment [ /= ] :
        Division Assignment operators are used to evaluates the Division on RHS and then assign the result to LHS of variable.
"""

n1 = 10
print(n1)
n1 /= 3
print(n1)

"""
6.Floor Division Assignment [ //= ] :
        Floor Division Assignment operators are used to evaluates the Floor Division on RHS and then assign the result to LHS of variable.
"""

n1 = 10
print(n1)
n1 //= 3
print(n1)

"""
7.Modulus Assignment [ %= ] :
        Modulus Assignment operators are used to evaluates the Modulus on RHS and then assign the result to LHS of variable.
"""

n1 = 10
print(n1)
n1 %= 3
print(n1)

"""
8.Exponent Assignment [ **= ] :
        Exponent Assignment operators are used to evaluates the Exponent on RHS and then assign the result to LHS of variable.
"""

n1 = 10
print(n1)
n1 **= 3
print(n1)
