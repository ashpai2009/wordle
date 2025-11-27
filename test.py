from runner import Runner
from pathlib import Path
from solvers.random_solver import RandomSolver
from solvers.manual_solver import ManualSolver
#target word = hello

words = Path("/Users/ashmit/Documents/code/wordle/data/words.txt")
solver = RandomSolver(words)

runner = Runner(words, solver)

runner.run()

print(runner.wordle.target_word)