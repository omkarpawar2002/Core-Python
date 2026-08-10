# Write a program to print your name, age, and city using variables.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter city name : ")
print(f"Name : {name}\nAge : {age}\nCity : {city}")

# Write a program to take your name as input and greet the user.
name = input("Enter your name : ")
print(f"Welcome {name}")

# Write a program to take two integers and print their sum, difference, product, and quotient.
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(f"Sum of {num1} and {num2} = {num1 + num2}")
print(f"Difference of {num1} and {num2} = {num1 - num2}")
print(f"Product of {num1} and {num2} = {num1 * num2}")
print(f"Quotient of {num1} and {num2} = {num1 / num2}")

# Write a program to print the data type of different variables using type().
age = 23
price = 299.99
name = "kiran"
is_student = False
print(type(age))
print(type(price))
print(type(name))
print(type(is_student))

# Write a program to swap two numbers using multiple assignment.
num1 = 12
num2 = 13
print(num1,num2)
num1 , num2 = num2 , num1
print(num1,num2)

# Write a program to convert a string input into an integer.
age = input("Enter your age : ")
print(age,type(age))
age = int(age)
print(age,type(age))

# Write a program to convert an integer into a float.
roll_no = 101
print(roll_no,type(roll_no))
roll_no = float(roll_no)
print(roll_no,type(roll_no))

# Write a program to convert a float into an integer.
price = 499.99
print(price,type(price))
price = int(price)
print(price,type(price))

# Write a program to print the id() of two variables.
n1 = 5
n2 = "5"
print(n1,id(n1))
print(n2,id(n2))

# Write a program to calculate the average of three numbers entered by the user.
number_1 = int(input("Enter first number : "))
number_2 = int(input("Enter second number : "))
number_3 = int(input("Enter third number : "))
total = number_1 + number_2 + number_3
avg = total / 3
print(f"Average : {avg}")