#
# File: print_consonants.py
# Author: Fahad
# Description: Program to print only the consonants from a sentence.
# This is my own work as defined by the University's Academic Misconduct policy.
#

sentence = "over the top"

for character in sentence:
    if character != 'a' and character != 'e' and character != 'i' and character != 'o' and character != 'u' and character != ' ':
        print(character)
