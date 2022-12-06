input_file = open("input.txt")
file_contents = input_file.read()
contents_split = file_contents.splitlines()

input_file.close()

def decide_winner(str):
    # A = Rock B = Paper C = Scissors
    # X = Rock Y = Paper Z = Scissors
    # Win = 6 Points Draw = 3 Point Lose = 0 Points
    opponent = str.split()[0]
    player = str.split()[1]
    if opponent == 'A' and player == 'Y':
        return 6
    elif opponent == 'A' and player == 'X':
        return 3
    elif opponent == 'B' and player == 'Z':
        return 6
    elif opponent == 'B' and player == 'Y':
        return 3
    elif opponent == 'C' and player == 'X':
        return 6
    elif opponent == 'C' and player == 'Z':
        return 3
    else:
        return 0

def decide_move(str):
    # A = Rock B = Paper C = Scissors
    # X = Lose Y = Draw Z = Win
    # Rock = 1 Points Paper = 2 Point Scissors = 3 Points
    opponent = str.split()[0]
    result = str.split()[1]
    if opponent == 'A' and result == 'X':
        return 3
    if opponent == 'A' and result == 'Y':
        return 1
    if opponent == 'A' and result == 'Z':
        return 2
    if opponent == 'B' and result == 'X':
        return 1
    if opponent == 'B' and result == 'Y':
        return 2
    if opponent == 'B' and result == 'Z':
        return 3
    if opponent == 'C' and result == 'X':
        return 2
    if opponent == 'C' and result == 'Y':
        return 3
    if opponent == 'C' and result == 'Z':
        return 1


# Part 1
score = 0
for str in contents_split:
    score += decide_winner(str)
    if str.split()[1] == 'X':
        score += 1
    elif str.split()[1] == 'Y':
        score += 2
    elif str.split()[1] == 'Z':
        score += 3

print(score)

# Part 2
score = 0 
for str in contents_split:
    score += decide_move(str)
    if str.split()[1] == 'X':
        score += 0
    elif str.split()[1] == 'Y':
        score += 3
    elif str.split()[1] == 'Z':
        score += 6

print(score)


