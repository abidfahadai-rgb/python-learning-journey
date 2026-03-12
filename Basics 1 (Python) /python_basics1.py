# File: python_basics_strings.py
# Author: Fahad
# Description: Demonstrates basic Python variables, strings,
# string length, indexing, slicing, and escape characters.

# -------------------------
# 1. Basic Variables
# -------------------------

number1 = 5                 # Integer
number_2 = 4.99             # Float

# String example
string_example = "python basics"

multi_line_string = """
Hi this is Abid
Let's learn python together
"""

boolean_value = True        # Boolean

print(number1)
print(number_2)
print(string_example)
print(boolean_value)

print()


# -------------------------
# 2. String Length
# -------------------------

course = "Learning Code"

# len() returns number of characters
print("Length of course:", len(course))

print()


# -------------------------
# 3. String Indexing
# -------------------------

course_2 = "python basics"

print("Length of course_2:", len(course_2))

# First character
print("First character:", course_2[0])

# Last character
print("Last character:", course_2[-1])

print()


# -------------------------
# 4. String Slicing
# -------------------------

# Print entire string
print("Full string:", course_2[:])

# Print first four characters
print("First 4 characters:", course_2[0:4])

print()


# -------------------------
# 5. Escape Characters
# -------------------------

# \" allows quotes inside string
print("abid\"s code")

# \n creates a new line
print("abid\ncoder")

# \\ prints a backslash
print("This is a backslash: \\")