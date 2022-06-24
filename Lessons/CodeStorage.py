# #tic tac toe

# # A  | B  |  C
# #____|____|_____
# # D  | E  |  F
# #____|____|_____
# # G  | H  |  I


# gridContent = [ ['A','B','C'],['D','E','F'],['G','H','I']]
#         choiceChecker = 1
#         player1Choice = ''

#         def grid(content):

#             for i in content:

#                 for j in i:

#                     if i.index(j) == 2:

#                         print(j)
#                         print('----------')

#                     else:

#                         print(j, end=' | ')

#         def char(playerOne):

#             if playerOne == 'x':
#                 player2Choice = 'o'
#                 return player2Choice

#             elif playerOne == 'o':
#                 player2Choice = 'x'
#                 return player2Choice

#             else:
#                 return False


#         while choiceChecker == 1:

#             player1Choice = input('Player 1, Choose your character? x or o: ')

#             if char(player1Choice) == 'x' or char(player1Choice) == 'o':
#                 player2Choice = char(player1Choice)
#                 choiceChecker+=1

#             else:
#                 print('please enter a valid character')


#         grid(gridContent)

#         def changeChar(playerCharacter, gridPosition, grid):

#             for i in grid:

#                 for j in i:

#                     if j == gridPosition:
#                         grid[grid.index(i)][i.index(j)] = playerCharacter

            
#             return grid

#         grid(changeChar('x','A', gridContent))

            


#         print('player 1 is ' + player1Choice)
#         print('player 2 is ' + player2Choice)

