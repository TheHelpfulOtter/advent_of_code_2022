"""
https://adventofcode.com/2022/day/2#part2

X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

Ans 12683

current 12836

Very confusingly phrased question:
Basically, if the second column is X, you have to lose. Y, you have to draw, Z, you have to win

This means that you need to pick the piece that will cause the win, draw, or loss. REGARDLESS of what was said in part 1
e.g X = rock, Y = paper, Z = scissors
throw it away

So if the opponent chooses rock, and you have a Z, this means you need to win. So to win, you have to choose 
"""


def calc_score():
    file_object = open("day_2_puzzle_input.txt", "r")
    file_data = file_object.read()
    file_data = file_data.split("\n")

    player_2_score = 0

    # Calculate the score
    for move in file_data:
        # X is Lose
        if "X" in move:
            if move == ("A X"):  # Opp. chose rock, so you must choose scissors
                player_2_score += 0 + 3
            elif move == ("B X"):  # Opp. chose paper, so you must choose rock
                player_2_score += 0 + 1
            elif move == ("C X"):  # Opp. chose scissors, so you must choose paper
                player_2_score += 0 + 2

        # Y is draw
        if "Y" in move:
            if move == ("A Y"):
                player_2_score += 3 + 1
            elif move == ("B Y"):
                player_2_score += 3 + 2
            elif move == ("C Y"):
                player_2_score += 3 + 3

        # Z is win
        if "Z" in move:
            if move == ("A Z"):
                player_2_score += 6 + 2
            elif move == ("B Z"):
                player_2_score += 6 + 3
            elif move == ("C Z"):
                player_2_score += 6 + 1

    return player_2_score


total_score = calc_score()
print(total_score)
