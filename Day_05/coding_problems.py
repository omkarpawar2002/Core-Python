# Write a program to check whether a number is positive.
number = int(input("Enter any number : "))
if number > 0:
    print(f"{number} is Positive")

# Write a program to check whether a number is negative.
number = int(input("Enter any number : "))
if number < 0:
    print(f"{number} is Negative")

# Write a program to check whether a number is zero.
number = int(input("Enter any number : "))
if number == 0:
    print(f"{number} is Zero")

# Write a program to check whether a person is eligible to vote (age ≥ 18).
age = int(input("Enter any age : "))
if age >= 18:
    print("Eligible to vote")

# Write a program to check whether a number is even or odd.
number = int(input("Enter any number : "))
if number % 2 == 0:
    print(f"{number} is Even Number")
else:
    print(f"{number} is Odd Number")

# Write a program to compare two numbers and print the larger one.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n2 > n1:
    print(f"{n2} is greater than {n1}")
else:
    print("both are same")

# Write a program to check whether a student has passed (marks ≥ 40).
marks = int(input("Enter your marks : "))
if marks >= 40:
    print("Student is passed")
else:
    print("Student is failed")

# Write a program to check whether a character is uppercase or lowercase (assume the user enters an English alphabet).
ch = input("Enter any character : ")
if ch >= "a" and ch <= "z":
    print(f"{ch} is in lowercase")
elif ch >= "A" and ch <= "Z":
    print(f"{ch} is in uppercase")

# Write a program to check whether a number is divisible by 5.
number = int(input("Enter any number : "))
if number % 5 == 0:
    print(f"{number} is Divisible by 5")
else:
    print(f"{number} is not Divisible by 5")

# Write a program to print "Adult" if age is 18 or above; otherwise print "Minor".
age = int(input("Enter your age : "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Write a program to find the largest of three numbers using if-elif-else.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
if n1 >= n2 and n1 >= n3:
    print(f"{n1} is greater than {n2},{n3}")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} is greater than {n1},{n3}")
else:
    print(f"{n3} is greater than {n2},{n1}")

# Write a program to find the smallest of three numbers.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
if n1 <= n2 and n1 <= n3:
    print(f"{n1} is smaller than {n2},{n3}")
elif n2 <= n1 and n2 <= n3:
    print(f"{n2} is smaller than {n1},{n3}")
else:
    print(f"{n3} is smaller than {n2},{n1}")

"""
Write a program to assign grades:
90 to 100 → A
75 to 89 → B
50 to 74 → C
Below 50 → F
"""
marks = int(input("Enter your marks : "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade F")

# Write a program to check whether a year is a century year (e.g., 1900, 2000, 2100).
year = int(input("Enter any year : "))
if year % 100 == 0:
    print(f"{year} is a Century Year")
else:
    print(f"{year} is not a Century Year")

# Write a program to determine whether a number is a one-digit, two-digit, or three-digit number (assume only positive integers).
number = int(input("Enter any number : "))
if number > 0:
    if number >= 1 and number <= 9:
        print(f"{number} is 1 digit number")
    elif number >= 10 and number <= 99:
        print(f"{number} is 2 digit number")
    elif number >= 100 and number <= 999:
        print(f"{number} is 3 digit number")

# Write a program that checks whether a password entered by the user matches a predefined password.
user_password = input("Enter any password : ")
password = "admin@123"
if user_password == password:
    print("Password Match")
else:
    print("Password Not Match")

"""
Write a program to determine ticket pricing:
Child (below 12)
Teen (12–17)
Adult (18–59)
Senior (60 and above)
"""
age = int(input("Enter your age : "))
ticket_price = 0
if age < 12:
    ticket_price = 0
elif age <= 17:
    ticket_price = 99
elif age <= 59:
    ticket_price = 299
else:
    ticket_price = 150
print(f"Age = {age} Now Pay Ticket Price = {ticket_price}")

# Write a program to compare two people's ages and print who is older, or print that they are the same age.
person1_age = int(input("Enter person 1 age : "))
person2_age = int(input("Enter person 2 age : "))
if person1_age > person2_age:
    print(
        f"Person 1 Age Is {person1_age} So He Is Older Than Person 2 Age Which Is {person2_age}"
    )
elif person2_age > person1_age:
    print(
        f"Person 2 Age Is {person2_age} So He Is Older Than Person 1 Age Which Is {person1_age}"
    )
else:
    print("Both Are Same Age")

"""
Write a program to check whether a person qualifies for a sports competition:
Age between 15 and 25 (inclusive)
Otherwise, not eligible.
"""
age = int(input("Enter your age : "))
if age >= 15 and age <= 25:
    print("Qualify For Sports Competition")
else:
    print("Not Qualify For Sports Competition")

"""
Write a menu-driven calculator that lets the user choose:
1 → Addition
2 → Subtraction
For any other choice, print "Invalid Choice".
"""
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
choice = int(
    input("*** Menu Driven ***\n 1.Addition \n 2.Subtraction \n Enter your choice : ")
)
if choice == 1:
    print(f"Addition of {num1} and {num2} = {num1 + num2}")
elif choice == 2:
    print(f"Subtraction of {num1} and {num2} = {num1 - num2}")
else:
    print("Invalid Choice")

"""
Write a program that determines a student's result:
If marks are below 40 → Fail
If marks are 40 or above and attendance is at least 75% → Pass
Otherwise → Detained due to low attendance.
"""
marks = int(input("Enter your marks : "))
attendance = int(input("Enter your attendance : "))
if marks < 40:
    print("Fail")
else:
    if attendance >= 75:
        print("Pass")
    else:
        print("Detained due to low attendance")

"""
Write a program for ATM withdrawal:
Check whether the balance is sufficient.
If sufficient, check whether the entered PIN is correct.
Print the appropriate message.
"""
balance = float(input("Enter your balance : "))
if balance >= 1000:
    print("Balance Sufficient")
    pin = int(input("Enter pin : "))
    if pin == 1234:
        print("Withdrawal Successful")
    else:
        print("Incorrect Pin")
else:
    print("Insufficient Balance")

"""
Write a login system:
Check the username.
If correct, check the password.
Display appropriate messages.
"""
username = input("Enter username : ")
password = input("Enter password : ")
if username == "admin" and password == "admin@123":
    print("Login Success!")
else:
    print("Username and Password not match")

"""
Write a movie ticket eligibility program:
Age must be at least 13.
If age is below 13, allow entry only if accompanied by an adult (use a boolean variable).
"""
age = int(input("Enter your age : "))
with_adult = True
if age >= 13:
    print("Eligible")
else:
    if with_adult:
        print("Allowed")
    else:
        print("Not Allowed")


"""
Write a scholarship eligibility checker:
Student must have passed.
If passed, check whether marks are at least 90.
Print the result.
"""
marks = int(input("Enter your marks : "))
if marks >= 40:
    if marks >= 90:
        print("Student Is Passed and Eligible For Scholarship")
    else:
        print("Student Is Passed but Not Eligible For Scholarship")
else:
    print("Failed")

"""
Write a driving license eligibility checker:
If age is at least 18, then check whether the person has the required documents (use a boolean variable).
"""
age = int(input("Enter your age : "))
has_identity_proof = False
if age >= 18:
    if has_identity_proof:
        print("Eligibile For Driving License")
    else:
        print("First Open pan card Then Apply")
else:
    print("Minor")

"""
Write a bank account type checker:
Balance ≥ 50,000 → Premium
Balance ≥ 10,000 → Gold
Balance ≥ 1,000 → Silver
Otherwise → Basic
"""
balance = float(input("Enter your bank balance : "))
account_type = ""
if balance >= 50000:
    account_type = "Premium"
elif balance >= 10000:
    account_type = "Gold"
elif balance >= 1000:
    account_type = "Silver"
else:
    account_type = "Basic"
print(f"Balance = {balance} With {account_type} Account.")

"""
Write a hospital priority system:
Critical → Highest Priority
Serious → Medium Priority
Stable → Normal Priority
Any other input → Unknown Status
"""
patient_type = int(
    input(
        "** Enter Patient Type ** "
        "\n 1.Critical "
        "\n 2.Serious "
        "\n 3.Stable "
        "\n Enter choice : "
    )
)
if patient_type == 1:
    print("Highest Priority")
elif patient_type == 2:
    print("Medium Priority")
elif patient_type == 3:
    print("Normal Priority")
else:
    print("Unknown Status")

"""
Write a school admission checker:
Check minimum age.
If eligible by age, then check whether required documents are submitted (use a boolean variable).
"""
age = int(input("Enter your age : "))
documents_submitted = True
if age >= 6:
    if documents_submitted:
        print("Eligible For Admission")
    else:
        print("First Submit the document")
else:
    print("Not eligible for school admission")

"""
Write a restaurant table booking checker:
If seats are available, then check whether the booking time is within business hours (use suitable variables).
Display the appropriate message.
"""
seats_available = True
booking_time = "Normal Hours"
if seats_available:
    if booking_time == "Normal Hours":
        print("Seats Available")
    else:
        print("Not Possible")
else:
    print("Seats Not Available")
