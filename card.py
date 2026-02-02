class Card:
    # 
    def __init__(self, rank: int, suit: int):
        # Doesn't matter which suit corresponds to which number, since we only care when they're equal
        if not 0 <= suit <= 3:
            raise ValueError("Invalid Rank")
        
        # let ace = 14, k = 13, q = 12, j = 11
        if not 2 <= rank <= 14:
            raise ValueError("Invalid value")
        
        self.rank = rank
        self.suit = suit
