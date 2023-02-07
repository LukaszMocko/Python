import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# two_hearts = Card('Hearts', 'Two')


class Deck:

    def __init__(self):

        self.all_cards = []

        '''I create 52 cards, every variation available'''
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    '''The deck created was created in order. Now I shuffle the deck'''
    def shuffle(self):
        random.shuffle(self.all_cards)

    '''we take one card '''
    def deal_one(self):
        return self.all_cards.pop()


'''I create an instance for class Deck'''
deck = Deck()
# deck.shuffle()

'''I can pop/take one random card the shuffled (in 45.line) deck, but the len of all.cards reduces! '''
# my_card = deck.deal_one()

# first_card = deck.all_cards[0]

# for c in deck.all_cards:
#     print(c)


class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            '''Adds multiple cards'''
            self.all_cards.extend(new_cards)
        else:
            '''Adds one card to the list'''
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

#
# new_player = Player('Andrzej')
# print(new_player)
#
# new_player.add_cards(my_card)
# print(new_player)
# print(new_player.all_cards[0])
#
# new_player.add_cards([my_card, my_card, my_card, my_card])
# print(new_player)
# print(new_player.all_cards[0])
#
# new_player.remove_one()
# print(new_player, '\n -----------------------------------------------------------------')


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


# def game_on():
#     if len(deck.all_cards) > 0:
#         return True
#     else:
#         return False




    # play_game = input('Are you ready? y or n ')         #START
    #
    # if play_game == 'y':
    #     game_on = True
    # else:
    #     game_on = False
    #
    # while game_on:

deck.shuffle()
player_one = Player('Andrzej')
player_two = Player('Bartolomiusz')

for x in range(26):

    player_one.add_cards(deck.deal_one())
    player_two.add_cards(deck.deal_one())


round = 0
game_on = True
print('The War game begins now')

while game_on:

    round += 1
    print(f'Round {round}')

    if len(player_one.all_cards) == 0:
        print('Player 1 is out of cards. Player 2 wins')
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print('Player 2 is out of cards. Player 1 wins')
        game_on = False
        break

    #NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    #WAR
    at_war = True

    while at_war:
        # [-1] because we have to draw the card from the end of the list.
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            #cards are equal, so it is war.
            print('WAR')

            if len(player_one.all_cards) < 5:
                print('PLayer 1 is unable to fight the war')
                print('Player 2 wins')
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print('PLayer 2 is unable to fight the war')
                print('Player 1 wins')
                game_on = False
                break
            else:
                for x in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


