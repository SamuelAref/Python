import random

errorChecker = 0

while errorChecker == 0:

    computerRandom = random.randint(0,2)
    computerOptions = [ 'r', 'p', 's']
    userChoice = input('rock(r), paper(p) or scissors(s)? q to quit:  ')

    if userChoice == computerOptions[computerRandom]:
        print('tie: ' + userChoice +' Vs ' + computerOptions[computerRandom])

    elif userChoice == 'r' and computerOptions[computerRandom] == 'p':
        print('Computer wins ' + userChoice +' Vs ' + computerOptions[computerRandom])

    elif userChoice == 'r' and computerOptions[computerRandom] == 's':
        print('You win: ' + userChoice +' Vs ' + computerOptions[computerRandom])

    elif userChoice == 'p' and computerOptions[computerRandom] == 's':
        print('Computer wins: ' + userChoice +' Vs ' + computerOptions[computerRandom])

    elif userChoice == 'p' and computerOptions[computerRandom] == 'r':
        print('You win: ' + userChoice +' Vs ' + computerOptions[computerRandom])

    elif userChoice == 's' and computerOptions[computerRandom] == 'r':
        print('Computer wins: ' + userChoice +' Vs ' + computerOptions[computerRandom])

    elif userChoice == 's' and computerOptions[computerRandom] == 'p':
        print('You win: ' + userChoice +' Vs ' + computerOptions[computerRandom])

    elif userChoice == 'q':
        errorChecker+=1
    
    else:
        print('enter a valid response')