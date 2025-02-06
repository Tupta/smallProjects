#!python

import random
#This program is Caesar Cipher Hacker, but at the end it's You who mus chose right version

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#We have to get crypted text
message = input('Please enter Your crypterd message :>').upper()


#Empty list for encrypted messages
encrypted = []
#no we have to try encrypted text for 26 times

for number in range(0,26):
    encrypted = []
    for letter in message:
        if letter in Letters:
            num = Letters.find(letter)
            
            #print(num)
            #print(Letters[(num + number) % 26])
            encrypted.append(Letters[(num + number) % 26])
        else:
            encrypted.append(letter)    

    print(f"szyfr_{number} daje taką wiadomość: {''.join(encrypted)}")  