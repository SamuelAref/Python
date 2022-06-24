import computer_guess, guess


print("Hello, do you want to guess the computer's number (1) or should the computer guess your number (2) or q to quit? ")
type_of_game = input("Answer: ")
input_error = 0

while type_of_game.upper() != 'Q':


    if type_of_game == '1':
        guess.user_guess()
        break




    elif type_of_game == '2':
        computer_guess.compter_guess()
        break

    else:
        print('please input the given commands correctly')
        print(" do you want to guess the computer's number (1) or should the computer guess your number (2) or q to quit? ")
        type_of_game = input("Answer: ")
print('Thanks for playing, goodbye')