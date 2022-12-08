"""
https://adventofcode.com/2022/day/2#part2

X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
"""


# player_1_moves = {"A": "Rock", "B": "Paper", "C": "Scissors"}
# player_2_moves = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
# #                 Rock = LOSE   Paper = DRAW  Scissors = WIN

# Player 2's perspective
# game_moves = {
#     "A X": "draw",
#     "A Y": "win",
#     "A Z": "lose",
#     "B X": "lose",
#     "B Y": "draw",
#     "B Z": "win",
#     "C X": "win",
#     "C Y": "lose",
#     "C Z": "draw",
# }


# file_data = [x.split(" ") for x in file_data]


def calc_score():
    file_object = open("day_2_puzzle_input.txt", "r")
    file_data = file_object.read()
    file_data = file_data.split("\n")

    player_2_score = 0
    i = 0

    # Calculate the score
    for move in file_data:
        i += 1
        # Draw
        if move in ("A X", "B Y", "C Z"):
            print("DRAW Added 3 points")
            player_2_score += 3
        # Win
        elif move in ("A Y", "B Z", "C X"):
            print("WIN Added 6 points")
            player_2_score += 6
        # Lose
        elif move in ("A Z", "B X", "C Y"):
            print("LOSE Added 0 points")
            player_2_score += 0

        # Chose rock
        if "X" in move:
            print("ROCK Added 1 point")
            player_2_score += 1
        # Chose paper
        elif "Y" in move:
            print("PAPER Added 2 points")
            player_2_score += 2
        # Chose scissors
        elif "Z" in move:
            print("SCISSORS Added 3 points")
            player_2_score += 3

        print("===================================================")
        print(f"Current score is: {player_2_score } for move {i + 1}")
        print("===================================================")

    return player_2_score


total_score = calc_score()
print(total_score)

# for i in range(len(file_data)):
#     p1_move = player_1_moves[file_data[i][0]]
#     p2_move = player_2_moves[file_data[i][1]]


#     ## Get points for making a move
#     # Player 1
#     if p1_move == "Rock":
#         player_1_score += 1
#     elif p1_move == "Paper":
#         player_1_score += 2
#     elif p1_move == "Scissors":
#         player_1_score += 3

#     # Player 2
#     if p2_move == "Rock":
#         player_2_score += 1
#     elif p2_move == "Paper":
#         player_2_score += 2
#     elif p2_move == "Scissors":
#         player_2_score += 3

#     ## Scoring
#     if p2_move == "Paper":  # p2 Paper = DRAW
#         player_1_score += 3
#         player_2_score += 3
#     elif p2_move == "Scissors":  # p2 Scissors = WIN
#         player_1_score += 0
#         player_2_score += 6
#     elif p2_move == "Rock":  # p2 Rock = LOSE
#         player_1_score += 6
#         player_2_score += 0


# print(f"Player 1 score: {player_1_score}")
# print(f"Player 2 score: {player_2_score}")

# for player_2_move in game_moves:
#     # Draw
#     if move in ("A X", "B Y", "C Z"):
#         player_2_score += 3
#     # Win
#     elif move in player_2_move == "A Y" or "B Z" or "C X":
#         player_2_score += 6
#     # Lose
#     elif move == player_2_move == "A Z" or "B X" or "C Y":
#         player_1_score += 6
