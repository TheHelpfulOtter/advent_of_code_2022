"""
https://adventofcode.com/2022/day/2

The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

player_1_moves = {"A": "Rock", "B": "Paper", "C": "Scissors"}
player_2_moves = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
player_1_score = 0
player_2_score = 0

file_object = open("day_2_puzzle_input.txt", "r")
file_data = file_object.read()
file_data = file_data.split("\n")
file_data = [x.split(" ") for x in file_data]

for i in range(len(file_data)):
    p1_move = player_1_moves[file_data[i][0]]
    p2_move = player_2_moves[file_data[i][1]]

    ## Get points for making a move
    # Player 1
    if p1_move == "Rock":
        player_1_score += 1
    elif p1_move == "Paper":
        player_1_score += 2
    elif p1_move == "Scissors":
        player_1_score += 3

    # Player 2
    if p2_move == "Rock":
        player_2_score += 1
    elif p2_move == "Paper":
        player_2_score += 2
    elif p2_move == "Scissors":
        player_2_score += 3

    ## Scoring
    if p1_move == p2_move:
        player_1_score += 3
        player_2_score += 3
    elif p1_move == "Rock" and p2_move == "Paper":
        player_1_score += 0
        player_2_score += 6
    elif p1_move == "Paper" and p2_move == "Scissors":
        player_1_score += 0
        player_2_score += 6
    elif p1_move == "Scissors" and p2_move == "Rock":
        player_1_score += 0
        player_2_score += 6
    elif p1_move == "Rock" and p2_move == "Scissors":
        player_1_score += 6
        player_2_score += 0
    elif p1_move == "Paper" and p2_move == "Rock":
        player_1_score += 6
        player_2_score += 0
    elif p1_move == "Scissors" and p2_move == "Paper":
        player_1_score += 6
        player_2_score += 0


print(f"Player 1 score: {player_1_score}")
print(f"Player 2 score: {player_2_score}")
