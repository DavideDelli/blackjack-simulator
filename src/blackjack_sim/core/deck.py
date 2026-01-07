import random
from typing import List, Optional
from src.blackjack_sim.core.card import Card, Rank, Suit

class Deck:
    def __init__(self, num_decks: int = 1):
        self.num_decks = num_decks
        self.cards: List[Card] = []
        self.reset()

    def reset(self):    #regenerate and shuffle the deck
        self.cards = [
            Card(rank, suit)
            for _ in range(self.num_decks)
            for suit in Suit
            for rank in Rank
        ]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self) -> Optional[Card]:
        if not self.cards:
            return None
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)
    
