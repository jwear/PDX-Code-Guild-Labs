from card import Card, Deck
from hand import Hand

class Player:
    def __init__(self, name="Player"):
        self.hands = list()
        self.hands.append(Hand())
        self.name = name

class Dealer(Player):
    def __init__(self, *args)
        super().__init__(*args)

class TooManyPlayers(BaseException):
    pass

class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.players = [Dealer(), Player()]
        self.max_players = max_players

    def add_player(self, player):
        if len(self.players) <= 8:
            raise TooManyPlayers

        self.players.append(player)

    def initial_deal(self):
        self.deck.shuffle()
        self.deck.cut()

    def deal(self):
        for player in players:
            player.hand.add_card(self.deck.draw())

class BlackJackTable(Table)
    def initial_deal(self):
        super().initial_deal()
        for player in players:
            player.hand.add_card(self.deck.draw(card=2))

class Game:
    def __init__(self):
        self.table = BlackJackTable()

    def start(self):
        self.table.initial_deal()
