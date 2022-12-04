file = open('inputs\day_2.txt', 'r')
lines = file.readlines()

score = 0

for line in lines:
    moves = line.split()
    opp_move = moves[0]
    my_move = moves[1]
    if opp_move == 'A':
        if my_move == 'X':
            score = score + 4
        elif my_move == 'Y':
            score = score + 8
        elif my_move == 'Z':
            score = score + 3
    elif opp_move == 'B':
        if my_move == 'X':
            score = score + 1
        elif my_move == 'Y':
            score = score + 5
        elif my_move == 'Z':
            score = score + 9
    elif opp_move == 'C':
        if my_move == 'X':
            score = score + 7
        elif my_move == 'Y':
            score = score + 2
        elif my_move == 'Z':
            score = score + 6

print(score)
score = 0

for line in lines:
    moves = line.split()
    opp_move = moves[0]
    my_move = moves[1]
    if opp_move == 'A':
        if my_move == 'X':
            score = score + 3
        elif my_move == 'Y':
            score = score + 4
        elif my_move == 'Z':
            score = score + 8
    elif opp_move == 'B':
        if my_move == 'X':
            score = score + 1
        elif my_move == 'Y':
            score = score + 5
        elif my_move == 'Z':
            score = score + 9
    elif opp_move == 'C':
        if my_move == 'X':
            score = score + 2
        elif my_move == 'Y':
            score = score + 6
        elif my_move == 'Z':
            score = score + 7

print(score)

file.close