#
# File: even_numbers_step_range.py
# Author: Fahad
# Description: Program to print even numbers up to a stop value using the step value in range().
# This is my own work as defined by the University's Academic Misconduct policy.
#
# range(start, stop, step)
# Why 101?
# Because Python stops before the stop value.
#

stop_value = 100

for number in range(2, stop_value + 1, 2):
    if number == stop_value:
        print(number)
    else:
        print(number, end=", ")
