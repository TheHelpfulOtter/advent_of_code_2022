"""
https://adventofcode.com/2022/day/1#part2
"""

num_list = []
current_value = 0
first_value = 0
second_value = 0
third_value = 0

# Open and read the text file
file_object = open("day_1_puzzle_input.txt", "r")
file_data = file_object.read()
file_data = file_data.split("\n\n")

# Text is separated by /n, remove and add to list
for text_block in file_data:
    text_block = text_block.replace("\n", ",")
    num_list.append(text_block)

# Since the text is still one giant string, split the string into individual elements and then sum() them
for i in range(len(num_list)):
    num_list[i] = num_list[i].split(",")

    # Remove blank string elements at the end of an element
    if num_list[i][-1] == "":
        num_list[i].pop()

    # Convert string values into int using list comprehension
    num_list[i] = [int(item) for item in num_list[i]]

    # Sum the values and replace if it is larger
    current_value = sum(num_list[i])

    # Compare values and assign
    if current_value > first_value:
        first_value = current_value
    elif current_value < first_value and current_value >= second_value:
        second_value = current_value
    elif current_value < second_value and current_value >= third_value:
        third_value = current_value

total_calories = first_value + second_value + third_value

print(f"The top 3 elves' total calories are {total_calories}.")
