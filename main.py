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

NUM_PLAYERS = 5
players = []
for i in range(NUM_PLAYERS):
    print(i)
    players.append(Player())

print(f"num players: {len(players)}")

# Deal initial cards to players
for p in players:
    cards = deck.deal_cards(2)

    # Turn the initial cards dealt to players face up
    for c in cards:
        c.turn_face_up()

    print(deck.num_cards())
    print(cards)
    print(p.hand)
    p.receive_cards(cards)
    print(p.hand)

# Play a single round
# TODO: THIS IS WIP. FINISH.
for p in players:
    winners = []
    next_rounds_active_players = []

    # first player checks their status
    status = p.get_status()

    # if bust remove player
    if status == PlayerStatus.BUST:
        continue; 
    if status == PlayerStatus.TWENTYONE:
        winners.append(p)
