from runner import Runner
from pathlib import Path
from solvers.random_solver import RandomSolver
from solvers.manual_solver import ManualSolver
#target word = hello

words = Path("/Users/ashmit/Documents/code/wordle/data/words.txt")
solver = RandomSolver(words)

runner = Runner(words, solver)


correct = 0
total = 100
attempts_per_win = []


for i in range(total):
    runner.run()

    if runner.wordle.guesses[-1] == runner.wordle.target_word:
        correct += 1

        attempts_per_win.append(len(runner.wordle.guesses))




percent = (correct/total) * 100

average_attempts = 0
for attempts in attempts_per_win:
    average_attempts += attempts

try:
    average_attempts = average_attempts/len(attempts_per_win)

except ZeroDivisionError:
    print("Your solver won 0 games...")
    
print(f"The solver scored {correct}/{total} which is {percent}%")
print(f"The solver averaged {average_attempts} per game won")

