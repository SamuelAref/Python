#tic tac toe

gridContent = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
playerOne = ''
playerTwo = ''
playerCounter = 1 #checks player one or two

#Functions 

#output the grid
def gridOutput(grid):

    gridContentCounter = 0

    for i in grid:

        if grid.index(i) == 2  or grid.index(i) == 5  or  grid.index(i) == 8 or gridContentCounter == 2  or gridContentCounter == 5  or  gridContentCounter == 8:

            print(i)
            
        else:

            print(i, end='  ')

        gridContentCounter+=1

#checks wins    
def winChecker(grid):

    if grid.__getitem__(0) == grid.__getitem__(1) and grid.__getitem__(1) == grid.__getitem__(2):
        return True

    elif grid.__getitem__(3) == grid.__getitem__(4) and grid.__getitem__(4) == grid.__getitem__(5):
        return True
        
    elif grid.__getitem__(6) == grid.__getitem__(7) and grid.__getitem__(7) == grid.__getitem__(8):
        return True

    elif grid.__getitem__(0) == grid.__getitem__(3) and grid.__getitem__(3) == grid.__getitem__(6):
        return True
        
    elif grid.__getitem__(1) == grid.__getitem__(4) and grid.__getitem__(4) == grid.__getitem__(7):
        return True

    elif grid.__getitem__(2) == grid.__getitem__(5) and grid.__getitem__(5) == grid.__getitem__(8):
        return True
    
    elif grid.__getitem__(0) == grid.__getitem__(4) and grid.__getitem__(4) == grid.__getitem__(8):
        return True
        
    elif grid.__getitem__(2) == grid.__getitem__(4) and grid.__getitem__(4) == grid.__getitem__(6):
        return True

    else:
        return False

#grids char changing
def changeChar(playerChar, gridChoice, grid):

    for i in grid:

        if i == gridChoice:

            grid[grid.index(i)] = playerChar
            return grid      

#End of Functions

#Choosing x and o
while playerTwo != 'x' and playerTwo != 'o':

    playerOne = input('Choose x or o? ')

    if playerOne == 'x':

        playerTwo = 'o'

    elif playerOne == 'o':

        playerTwo = 'x'

    else : 

        print('pleas enter a valid response')

print('player one: ', playerOne)
print('player two: ', playerTwo)

#grid input and turns
while winChecker(gridContent) == False:

    gridOutput(gridContent)

    if playerCounter == 1:
        
        gridChoice = input('Player one, Enter a character: ')
        gridContent = changeChar(playerOne, gridChoice, gridContent)
        winChecker(gridContent)
        playerCounter +=1

    elif playerCounter == 2:

        gridChoice = input('Player two, Enter a character: ')
        gridContent = changeChar(playerTwo, gridChoice, gridContent)
        winChecker(gridContent)
        playerCounter -=1

#final Output
gridOutput(gridContent)

if playerCounter == 2:

    print('player one wins')

elif playerCounter == 1:

    print('player two wins')



    
