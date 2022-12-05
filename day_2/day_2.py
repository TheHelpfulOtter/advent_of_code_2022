"""
https://adventofcode.com/2022/day/2

The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

player_1 = {"A": "Rock", "B": "Paper", "C": "Scissors"}

player_2 = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

rounds = [
    [player_1["A"], player_2["Y"]],
    [player_1["B"], player_2["X"]],
    [player_1["C"], player_2["Z"]],
]

player_1_score = 0
player_2_score = 0

for i in range(len(rounds)):
    # Get score for move choice
    if rounds[i][0] == "Rock":
        player_1_score += 1
    elif rounds[i][0] == "Paper":
        player_1_score += 2
    elif rounds[i][0] == "Scissors":
        player_1_score += 3

    if rounds[i][1] == "Rock":
        player_2_score += 1
    elif rounds[i][1] == "Paper":
        player_2_score += 2
    elif rounds[i][1] == "Scissors":
        player_2_score += 3

    # Get win loss score


print(player_1_score)
print(player_2_score)
