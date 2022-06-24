import random
from words import words

def rand():
    random_word = random.randint(0,9)
    return random_word

random_value = rand()
selected_word = words[random_value]
print(words[random_value])
print(selected_word)

def disp(x):
    for item in x:
        prin = print('_', end=' ')


block_letter = disp(range(0,len(words[random_value])))

def find(letter):
    print(selected_word.find(letter))


letter_guess = input("guess a letter: ")
found = find(letter_guess)

if find(letter_guess) != -1:
    # block_letter.replace(block_letter(find(letter_guess)),letter_guess)
    str(disp(range(0,len(words[random_value]))))[0]




