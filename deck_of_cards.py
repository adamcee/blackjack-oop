"""deck_of_cards.py
Contains classes, etc, for constructing & managing a deck of cards.
"""
from random import shuffle

class Card:
    """
    Represent a playing card (ace of spades, etc)in a deck.
    Meant to model the popular 52-card deck used for games like Poker, Blackjack, etc.
    See https://en.wikipedia.org/wiki/Standard_52-card_deck for details
    """
    RANKS = { 1: 'ace', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                    8: 'eight', 9: 'nine', 10: 'ten', 11: 'jack', 12: 'queen', 13: 'king', 14: 'joker' }

    SUITES = { 1: 'clubs', 2: 'diamonds', 3: 'hearts', 4: 'spades' }

    def __init__(self, rank, suite):
        """
        Params
        ------
        rank: int
            An integer representing the rank of the card.
        suite: int
            An integer representing the suite of the card.

        Attributes
        ----------
        rank & suite attributes are same as params
        is_face_up: Boolean
            When false, no one but the player can see this card. 
            When true, all other players/dealer can see card.
        """

        self.rank = rank
        self.suite = suite
        self.is_face_up = False

    def rank_name(self):
        """ Return the cards rank name ('Queen', 'Four', etc)"""
        return Card.RANKS[self.rank]

    def suite_name(self):
        """ Return the cards rank name ('Queen', 'Four', etc)"""
        # If the card is a joker it will not have a suite
        if self.suite is None:
            return None
        return Card.SUITES[self.suite]

    def card_name(self, capitalize_first_letter=False):
        """Return the cards name. Ex: 'four of clubs'"""
        
        name = f"{self.rank_name()} of {self.suite_name()}"
        # Special case - Joker has no suite
        if self.rank == 14:
            name = self.rank_name()
        
        if capitalize_first_letter is True:
            return name.capitalize()

        return name

    def is_joker(self):
        """Return true if joker"""
        if self.rank == 14:
            return True
        return False

    def is_ace(self):
        """Returns true if the card is an ace"""
        if self.rank == 1:
            return True
        return False

    def is_royal(self):
        """Returns true if the card is jack, queen, or king"""
        if (10 < self.rank < 14):
            return True
        return False

    def is_number(self):
        """Return true if number card"""
        if (1 < self.rank < 11):
            return True
        return False

    def turn_face_up(self):
        """Turn card face up"""
        self.is_face_up = True

    def __str__(self):
        return self.card_name()
    
    def __repr__(self):
        return self.card_name()


class BlackJackCard(Card):
    """A blackjack card. Represents the card's score or value in the game
    Attributes
    ----------
    if_ace_use_as_one: bool
        Aces are either valued at 1 or 11. If the card is an ace and this is true,
        this card is valued at 1. If it's an ace and this is false, 11. If card is not
        ace does not apply.
    
    value: int
        The value of the card in the game
    """

    def __init__(self, rank, suite):
        """Create the card"""
        super().__init__(rank, suite)
        self.value = self.get_value()

    def get_value(self):
        """Get the value of a card in the game
        - non-royal /ace cards have value equal to their rank
        - Jack, Queen, King, have value of 10
        - Ace has value of either 1 or 11
        """
        if self.is_number() is True:
            return self.rank
        if self.is_royal() is True:
            return 10
        if self.is_ace() is True:
            return (1, 11)

class Deck:
    """Represents a deck of 52 playing cards. 
    See https://en.wikipedia.org/wiki/Standard_52-card_deck for details

    Attributes
    -----------
    cards: list[Card]
       Represents the cards *currently* in the deck.
    """
    def __init__(self, Card_Class=Card, include_jokers=False):
        """Initialize the deck
        Params
        ------
        include_jokers: Bool
            If we want the deck to have jokers or not
        
        """
        self.Card_Class = Card_Class
        self.include_jokers = include_jokers
        self.cards = []

        # Populate the deck with a fresh set of cards
        self.reset_fresh_deck()

    def reset_fresh_deck(self, shuffle_deck=True):
        """Set or reset the deck to be a fresh set of cards."""
        # Get rid of any cards still in the deck
        self.cards = []

        # Build the fresh deck
        for suite in Card.SUITES:
            for rank in Card.RANKS:
                # We ignore Joker here - it's a special case we handle separately elsewhere
                if(rank != 14):
                    self.cards.append(self.Card_Class(rank, suite))

        if self.include_jokers:
            self.cards.append(Card(Card.RANKS[14], None))

        #Shuffle the deck
        if shuffle_deck is True:
            shuffle(self.cards)

    def num_cards(self):
        """Get number of cards currently in the deck"""
        return len(self.cards)

    def deal_cards(self, num_cards=1):
        """Deals cards from the deck. Common use case is dealing cards to a player

        Params
        ------
        num_cards: int
            Number of cards to deal

        Returns a list of cards
        """
        # EDGE CASE: num_cards == 0 will delete all cards b/c of the slicing logic so handle here
        if num_cards == 0:
            return []

        # get copy of the cards and then delete from deck
        cards = self.cards[-num_cards:]
        del self.cards[-num_cards:]
        return cards
