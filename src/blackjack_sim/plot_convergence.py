import os  # <--- Aggiunto per gestire le cartelle
import time
import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

# Internal imports from our package
from blackjack_sim.core.deck import Deck
from blackjack_sim.simulation.game import Game
from blackjack_sim.simulation.result import GameResult
from blackjack_sim.strategies.basic_strategy import BasicStrategy

def simulate_chunk(num_games: int) -> Tuple[int, int]:
    """
    Simulates a small chunk of games and returns (wins, total_games).
    Used to build the dataset for the graph incrementally.
    """
    wins = 0
    strategy = BasicStrategy()
    deck = Deck(num_decks=6)

    for _ in range(num_games):
        if len(deck) < 15:
            deck.reset()

        game = Game(deck, strategy)
        result = game.play_round()

        if result in (GameResult.PLAYER_WIN, GameResult.PLAYER_BLACKJACK):
            wins += 1
            
    return wins, num_games

def main():
    # CONFIGURATION
    TOTAL_GAMES = 2_000_000
    BATCH_SIZE = 5_000
    THREADS = multiprocessing.cpu_count()

    print(f"--- Starting Convergence Analysis ---")
    print(f"Target: {TOTAL_GAMES:,} games")
    print(f"Batch Size: {BATCH_SIZE:,}")
    print(f"Threads: {THREADS}")

    # 1. Prepare tasks
    num_batches = TOTAL_GAMES // BATCH_SIZE
    tasks = [BATCH_SIZE] * num_batches

    start_time = time.time()

    # 2. Run Simulation in Parallel
    with multiprocessing.Pool(processes=THREADS) as pool:
        results = pool.map(simulate_chunk, tasks)

    elapsed = time.time() - start_time
    print(f"Simulation complete in {elapsed:.2f}s")

    # 3. Data Processing with NumPy
    results_array = np.array(results) 
    wins_per_batch = results_array[:, 0]
    games_per_batch = results_array[:, 1]

    cumulative_wins = np.cumsum(wins_per_batch)
    cumulative_games = np.cumsum(games_per_batch)
    win_rates = (cumulative_wins / cumulative_games) * 100

    # 4. Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(cumulative_games, win_rates, label='Actual Win Rate', color='#007acc', linewidth=1.5)
    
    final_rate = win_rates[-1]
    plt.axhline(y=final_rate, color='r', linestyle='--', alpha=0.7, label=f'Converged Value ({final_rate:.2f}%)')

    plt.title(f'Monte Carlo Simulation: Law of Large Numbers ({TOTAL_GAMES:,} Hands)')
    plt.xlabel('Number of Games Simulated')
    plt.ylabel('Player Win Rate (%)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.ylim(40, 45)
    plt.gca().get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

    # --- MODIFICA PER SALVATAGGIO AUTOMATICO ---
    
    # Definiamo il percorso relativo alla root del progetto
    output_dir = "docs/images"
    
    # Crea la cartella se non esiste (come 'mkdir -p')
    os.makedirs(output_dir, exist_ok=True)
    
    # Unisce cartella e nome file in modo sicuro
    output_file = os.path.join(output_dir, "convergence_plot.png")
    
    plt.savefig(output_file, dpi=300)
    print(f"\nGraph saved to: {output_file}")
    
    # -------------------------------------------
    
    print("Close the window to exit.")
    plt.show()

if __name__ == "__main__":
    main()