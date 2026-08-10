"""

Project – Banking System (Revision Challenge) ⭐⭐
Objective

Combine almost every concept from Days 2–6 into one program.

Concepts Used
Variables
Input/Output
Operators
Control Flow
Loops
break
continue
Nested Conditions

Functional Requirements
Ask the user to log in with a predefined PIN.
Allow a maximum of 3 login attempts.
If login is successful, display a menu:
Check Balance
Deposit
Withdraw
Change PIN (without using functions)
Exit
Validate all user inputs.
Prevent invalid transactions.
Continue showing the menu until the user exits.

"""
pin = 457837
login_attempts = 3
while login_attempts > 0:
    user_pin = int(input("Enter login pin : "))
    if(user_pin == pin):
        balance = 10000
        while True:
            print("===========================================")
            choice = int(
                input(
                    "\n -------- ATM Simulation --------"
                    "\n 1.Check Balance "
                    "\n 2.Deposit  "
                    "\n 3.Withdrawl "
                    "\n 4.Exit "
                    "\n Enter your choice : "
                )
            )
            if(choice == 1):
                print("Balance Available = ",balance)
            elif(choice == 2):
                d_amt = int(input("Enter amount want to deposit : "))
                if(d_amt > 0):
                    balance += d_amt
                    print("Amount Deposit Successfully")
                else:
                    print("Deposit Valid Amount")
            elif(choice == 3):
                w_amt = int(input("Enter amount want to withdrawl : "))
                if(w_amt <= 0):
                    print("Enter valid amount")
                else:
                    if(w_amt <= balance):
                        balance -= w_amt
                        print("Amount Withdrawl Successfully")
                    else:
                        print("Insufficient Fund")
            elif(choice == 4):
                print("===========================================")
                print("Thank you for using this application")
                break
            else:
                print("Incorrect Choice")
    else:
        change_pin = input("Do you want to change pin : ")
        if(change_pin == "yes"):
            new_pin = int(input("Enter new pin : "))
            pin = new_pin
        else:
            login_attempts -= 1
            print(f"You have {login_attempts} attmpts only")
