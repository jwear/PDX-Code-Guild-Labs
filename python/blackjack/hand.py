from card import Card
from card import Deck

class Hand:

    def __init__(self, hand):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)
        return self.hand

    def user_input(self, user_hand):
        user_hand = input('Please enter a hand: ').lower()
        return Hand(user_hand)
