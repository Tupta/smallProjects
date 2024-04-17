
# Project_1 Bagels
# You must guess a secret three-digit number based on clues
# You have 10 tries to guess the secret number.
#
# Hints in response to your guess: 
# “Pico” when your guess has a correct digit in the wrong place,
# “Fermi” when your guess has a correct digit in the correct place,
# “Bagels” if your guess has no correct digits


Num_Digits = 3 
Max_Guesses = 10

def main():
    print(''' Bagels, a deductive logic game. By Al Sweigart
          
      I am thinking of a {}-digit number with no repeated digits.
 
 Try to guess what it is. Here are some clues:
 When I say:    That means:
 Pico         One digit is correct but in the wrong position.
 Fermi        One digit is correct and in the right position.
 Bagels       No digit is correct.'''.format(Num_Digits)    )
    

while True:  #main game loop
    # This stores the secret number the player needs to guess:
    secretNum = getSecretNum()
    print('I have thought up a number')
    print(' You have {} guesses to get it.'.format(Max_Guesses))
    
    numGuesses = 1
    while numGuesses <= Max_Guesses:
        guess =''
        # 