#
# File: practical2ex7.py
# Author: Fahad
# Email Id: your_email@example.com
# Description: Practical 2, exercise 7. Calculates the percentage of males
# and females in a class.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Ask the user for number of males and females
males = int(input("Enter the number of males in the class: "))
females = int(input("Enter the number of females in the class: "))

# Calculate total students
total = males + females

# Calculate percentages
male_percentage = (males / total) * 100
female_percentage = (females / total) * 100

# Display the results
print("Percentage of males:", male_percentage, "%")
print("Percentage of females:", female_percentage, "%")
