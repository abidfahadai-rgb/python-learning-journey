#
# File: python_loop_and_string_examples.py
# Author: Fahad
# Description: Demonstrates Python loops, range usage, string iteration,
# list membership checking, and nested loops for pattern printing.
#

# 
# Example 1: Using range() in a for loop
# range(start, stop, step)
# ------------------------------

for k in range(4):
    print(k)

print()  # blank line for readability after each example


#
# Example 2: range with step value
# Prints even numbers from 0 to 8
# range(start, stop, step)
# --------------------------------

for k in range(0, 10, 2):
    print("k is:", k)

print()


# 
# Example 3: Loop through a string
# Line 38 go through each character in the string and store it in k.
# -------------------------------------

string = "Sooo much fun!"

for k in string:
    print(k)

print()


#
# Example 4: Checking if an item exists in a list
# ------------------------------------------

fruit = ["apple", "pear", "banana", "orange", "watermelon"]

if "pear" in fruit:
    print("Yes it is!")
else:
    print("No it isn't!")

print()


# 
# Notes
# print(' ')  - prints a space
# end=''      - prevents moving to the next line
# sep=''      - Removes separator between printed values
# ---------------------------------------------------


# 
# Example 5: Nested loops pattern
# ---------------------------------------------------

for loop in range(3):
    for loop1 in range(1):
        for loop2 in range(2):
            print("#", sep="", end="")
        print(" ", sep="", end="")
    print("!")