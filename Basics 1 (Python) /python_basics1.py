# File: python_basics1.py
# Author: Abid Fahad Khan
# Description: Demonstrates basic Python variables, strings,
# string length, indexing, slicing, and escape characters.

# -------------------------
# Basic Variables
# -------------------------

number1 = 5                 # Integer
number_2 = 4.99             # Float

# String examples
string_example = "python basics"

multi_line_string = """
Hi this is Abid
Let's learn python together
"""

boolean_value = True        # Boolean


# -------------------------
# String Length
# -------------------------

course = "Learning Code"

# len() returns the number of characters in a string
print("Length of course:", len(course))


# -------------------------
# String Indexing
# -------------------------

course_2 = "python basics"

print("Length of course_2:", len(course_2))

# First character
print("First character:", course_2[0])

# Last character
print("Last character:", course_2[-1])


# -------------------------
# String Slicing
# -------------------------

# Print entire string
print("Full string:", course_2[:])

# Print first four characters
print("First 4 characters:", course_2[0:4])


# -------------------------
# Escape Characters
# -------------------------

# \" allows quotes inside a string
print("abid\"s code")

# \n moves text to the next line
print("abid\ncoder")

# \\ prints a backslash
print("This is a backslash: \\")
