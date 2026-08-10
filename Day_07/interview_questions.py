# What is dynamic typing?
"""
    1.Dynamic typing means before declaring a variable like other programming languages like java , c , c++ so in python we no need 
      to specify the data type.
    2.During runtime python will automatically find out which type of variable is this.
"""

# What is the difference between mutable and immutable objects? (Answer only from your current beginner understanding.)
"""
    1.Mutable objects are those who can change once we create it.
    2.Immutable objects are those who can not change once we create it.
"""

# What is the difference between == and is?
"""
    1. == is an is equals to operator which used to check whether both LHS and RHS are equals.
    2. is operator is used to check whether both variable refferes the same object in memory.
"""

# Explain the difference between for and while loops.
"""
    1.for loop is used when we know the exact number of times the iteration is required.
    2.while loop is used when we don't know the exact number of times the iterations is required

    1.for loop is best and work with sequences and range() function mostly.
    2.while loop also best for condition based expressions.
"""

# What happens if you forget to update the condition in a while loop?
"""
    1.If we forget to update the variable who totally depends on condition in while loop so loop run infinitely.
    2.But sometimes run infinitely is best for running servers.
"""

# What are assignment operators? Give examples.
"""
    Assignment operator is used to assign the RHS value to the LHS of variable.

    1.Addition Assignment operators are used to evaluates the Addition on RHS and then assign the result to LHS of variable.
    2.Subtraction Assignment operators are used to evaluates the Subtraction on RHS and then assign the result to LHS of variable.
    3.Multiplication Assignment operators are used to evaluates the Multiplication on RHS and then assign the result to LHS of variable.
    4.Division Assignment operators are used to evaluates the Division on RHS and then assign the result to LHS of variable.
    5.Floor Division Assignment operators are used to evaluates the Floor Division on RHS and then assign the result to LHS of variable.
    6.Modulus Assignment operators are used to evaluates the Modulus on RHS and then assign the result to LHS of variable.
    7.Exponent Assignment operators are used to evaluates the Exponent on RHS and then assign the result to LHS of variable.
"""

# What is the difference between break, continue, and pass?
"""
    1.break keyword is used when we immediately want to exit the loop.
    2.continue keyword is used when we want to skip the current iteration and jump on the next iteration.
    3.pass keyword is used as a placeholder. Program is syntactially correct but we don't want to implement any functionality so to avoid errors we used pass which does nothing.
"""

# Why do we use type conversion?
"""
    1.type conversion we used to convert the 1 data type into another.
    2.we know input always return string but if we want to perform the calculation so we need to convert them into their respective data type so we can perform operation.
"""

# Explain operator precedence with an example.
"""
    Operator precedance tell us which expression evalute first.

    print(5 + 4 * 4)  // 21
    print((5 + 4) * 4)  // 36
    Look here output is different because in first example * have more precidence than + operator.
    And in second example () paranthesis have more precidance than * operator.
"""