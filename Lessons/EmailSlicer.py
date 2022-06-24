#email slicer

# you enter an email for example

# email = samuelarefeaynie2@gmail.com
# sliced = userName = samuelarefeaynie2 domain = gmail.com 



email = input('Enter your Email: ')

holder = email.split('@')

print('Username = ', holder[0])
print('Domain ', holder[1])


