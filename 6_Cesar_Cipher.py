# #!python

#Cesar Cipher is a easy encrypting and decrypting algorythm.
#The Caesar cipher encrypts letters by shifting them over by a
#key number. For example, a key of 2 means the letter A is
#encrypted into C, the letter B encrypted into D, and so on.

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# User choose enter if he want Encrypting or Decrypting
# keep asking asking until user enters e or d

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    
    user_choice = input('> ').lower()
    if user_choice.startswith('e'):
        mode = 'encrypt'
        break
    elif user_choice.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

#set key value similar like encrypot/decrypt decision
while True:
    maxKey = len(Letters) - 1
    print(f' please enter key value (0 to {maxKey})')
    key_value = (input('>'   ))
    if not key_value.isdecimal(): #Key value must be a number
        continue
    if 0 <= int(key_value) <= maxKey:
        break
    
# now it's a time to get a message from user
print(f'Enter the message to {mode}.')
message = input('> ').upper() #we have capitals letters in our Letters so that must be the same

#we must have empty list for changed message
translated  = []

for letter in message:
    if letter in Letters:
        num = Letters.find(letter) #set letter index
        if mode == 'encrypt':
            num = num + int(key_value)
        elif mode == 'decrypt':
            num = num - int(key_value)
        
        num %= len(Letters)
        
        translated.append(Letters[num])
    else:#just insert symbol into the translatd mesaage
        translated.append(letter)
        
#print the result:

print(f"Oto twoja {mode} wiadomość: {''.join(translated)}")

    