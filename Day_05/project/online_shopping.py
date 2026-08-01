"""
🟡 Project 4 – Online Shopping Discount System
🎯 Objective

Calculate discount eligibility for customers.

📚 Concepts Used
if
elif
Nested if
✅ Functional Requirements

Inputs:

Customer Type
Regular
Silver
Gold
Purchase Amount

Rules:

Gold customers:
₹5000 or more → 20%
Otherwise → 15%
Silver:
₹3000 or more → 10%
Otherwise → 5%
Regular:
₹5000 or more → 5%
Otherwise → No Discount

Display:

Customer Type
Discount Percentage
Final Message
⭐ Challenge

Display a congratulatory message for customers receiving the highest discount.
"""

customer_type = int(input("Enter Customer Type\n 1.Gold\n 2.Silver\n 3.Regular :- "))
discount = 0
purchase_amount = float(input("Enter purchase amount : "))
if customer_type == 1:
    customer_type = "Gold"
    if purchase_amount >= 5000:
        discount = 20
    else:
        discount = 15
elif customer_type == 2:
    customer_type = "Silver"
    if purchase_amount >= 3000:
        discount = 10
    else:
        discount = 5
elif customer_type == 3:
    customer_type = "Regular"
    if purchase_amount >= 5000:
        discount = 5
    else:
        discount = 0
else:
    customer_type = "Unknown"
    print("Unknown Customer Type")

print("===============================")
print("ONLINE SHOPPING DISCOUNT SYSTEM")
print("===============================")
print(f"Customer Type : {customer_type}")
print(f"Purchase Amount : {purchase_amount}")
print(f"Discount : {discount}")
if customer_type == "Gold":
    print("Congratulation You Get Highest Discount")
discount = purchase_amount * (discount / 100)
print(f"Final Bill : {purchase_amount - discount}")
print("===============================")
