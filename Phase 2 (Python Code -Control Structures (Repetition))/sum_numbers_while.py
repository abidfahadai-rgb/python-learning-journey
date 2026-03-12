#
# File: sum_numbers_while.py
# Author: Fahad 
# Description: Program that keeps asking the user for numbers and
# adds them together until the user enters -1.
#

total = 0

num = int(input("Please enter a number (-1 to quit): "))

while num >= 0:
    print("Number is:", num)
    total = total + num
    num = int(input("Please enter a number (-1 to quit): "))

print("Sum of all numbers entered is:", total)
