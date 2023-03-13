"""player.py - Player class"""

class PlayerStatus:
    """Hold some string consts representing player status"""
    ACTIVE = 'active'
    TWENTYONE = '21'
    BUST = 'bust'

class Player:
    """Player in a game of blackjack
    Params
    ------
    dealer: Dealer | None
        The dealer of the game. The Player must have knowledge of the dealer 
        in order to request a card, etc.
    """

    def __init__(self, deck):
        """Create a new player.
        Params
        -----
        deck: Deck
            The blackjack deck. This is so the player can get cards

        Attributes
        ----------
        status: PlayerStatus (string)
            Status of the player in the game
        """
        self.hand = []
        self.deck = deck
        self.status = PlayerStatus.ACTIVE

    def receive_cards(self, new_cards):
        """Add 1 or more cards to players hand
        Params
        -----
        new_cards: list[Card]
        """
        self.hand.extend(new_cards)

    def get_best_current_score(self):
        """Look at the player's current hand and calculate their  best possible current score
        NOTE: This is a very naive algorithm.
        """

        aces = []
        score = 0

        for _card in self.hand:
            # Save aces for last. This way, after calculating the score of all other cards
            # in our hand we can decide if aces should be valued at 1 or 11
            if _card.is_ace():
                aces.append(_card)
            else:
                score += _card.get_value()

        num_aces = len(aces)

        # If we don't have any aces just return our score
        if num_aces == 0:
            return score

        # Otherwise -- Handle aces.
        # First check highest possible score (each ace valued at 11)
        highest_possible_score = score + num_aces * 11

        # if highest score is over 21, return lowest possible score
        # which is each ace valued at 1
        if highest_possible_score > 21:
            return score + num_aces
        
        # otherwise our highest possible score is at or below 21 and thus valid 
        # so return it
        return highest_possible_score

    def get_status(self):
        score = self.get_best_current_score()

        if score == 21:
            self.status = PlayerStatus.TWENTYONE
        if score > 21:
            self.status = PlayerStatus.BUST
        else:
            self.status = PlayerStatus.ACTIVE

        return self.status

    def take_turn(self):
        """Player takes their turn and decides whether to hit or stay, etc
        TODO: THIS IS WIP. FINISH.
        NOTE: This is a very naive algorithm. 
        """

        # We check player status first to handle the edge case of the games
        # very first turn.
        score = self.get_best_current_score()


        if self.get_be

        score = self.get_best_current_score()
        if score < 21:
            _card = self.deck.deal_cards()
            self.receive_cards(_card)

