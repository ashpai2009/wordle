from solvers.base_solver import BaseSolver
from wordle import Wordle
from typing import Dict, List
from collections import defaultdict
import math
import multiprocessing as mp

class EntropyOptimalSolver(BaseSolver):
    def guess(self) -> str:
        """
        Guesses a word based on current knowledge, using the strategy that maximizes the entropy of the feedback.

        Returns:
            The word to guess.
        """
        # TODO: Part 2.IV
        pass # Remove this line when you have implemented the method.
