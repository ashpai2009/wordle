import random
from collections import defaultdict

from typing import List
from pathlib import Path

class Wordle:
    """
    Manages Wordle state and logic.

    Attributes:
        words (List[str]): The list of all words.
        target_word (str): The target word to guess.
        target_word_freqs (Dict[str, int]): The frequency of each letter in the target word.
        guesses (List[str]): The list of guesses made by the player.
        num_guesses (int): The number of guesses made by the player.
        won (bool): Whether the player has won the game.
    """
    MAX_GUESSES: int = 6

    def __init__(self, words_path: Path):
        """
        Initialize the Wordle game.

        Args:
            words_path: Path to the file containing the words.
        """
        with open(words_path, "r") as file:
            self.words: List[str] = [line.strip() for line in file.readlines()]
        self.reset()
    
    def guess(self, word: str) -> List[int]:
        """
        Process a guess, and return the feedback.

        Args:
            word (str): The guessed word. Must be a valid word in the word list.

        Returns:
            A list of integers, where each integer represents the feedback of the guess.
                0: The letter is not in the word.
                1: The letter is in the word, but in the wrong position.
                2: The letter is in the word, and in the correct position.
        """
        # TODO: Part 1.III.B
        pass # Remove this line when you have implemented the method.

    @staticmethod
    def get_feedback(guess_word: str, candidate_word: str) -> str:
        """
        Get the feedback for a guess.

        Args:
            guess_word (str): The guess word.
            candidate_word (str): The candidate word.

        Returns:
            A list of integers, where each integer represents the feedback of the guess.
                0: The letter is not in the word.
                1: The letter is in the word, but in the wrong position.
                2: The letter is in the word, and in the correct position.
            
        Note: If two letters in the guessed word are the same, and the target word contains
        only one occurrence of that letter, then only one of those letters will be marked
        as a match — either green (2) if it is in the correct position, or yellow (1) if 
        it is in the wrong position. The other occurrences will be marked as 0 (not in the word).
        This mimics NYT Wordle's behavior of not overcounting duplicate letters in a guess.
        """
        # TODO: Part 1.III.A
        pass # Remove this line when you have implemented the method.   
    
    def reset(self) -> str:
        """
        Reset the game state, by selecting a new random word, and resetting the guess counter.

        Returns:
            The target word.
        """
        # TODO: Part 1.I.B
        pass # Remove this line when you have implemented the method.
    
    def reset_with_target_word(self, word: str) -> None:
        """
        Reset the game state, with a specific target word.

        Args:
            word (str): The target word.
        """
        # TODO: Part 1.I.A
        pass # Remove this line when you have implemented the method.
    
    def game_over(self) -> bool:
        """
        Check if the game has ended.

        Returns:
            True if the game has ended, False otherwise.
        """
        # TODO: Part 1.II
        pass # Remove this line when you have implemented the method.
