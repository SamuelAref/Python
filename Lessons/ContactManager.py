#Contact Book


#   - View List of Contacts
#   - Add Contact
#   - Delete Contact

class Contact(object):

    def __init__(self):
        pass


    def add(self, firstName, lastName, phoneNumber):

        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber

        return  [self.firstName, self.lastName, self.phoneNumber]

Contacts = []
Create = Contact()
Contacts.append(Create.add('Samuel', 'Arefeaynie', '+251938341891'))

print('Hi, Welcome to the Contact Manager')

userChoice = 0
firstName = ''
lastName = ''
phoneNumber = ''

while userChoice != '4':

    print('1 to view all contacts')
    print('2 for adding contact')
    print('3 for deleting contact')
    print('4 to quit')

    userChoice = input('Enter your Choice: ')

    if userChoice == '1':

        print('-------------')
        
        for i in Contacts:

            print(i)

        print('-------------')
        
    elif userChoice == '2':

        print('-------------')

        firstName = input('Enter First Name: ')
        lastName = input('Enter Last Name: ')
        phoneNumber = input('Enter phone Number: ')

        Contacts.append(Create.add(firstName, lastName,phoneNumber))

        print('Contact Added')

        print('-------------')

    elif userChoice == '3':

        
        print('-------------')
        
        for i in Contacts:

            print(i)

        print('-------------')
        
        firstName = input('Enter First Name you want to delete: ')
        contactCounter = 0

        for i in Contacts:

            if i[0] == firstName:
                Contacts.remove(i)
                contactCounter = 1

            else: 
                continue

        if contactCounter == 1:
            
            print('Contact Deleted')

        elif contactCounter == 0:

            print('No contact found by that name')

    elif userChoice != '1' and userChoice != '2' and userChoice != '3' and userChoice != '4' :
        print('please Enter a valid input ')








    








