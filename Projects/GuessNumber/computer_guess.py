
def compter_guess():

    import random
    def rand(x, y):
        random_number = random.randint(x, y)
        return random_number

    guess = rand(1, 1000)
    low = 1
    high = 1000
    answer = input(f' Is {guess} too low(l), too high(h), or correct(c): ')

    while answer.upper() != 'C':
        soln = answer
        if soln.upper() == 'L':
            low = guess
            guess = rand(low, high)
            rand(low, high)
            answer = input(f' Is {guess} too low(l), too high(h), or correct(c): ')

        elif soln.upper() == 'H':
            high = guess
            guess = rand(low,high)
            rand(low, high)
            answer = input(f' Is {guess} too low(l), too high(h), or correct(c): ')

    print('correct')

