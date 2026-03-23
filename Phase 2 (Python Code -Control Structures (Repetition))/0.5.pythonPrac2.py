import random

# Roll two dice
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

# Check results
if die1 == die2:
    print(f"You rolled a pair of {die1}s!")
else:
    print(f"You rolled a {die1} and a {die2}")



# Ask user for input
number = int(input("Enter an integer from 1-10: "))

# Check range and display Roman numeral
if number == 1:
    print("I")
elif number == 2:
    print("II")
elif number == 3:
    print("III")
elif number == 4:
    print("IV")
elif number == 5:
    print("V")
elif number == 6:
    print("VI")
elif number == 7:
    print("VII")
elif number == 8:
    print("VIII")
elif number == 9:
    print("IX")
elif number == 10:
    print("X")
else:
    print("Error: Number must be between 1 and 10.")



# Get user input
day = int(input("Enter the day of month: "))
month = int(input("Enter the month in numeric form: "))
year = int(input("Enter the year in two digit format: "))

# Check if the date is magic
if day * month == year:
    print(f"The date {day}/{month}/{year} is a magic date.")
else:
    print(f"The date {day}/{month}/{year} is not a magic date.")



import random

number = random.radint(0,10)
guess = int(input("Please enter the first number:"))

if number==guess:
 print ("You have entered the correct number:")
else:
 print("Wrong")



import random

count = 0
even = 0
odd = 0

while count < 100:
    number = random.randint(1, 1000)

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

    count += 1

print(f"Out of 100 random numbers, {odd} were odd, and {even} were even.")




import random

outer_count = 0

while outer_count < 10:                           # Repeat 10 times
    count = 0
    even = 0
    odd = 0

    while count < 100:                           # Generate 100 numbers
        number = random.randint(1, 1000)

        if number % 2 == 0:
            even += 1
        else:
            odd += 1

        count += 1

    print(f"Out of 100 random numbers, {odd} were odd, and {even} were even.")

    outer_count += 1




import random

for i in range(10):                             # Outer loop → repeat 10 times
    even = 0
    odd = 0

    for j in range(100):                        # Inner loop → generate 100 numbers
        number = random.randint(1, 1000)

        if number % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"Out of 100 random numbers, {odd} were odd, and {even} were even.")



index1 = 0
index2 = 0
input1 = int(input("Enter an integer: "))
input2 = int(input("Enter another integer: "))
while index1 < input1:
    while index2 < input2:
        print("#", end="")
        index2 = index2 + 1
    print()
    index2 = 0
    index1 = index1 + 1