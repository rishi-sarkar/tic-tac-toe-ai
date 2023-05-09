# Tic Tac Toe

board = [' ' for x in range(9)]


def clear():
    print('\n' * 50)


def printBoard():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')
    print('\n')


def playerMove():
    while True:
        move = input("Select a position to place an 'x' from 1 - 9: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if board[move - 1] == ' ':
                    board[move - 1] = 'x'
                    break
        except TypeError:
            pass


def compMove():
    bestMove = - 1  # just changed this, might mess game up
    bestScore = -100
    for x in range(9):
        if board[x] == ' ':
            board[x] = 'o'
            score = minimax(False)
            board[x] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = x
    return bestMove


def minimax(isMaximizing):
    if isWinner('o') and not isMaximizing:
        return 1
    elif isWinner('x') and isMaximizing:
        return -1
    elif isBoardFull():
        return 0
    else:
        if (isMaximizing):  # Computer's Move
            bestScore = -100
            for x in range(9):
                if board[x] == ' ':
                    board[x] = 'o'
                    score = minimax(False)
                    board[x] = ' '
                    bestScore = max(bestScore, score)
            return bestScore
        else:  # Player's Move
            bestScore = 100
            for x in range(9):
                if board[x] == ' ':
                    board[x] = 'x'
                    score = minimax(True)
                    board[x] = ' '
                    bestScore = min(bestScore, score)
            return bestScore


def isWinner(piece):
    for x in range(0, 9, 3):
        if (board[x] == board[x + 1] and board[x] == board[x + 2] and board[x] == piece):
            return True
    for x in range(0, 3):
        if (board[x] == board[x + 3] and board[x] == board[x + 6] and board[x] == piece):
            return True
    if (board[0] == board[4] and board[0] == board[8] and board[0] == piece):
        return True
    elif (board[2] == board[4] and board[2] == board[6] and board[2] == piece):
        return True
    return False


def isBoardFull():
    if board.count(' ') == 0:
        return True
    return False


def scoreBoard(score):
    print('\n\n---------------')
    print('Player      |{}|'.format(score[0]))
    print('Computer    |{}|'.format(score[1]))
    print('---------------')


def main():
    score = [0, 0]
    clear()
    print('Welcome to Tic Tac Toe')
    printBoard()

    while not (isBoardFull()):
        hasWon = 0
        if not (isWinner('o')):  # computer did not win
            playerMove()
        else:
            print("Sorry, the computer won this game.")
            hasWon = 1
            score[1] += 1
            break
        if not (isWinner('x')):  # player did not win
            move = compMove()
            clear()
            print("Player Move:")
            printBoard()
            if move != -1:
                board[move] = 'o'
                print('Computer Move:')
                printBoard()
        else:
            print("Congrats! you won this game")
            hasWon = 1
            score[0] += 1
            break

    if isBoardFull() and hasWon == 0:
        print('Tie Game')

    scoreBoard(score)


main()
