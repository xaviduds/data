# make a tictactoe game, now make it without so many conditionals
gameGrid = [['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]']]

playerTurn = 0

while playerTurn <= 9:
    for square in gameGrid:
        print(square)
    lineChoice = int(input('Which line? '))
    columnChoice = int(input('Which column? '))
    if gameGrid[lineChoice - 1][columnChoice - 1] == '[ ]':
        if playerTurn % 2 == 1:
            gameGrid[lineChoice - 1][columnChoice - 1] = '[O]'
            playerTurn += 1
        else:
            gameGrid[lineChoice - 1][columnChoice - 1] = '[X]'
            playerTurn += 1
    else:
        print('Already played.')

print('Game over, thanks for playing')