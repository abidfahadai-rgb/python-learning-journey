#
# File: practical2ex8.py
# Author: Fahad
# Email Id: your_email@example.com
# Description: Practical 2, exercise 8. Calculates a new price after applying a discount.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Ask the user for price and discount
price = float(input("Please enter price in dollars: "))
discount = float(input("Enter discount (%): ")) / 100

# Calculate the discounted price
new_price = price - (price * discount)

# Display the result
print("Price with discount is:", new_price)
