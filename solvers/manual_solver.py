from solvers.base_solver import BaseSolver

class ManualSolver(BaseSolver):
    def guess(self) -> str:
        """
        Guesses a word based on current knowledge, using user input.

        Returns:
            The word to guess.
            
        """

        guess = input("Pick a word you want to guess: ").lower().strip()

        self.guesses.append(guess)

        return guess



        # TODO: Part 2.II
        pass # Remove this line when you have implemented the method.
