from solvers.entropy_optimal_solver import EntropyOptimalSolver
from solvers.random_solver import RandomSolver
from solvers.manual_solver import ManualSolver
from runner import Runner
import argparse
from pathlib import Path
from typing import Optional

def main():
    """
    Main entrypoint for running the Wordle game.

    CLI Args:
        --solver (str): The solver to use.
        --words_file (str): The name of the words file to use (must be in data directory).
        --target_word (Optional[str]): The target word to guess. If not provided, a random word will be selected.
    """
    parser = argparse.ArgumentParser(description="Play Wordle with different solvers.")
    parser.add_argument(
        "--solver",
        type=str,
        default="random",
        choices=["entropy_optimal", "random", "manual"],
        help="Solver to use."
    )
    parser.add_argument(
        "--words_file",
        type=str,
        default="words.txt",
        help="Name of the words file to use (must be in data directory)"
    )
    parser.add_argument(
        "--target_word",
        type=str,
        default=None,
        help="Target word to guess."
    )
    args = parser.parse_args()

    words_path = Path(__file__).parent / "data" / args.words_file

    if args.solver == "entropy_optimal":
        solver = EntropyOptimalSolver(words_path)
    elif args.solver == "random":
        solver = RandomSolver(words_path)
    elif args.solver == "manual":
        solver = ManualSolver(words_path)
    
    runner = Runner(words_path, solver, args.target_word)
    runner.run()

if __name__ == "__main__":
    main()
