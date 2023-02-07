from IPython.display import clear_output


board = [' ']*10


def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


# display_board(board)


# print('_____________________________________________________________________________________________________')


def player_input():
    pInput = ''
    marker1 = 'x'
    marker2 = 'o'
    player1_marker = 'None'
    player2_marker = 'None'

    while pInput != marker1 or pInput != marker2:
        pInput = input(' Choose your marker Player 1: "X" or "O"')

        if pInput == marker1 or pInput == marker2:
            player1_marker = pInput

            if player1_marker == marker1:
                # player2_marker = marker2
                return ('x', 'o')
            else:
                # player2_marker = marker1
                return ('o', 'x')
            # break

        else:
            continue

    # return (player1_marker, player2_marker)


# player1_marker, player2_marker = player_input()        #this executes my function in terminal somehow, overwriting
                                                       #my variables with the function output

# print(' Player1\'s marker is ', player1_marker, '\n', 'Player2\'s marker is ', player2_marker)


# print('_____________________________________________________________________________________________________')


test_board = ['#', 'x', 'x', 'o', 'o', 'x', 'o', 'x', 'o', 'o']

def place_marker(board, marker, position):

    board[position] = marker


# place_marker(test_board, '$', 8)
# display_board(test_board)


# print('_____________________________________________________________________________________________________')



def win_check(board, mark):

    ''' we need to check if the same mark is in all 3 dimensions:'''
    return ((board[7] == board[8] == board[9]) == mark or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))


# print('_____________________________________________________________________________________________________')


import random

def choose_first():
#this flips a 'coin' to determine which player starts first
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# print('_____________________________________________________________________________________________________')


def space_check(board, position):
# checks if the position you wanna put your marker is empty.
    return board[position] == ' '


# print('_____________________________________________________________________________________________________')


def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    """ if the board is full it will return TRUE. If not i will check and return False"""
    return True


# print('_____________________________________________________________________________________________________')


def player_choice(board):

    position = 0

    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose an empty space to put your marker (1-9):'))

    return position


# print('_____________________________________________________________________________________________________')


def replay():

    choice = ''

    while choice not in ['Y', 'N', 'y', 'n']:
        choice = input('Do You want to keep playing? (Y or N)')

        if choice not in ['Y', 'N', 'y', 'n']:
            print('Invalid typo. Type Y or N')

    if choice in ['Y', 'y']:
        return True
    else:
        return False


# def replay():
#     choice = input('Play again? Enter Y or N')
#     return choice == 'Y'

# print('_____________________________________________________________________________________________________')


# COMBINE ALL OF THE ABOVE TO RUN THE GAME


print('TIC TAC TOE')

while True:

    # Prepare the game:
    '''set up: board -> choose markers -> who's first'''

    the_board = board                                   #board
    player1_marker, player2_marker = player_input()     #markers. it shows the question from the function in console
    turn = choose_first()                               #who's turn is now
    print(turn + ' goes first')

    play_game = input('Are you ready? y or n ')         #START

    if play_game == 'y':
        game_on = True
    else:
        game_on = False


    ## Gameplay:
    '''player 1 turn -> player 2 turn'''

    while game_on:

        if turn == 'Player 1':
            #SHOW THE BOARD
            display_board(the_board)
            #CHOOSE A POSITION FOR THE PLAYERS' MARK ON THE BOARD
            position = player_choice(the_board)
            #PLACE THE MARKER ON THE SELECTED POSITION
            place_marker(the_board, player1_marker, position)
            #CHECK IF THE PLAYER WON WITH HIS RECENT MOVE
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON')
                game_on = False                 # THIS BREAK THE ENTIRE WHILE LOOP AND THE GAME IS OVER
            #CHECK IF THERE IS A TIE RESULTED BY THE RECENT MOVE
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE')
                    game_on = False  # we can use break here also interchangeably
                else:
            # NO TIE OR WIN? GAME_ON -> PLAYERS 2 TURN
                    turn = 'Player 2'

        else:
            # SHOW THE BOARD
            display_board(the_board)
            # CHOOSE A POSITION FOR THE PLAYERS' MARK ON THE BOARD
            position = player_choice(the_board)
            # PLACE THE MARKER ON THE SELECTED POSITION
            place_marker(the_board, player2_marker, position)
            # CHECK IF THE PLAYER WON WITH HIS RECENT MOVE
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON')
                game_on = False  # THIS BREAK THE ENTIRE WHILE LOOP AND THE GAME IS OVER
            # CHECK IF THERE IS A TIE RESULTED BY THE RECENT MOVE
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE')
                    game_on = False  # we can use break also here
                else:
                    # NO TIE OR WIN? GAME_ON -> PLAYERS 2 TURN
                    turn = 'Player 1'


    if not replay():
        print('Thanks for the game')
        break