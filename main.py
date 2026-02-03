from player import Player
from deck import Deck

def main():
    # Poker will be heads-up (two players)
    player1 = Player(100)
    player2 = Player(100)

    while player1.chips > 0 and player2.chips > 0:
        deck = Deck()

        player1.deal_hand(deck.pick_card, deck.pick_card)
        player2.deal_hand(deck.pick_card, deck.pick_card)


if __name__ == "__main__":
    main()