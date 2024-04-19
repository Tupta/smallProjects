import random

Num_Digits = 3
Max_Guesses = 10

def main():
    print(''' Bagels, a deductive logic game. By Al Sweigart
          
      I am thinking of a {}-digit number with no repeated digits.
 
 Try to guess what it is. Here are some clues:
 When I say:    That means:
 Pico         One digit is correct but in the wrong position.
 Fermi        One digit is correct and in the right position.
 Bagels       No digit is correct.'''.format(Num_Digits))
    

def getSecretNum():
    """Returns a string made up of Num_Digits unique random digits."""
    numbers = list('0123456789')  # create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle numbers into random order.
    
    # create the Secret number from digits in the list:
    secretNum = ''
    for i in range(Num_Digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels
    clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'You got it'
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all
    
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues
        return ' '.join(clues)

if __name__ == '__main__':
    main()
    
    while True:  # main game loop
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number')
        print(f' You have {Max_Guesses} guesses to get it.')
        
        numGuesses = 1
        while numGuesses <= Max_Guesses:
            guess = ''
            # keep looping until they enter valid guess:
            while len(guess) != Num_Digits or not guess.isdecimal():
                print(f'Guess #{numGuesses}: ')
                guess = input('> ')
                
                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1
                
                if guess == secretNum:
                    break
                if numGuesses > Max_Guesses:
                    print('You ran out of guesses')
                    print(f' The anserw was {secretNum}.')
                    
        # ask player if they want to play again?
        print(f'Do you want to play again? (y/n)')
        if not input('>').lower().startswith('y'):
            break
    print('Thanks for playing!!!')
