import random

def rand():
    random_num = random.randint(1,3)
    return  random_num

values = {
    1 : 'rock',
    2 : 'paper',
    3 : 'scissors'
}
# print(values[rand()])
print('1 for rock, 2 for paper and 3 for scissors')
choice = int(input('your choice: '))



if choice == 1 and values[rand()] == 'paper':
    print(f'{values[1]} vs {values[rand()]}')
    print("you lose")
elif choice == 2 and values[rand()] == 'scissors':
    print(f'{values[2]} vs {values[rand()]}')
    print("you lose")
elif choice == 3 and values[rand()] == 'paper':
    print(f'{values[3]} vs {values[rand()]}')
    # print("you win")
elif choice == 1 and values[rand()] == 'scissors':
    print(f'{values[1]} vs {values[rand()]}')
    # print("you win")
elif choice == 2 and values[rand()] == 'rock':
    print(f'{values[2]} vs {values[rand()]}')
    # print("you win")
elif choice == 3 and values[rand()] == 'rock':
    print(f'{values[3]} vs {values[rand()]}')
    print("you lose")