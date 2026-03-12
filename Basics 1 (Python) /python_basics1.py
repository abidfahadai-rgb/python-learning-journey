# File: python_strings_basics.py
# Author: Fahad
# Description: Beginner Python notes covering variables, strings,
# string length, indexing, slicing, and escape characters.


# -----------------------------------
# 1. VARIABLES
# -----------------------------------

number1 = 5        # Integer -> whole number
number_2 = 4.99    # Float -> decimal number
boolean_value = True  # Boolean -> True or False

string_example = "python basics"   # String -> text


# multi-line string using triple quotes
multi_line_string = """
Hi this is Abid
Let's learn python together
"""

print(number1)
print(number_2)
print(boolean_value)
print(string_example)


# -----------------------------------
# 2. STRING LENGTH
# -----------------------------------

course = "Learning Code"

# len() returns number of characters in the string
print("Length of course:", len(course))


# -----------------------------------
# 3. STRING INDEXING
# -----------------------------------

course_2 = "python basics"

# indexing starts from 0 in Python

print("First character:", course_2[0])   # p
print("Second character:", course_2[1])  # y

# negative index counts from the end

print("Last character:", course_2[-1])   # s


# -----------------------------------
# 4. STRING SLICING
# -----------------------------------

# slicing extracts part of a string
# format -> string[start:end]

print("Full string:", course_2[:])

print("First 4 characters:", course_2[0:4])

print("From index 2 onwards:", course_2[2:])


# -----------------------------------
# 5. ESCAPE CHARACTERS
# -----------------------------------

# \" allows quotation marks inside a string
print("abid\"s code")

# \n moves text to the next line
print("abid\ncoder")

# \\ prints a backslash
print("This is a backslash: \\")