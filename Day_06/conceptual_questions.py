# 1.What is the difference between a for loop and a while loop? When would you use each one?
"""
1.for loop is used when we know the exact number of times iteration is required.
2.while loop is used when we don't know the exact number of times the iteration is required.

3.for loop is used when we work with range() function or sequences.
4.while loop is used when we work with conditional based.
"""

# 2.What is an iteration?
"""
Iteration means when a loop runs completely one cycle for every element in sequences so that is iteration.
"""

# 3.What is the purpose of the range() function?
"""
range() function is used to generate the sequence of numbers with particular range.
"""

# 4.What is an infinite loop? Mention two common reasons why it happens.
"""
1.Infinite loop is when our loop continuously running.
2.The reason is if we does not update the variable which depends on condition.
3.And sometimes we used flag True but we never change it.
"""

# 5.Explain the difference between break and continue with an example.
"""
1.break keyword is used when we immediately want to exit the loop.
2. Example :

        for i in range(1,6):
            if(i == 2):
                break
            print(i)

1.continue keyword is used when we want to skip the current iteration and jump on the next iteration.
2. Example :

        for i in range(1,6):
            if(i == 2):
                continue
            print(i)
"""

# 6.What is the purpose of the pass statement? When is it commonly used?
"""
1.pass statement is used when we don't want to implement any functionality but to prevent error we used pass keyword.
2.pass acts as a placeholder.
"""

# 7.What is a nested loop? Explain the roles of the outer loop and the inner loop.
"""
1.Nested loop is when a loop inside another loop.
2.Nested loop used at the time of solving patters.
3.Outer loop work for rows and inner loop work for columns.
"""

# 8.When does the else block of a loop execute?
"""
When our loop run successfully without using break keyword then else block execute.
And if loop terminate using break keyword then else does not run.
"""

# 9.What are two good practices for writing clean and efficient loops?
"""
Use good variable name so it make a program readable.
"""

# 10.Why is pattern printing considered a good exercise for learning loops?
"""
Because pattern printing makes the understanding of loops in depth.
With the help of pattern printing we understood the concept of nested loops.
"""