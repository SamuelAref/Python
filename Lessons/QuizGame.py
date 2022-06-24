#Quiz game 
start = input('Start the quiz? y/n : ')

while start != 'y' and start != 'n':

    print('invalid input try again')
    start = input('Start the quiz? y/n : ')

if start == 'y':
        questions = [ 'How many days do we have in a week?', 'How many days are there in a year?', 'How many colors are there in a rainbow?', "Which animal is known as the 'Ship of the Desert'"]
        answers = ['7', '365', '7','camel']
        correctCounter = 0

        def answerChecker(answer, question):

            if answers[question] == answer.lower():
                return True

            else:
                return False

        for q in questions:

            print(q)
            answer = input('answer : ')
            if answerChecker(answer, questions.index(q)):
                correctCounter +=1
                
        print('you answered', correctCounter, '/4')

else:
    print('bye')

     

        
