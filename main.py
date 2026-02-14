from player import Player
from deck import Deck
from hand import Hand
from card import Card
from typing import List, Tuple
from collections import defaultdict

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
    if winner is None:
        player1.chips += pot / 2
        player2.chips += pot / 2
    else:
        winner.chips += pot

def determine_winner(player1 : Player, player2 : Player, river : List[Card]) -> Player:
    if player1.hand is None:
        return player2
    elif player2.hand is None:
        return player1
    else:
        player1_best_five_cards = make_best_hand(player1.cards + river)
        player2_best_five_cards = make_best_hand(player2.cards + river)

        if player1_best_five_cards > player2_best_five_cards:
            return player1
        elif player2_best_five_cards > player1_best_five_cards:
            return player2
        else:
            return None # split pot

def make_best_hand(all_cards : List[Card]) -> Tuple[int, ...]:
    # return type -> rank of hand and then some consistent formatting for each of those hands
    # e.g. pair is second worst hadn so it will be (2, 4, 8, 5, 3) order matters since when python comapres typles it'll go in order
    
    # same thing as saying value = make_sf(all_cards), if value return value
    if value := make_straight_flush(all_cards):
        return value
    
    if value := make_quads(all_cards):
        return value

    if value := make_full_house(all_cards):
        return value

    if value := make_flush(all_cards):
        return value

    if value := make_straight(all_cards):
        return value

    if value := make_trips(all_cards):
        return value

    if value := make_two_pair(all_cards):
        return value

    if value := make_one_pair(all_cards):
        return value

    return make_high_card(all_cards)

def make_straight_flush(all_cards : List[Card]) -> Tuple[int, ...]:
    pass
def make_quads(all_cards : List[Card]) -> Tuple[int, ...]:
    freq = defaultdict(int)
    for card in all_cards:
        freq[card.rank] += 1
    
    highest_freq_tuple = max(freq.items(), key = lambda item : item[1])
    # card, freq

    highest_freq_card, highest_freq = highest_freq_tuple
    kicker = get_kicker(all_cards, highest_freq_tuple)
    
    if highest_freq < 4:
        return None
    
    return (8, highest_freq_card.rank, kicker)

def make_full_house(all_cards : List[Card]) -> Tuple[int, ...]:
    freq = defaultdict(int)
    for card in all_cards:
        freq[card.rank] += 1
    
    top_two_freq_tuple = sorted(freq.items(), key = lambda item : (item[1], item[0]), reverse=True)[:2]
    # tuple of card, freq

    if top_two_freq_tuple[0][1] != 3 or top_two_freq_tuple[1][1] != 2:
        return None
    
    return(7, top_two_freq_tuple[0][0].rank, top_two_freq_tuple[1][0].rank)
    # 7 (rank of full house in relation to other hands), rank of 3 of a kind, rank of 2 of a kind


def make_flush(all_cards : List[Card]) -> Tuple[int, ...]:
    freq = defaultdict(int)
    for card in all_cards:
        freq[card.suit] += 1
    # {2 : 3} -- club shows up 3 times

    list_of_suit_and_freq_tuple = sorted(freq.items(), key = lambda item : (item[1]), reverse=True)
    most_common_suit, freq_of_most_common_suit = list_of_suit_and_freq_tuple[0]
    if freq_of_most_common_suit < 5:
        return None
    
    cards_of_most_common_suit = []
    for card in all_cards:
        if card.suit == most_common_suit:
            cards_of_most_common_suit.append(card)
    
    cards_of_most_common_suit.sort(key=lambda card : card.rank, reverse=True)
    return (6, *(c.rank for c in cards_of_most_common_suit)[:5]) # only 5 highest
    # c.rank because we want to compare based off of rank and not Card objects


def make_straight(all_cards : List[Card]) -> Tuple[int, ...]:
    pass   
def make_trips(all_cards : List[Card]) -> Tuple[int, ...]:
    freq = defaultdict(int)
    for card in all_cards:
        freq[card.rank] += 1
    
    top_freq_tuple = sorted(freq.items(), key = lambda item : (item[1], item[0]), reverse=True)[0]
    # item[1] = frequency, item[0] = rank
    top_freq_card, freq = top_freq_tuple

    kickers = []

    for c in sorted(all_cards, key=lambda item:(item.rank), reverse=True):
        if len(kickers) == 2:
            break
        if c.rank == top_freq_card.rank:
            continue
        kickers.append(c)

    if freq < 3:
        return None
    else:
        return (5, top_freq_card.rank, kickers[0].rank, kickers[1].rank)
    # card : freq
def make_two_pair(all_cards : List[Card]) -> Tuple[int, ...]:
    freq = defaultdict(int)
    for card in all_cards:
        freq[card.rank] += 1

    top_two_freq_cards = sorted(freq.items(), key = lambda item : (item[1], item[0].rank), reverse=True)[:2]
    # items are in form card.rank : freq
    if top_two_freq_cards[0][1] < 2 or top_two_freq_cards[1][1] < 2:
        return None
    
    kicker = None
    for c in sorted(all_cards, key = lambda item : item.rank, reverse=True):
        if c.rank != top_two_freq_cards[0][0] or c.rank != top_two_freq_cards[1][0]:
            kicker = c
            break
    
    return (4, top_two_freq_cards[0][0], top_two_freq_cards[1][0], kicker.rank)
    
def make_one_pair(all_cards : List[Card]) -> Tuple[int, ...]:
    freq = defaultdict(int)
    for card in all_cards:
        freq[card.rank] += 1

    top_freq_tuple = sorted(freq.items(), key = lambda item : (item[1], item[0]), reverse=True)[0]
    # items are in form card.rank : freq
    if top_freq_tuple[1] < 2:
        return None
    
    kickers = []
    for c in sorted(all_cards, key=lambda item: item.rank, reverse=True):
        if len(kickers) == 4:
            break
        if c.rank == top_freq_tuple[0]:
            continue
        kickers.append(c)
    
    return (3, top_freq_tuple[0], *(k.rank for k in kickers)) # *kickers expands list into individual elements
    
def make_high_card(all_cards : List[Card]) -> Tuple[int, ...]:
    pass     

def get_kicker(all_cards : List[Card]):
    pass

def test_pair():
    deck = Deck()
    all_cards = []
    for i in range(7):
        all_cards.append(deck.pick_card())

    print("All cards to make a hand with: " + cards_to_readable_output(all_cards))
    tuple_generated = make_one_pair(all_cards)
    if tuple_generated:
        print("Tuple generated" + str(make_one_pair(all_cards)))
    else:
        print("No one pair :broken_heart:")
    

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
    test_pair()