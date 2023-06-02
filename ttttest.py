import tttlogic

board1 = {'1': '', '2': '', '3': '', '4': 'O', '5': 'O', '6': '', '7': 'X', '8': 'X', '9': 'X'}
assert tttlogic.getCurrentState(board1) == 'X' 

emptyBoard = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
assert tttlogic.getCurrentState(emptyBoard) == 'keep playing' 

player1Name = 'Jace'
player2Name = 'Lucas'
player1Turn = False

player1Symbol = tttlogic.assignSymbol(player1Name, player2Name, player1Turn)

print("New Statement")
