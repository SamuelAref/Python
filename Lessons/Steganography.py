#steganography

# how to encrypt an input

# create a dictionary

# Encrypting 

import random


alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Encrypted = ''
EncryptingArray = []


unEncrypted = input('Input your string: ')

def encrypt(unencrypted):

    for i in unencrypted:

        rand = random.randint(0,25)
        EncryptingArray.append(rand)
        unencrypted =  unencrypted.replace(i,alphabet[rand])
    
    return unencrypted


# def decrypt(encrypted):

#     for i 

print(encrypt(unEncrypted))
print(EncryptingArray)
# print(Encrypted)