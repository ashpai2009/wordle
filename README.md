# Wordle Project  
In this project, we will implement the game of Wordle.  
More specifically, we have three parts to this project:  
- **Part 1:** Implement the Wordle game
- **Part 2:** Implement Wordle solvers  
- **Part 3:** Implement Runner
  
Before we start, let's take a look at all the files we have.
## Project Structure
In this section, we overview the various files in this project, and their purposes.
- `./data`: Contains data for the project. 
  - `words.txt`: File containing the list of five-letter words we will use.
- `./solvers`: Contains the Wordle solvers' implementation
  - `base_solver.py`: Contains the base class for a Wordle solver. Implement the constructor, and various other helper utilities that all Wordle solvers will need to have.
  - `manual_solver.py`: Contains a Wordle solver that uses user input to produces guesses.
  - `random_solver.py`: Contains a naive, automated Wordle solver that randomly chooses from the remaining valid words using the knowledge it has from the game.
  - `entropy_optimal_solver.py`: This is not in-scope for the project, but it implements an entropy-optimal solution to Wordle, and is able to achieve a higher success rate than random guessing. It can be implemented as an extension.
- `main.py`: The main entrypoint for running the Wordle game. Calls the `Runner` class.
- `runner.py`: Uses the solver of choice to run the Wordle game.
- `wordle.py`: The main class that manages Wordle game state. Manages things like # of guesses remaining, etc.

There are comments marked `TODO: Part <section_name>` to help you find the associated code with each part. Try to test frequently after implementing each part to make debugging easier.

## Part 1: Wordle Game
In this first part, we will focus on implementing the core logic of the Wordle game itself.

Take a look at `wordle.py`. We will see that we have to implement various methods in order to manage game state. 

### I. Initializing Default Game State
In this section, we will focus on initializing the default game state. This is handled by the constructor, but the constructor uses the `reset` and `reset_with_target_word` helper methods.

#### A. Helper Method: `reset_with_target_word`
This method accepts a target word, and will use that to reset some of the attributes to the default values. The attributes are described in a doctstring at a top of the class. Use the descriptions to figure out what each attribute must be initialized to. 

#### B. Helper Method: `reset`
This method does not accept a target word; instead, it will generate a random word from the list of words.  

**Hint #1:** Which attribute manages the list of all words?  
**Hint #2**: Take a look at the documentation `random.choice` online (library already imported) to see how to choose a random word from the list of all words.  
  
After implementing these two words, the constructor should work as expected. Try testing it out to ensure it works as expected.

### II. `game_over`
This is a relatively simple method that returns a boolean telling us whether the Wordle game is done or not. Think about what conditions could be met in order for the game to be finished. Hint #1: There are two conditions, one for win and one for loss.

### III. Processing Guesses
This is the most difficult part of implementing the `Wordle` class. We need to be able to take in guesses, and return feedback. 

#### A. Helper Method: `get_feedback`
This is a static method, which means it does not have access to the class attributes; that's okay, since this method does not need to do that. Essentially, it is just a normal function attached to the class. Be careful when implementing this method, as you need to think carefully to not double count greens/prior yellows when returning the feedback. The feedback is a list of length 5. 0 means gray, 1 means yellow, 2 means green. 

If the double counting is confusing here, try reading the doctstring for the method to get a better idea. You can also try using the online NYT world to see how they return feedback in terms of colors, and cross-check with your implementation.

#### B. Main Method: `guess`
This method takes in a guessed word, and will update the relevant attributes to manage the game state. Think about which of the attributes need to change each time a guess is made. The method has already been started; it includes some basic checks to ensure that none of the Wordle constraints are violated. However, we still need to update some attributes, and return the feedback. To get the feedback, we can use the helper method `get_feedback`, which should have been implemented in the last section.

## Part 2: Wordle Solver
### I. `BaseSolver`
In this section, we implement the `BaseSolver` class. All Wordle Solvers in our code will inherit from this base class, as it provides some useful utilities and functionality that all solvers will need. 

#### A. Initializing Default Game State
Much like in the `Wordle` class, the constructor is already implemented, but it uses a `reset` method that initializes various attributes needed to maintain the solver's knowledge. Read the docstring at the top of the class, and implement the `reset` method to initialize attributes to default values.

#### B. Determining Whether Word is Valid
The Wordle solver will need to, given its current knowledge, be able to determine whether a word is valid or not. It needs to be able to do this in order to make proper guesses. Otherwise, it would continue to guess invalid words, and would not be able to make progress. 
   
In this section, we will implement the method `_is_word_valid` to do this. We will need to use the various attributes listed at the top of the class, and initialized in `reset`.  

**Hint #1:** First, try to figure out which attributes are relevant to determining whether a word is valid or not.  
**Hint #2:** We can make multiple passes of the guess word to do this; no need to try and fit all the checks in one iteration of the word.  
**Hint #3:** The relevant attributes are: `pos_to_letter`, `letter_to_invalid_pos`, `min_letter_freqs`, `max_letter_freqs`.

#### C. Updating the Solver's Knowledge
Of course, we will need to have a method to update the solver's knowledge after it receives feedback from the `Wordle` class. If we did not do this, then it wouldn't be able to "learn" after making a guess, and would not be able to make gradually better guesses. In this section, we implement the `update_knowledge` method to do so. This method is quite tricky, and there are many nuances involved, so it's best to think things out before coding.  

The method takes in a `guess` and a `feedback` list (see Part 1 for details). Using this, how can we update the solver's "knowledge" (the attributes discussed in the Part B of this section)?  

**Hint #1:** Try to make one pass over `guess` for each attribute; this keeps things simple, and can limit confusion.  
**Hint #2:** For `pos_to_letter`, how do we know whether a letter is in the right position based on `feedback`?  
**Hint #3:** For `letter_to_invalid_pos`, how do we know whether a letter is NOT in the right position? Is this signified by gray and/or green and/or yellow letter?  
**Hint #4:** For each unique letter in a `guess`, how can we use the `feedback` to determine the minimum frequency for that letter in the target word. Think about what happens when we have several `green` and/or `yellow` feedback for the letter type.  
**Hint #5:** When can we determine that a certain letter cannot occur more than a certain number of times in the target word?  
**Caution:** When updating `min_letter_freqs`, `max_letter_freqs` make sure not to reassign a letter to a less tight bound (compared to knowledge from previous rounds). This would lead to the solver losing information.  

Once we complete this section, most of the logic for our solvers is complete. We can start focusing on implementing the `guess` method in our solver subclasses.

### II. Manual Solver
Now, we focus on the most basic solver: the `ManualSolver`. This solver will actually not use any of the knowledge attributes; instead, it will rely on the user's input to make a guess.  

Update the `guess` method in `ManualSolver` to return the user's input as a guess. I.e, it should ask the user for input, and then return that.

### III. Random Solver
In this section, we focus on our first automated solver, the `RandomSolver`. This solver will simply choose a random word from the remaining list of valid words (which attribute stores this?). Once again, we can use `random.choice` (`random` library already imported).

### IV. Entropy Optimal Solver (BONUS)
The random solver is not always successful, and it is definitely not the most efficient in terms of number of guesses required. We can implement a far better solver by making better use of the knowledge we have.  

This video by 3Blue1Brown has more context:  
https://www.youtube.com/watch?v=v68zYyaEmEA&ab_channel=3Blue1Brown

## Part 3: Runner
Finally, we have to implement the `Runner`, which will take a solver, a filepath to a list of words, and run the `Wordle` game. The constructor for the `Runner` class is already implemented, and it should give enough context to implement the `run` method. Make sure to use the methods you implemented for `Wordle` and the solvers here; they will be very useful.

You can print out intermediate results of the game (i.e, what the solver predicts in each round, and what the feedback is) in the run method, so you can see the progress in the terminal. This part is quite flexible.

## Playing Wordle
Once the above parts are all implemented (correctly), we can run `python3 main.py --solver <solver_name>` to run the Wordle game with our solver of choice. Take a look at `main.py` to see the various other script arguments that can be passed in. If it's confusing, try asking ChatGPT to explain it.