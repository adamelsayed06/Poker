from player import Player
from deck import Deck
from hand import Hand
from card import Card
import time

def card_to_readable_output(card : Card) -> str:
    cleaned_suit = None
    cleaned_rank = None

    if card.rank == 11:
        cleaned_rank = "J"
    elif card.rank == 12:
        cleaned_rank = "Q"
    elif card.rank == 13:
        cleaned_rank = "K"
    elif card.rank == 14:
        cleaned_rank = "A"
    else:
        cleaned_rank = card.rank

    if card.suit == 0:
        cleaned_suit = "♣"
    elif card.suit == 1:
        cleaned_suit = "♦"
    elif card.suit == 2:
        cleaned_suit = "♥"
    elif card.suit == 3:
        cleaned_suit = "♠"
    else:
        cleaned_suit = card.suit # should never reach this case, only 4 suits

    return (f"{cleaned_rank}{cleaned_suit}")

def main():
    # Poker will be heads-up (two players)
    player1 = Player(100)
    player2 = Player(100)

    while player1.chips > 0 and player2.chips > 0:
        deck = Deck() # initializes a new deck -> so we will never run out of cards

        player1.deal_hand(Hand(deck.pick_card(), deck.pick_card()))
        player2.deal_hand(Hand(deck.pick_card(), deck.pick_card()))

        river = []
        river.append(deck.pick_card())
        river.append(deck.pick_card())
        river.append(deck.pick_card())

        print("Player 1's Hand is: " + card_to_readable_output(player1.hand.first_card) + " " + card_to_readable_output(player1.hand.second_card))
        print("Player 2's hand is: " + card_to_readable_output(player2.hand.first_card) + " " + card_to_readable_output(player2.hand.second_card))

        print(f"River: {card_to_readable_output(river[0])} {card_to_readable_output(river[1])} {card_to_readable_output(river[2])}")
        time.sleep(10)

        make_betting_decision()

        river.append(deck.pick_card())

        make_betting_decision()

        river.append(deck.pick_card())
        
        make_betting_decision()


if __name__ == "__main__":
    main()