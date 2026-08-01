# Conditional Statements :
"""
Conditional Statements are used to manipulate the flow of our program execution.
Conditional statements are used when we want to take decision.

There are 4 types of conditional statement in python :
    1.If statement
    2.If-else statement
    3.If-elif-* statement
    4.If-elif-*-else statement
"""

# 1.If Statement :
"""
1.When we want to check only 1 condition then we used if statement.
2.The if block will get execute only when the condition specified after the if keyword is True oterwise if block will be skipped.
3.syntax :
            if(condition):
                ========
                ========
"""
age = int(input("Enter your age : "))
if age >= 18:
    print("Adult")


# 2.If-else statement :
"""
1.When we have 2 outcomes either this or this so we used if-else statement.
2.If block will get execute only when the condition specified after the if keyword is True otherwise it will be skipped and else block will get executed.
3.else block always follows if block.
4.else only execute when if block will become False.
5.syntax :
            if(condition):
                ============
                ============
                ============
            else:
                ============
                ============
                ============
6.Also remember else block does not have any condition.
"""
age = int(input("Enter your age : "))
if age >= 18:
    print("Eligible To Vote")
else:
    print("Not Eligible To Vote")
