from hand import Hand
class Player:
    def __init__(self, hand : Hand, chips : int):
        if money < 0:
            raise ValueError("Player cannot have negative money")
        self.hand = hand
        self.chips = chips
    