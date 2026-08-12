"""
Project: Text Analyzer
Objective

Build a small console program that accepts a piece of text from the user and analyzes it using the Day 8 string concepts.

Your final program could produce something similar to:

===== TEXT ANALYZER =====

Enter text: Python

Original: Python
First character: P
Last character: n
First 3 characters: Pyt
Reverse: nohtyP
Palindrome: No
Character count: 6
UTF-8 encoded: b'Python'
Decoded text: Python

The exact formatting is up to you.
"""

print("===== TEXT ANALYZER =====\n")
input_data = input("Enter input here : ")
print("\noriginal :",input_data)
print("First Character :",input_data[0])
print("Last Character :",input_data[-1])
print("First 3 Characters :",input_data[:3])
print("Reversed :",input_data[::-1])
print("Palindrome : Yes" if(input_data == input_data[::-1]) else "Palindrome : No")
count = 0
for i in input_data:
    count += 1
print("Character count =",count)
encoded_text = input_data.encode('utf-8')
print("UTF-8 encoded:",encoded_text)
decoded_text = encoded_text.decode()
print("Decoded text:",decoded_text)