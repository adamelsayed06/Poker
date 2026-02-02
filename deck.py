import random
from card import Card
from typing import List

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))

    def pick_card(self) -> Card:
        idx = random.randint(0, len(self.cards))
        returned_card = self.cards[idx]
        self.cards.pop(idx)

        return returned_card
# we pick from the deck, return the card and remove it from the deck, we can use this for the turn cards and the player cards
