# Control statement :
"""
Control statements control the flow of program execution. Loops are one type of control statement used to execute code repeatedly.

So there are 2 types of loop in python :
    1.for
    2.while
"""

# Iteration :
"""
Iteration means when a loop runs complete one cycle for every element in sequence.
"""

# range() :
"""
1.range() function mainly work with for loop.
2.range() is used to generate the sequence of number.
3.In range(5) function if we have one value so it treated as a stop value so output = 0 1 2 3 4
4.In range(1,5) function if we have two value so it treated as a start value 1 or stop value 5 so output = 1 2 3 4
5.In range(1,7,2) function if we have three value so it treated as a start value 1 or stop value 7 or step value 2 so output = 1 3 5
6.Always remember stop value is exclusive.
"""

# 1.For loop :
"""
1.For loop is used when we know the exact number of time the iteration is required.
2.for loop mainly used with range() function or also work with sequences.
3.syntax :
            for variable in range():
                ==================
                ==================
"""

# Single value means stop value so start from 0 and end on 9 because 10 is not included
for i in range(10):
    print(i)


# start from 1 and end on 11 so 11 is not included
for i in range(1, 11):
    print(i)


# start value 1 stop value 11 or step is 2 and 11 not included
for i in range(1, 11, 2):
    print(i)

# For loop also work with sequences like [ list , tuple , string ] :
li = [10, 20, 30, 40, 50]
for i in li:
    print(i)


# 2.While loop :
"""
1.While loop is used when we don't know the exact number of times the iteration is required.
2.syntax :
            while (condition):
                ===================
                ===================
                ===================
"""
i = 5
while i > 0:
    print(i)
    i -= 1


# Infinite loop :
"""
i = 5
while i > 0:
    print(i)

We need to just check variable is updated or not because we need to stop the loop so condition become false.
If condition are always True then loop runs infinitely so try to avoid this.
"""
