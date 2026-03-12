#
# File: reverse_star_triangle.py
# Author: Fahad
# Description: Program that prints a reverse triangle star pattern using nested loops.
#

height = 6

for row in range(height, 0, -1):
    for column in range(1, row + 1):
        print("*", end="")
    print()