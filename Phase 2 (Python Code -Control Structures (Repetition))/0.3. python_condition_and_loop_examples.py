#
# File: python_condition_and_loop_examples.py
# Author: Fahad
# Description: Examples demonstrating while loops and conditional statements in Python.
#

# 
# (a) While loop example
# ---------------------------------------------------

k = 1

while k <= 5:
    print("Stuck in a loop!")
    k = k + 1

print() # blank line for readability after each example


# 
# (b) While loop decreasing example
# ---------------------------------------------------

k = 6

while k >= 2:
    print("Still looping.")
    k = k - 2

# if we want to use for loop for the output
# for k in range(6, 1, -2):
#    print("Still looping.")
#
# if -  runs once if condition is true
# while -   runs repeatedly while condition stays true

print()


# 
# (c) Simple if statement
# ---------------------------------------------------

num1 = 2
num2 = 4

if num1 < num2:
    print("Yes.")

print()


# 
# (d) Comparing two strings
# ---------------------------------------------------

str1 = "kramer"
str2 = "george"

if str1 == str2:
    print("Equal.")
else:
    print("Not equal.")

print()


# 
# (e) Grade classification example
# ---------------------------------------------------

mark = 78

if mark >= 85:
    print("HD")
elif mark >= 75:
    print("D")
elif mark >= 65:
    print("C")
elif mark >= 55:
    print("P1")
elif mark >= 50:
    print("P2")
elif mark >= 40:
    print("F1")
else:
    print("F2")