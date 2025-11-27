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
        pos_to_letter (Dict[int, str]): Maps index to known letter at that index.       green letters
        letter_to_invalid_pos (Dict[str, Set[int]]): Maps letter to list of invalid indexes.     yellow letters and even gray letters
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

        self.guesses = []
        self.valid_words = self.words
        self.pos_to_letter = {}
        self.letter_to_invalid_pos = {}
        self.min_letter_freqs = {}
        self.max_letter_freqs = {}




    def update_knowledge(self, guess: str, feedback: List[int]) -> None:
        """
        Updates the solver's knowledge based on the guess and feedback.

        Args:
            guess (str): The guess made by the solver.
            feedback (List[int]): The feedback for the guess.

             Attributes:
        words (List[str]): The list of all words.
        guesses (List[str]): The list of guesses made by the solver thus far.
        valid_words (List[str]): The list of words that are still valid given current knowledge.
        pos_to_letter (Dict[int, str]): Maps index to known letter at that index.       green letters
        letter_to_invalid_pos (Dict[str, Set[int]]): Maps letter to list of invalid indexes.     yellow letters and even gray letters
        min_letter_freqs (Dict[str, int]): Maps letter to minimum freq of that letter in the target word.    
        max_letter_freqs (Dict[str, int]): Maps letter to maximum freq of that letter in the target word.  

        target = hello
        guess = hilts

        feedback = [2, 0, 2, 0, 0]

        pos_to_letter = {0: "h", 2 : "l}
        

        """

        for index in range(len(feedback)):
            if feedback[index] == 2:
                self.pos_to_letter[index] = guess[index]


        for index in range(len(feedback)):
            if feedback[index] == 0 or feedback[index] == 1:
                if guess[index] not in self.letter_to_invalid_pos:
                    self.letter_to_invalid_pos[guess[index]] = [index]
            
                else:
            
                    self.letter_to_invalid_pos[guess[index]].append(index)        

        letter_freq = {}
        for index in range(len(feedback)):
            if feedback[index] == 1 or feedback[index] == 2:
                if guess[index] in letter_freq:
                    letter_freq[guess[index]] += 1
                else:
                    letter_freq[guess[index]] = 1


        for letter in letter_freq:
            if letter in self.min_letter_freqs:
                if letter_freq[letter] > self.min_letter_freqs[letter]:
                    self.min_letter_freqs[letter] = letter_freq[letter]

            else:
                self.min_letter_freqs[letter] = 1

        new_valid = []
        for word in self.valid_words:
            if self._is_word_valid(word):
                new_valid.append(word)

        self.valid_words = new_valid
    def _is_word_valid(self, word: str) -> bool:
        """
        Checks if a word is valid given current knowledge.

        Args:
            word (str): The word to check.

        Returns:
            True if the word is valid given current knowledge, False otherwise.



         Attributes:
        words (List[str]): The list of all words.
        guesses (List[str]): The list of guesses made by the solver thus far.
        valid_words (List[str]): The list of words that are still valid given current knowledge.
        pos_to_letter (Dict[int, str]): Maps index to known letter at that index.       green letters
        letter_to_invalid_pos (Dict[str, Set[int]]): Maps letter to list of invalid indexes.     yellow letters and even gray letters
        min_letter_freqs (Dict[str, int]): Maps letter to minimum freq of that letter in the target word.    
        max_letter_freqs (Dict[str, int]): Maps letter to maximum freq of that letter in the target word. 


        """
        if word not in self.valid_words:
            return False

        for index in self.pos_to_letter:
            if word[index] != self.pos_to_letter[index]:
                return False
        
        for index in range(len(word)):
            if index in self.letter_to_invalid_pos.get(word[index], []):
                return False

            
        
        word_freqs = {}

        for letter in word:
            if letter in word_freqs:
                word_freqs[letter] += 1
                
            else:
                word_freqs[letter] = 1

        for letter in self.min_letter_freqs:

            # if word_freqs[letter] < self.min_letter_freqs[letter]:
            #     return False
            
            if word_freqs.get(letter, 0) < self.min_letter_freqs[letter]:
                return False

        for letter in self.max_letter_freqs:
           
            if word_freqs.get(letter, 0) > self.max_letter_freqs[letter]:
                return False

        return True





    def guess(self) -> str:
        """
        Guesses a word based on current knowledge.
        """
        raise NotImplementedError("Subclasses must implement this method")
