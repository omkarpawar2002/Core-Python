"""

Project – ATM Simulation
Objective

Create a simple ATM system.

Concepts Used
Variables
Loops
if-elif-else
Arithmetic Operators
Functional Requirements

Start with a balance (for example, ₹10,000).

Display a menu:

Check Balance
Deposit
Withdraw
Exit

Rules:

Deposit increases the balance.
Withdraw decreases the balance only if there are sufficient funds.
Prevent negative withdrawals.
Continue showing the menu until Exit is selected.

"""

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
        balance += d_amt
        print("Amount Deposit Successfully")
    elif(choice == 3):
        w_amt = int(input("Enter amount want to withdrawl : "))
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