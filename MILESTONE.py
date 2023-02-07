# TIC TAC TOE

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

display(row1, row2, row3)

#User input

# position_index = int(input('Choose an index position: '))
# row1[position_index]
#
# def user_choice():
#
#     choice = input('Enter a number (0-10): ')
#
#     if choice.isdigit():
#         choice = int(choice)
#         print(choice, 'is digit')
#
#         # if 0 <= choice <= 10:
#         acceptableRange = range(0,10)
#         if choice in acceptableRange:
#             print('digit in range')
#             return choice
#         else:
#             print(choice, 'is not in specified range. Type again...')
#             return user_choice()
#
#     else:
#         print(choice, 'is not a digit. Type again...')
#         return user_choice()
#
# user_choice()


# GRA

game_list = [0,1,2]

def display_game():
    print(game_list)


def position_choice():

    choice = 'string'

    while choice not in ['0', '1', '2']:
        choice = input('Pick a position from range: 0 1 2 ___')

        if choice not in ['0', '1', '2']:
            print('Invalid choice')
    return int(choice)


def replacement_choice(game_list, position):

    user_placement = input('Type a string to place at just selected position: ')
    game_list[position] = user_placement
    return game_list


# replacement_choice(game_list, position_choice())
# print(game_list)

def gameon_choice():

    choice = 'string'

    while choice not in ['Y', 'N', 'y', 'n']:
        choice = input('Do You want to keep playing? (Y or N)')

        if choice not in ['Y', 'N', 'y', 'n']:
            print('Invalid typo. Type Y or N')

    if choice in ['Y', 'y']:
        return True
    else:
        return False

# GRA

game_on = True
# game_list = [0,1,2]

while game_on:

    display_game()
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    display_game()
    game_on = gameon_choice()