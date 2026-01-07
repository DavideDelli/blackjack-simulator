from dataclasses import dataclass
from enum import IntEnum, auto

class Suit(IntEnum):
    HEARTS = auto()     #Cuori
    DIAMONDS = auto()   #Quadri
    CLUBS = auto()      #Fiori
    SPADES = auto()     #Picche

    def __str__(self):
        symbols = {
            self.HEARTS: "♥", self.DIAMONDS: "♦",
            self.CLUBS: "♣", self.SPADES: "♠"
        }
        return symbols[self]
    
class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    @property
    def value_list(self) -> list[int]:  #return the values of the card
        if self in (Rank.JACK, Rank.QUEEN, Rank.KING):
            return [10]
        if self == Rank.ACE:
            return [1, 11]
        return [self.value]
    
    def __str__(self):
        mapping = {11: "J", 12: "Q", 13: "K", 14: "A"}
        return mapping.get(self.value, str(self.value))
    
@dataclass(frozen=True)
class Card:
    rank: Rank
    suit: Suit

    def __str__(self):
        return f"{self.rank}{self.suit}"