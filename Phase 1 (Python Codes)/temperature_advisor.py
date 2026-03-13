#
# File: practical2ex12.py
# Author: Fahad
# Email Id: your_email@example.com
# Description: Practical 2, exercise 12. Displays a message based on temperature.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Ask the user to enter the temperature
temperature = int(input("Enter the temperature in degrees: "))

# Check the temperature
if temperature >= 40:
    print("Way too hot - stay inside!")

elif temperature >= 30:
    print("Hot - beach time!")

elif temperature >= 20:
    print("Lovely day - how about a picnic!?!")

elif temperature >= 10:
    print("On the cold side - better take a jacket!")

else:
    print("Way too cold - stoke up the fire!")

#So why does the program still work correctly?

#Because Python checks conditions from top to bottom and 
#stops at the first true condition.
