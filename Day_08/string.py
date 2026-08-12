"""
String : 
        1.string is a sequence of characters.
        2.Anything which kept together inside single , qouble quotes are treated as a string in python.
        3.String is a immutable.
"""

# using single quotes
name = 'welcome'

# using double quotes
name = "kirti"

# Indexing  : 
"""
    1.We know string is a sequence of characters so we can access them using indexing.
    2.Indexing is a position number which given to every element in sequence.
    3.Indexing is starts from 0.
    4.Python supports both positive indexing and negative indexing.
    5.Positive indexing start from 0 and negative indexing start with -1.
"""
data = "Python is a programming language"
print(data[0])
print(data[-1])

# Once we create string we can not change single character but we can replace with new string.
data = "welcome"
# data[0] = "z"  Here error occur.
data = "zelcome" # Here we replace string from welcome to zelcome
print(data)

# Slicing :
"""
1.Slicing means break down the sequences into sub-sequences.
2.If we want to work with single element then go with indexing.
3.But if we want to work with more than 1 element then go with slicing.
"""
word = "Python"
print(word[1:4])
print(word[1:4:2])
print(word[::-1])