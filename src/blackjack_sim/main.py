import argparse
import time
import multiprocessing
from typing import Tuple

# Importing internal modules using the absolute path
from blackjack_sim.core.deck import Deck
from blackjack_sim.simulation.game import Game
from blackjack_sim.simulation.result import GameResult
from blackjack_sim.strategies.basic_strategy import BasicStrategy

def simulate_batch(num_games: int) -> Tuple[int, int, int]:
    """
    Worker function to simulate a specific number of games on a single CPU core.
    
    Args:
        num_games (int): The number of blackjack hands to simulate in this batch.
        
    Returns:
        Tuple[int, int, int]: A tuple containing (wins, draws, losses).
    """
    # Initialize counters for this batch
    wins = 0
    draws = 0
    losses = 0

    # Initialize the strategy (stateless, so we can reuse it)
    strategy = BasicStrategy()
    
    # Initialize the deck with 6 decks (Standard Casino Shoe)
    # We create the deck ONCE per batch to avoid overhead, resetting it when needed.
    deck = Deck(num_decks=6)

    for _ in range(num_games):
        # Professional Rule: Reshuffle the deck if less than 15 cards remain (Penetration)
        # This simulates the "Cut Card" mechanic in real casinos.
        if len(deck) < 15:
            deck.reset()

        # Instantiate a new Game with the existing deck and strategy
        game = Game(deck, strategy)
        
        # Play the round and capture the result
        result = game.play_round()

        # Aggregating results based on the outcome
        if result in (GameResult.PLAYER_WIN, GameResult.PLAYER_BLACKJACK):
            wins += 1
        elif result == GameResult.PUSH:
            draws += 1
        else:
            # Covers DEALER_WIN
            losses += 1

    return wins, draws, losses

def main():
    """
    Main entry point for the simulation CLI.
    Parses arguments and orchestrates the multiprocessing workload.
    """
    
    # 1. Setup Argument Parser for CLI interaction
    parser = argparse.ArgumentParser(description="Monte Carlo Blackjack Simulator (High Performance)")
    parser.add_argument("--games", type=int, default=1_000_000, help="Total number of games to simulate")
    parser.add_argument("--threads", type=int, default=multiprocessing.cpu_count(), help="Number of CPU threads to use")
    
    args = parser.parse_args()

    total_games = args.games
    num_threads = args.threads

    print(f"--- Starting Simulation ---")
    print(f"Total Games: {total_games:,}")
    print(f"Threads:     {num_threads} (Detected CPU Cores)")
    print(f"---------------------------")

    # 2. Start the Timer to measure performance
    start_time = time.time()

    # 3. Divide the workload
    # We split the total games into equal chunks for each thread.
    games_per_thread = total_games // num_threads
    
    # Handle the remainder if total_games isn't perfectly divisible
    remainder = total_games % num_threads
    
    # Create a list of tasks (integers representing games to play)
    # Example: [1000, 1000, 1000, 1001] if threads=4 and games=4001
    tasks = [games_per_thread + (1 if i < remainder else 0) for i in range(num_threads)]

    # 4. Execute Multiprocessing
    # Pool() manages a pool of worker processes.
    with multiprocessing.Pool(processes=num_threads) as pool:
        # map() maps the function 'simulate_batch' to the 'tasks' list
        results = pool.map(simulate_batch, tasks)

    # 5. Aggregate Results from all threads
    total_wins = sum(r[0] for r in results)
    total_draws = sum(r[1] for r in results)
    total_losses = sum(r[2] for r in results)

    # 6. Stop Timer and Calculate Statistics
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    win_rate = (total_wins / total_games) * 100
    draw_rate = (total_draws / total_games) * 100
    loss_rate = (total_losses / total_games) * 100
    games_per_sec = total_games / elapsed_time

    # 7. Print Final Report
    print(f"\n--- Simulation Results ---")
    print(f"Time Elapsed:  {elapsed_time:.4f} seconds")
    print(f"Speed:         {games_per_sec:,.0f} hands/sec")
    print(f"--------------------------")
    print(f"Player Wins:   {total_wins:,} ({win_rate:.2f}%)")
    print(f"Draws (Push):  {total_draws:,} ({draw_rate:.2f}%)")
    print(f"Dealer Wins:   {total_losses:,} ({loss_rate:.2f}%)")
    print(f"--------------------------")
    
    # Theoretical check: Basic Strategy typically yields ~42.5% wins, ~8.5% ties, ~49% losses.
    # If our results are far off, we might have a bug in the logic.

if __name__ == "__main__":
    main()