import random

number = random.randint(1, 10)
print('Random number is:', number)

guess = int(input('Please enter your guess: '))
print('You guessed:', guess)

if number == guess:
    print('Well done - you guessed it!')
elif guess < number:
    print('Too low')
elif guess > number:
    print('Too high')