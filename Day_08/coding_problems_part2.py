# 16. Create a string containing your full name and print: First character , Last character , Second character , Second-last character
full_name = "James Gosling"
print("First character :", full_name[0])
print("Last character :", full_name[-1])
print("Second character :", full_name[1])
print("Second-last character :", full_name[-2])

# 17. Given: python text = "Python Programming" Print the character at:Index 0 , 7 , -1 , -5
text = "Python Programming"
print(text[0])
print(text[7])
print(text[-1])
print(text[-5])

# 18. Take a string as input and print its first character and last character.
name = input("Enter name : ")
print("First character =", name[0])
print("Last character =", name[-1])

# 19. Take a word as input and print its first three characters using slicing.
word = input("Enter word : ")
print("First three characters =", word[:3])

# 20. Take a string as input and print its last three characters using slicing and negative indexing.
input_str = input("Enter input : ")
print(input_str[-3:])

# 21. Given: python text = "Programming"  Print Code Program using slicing.
text = "Programming"
print(text[:7])

# 22. Given python text = "Programming" Print Code gram using slicing.
text = "Programming"
print(text[3:7])

# 23. Given python text = "PythonProgramming" Print only: Code Python using slicing.
text = "PythonProgramming"
print(text[:6])

# 24. Take a string as input and print First half Second half (Assume the input has an even number of characters.)
input_data = "Kartik"
count = 0
for i in input_data:
    count += 1
first_half = count // 2
second_half = first_half
print("First Half =", input_data[:first_half])
print("Second Half =", input_data[first_half:])

# 25. Take a string as input and print every second character.
# Example:
# Input: Python
# Output: Pto
input_data = input("Enter your input here : ")
print(input_data[::2])

# Reverse & Palindrome
# 26. Take a string as input and print it in reverse using slicing.
data = input("Enter input : ")
print(data[::-1])

# 27. Take a string as input and determine whether it reads the same forward and backward.
# Example:
# Input: level → Output: Palindrome
# Input: python → Output: Not a palindrome
data = input("Enter input data here : ")
if data == data[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# 28. Take a string as input and print both the original string and its reversed version.
# Example:
# Original: Python
# Reverse: nohtyP
input_data = input("Enter input : ")
print("Original =", input_data)
print("Reversed =", input_data[::-1])

# 29. Write a program that produces exactly this output:
# Name: Siri
# Course: Python
# Level: Beginner
# Use \n.
name = "Siri"
course = "Python"
level = "Beginner"
print("Name:", name, "\nCourse:", course, "\nLevel:", level)

# 30. Write a program that stores and prints this Windows-style path:
# C:\Users\Siri\Documents\Python
# Use a raw string.
data = r"C:\Users\Siri\Documents\Python"
print(data)
