import random

def rand():
    random_num = random.randint(1,3)
    return  random_num

computer = rand()
# Assumptions
# 1 = rock
# 2 = paper
# 3 = scissors

assume = { 1 : 'rock', 2 : 'paper', 3 : 'scissors'}

user_choice = int(input('1 for rock, 2 for paper, 3 for scissor: '))

if computer == user_choice:
    print(f'{assume[computer]} vs {assume[user_choice]}')
    print("It's a tie")
elif computer == 1 and user_choice == 2:
    print(f'{assume[computer]} vs {assume[user_choice]}')
    print("you win")
elif computer == 1 and user_choice == 3:
    print(f'{assume[computer]} vs {assume[user_choice]}')
    print("you loose")
elif computer == 2 and user_choice == 1:
    print(f'{assume[computer]} vs {assume[user_choice]}')
    print("you loose")
elif computer == 2 and user_choice == 3:
    print(f'{assume[computer]} vs {assume[user_choice]}')
    print("you win")
elif computer == 3 and user_choice == 1:
    print(f'{assume[computer]} vs {assume[user_choice]}')
    print("you win")
elif computer == 3 and user_choice == 2:
    print(f'{assume[computer]} vs {assume[user_choice]}')
    print("you loose")



