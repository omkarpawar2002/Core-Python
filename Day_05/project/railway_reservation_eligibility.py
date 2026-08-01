"""

🟡 Project 5 – Railway Reservation Eligibility
🎯 Objective

Determine whether a passenger can reserve a seat.

📚 Concepts Used
Nested if
Boolean evaluation
elif
✅ Functional Requirements

Inputs:

Age
Ticket Available (True/False)
ID Proof Available (True/False)

Rules:

Ticket must be available.
If available:
Check ID proof.
If ID proof is available:
Booking Confirmed.
Otherwise:
Booking Rejected.
⭐ Challenge

Display a special message for senior citizens (60+).

"""

age = int(input("Enter your age : "))
if age > 0:
    ticket_available = input("Enter ticket available [yes or no] : ")
    if ticket_available == "yes":
        has_id = input("Do you have Id Card [yes or no] : ")
        if has_id == "yes":
            if age >= 60:
                print("Booking Confirmed\nSenior Citizen\nSpecial Discount")
            else:
                print("Booking Confirmed")
        else:
            print("Booking Rejected Due To Id Card Not Available")
    else:
        print("Booking Rejected Due To Ticket Unavailable")
else:
    print("Invalid Age")