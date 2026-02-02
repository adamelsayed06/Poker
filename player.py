from hand import Hand
class Player:
    def __init__(self, hand : Hand, chips : int):
        if chips < 0:
            raise ValueError("Player cannot have negative money")
        self.hand = hand
        self.chips = chips

    def make_bet(self, bet_size : int):
        chips -= bet_size

    def fold(self):
        hand = None
    
    # what are the responsibilities of this class?
    # i think it makes sense to have it
    # we can have a game class, goes around checks is the player in the game? 
    # 