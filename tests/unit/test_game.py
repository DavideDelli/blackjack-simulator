import pytest
from blackjack_sim.core.card import Card, Rank, Suit
from blackjack_sim.core.deck import Deck
from blackjack_sim.strategies.basic_strategy import BasicStrategy
from blackjack_sim.simulation.game import Game
from blackjack_sim.simulation.result import GameResult

class MockDeck(Deck):
    """Mazzo truccato: restituisce carte predeterminate."""
    def __init__(self, cards):
        # Le carte vengono pescate con pop(), quindi l'ultima della lista è la prima pescata
        self.cards = cards 

    def shuffle(self):
        pass # Non mescolare!

def test_player_natural_blackjack():
    # Simuliamo: Player(A, K), Dealer(2, 3)
    # Ordine pescata nel codice: P, D, P, D
    cards = [
        Card(Rank.THREE, Suit.CLUBS),   # 4° (Dealer)
        Card(Rank.KING, Suit.HEARTS),   # 3° (Player) -> BJ!
        Card(Rank.TWO, Suit.DIAMONDS),  # 2° (Dealer)
        Card(Rank.ACE, Suit.SPADES)     # 1° (Player)
    ]
    
    deck = MockDeck(cards)
    game = Game(deck, BasicStrategy())
    
    assert game.play_round() == GameResult.PLAYER_BLACKJACK

def test_dealer_busts():
    # Player sta con 20 (K+K). Dealer ha 16 (10+6) e pesca 10 -> Sballa (26)
    cards = [
        Card(Rank.TEN, Suit.DIAMONDS),  # 5° (Dealer Hit) -> BUST
        Card(Rank.SIX, Suit.CLUBS),     # 4° (Dealer)
        Card(Rank.KING, Suit.HEARTS),   # 3° (Player)
        Card(Rank.TEN, Suit.SPADES),    # 2° (Dealer)
        Card(Rank.KING, Suit.DIAMONDS)  # 1° (Player)
    ]
    
    deck = MockDeck(cards)
    game = Game(deck, BasicStrategy())
    
    assert game.play_round() == GameResult.PLAYER_WIN