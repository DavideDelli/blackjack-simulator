from src.blackjack_sim.core.deck import Deck
from src.blackjack_sim.core.hand import Hand
from src.blackjack_sim.core.action import Action
from src.blackjack_sim.strategies.basic_strategy import BasicStrategy
from src.blackjack_sim.simulation.result import GameResult

class Game:
    def __init__(self, deck: Deck, strategy: BasicStrategy):
        self.deck = deck
        self.strategy = strategy

    def play_round(self) -> GameResult:
        player_hand = Hand()
        dealer_hand = Hand()

        # 1.
        for _ in range(2):
            player_hand.add_card(self.deck.draw())
            dealer_hand.add_card(self.deck.draw())

        dealer_up_card = dealer_hand.cards[0]

        # 2. Immediate checkup for a blackjack
        p_bj = player_hand.is_blackjack
        d_bj = dealer_hand.is_blackjack

        if p_bj and d_bj:
            return GameResult.PUSH
        if p_bj:
            return GameResult.PLAYER_BLACKJACK
        if d_bj:
            return GameResult.DEALER_WIN

        # 3. player turn
        while True:
            if player_hand.is_busted:
                return GameResult.DEALER_WIN

            action = self.strategy.decide(player_hand, dealer_up_card)

            if action == Action.STAND:
                break
            
            elif action == Action.HIT:
                player_hand.add_card(self.deck.draw())
            
            elif action == Action.DOUBLE:
                player_hand.add_card(self.deck.draw())
                if player_hand.is_busted:
                    return GameResult.DEALER_WIN
                break
            
            else:
                break

        # 4. Dealer turn
        while dealer_hand.value < 17:
            dealer_hand.add_card(self.deck.draw())

        # 5. Det winner
        if dealer_hand.is_busted:
            return GameResult.PLAYER_WIN
        
        if player_hand.value > dealer_hand.value:
            return GameResult.PLAYER_WIN
        elif dealer_hand.value > player_hand.value:
            return GameResult.DEALER_WIN
        else:
            return GameResult.PUSH