from collections import defaultdict
from typing import Dict, List, Set
from pathlib import Path

class BaseSolver:
    """
    Base class for all Wordle solvers.

    Attributes:
        words (List[str]): The list of all words.
        guesses (List[str]): The list of guesses made by the solver thus far.
        valid_words (List[str]): The list of words that are still valid given current knowledge.
        pos_to_letter (Dict[int, str]): Maps index to known letter at that index.
        letter_to_invalid_pos (Dict[str, Set[int]]): Maps letter to list of invalid indexes.
        min_letter_freqs (Dict[str, int]): Maps letter to minimum freq of that letter in the target word.
        max_letter_freqs (Dict[str, int]): Maps letter to maximum freq of that letter in the target word.
    """
    def __init__(self, words_path: Path):
        """
        Initialize the solver.

        Args:
            words_path (Path): Path to the file containing the words.
        """
        with open(words_path, "r") as file:
            self.words: List[str] = [line.strip() for line in file.readlines()]
        self.reset()
    
    def reset(self) -> None:
        """
        Resets the solver to its initial state (see attributes above).
        """
        # TODO: Part 2.I.A
        pass # Remove this line when you have implemented the method.

    def update_knowledge(self, guess: str, feedback: List[int]) -> None:
        """
        Updates the solver's knowledge based on the guess and feedback.

        Args:
            guess (str): The guess made by the solver.
            feedback (List[int]): The feedback for the guess.
        """
        # TODO: Part 2.I.C
        pass # Remove this line when you have implemented the method.

    def _is_word_valid(self, word: str) -> bool:
        """
        Checks if a word is valid given current knowledge.

        Args:
            word (str): The word to check.

        Returns:
            True if the word is valid given current knowledge, False otherwise.
        """
        # TODO: Part 2.I.B
        pass # Remove this line when you have implemented the method.

    def guess(self) -> str:
        """
        Guesses a word based on current knowledge.
        """
        raise NotImplementedError("Subclasses must implement this method")
