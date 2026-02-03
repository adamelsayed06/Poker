from player import Player
from deck import Deck
from hand import Hand
from card import Card
from typing import List

def cards_to_readable_output(cards : List[Card]) -> str:
    cleaned_suit = None
    cleaned_rank = None
    output = ""

    for card in cards:
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

        output += (f"{cleaned_rank}{cleaned_suit}")

    return output

def handle_bet(player : Player, player_amount_at_stake : int, amount_needed_to_be_put_at_stake : int) -> None:
    if player_amount_at_stake == -1:
        player.fold()
    else:
        if player_amount_at_stake < amount_needed_to_be_put_at_stake:
            print("Error: You did not put enough money in... folding your hand") # refactor?
            player.fold()
        elif player_amount_at_stake == amount_needed_to_be_put_at_stake:
            print("Bet called / checked")
        else:
            print("Bet raised")

def make_betting_decision(player1 : Player, player2 : Player) -> int:
    min_bet = 0
    player_1_amount_at_stake = 0
    player_2_amount_at_stake = 0

    while True: # emulates a do-while loop
        player_1_amount_at_stake = int(input("Player 1, input your TOTAL bet size: (0 to check, -1 to fold): "))
        handle_bet(player1, player_1_amount_at_stake, min_bet)

        player_2_amount_at_stake = int(input("Player 2, input your TOTAL bet size: (0 to check, -1 to fold)"))
        handle_bet(player2, player_2_amount_at_stake, min_bet)
        if player_1_amount_at_stake == player_2_amount_at_stake:
            break        

    return player_1_amount_at_stake + player_2_amount_at_stake

def payout_winner(player1 : Player, player2 : Player, river : List[Card], pot: int) -> None:
    winner = determine_winner(player1, player2, river)
    winner.chips += pot

def determine_winner(player1 : Player, player2 : Player, river : List[Card]) -> Player:
    if player1.hand is None:
        return player2
    elif player2.hand is None:
        return player1
    else:
        return None

def main():
    # Poker will be heads-up (two players) -> later we can pass in a number of players and implement that
    player1 = Player(100)
    player2 = Player(100)

    while player1.chips > 0 and player2.chips > 0:

        deck = Deck() # initializes a new deck -> so we will never run out of cards
        pot = 0

        player1.deal_hand(Hand(deck.pick_card(), deck.pick_card()))
        player2.deal_hand(Hand(deck.pick_card(), deck.pick_card()))

        pot += make_betting_decision(player1, player2)

        river = []
        river.append(deck.pick_card())
        river.append(deck.pick_card())
        river.append(deck.pick_card())

        print("Player 1's Hand is: " + cards_to_readable_output([player1.hand.first_card, player1.hand.second_card]))
        print("Player 2's hand is: " + cards_to_readable_output([player2.hand.first_card, player2.hand.second_card]))

        print(f"Flop: {cards_to_readable_output(river)}")

        pot += make_betting_decision(player1, player2)

        river.append(deck.pick_card())
        print(f"Turn: {cards_to_readable_output(river)}")

        pot += make_betting_decision(player1, player2)

        river.append(deck.pick_card())
        print(f"River: {cards_to_readable_output(river)}")
        
        pot += make_betting_decision(player1, player2)

        payout_winner(player1, player2, river, pot)

if __name__ == "__main__":
    main()