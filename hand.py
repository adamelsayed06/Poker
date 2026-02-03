from card import Card

class Hand:
    def __init__(self, first_card : Card, second_card : Card):
       # if first_card == second_card:
            #raise ValueError("Cannot have two of the same cards")
        
        self.first_card = first_card
        self.second_card = second_card

