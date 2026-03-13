#
# File: practical2ex13.py
# Author: Fahad
# Email Id: your_email@example.com
# Description: Practical 2, exercise 13. Calculates Joe's stock transaction details.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Purchase details
shares_bought = 2000
purchase_price = 40.00
purchase_commission_rate = 0.03

# Sale details
shares_sold = 2000
sale_price = 42.75
sale_commission_rate = 0.03

# Amount Joe paid for the stock
amount_paid = shares_bought * purchase_price

# Commission paid when buying
buy_commission = amount_paid * purchase_commission_rate

# Amount Joe sold the stock for
amount_sold = shares_sold * sale_price

# Commission paid when selling
sell_commission = amount_sold * sale_commission_rate

# Final money left
money_left = amount_sold - sell_commission - amount_paid - buy_commission

# Display results
print("Amount paid for the stock:", amount_paid)
print("Commission paid when buying:", buy_commission)
print("Amount sold for:", amount_sold)
print("Commission paid when selling:", sell_commission)
print("Money left after selling and commissions:", money_left)
