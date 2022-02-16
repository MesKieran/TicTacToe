gameboard = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print("- - -")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("- - -")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game(board):
    game_over = False
    while not game_over:
        player1move = input("which move u want to make player1?")
        if board[player1move] == ' ':
            board[player1move] = 'x'
        printBoard(board)
        if isGameOver(board):
            break
        player2move = input("which move u want to make player2?")
        if board[player2move] == ' ':
            board[player2move] = 'o'
        printBoard(board)
        if isGameOver(board):
            game_over = True
    print("game over!")

def isGameOver(board):
    if board['1'] == board['2'] == board['3'] == 'x' or board['1'] == board['2'] == board['3'] == 'o':
        return True
    elif board['4'] == board['5'] == board['6'] == 'x' or board['4'] == board['5'] == board['6'] == 'o':
        return True
    elif board['7'] == board['8'] == board['9'] == 'x' or board['7'] == board['8'] == board['9'] == 'o':
        return True
    elif board['1'] == board['5'] == board['9'] == 'x' or board['1'] == board['5'] == board['9'] == 'o':
        return True
    elif board['3'] == board['5'] == board['7'] == 'x' or board['3'] == board['5'] == board['7'] == 'o':
        return True
    elif board['1'] == board['4'] == board['7'] == 'x' or board['1'] == board['4'] == board['7'] == 'o':
        return True
    elif board['2'] == board['5'] == board['8'] == 'x' or board['2'] == board['5'] == board['8'] == 'o':
        return True
    elif board['3'] == board['6'] == board['9'] == 'x' or board['3'] == board['6'] == board['9'] == 'o':
        return True
    else:
        return False

printBoard(gameboard)
game(gameboard)

