"""

🔵 Project 8 – Airport Security Check System
🎯 Objective

Verify whether a passenger can proceed to boarding.

📚 Concepts Used
Nested if
Boolean evaluation
Branching logic
✅ Functional Requirements

Inputs:

Passport Available (True/False)
Visa Required (True/False)
Visa Available (True/False)
Security Cleared (True/False)

Rules:

Passport is mandatory.
If visa is required, verify the visa.
After document verification, perform the security check.
Display:
Boarding Allowed
Boarding Denied
Reason
⭐ Challenge

Display a different message for domestic and international passengers.

"""

passport = input("Is passport available [yes/no] : ")
if passport == "yes":
    flight_type = input("Enter flight type [domestic/international] : ")
    if flight_type == "international":
        visa_available = input("Is visa available [yes/no] : ")
        if visa_available == "yes":
            security_check = input("Have you done with security check [yes/no] : ")
            if security_check == "yes":
                print("Boarding Allowed")
            else:
                print("Boarding Denied Due To Security Check")
        else:
            print("Visa Not Available")
            print("So you are not allowed for international flights.")
    elif flight_type == "domestic":
        print("Visa is not required for domestic flights.")
        security_check = input("Have you done with security check [yes/no] : ")
        if security_check == "yes":
            print("Boarding Allowed")
        else:
            print("Boarding Denied Due To Security Check")
    else:
        print("Flight type not match")
else:
    print("Passport Not Available")
