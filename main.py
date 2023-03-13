"""main.py - Run this file to start a blackjack game"""

from deck_of_cards import BlackJackCard, Deck
from player import Player, PlayerStatus

deck = Deck(BlackJackCard)

# Print some stuff to test the Deck works
# print(deck.cards)
# print(deck.num_cards())
# print(deck.deal_cards())
# print(deck.num_cards())
# deck.reset_fresh_deck()
# print(deck.num_cards())

# old, from testing
# player_a = Player()
# player_b = Player()
# player_c = Player()

# Game state - create the players
NUM_PLAYERS = 5
players = []
for i in range(NUM_PLAYERS):
    players.append(Player(i, deck))

# More Game state
CONTINUE_GAME = True
winners = []
busted_players = []

# First round - deal out initial cards, check for any players
# who are immediate bust or immediate 21
for _player in players:
    first_hand =  deck.deal_cards(2)
    _player.receive_cards(first_hand)

    status = _player.get_status()
    if status == PlayerStatus.TWENTYONE:
        winners.append(_player)

# After the initial deal, check if we have any immediate winners
if len(winners) > 0:
    CONTINUE_GAME = False

# Main game loop
while CONTINUE_GAME is True:
    # If all players are busted the game is over.
    if len(busted_players) == len(players):
        CONTINUE_GAME = False
        break

    # One round of play
    for _player in players:
        # 1. If player is bust we add them to the busted list, ignore them and move on to the next player
        if _player.get_status() == PlayerStatus.BUST:
            busted_players.append(_player)
            continue

        # 2. TODO: player choose to hit or stay. Need some sort of loop/recursion for continuous hits

        # 3. If player gets 21 we add them to the winners list, and, as we are past the first round,
        # a winner means the game is over.
        if status == PlayerStatus.TWENTYONE:
            winners.append(_player)
            CONTINUE_GAME = False
            break  

# The game is over, announce the winners and the losers
print("The game is over!")
if len(winners) > 0:
    print("Winners:")
    for w in winners:
        print(w.name)
else:
    print("There were no winners.")

print("Losers:")
for bp in busted_players:
    print(bp.name)
