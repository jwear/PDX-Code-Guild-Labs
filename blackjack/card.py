import random

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        if rank == 'A':
            self.rank_point = 11
        elif rank in ['K', 'Q', 'J']:
            self.rank_point = 10
        elif rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            self.rank_point = int(rank)

    def __str__(self):
        return 'Card: [%s%s]' % (self.suit, self.rank)

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_rank_point(self):
        return self.rank_point

    def set_rank_point(self, rank_point):
        self.rank_point = rank_point

class Deck:

    def __init__(self, cards_in_deck):
        cards_in_deck = []
        suits = ['S', 'H', 'D', 'C']
        ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        for suit in suits:
            for rank in ranks:
                cards_in_deck.append(Card(suit, rank))
                self.cards_in_deck = cards_in_deck[:]
        self.shuffle()

    def __str__(self):
        return 'Deck: %s' % str(len(self.cards_in_deck))

    def shuffle(self):
        random.shuffle(self.cards_in_deck)

    def cut_deck(self):
        half = len(self.cards_in_deck) / 2
        return self.cards_in_deck[half:] + self.cards_in_deck[:half]

    def draw_card(self):
        card = self.cards_in_deck.pop(0)
        return card
