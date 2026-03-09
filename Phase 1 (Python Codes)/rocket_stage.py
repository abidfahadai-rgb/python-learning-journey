#
# File: practical2ex11.py
# Author: Abid Fahad Khan
# Email Id: your_email@example.com
# Description: Practical 2, exercise 11. Determines the stage of missile flight.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Ask the user to enter the time in seconds
time = int(input("Enter the time in seconds: "))

# Determine the stage
if time >= 0 and time < 100:
    print("Stage 1 flight")

elif time >= 100 and time < 170:
    print("Stage 2 flight")

elif time >= 170 and time < 260:
    print("Stage 3 flight")

else:
    print("Free flight (unpowered)")
