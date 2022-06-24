
import random

def userGuess():

    computerRandom = random.randint(0,10)
    guessCounter = 3

    while guessCounter !=0:
        userGuess = input("guess the computer's number from 0 to 9 : ")

        if userGuess.isdigit():

            if computerRandom == userGuess:
                print('you guessed correct, it was ', userGuess)
                break

            else:

                if guessCounter == 1:
                    print('you lose, the number was ', computerRandom)
                    guessCounter-=1

                else:
                    print('you guessed wrong try again ')
                    guessCounter-=1

        else: 
            print('please enter a number')

def ComputerGuess():

    print('choose a number between 0 and 100')
    initialRange = 0
    finalRange = 100
    computerTry = random.randint(initialRange,finalRange)
    response = input('is' + str(computerTry) + 'too high(h). too low(l) or correct(c)?  h/l/c')

    while response != 'c':

        if response == 'h':

            finalRange = computerTry
            computerTry = random.randint(initialRange,finalRange)
            response = input('is' + str(computerTry) + 'too high(h). too low(l) or correct(c)?  h/l/c')

        elif response == 'l':

            initialRange = computerTry
            computerTry = random.randint(initialRange,finalRange)
            response = input('is' + str(computerTry) + 'too high(h). too low(l) or correct(c)?  h/l/c')

        else:
            print('invalid response')
            response = input('is' + str(computerTry) + 'too high(h). too low(l) or correct(c)?  h/l/c')

choice = input('do you want to guess (1), or shall the computer guess(2)? (1),(2)')

if choice == '1':
    userGuess()

elif choice == '2':

    ComputerGuess()