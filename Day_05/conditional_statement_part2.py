# 3.If-elif-* statement :
"""
1.When we want to check multiple conditions then we used if - elif - * statement.
2.* means single if block followed by multiple elif blocks.
3.If block will get execute only when the condition specified after the if keyword is True otherwise it will be skipped and check the next elif block and elif block is True then elif block will run and rest will be skipped and if it False then it check the next elif block ,....
4.syntax :
            if(condition):
                ============
                ============
            elif(condition):
                ============
                ============
            elif(condition):
                ============
                ============
            elif(condition):
                ============
                ============
"""

number = int(input("Enter your number : "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative Number")
elif number == 0:
    print("Number is Zero")


# 4.If-elif-*-else statement :
"""
1.When we want to check multiple conditions then we used if - elif - * - else statement.
2.* means single if block followed by multiple elif blocks and multiple elif block followed by single else block.
3.If block will get execute only when the condition specified after the if keyword is True otherwise it will be skipped and check the next elif block and elif block is True then elif block will run and rest will be skipped and if it False then it check the next elif block and so on or if no any condition match then last else block executed.
4.syntax :
            if(condition):
                ============
                ============
            elif(condition):
                ============
                ============
            elif(condition):
                ============
                ============
            elif(condition):
                ============
                ============
            else:
                ============
                ============         
"""

number = int(input("Enter your number : "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative Number")
else:
    print("Number is Zero")


# Nested If Statement :
"""
When if inside another if is known as nested if statement.

Syntax : 
            if(condition):
                if(condition):
                    =============
                    =============
"""
age = int(input("Enter your age : "))
has_license = True
if age >= 18:
    if has_license:
        print("Eligible For Truck Driving")
else:
    print("Minor")
