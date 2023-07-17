import sys

board = [' ' for _ in range(9)]  # create the board


def print_board():
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def check_win():
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True

    # check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True

    # check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True

    return False


try:
    print('\nWelcome to Tic Tac Toe!')
    print_board()

    player = 'X'
    while True:
        print(f"\nPlayer {player}'s turn")
        position = int(input('Enter a position (1-9): ')) - 1

        if board[position] == ' ':
            board[position] = player
            print_board()

            if check_win():
                print(f'Player {player} wins!')
                break
            elif ' ' not in board:
                print("It's a tie!")
                break

            # Switch players
            player = 'O' if player == 'X' else 'X'
        else:
            print('Invalid move. Try again.')
except KeyboardInterrupt:
    print("\n[-] ctrl + c detected, the game has been terminated")
    sys.exit(0)
