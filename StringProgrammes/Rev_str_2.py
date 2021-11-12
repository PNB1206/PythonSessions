import logging




""" Printing even characters and Odd characters separatly"""

def print_even_char_in_aString():
    s = 'JesusChrist'
    i=0
    print('Printing even characters')
    while i < len(s):
        if i%2 == 0:
            print(s[i])
        i = i +2
    i =1
    print()
    print('Printing Odd characters')
    while i < len(s):
        if i%2 !=0:
            print(s[i])
        i= i+2

print_even_char_in_aString()