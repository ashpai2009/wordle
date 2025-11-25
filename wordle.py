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
        candidate_word_freq = {}
        for letter in candidate_word:
            if letter in candidate_word_freq:
                candidate_word_freq[letter] += 1
            else:
                candidate_word_freq[letter] = 1            
      
        feedback = []
        
        for i in range(len(guess_word)):
            if guess_word[i] == candidate_word[i]:
                feedback.append(2)
                candidate_word_freq[guess_word[i]] -= 1
                if candidate_word_freq[guess_word[i]] == 0:
                    del candidate_word_freq[guess_word[i]]
            else:
                feedback.append(0)

        for i in range(len(guess_word)):
            if guess_word[i] in candidate_word_freq and guess_word[i] != candidate_word[i]:
                candidate_word_freq[guess_word[i]] -= 1
                if candidate_word_freq[guess_word[i]] == 0:
                    del candidate_word_freq[guess_word[i]]
                feedback[i] = 1
            
        return feedback


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

        while word not in self.words:
            word = input("Pick a valid word: ")

        self.num_guesses -= 1
        self.guesses.append(word)

        return self.get_feedback(word, self.target_word)  


    def reset(self) -> str:
        """
        Reset the game state, by selecting a new random word, and resetting the guess counter.

        Returns:
            The target word.
        """

        self.target_word = random.choice(self.words)
        self.reset_with_target_word(self.target_word)

        



    
    def reset_with_target_word(self, word: str) -> None:
        """
        Reset the game state, with a specific target word.

        Args:
            word (str): The target word.
        """

        """
         Attributes:
        words (List[str]): The list of all words.
        target_word (str): The target word to guess.
        target_word_freqs (Dict[str, int]): The frequency of each letter in the target word.
        guesses (List[str]): The list of guesses made by the player.
        num_guesses (int): The number of guesses made by the player.
        won (bool): Whether the player has won the game.
    """
        self.target_word = word
        self.num_guesses = 6
        self.won = False
        
        self.guesses = []
        self.target_word_freqs = {}
        for i in word:
            if i in self.target_word_freqs:
                self.target_word_freqs[i] += 1
            else:
                self.target_word_freqs[i] = 1




        
    
    def game_over(self) -> bool:
        """
        Check if the game has ended.

        Returns:
            True if the game has ended, False otherwise.
        """
        
        if self.target_word in self.guesses:
            return True
        elif self.num_guesses == 0:
            return True
        else:
            return False
