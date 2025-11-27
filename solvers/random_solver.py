from solvers.base_solver import BaseSolver
import random

class RandomSolver(BaseSolver):
    def guess(self) -> str:
        """
        Guesses a word based on current knowledge, using a random choice from the remaining valid words.

        Returns:
            The word to guess.
        """

        guess = random.choice(self.valid_words).lower().strip()
        
        self.guesses.append(guess)

        return guess

