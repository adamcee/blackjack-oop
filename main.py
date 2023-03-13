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
active_players = []
for i in range(NUM_PLAYERS):
    active_players.append(Player(i, deck))

# More Game state
CONTINUE_GAME = True
winners = []
all_busted_players = []
recently_busted_players = []

# First round - deal out initial cards, check for any players
# who are immediate bust or immediate 21
for _player in active_players:
    first_hand =  deck.deal_cards(2)
    _player.receive_cards(first_hand)

    status = _player.get_status()
    if status == PlayerStatus.TWENTYONE:
        winners.append(_player)
    if status == PlayerStatus.BUST:
        recently_busted_players.append(_player)

# After the initial deal, check if we have any immediate winners
if len(winners) > 0:
    CONTINUE_GAME = False

# Main game loop
while CONTINUE_GAME is True:
    # Remove players busted in the last round from the active players list
    # and reset the recently busted players list
    for rbp in recently_busted_players:
        #TODO: Confirm use .remove() for an object in list works in python
        active_players.remove(rbp)
        all_busted_players.append(rbp)

    recently_busted_players = []

    # Check if there are still any active players
    if len(active_players) == 0:
        CONTINUE_GAME = False
        break

    # One round of play
    for _player in active_players:
        # TODO: player choose to hit or stay. Need some sort of loop/recursion for continuous hits
        # And we'll check player status as we go.

        # TODO: This is a very naive strategy. Improve.
        # TODO: Move this into a method on the Player class?
        # Keep asking for cards until we get 21 or go bust
        while _player.get_status() == PlayerStatus.ACTIVE:
            _player.receive_cards(deck.deal_cards())

        # If player gets 21 we add them to the winners list, and, as we are past the first round,
        # a winner means the game is over.
        if _player.get_status() == PlayerStatus.TWENTYONE:
            winners.append(_player)
            CONTINUE_GAME = False
            break

        # Check if player has busted
        if _player.get_status() == PlayerStatus.BUST:
            recently_busted_players.append(_player)

# The game is over, announce the winners and the losers
print("The game is over!")
if len(winners) > 0:
    print("Winners:")
    for w in winners:
        print(w.name)
else:
    print("There were no winners.")

print("Losers:")
for bp in all_busted_players:
    print(bp.name)
