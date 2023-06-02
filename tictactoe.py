import tttlogic


print('Welcome to Tic Tac Toe!')
player1 = input('What is player 1\'s name? ')
player2 = input('What is player 2\'s name? ')

player1Turn = tttlogic.firstPlayer()


print('This is a board with all of the locations for reference:')
instructionBoard = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
tttlogic.printBoard(instructionBoard)


theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
player1Symbol = tttlogic.assignP1Symbol(player1, player2, player1Turn)
if player1Symbol == 'X':
    player2Symbol = 'O'
else:
    player2Symbol = 'X'
    
while True:
    tttlogic.printBoard(theBoard)
    
    tttlogic.yourTurn(player1Turn, player1, player2)
    position = tttlogic.movePosition()  
    try: 
        position = int(position)
        if position not in range(1, 10):
            print('Number does not match a position. Try again.')
            continue
        position = str(position)
    except:
        print('Input is not a valid number. Try again.')
        continue
    goodMove = tttlogic.validMove(theBoard, position)
    if goodMove == False:
        print('Space is occupied. Try Again.')
        continue 
    if player1Turn:
        tttlogic.updateBoard(position, player1Symbol, theBoard)
    else:
        tttlogic.updateBoard(position, player2Symbol, theBoard)
    state = tttlogic.getCurrentState(theBoard)
    if state == 'keep playing':
        player1Turn = tttlogic.switchTurn(player1Turn)
        continue
    elif state == 'tie':
        print('Game Over. It\'s a Cat\'s Game!')
        break
    elif player1Turn:
        tttlogic.printBoard(theBoard)
        print(f'Game Over. {player1} won the game!')
        break
    else:
        tttlogic.printBoard(theBoard)
        print(f'Game Over. {player2} won the game!')
        break
        
