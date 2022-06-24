
def user_guess():

    import random


    def rand(x, y):
        random_number = random.randint(x, y)
        return random_number


    guess = rand(1, 1000)
    low = 1
    high = 1000

    answer = int(input('guess: '))

    while answer != guess:
        soln = answer
        if soln < guess:
            print('too low(l), guess again: ')
            answer = int(input('guess: '))

        elif soln > guess:
            print('too high(h), guess again: ')
            answer = int(input('guess: '))

    print('correct')