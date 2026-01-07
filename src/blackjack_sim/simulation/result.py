from enum import Enum, auto

class GameResult(Enum):
    PLAYER_WIN = auto()
    DEALER_WIN = auto()
    PUSH = auto()       # Pareggio
    PLAYER_BLACKJACK = auto() # Spesso paga 3:2