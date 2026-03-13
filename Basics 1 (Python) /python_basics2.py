# File: python_string_methods_math.py
# Author: Fahad
# Description: Beginner Python notes covering string methods,
# operators, and basic math functions.


# -----------------------------------
# 1. STRING METHODS
# -----------------------------------

course = "Python Programming"

# .upper() converts text to uppercase
print(course.upper())

# .lower() converts text to lowercase
print(course.lower())

# .title() capitalizes the first letter of each word
print(course.title())


# -----------------------------------
# 2. REMOVING EXTRA SPACES
# -----------------------------------

text = "   hello world   "

# strip() removes spaces from both sides
print(text.strip())

# lstrip() removes spaces from the left
print(text.lstrip())

# rstrip() removes spaces from the right
print(text.rstrip())


# -----------------------------------
# 3. FINDING TEXT
# -----------------------------------

course = "Python"

# find() returns the position of text
print(course.find("Py"))


# -----------------------------------
# 4. REPLACING TEXT
# -----------------------------------

# replace(old, new)
print(course.replace("P", "J"))


# -----------------------------------
# 5. CHECKING TEXT
# -----------------------------------

# 'in' checks if something exists in a string
print("Py" in course)

# 'not in' checks if something does NOT exist
print("Java" not in course)


# -----------------------------------
# 6. BASIC MATH OPERATORS
# -----------------------------------

print(10 + 3)   # addition
print(10 - 3)   # subtraction
print(10 * 3)   # multiplication
print(10 / 3)   # division

print(10 // 3)  # integer division (removes decimal)
print(10 % 3)   # remainder
print(10 ** 3)  # power


# -----------------------------------
# 7. BUILT-IN MATH FUNCTIONS
# -----------------------------------

# round() rounds number to nearest integer
print(round(2.9))

# abs() returns positive value
print(abs(-2.9))


# -----------------------------------
# 8. USING MATH MODULE
# -----------------------------------

# modules provide extra functions
import math

# ceil() rounds up
print(math.ceil(2.3))

# floor() rounds down
print(math.floor(2.9))


# -----------------------------------
# 9. SHORTCUT OPERATORS
# -----------------------------------

x = 10

# normal addition
x = x + 3
print(x)

# shortcut operator (same as the last example)
x += 3
print(x)