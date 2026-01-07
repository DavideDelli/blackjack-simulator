# ♠️ Monte Carlo Blackjack Simulator

![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-95%25-green)
![License](https://img.shields.io/badge/license-MIT-purple)

A high-performance, multi-threaded Monte Carlo simulator for Blackjack, built with modern Python engineering practices.

## 🚀 Features

* **High Performance Engine**: Capable of simulating **>800,000 hands/second** utilizing multi-core architecture.
* **Basic Strategy Implementation**: AI agents make decisions based on statistically optimal probability tables.
* **Production-Grade Structure**: Organized as an installable Python package (`src` layout).
* **Rigorous Testing**: Fully TDD (Test Driven Development) approach with `pytest`.
* **Configurable**: CLI arguments for custom simulation depth and thread count.

## 📊 Benchmark Results

Running on **AMD Ryzen 9 5900X** (12 Cores / 24 Threads):

| Games Simulated | Time Elapsed | Speed |
| :--- | :--- | :--- |
| 10,000,000 | **12.33s** | **810,635 hands/sec** |

### Statistical Outcome (Sample)
* **Player Win Rate**: 42.82%
* **Dealer Win Rate**: 48.63%
* **Push (Draw)**: 8.55%

## 🛠 Installation

Clone the repository and install the package in editable mode:

```bash
git clone [https://github.com/TuoUsername/blackjack-simulator.git](https://github.com/TuoUsername/blackjack-simulator.git)
cd blackjack-simulator

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate.fish  # Or .venv/bin/activate on Bash/Zsh

# Install dependencies and the package
pip install -e .
pip install pytest ruff