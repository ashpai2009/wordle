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

        while not self.wordle.game_over():

            guess = self.solver.guess()

            feedback = self.wordle.guess(guess)

            print(f"Ur guess is {guess} and ur feedback is {feedback}")

            self.solver.update_knowledge(guess, feedback)

            if self.wordle.game_over():
                break

        


