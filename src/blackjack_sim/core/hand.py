from typing import List
from blackjack_sim.core.card import Card, Rank

class Hand:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card):
        self.cards.append(card)

    @property
    def value(self) -> int:
        total = 0
        aces = 0

        #initial calculation: ace = 11
        for card in self.cards:
            if card.rank == Rank.ACE:
                aces += 1
                total += 11
            else:
                total += card.rank.value_list[0]
        
        #if busted, cut down the aces to 1
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total
    
    @property
    def is_blackjack(self) -> bool:
        return len(self.cards) == 2 and self.value == 21
    
    @property
    def is_busted(self) -> bool:
        return self.value > 21
    
    def __str__(self):
        return " ".join(str(c) for c in self.cards) + f" ({self.value})"