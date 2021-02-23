import random

RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
SUITS = ['♠️', '♣️', '♥️', '♦️']


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self, ranks, suits):
        ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        suits = ['♠️', '♣️', '♥️', '♦️']
        self.cards = []
        for rank in ranks:
            for suit in suits:
                card = Card(rank, suit)
                self.cards.append(card) 

    #TODO method to shuffle the deck
    # takes self and returns self with self.cards rearranged randomly
    def shuffle_deck(self):
        random.shuffle(self.cards)
        # return self.cards

    # TODO method to deal the top card of the deck to a player
    # takes a player and a deck and adds the top card from the deck to a player's hand
    def deal_card(self):
        card_draw = self.cards.pop()
        return card_draw

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f'{self.name} has a hand of {[str(card) for card in self.hand]}'

    def select_card(self):
        ranks_in_hand = self.get_ranks_in_hand()
        selected_card = random.choice(ranks_in_hand)
        print(f'{self.name} requests {selected_card}')
        return selected_card
        
    def get_ranks_in_hand(self):
        return [card.rank for card in self.hand]

class Game:
    def __init__(self, ranks, suits, name1, name2):
        self.deck = Deck(ranks, suits)
        self.deck.shuffle_deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.winner = False
        self.deal_hands()
        self.player1_books = []
        self.player2_books = []

    # TODO use deal_card() method from Deck class to deal 7 cards to each player
    def deal_hands(self):
        players = [self.player1, self.player2]
        for i in range(7):
            for player in players:
                player.hand.append(self.deck.deal_card())
        print(len(self.deck.cards))

    # TODO create turn action in which player asks for a card and goes fish according to the rules
    # Determine if the turn was a winning/losing turn
    def turn(self, requester, receiver):
        # player checks their hand of cards
        # player asks other player about 1 card
        # player 2 either loses cards or keeps cards
        # if 'Go Fish' player1 draws a card
        # TODO if player has no cards in hand, player draws one from deck.
        selected_card_rank = requester.select_card()
        print(f'{requester.name} says, "Got any {selected_card_rank}s? ')
        if selected_card_rank in receiver.get_ranks_in_hand():
            print(f'{receiver.name} says, "Here you go."')
            for index, card in enumerate(receiver.get_ranks_in_hand()):
                if selected_card_rank == card:
                    requester.hand.append(receiver.hand[index])
            receiver.hand = [card for card in receiver.hand if card.rank != selected_card_rank]
            # book_counting()
            # TODO have player put down "books" of 4 cards
            print(f'{requester} | {receiver}')
            self.turn(requester, receiver)
    
        elif selected_card_rank not in receiver.get_ranks_in_hand():
            print(f'{receiver.name} says, "Go fish!"')
            drawn_card = self.deck.deal_card()
            print(f'{requester.name} drew a {drawn_card}')
            requester.hand.append(drawn_card)
            if drawn_card.rank == selected_card_rank:
                # TODO have player put down "books" of 4 cards
                self.turn(requester, receiver)
            else: 
                print(f'{requester} | {receiver}')
                print("Your turn is over")
                return
        
        else:
            if (len(self.deck) == 0) and (len(self.player1.hand) == 0) and (len(self.player2.hand) == 0):
                
                print('Game is over!')

    def turn_taking(self):
        while (len(self.deck.cards) > 0): 
            game.turn(game.player1, game.player2)
            game.turn(game.player2, game.player1)
            
    # def book_counting(self):
    #     self.requester.hand
        # selecting players hands
        # checking if 4 of a kind
        # if 4 of a kind place in new list

                
# TODO allow user to input player names                               
game = Game(RANKS, SUITS, 'Rebecca', 'Grant')
# This depicts one turn. 
# TODO create a loop where players take turns until the game is over
# game ends when all books have been put down(13), so no cards in the deck or the hands
# winner of the game is person with the most books.
# game.turn(game.player1, game.player2)
# game.turn(game.player2, game.player1)
game.turn_taking()
# print('game over')

    # def turn(self):
    #     # player checks their hand of cards
    #     print(self.player1, self.player2)
    #     selected_card_rank = self.player1.select_card()
    #     for index, card in enumerate(self.player2.get_ranks_in_hand()):
    #         print(index, card)
    #         # if selected_card_rank == card:
    #         #     self.player1.hand.append(self.player2.hand[index])
    #         #     self.player2.hand = [card for card in self.player2.hand if card.rank != selected_card_rank]
    #         #     print(f'{self.player1} | {self.player2}')
            
    #         # else:
    #         #     print(f'Go fish!')


        # player asks other player about 1 card
        
        # player 2 either loses cards or keeps cards
        # if 'Go Fish' player1 draws a card
        # if drawn card is a match repeat from start ^

    
        
# new_game = Game(RANKS, SUITS, 'Rebecca', 'Grant')
# new_game.turn()
