from player import Player
from deck import Deck
from hand import Hand
from card import Card

def card_to_readable_output(self, card : Card) -> str:
    if card.suit == 0:
        return (f"{card.rank}♣")
    elif card.suit == 1:
        return (f"{card.rank}♦")
    elif card.suit == 2:
        return (f"{card.rank}♥")
    elif card.suit == 3:
        return (f"{card.rank}♠")

def main():
    # Poker will be heads-up (two players)
    player1 = Player(100)
    player2 = Player(100)

    while player1.chips > 0 and player2.chips > 0:
        deck = Deck()

        player1.deal_hand(deck.pick_card, deck.pick_card)
        player2.deal_hand(deck.pick_card, deck.pick_card)

        print("Player 1's Hand is: " + card_to_readable_output(player1.hand.first_card) + " " + card_to_readable_output(player1.hand.second_card))
        print("Player 2's hand is: " + card_to_readable_output(player2.hand.first_card) + " " + card_to_readable_output(player2.hand.second_card))


if __name__ == "__main__":
    main()