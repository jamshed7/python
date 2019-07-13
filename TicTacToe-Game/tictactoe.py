from IPython.display import clear_output
import random


def display_board(board):
    print('\n')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('\n')


def player_input():
    player1 = ''

    while player1!='X' and player1!='O':
        player1 = input("Player 1, please pick a marker 'X' or 'O'\n")

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print(f'Player 1 has picked {player1}.')
    print(f'Player 2 has been assigned {player2}.')

    return (player1, player2)


def place_marker(board, marker, position):
    board[int(position)] = marker


def win_check(board, mark):

    if board[1]==board[2]==board[3] == mark:
        return True
    elif board[4]==board[5]==board[6] == mark:
        return True
    elif board[7]==board[8]==board[9] == mark:
        return True
    elif board[1]==board[4]==board[7] == mark:
        return True
    elif board[2]==board[5]==board[8] == mark:
        return True
    elif board[3]==board[6]==board[9] == mark:
        return True
    elif board[1]==board[5]==board[9] == mark:
        return True
    elif board[3]==board[5]==board[7] == mark:
        return True
    else:
        return False


def choose_first():
    return random.randint(1,2)


def space_check(board, position):
    if board[int(position)] == ' ':
        return True
    else:
        return False


def full_board_check(board):
    if ' ' not in board:
        return True
    else:
        return False


def player_choice(board):
    position = ''

    while True:
        position = input('Choose a position you would like to play next? ')

        if space_check(board, position):
            break

    return position


def replay():

    play_again = input('Would you like to play again? (Yes/No)')

    if play_again == 'Yes':
        return True
    else:
        return False


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    print('\nThe game has started!\n')
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_marker , player2_marker = player_input()
    display_board(board)
    #pass

    while not full_board_check(board):
        #Player 1 Turn
        print("Player 1's turn:\n")
        position = player_choice(board)
        place_marker(board, player1_marker, position)
        display_board(board)
        if win_check(board, player1_marker):
            print('Player 1 has won the game!\n')
            break
        # Player2's turn.
        print("Player 2's turn:\n")
        position = player_choice(board)
        place_marker(board, player2_marker, position)
        display_board(board)
        if win_check(board, player2_marker):
            print('Player 2 has won the game!\n')
            break

    else:
        print('The game has tied!\n')


    if not replay():
        break
    else:
        continue
