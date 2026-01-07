from enum import Enum, auto

class Action(Enum):
    HIT = auto()        # new card
    STAND = auto()      # keep
    DOUBLE = auto()     # double
    SPLIT = auto()      # split
    SURRENDER = auto()  # give up

    def __str__(self):
        return self.name