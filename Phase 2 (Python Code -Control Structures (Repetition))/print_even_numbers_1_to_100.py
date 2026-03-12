#
# File: print_even_numbers_1_to_100.py
# Author: Fahad
# Description: Program to print all even numbers from 1 to 100 separated by commas.
# This is my own work as defined by the University's Academic Misconduct policy.
#

for number in range(1, 101):
    if number % 2 == 0:
        print(number, end=', ')
