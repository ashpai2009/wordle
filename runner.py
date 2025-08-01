from pathlib import Path
from wordle import Wordle
from solvers.base_solver import BaseSolver
from typing import Optional

class Runner:
    """
    Class for running a Wordle game with a solver.
    """

    def __init__(self, words_path: Path, solver: BaseSolver, target_word: Optional[str] = None):
        self.wordle = Wordle(words_path)
        self.solver = solver

        if target_word:
            self.wordle.reset_with_target_word(target_word)

    def run(self):
        """
        Runs through a Wordle game using the solver of choice.
        """
        # TODO: Part 3
        pass # Remove this line when you have implemented the method.
