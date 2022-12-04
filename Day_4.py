file = open('inputs\day_4.txt', 'r')
lines = file.readlines()

counter = 0

for line in lines:
    assignments = line.split(',')
    first_assignment = assignments[0].split('-')
    second_assignment = assignments[1].split('-')

    first_start = int(first_assignment[0])
    first_end = int(first_assignment[1])
    second_start = int(second_assignment[0])
    second_end = int(second_assignment[1])

    if first_start <= second_start and first_end >= second_end:
        counter += 1

    elif first_start >= second_start and first_end <= second_end:
        counter += 1

print(counter)

counter = 0

for line in lines:
    assignments = line.split(',')
    first_assignment = assignments[0].split('-')
    second_assignment = assignments[1].split('-')

    first_start = int(first_assignment[0])
    first_end = int(first_assignment[1])
    second_start = int(second_assignment[0])
    second_end = int(second_assignment[1])

    if first_start <= second_start and first_end >= second_start:
        counter += 1

    elif first_start >= second_start and first_start <= second_end:
        counter += 1

print(counter)

file.close