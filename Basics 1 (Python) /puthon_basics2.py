# File: python_operations_loops.py
# Author: Fahad
# Description: Demonstrates Python operators, string methods,
# math functions, loops and conditions.

# -------------------------
# 1. String Methods
# -------------------------

course = "Python Programming"

print(course.upper())
print(course.lower())
print(course.title())

print()


# -------------------------
# 2. Removing Spaces
# -------------------------

text = "   hello world   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

print()


# -------------------------
# 3. Find and Replace
# -------------------------

course = "Python"

print(course.find("Py"))
print(course.replace("P", "J"))

print()


# -------------------------
# 4. Membership Operators
# -------------------------

print("Py" in course)
print("Java" not in course)

print()


# -------------------------
# 5. Math Operators
# -------------------------

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

print()


# -------------------------
# 6. Built-in Math Functions
# -------------------------

print(round(2.9))
print(abs(-2.9))

print()


# -------------------------
# 7. Using Math Module
# -------------------------

import math

print(math.ceil(2.3))
print(math.floor(2.9))

print()


# -------------------------
# 8. Shortcut Operators
# -------------------------

x = 10

x = x + 3
print(x)
x += 3
print(x)
# this two means the same code

print()


