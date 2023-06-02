import random

def printBoard(board):
    print('')
    print('|', board['1'], '|', board['2'], '|', board['3'], '|')
    print('|', board['4'], '|', board['5'], '|', board['6'], '|')
    print('|', board['7'], '|', board['8'], '|', board['9'], '|')
    print('')

def firstPlayer():
    number = random.randint(1, 2)
    if number == 1:
        player1Turn = True
    else: 
        player1Turn = False
    return player1Turn

def assignP1Symbol(player1Name, player2Name, player1Turn):
    while True:
        if player1Turn:
            player1Symbol = input(f'{player1Name}, would you like to use X or O? ')
            if player1Symbol == 'X':
                print(f'Ok! {player1Name} will use X, which means {player2Name} will use O.')
            elif player1Symbol == 'O':
                print(f'Ok! {player1Name} will use O, which means {player2Name} will use X.')
            else:
                print('Not a valid marker. Try again.')
                continue
        else:
            player2Symbol = input(f'{player2Name}, would you like to use X or O? ')
            if player2Symbol == 'X':
                player1Symbol = 'O'
                print(f'Ok! {player2Name} will use X, which means {player1Name} will use O.')
            elif player2Symbol == 'O':
                player1Symbol = 'X'
                print(f'Ok! {player2Name} will use O, which means {player1Name} will use X.')
            else:
                print('Not a valid marker. Try again.')
                continue
        break
    return player1Symbol
    

def yourTurn(player1Turn, player1Name, player2Name):
    if player1Turn:
        print(f'It\'s {player1Name}\'s turn.')
    else:
        print(f'It\'s {player2Name}\'s turn.')


def movePosition():
    print('')
    return input('Where would you like to play? ')


def validMove(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def updateBoard(position, symbol, board):
   board[position] = symbol

# returns the symbol of the winner, 'tie', or returns 'keep playing'
def getCurrentState(board):
    if board['1'] == board['2'] == board['3'] == board['4'] == board['5'] == board['6'] == board['7'] == board['8'] == board['9']:
        return 'keep playing'
    elif board['1'] == board['2'] == board['3'] != ' ':
        return board['1']
    elif board['4'] == board['5'] == board['6'] != ' ':
        return board['4']
    elif board['7'] == board['8'] == board['9'] != ' ':
        return board['7']
    elif board['1'] == board['4'] == board['7'] != ' ':
        return board['1']
    elif board['2'] == board['5'] == board['8'] != ' ':
        return board['2']
    elif board['3'] == board['6'] == board['6'] != ' ':
        return board['3']
    elif board['1'] == board['5'] == board['9'] != ' ':
        return board['1']
    elif board['3'] == board['5'] == board['7'] != ' ':
        return board['3']
    elif board['1'] != ' ' and board['2'] != ' '  and board['3'] != ' '  and board['4'] != ' '  and board['5'] != ' '  and board['6'] != ' ' and board['7'] != ' ' and board['8'] != ' ' and board['9'] != ' ':
        return 'tie'
    else:
        return 'keep playing'



def switchTurn(playerTurn):
    if playerTurn == True:
        return False
    else:
        return True