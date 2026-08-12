# Write a program that creates a string containing your name and prints it.
name = "kiran"
print("Name :", name)

# Write a program that stores "Python" in a variable and prints its first character.
language = "Python"
print(language[0])

# Write a program that prints the first, third, and fifth characters of "Python" using indexing.
favourite_language = "Python"
print(favourite_language[0])
print(favourite_language[2])
print(favourite_language[4])

# Write a program that stores a word in a variable and prints its last character using negative indexing.
word = "Programming"
print(word[-1])

# Write a program that prints the first and last characters of a string.
word = "Programming"
print(word[0])
print(word[-1])

# Given word = "Programming", print the first 5 characters using slicing.
word = "Programming"
print(word[:5])

# Given word = "Python", print "thon" using slicing.
word = "Python"
print(word[2:])

# Given word = "Programming", print every second character using slicing.
word = "Programming"
print(word[::2])

# Given a string, print everything except its first character.
word = "Programming"
print(word[1:])

# Given a string, print everything except its last character.
word = "Programming"
print(word[:-1])

# Given word = "Python", create a new string "Jython" without directly modifying word using index assignment.
word = "Python"
new_word = "J" + word[1:]
print(new_word)

# Given word = "Python", create a new string where "Python" becomes "PyXhon". Do not modify an individual character directly.
word = "Python"
new_word = word[:2] + "X" + word[3:]
print(new_word)

# Reverse String: Write a program that takes a string and prints its reverse.
data = "Python"
print(data[::-1])

# Palindrome: Write a program that takes a string and determines whether it is a palindrome.
data = "madam"
if data == data[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# Count Characters: Write a program that takes a string and counts how many characters it contains.
data = "Python"
count = 0
for i in data:
    count += 1
print(count)