"""

Project 3: String Membership Checker

Difficulty: Beginner

Objective

Check whether a word or character exists inside a sentence.

Concepts Used
Membership operators
Strings
input()
Boolean values

Functional Requirements
Ask the user to enter a sentence.
Ask for a word or character to search.
Display whether it exists using in.
Display whether it does not exist using not in.

"""

sentence = input("Enter any sentence : ")
word = input("Enter any word : ")
print("Check Using In Operator = ", (word in sentence))
print("Check Using Not In Operator = ", (word not in sentence))
