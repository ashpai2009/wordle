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
        self.wordle.reset()
        self.solver.reset()
        while not self.wordle.game_over():
            

            guess = self.solver.guess()

            feedback = self.wordle.guess(guess)

            

            self.solver.update_knowledge(guess, feedback)

            if self.wordle.game_over():
                print(f"Your final guess is {guess}")
                print(f"The target word was {self.wordle.target_word}")



                break

        


