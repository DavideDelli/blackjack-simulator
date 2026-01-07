from blackjack_sim.core.card import Card
from blackjack_sim.core.hand import Hand
from blackjack_sim.core.action import Action

class BasicStrategy:
    def decide(self, player_hand: Hand, dealer_up_card: Card) -> Action:
        """
        Decide la mossa migliore basandosi sulla tabella della Basic Strategy.
        """
        total = player_hand.value
        # Valore carta dealer (es. K=10, A=11)
        dealer_val = dealer_up_card.rank.value_list[0] 
        if dealer_val == 1: dealer_val = 11 # Se l'asso torna 1, consideralo 11 per la tabella

        # --- HARD TOTALS STRATEGY (simple) ---
        
        # 1. Totali bassi: chiedi sempre
        if total <= 8:
            return Action.HIT
            
        # 2. Totali alti: stai sempre
        if total >= 17:
            return Action.STAND

        # 3. specific cases
        if total == 9:
            # Raddoppia se dealer ha 3-6
            if 3 <= dealer_val <= 6:
                return Action.DOUBLE
            return Action.HIT
            
        if total == 10:
            # Raddoppia se dealer ha 2-9
            if 2 <= dealer_val <= 9:
                return Action.DOUBLE
            return Action.HIT
            
        if total == 11:
            # Raddoppia sempre
            return Action.DOUBLE
            
        if total == 12:
            # Stai solo se dealer è debole (4-6), altrimenti Hit
            if 4 <= dealer_val <= 6:
                return Action.STAND
            return Action.HIT
            
        if 13 <= total <= 16:
            # Stai se dealer è debole (2-6), altrimenti Hit (rischio bust)
            if 2 <= dealer_val <= 6:
                return Action.STAND
            return Action.HIT

        return Action.STAND