file = open('inputs\problem_1.txt', 'r')
lines = file.readlines()

highest_calories = 0
second = 0
third = 0
current_calories = 0

for line in lines:
    if line in ['\n', '\r\n']:
        if current_calories >= highest_calories:
            third = second
            second = highest_calories
            highest_calories = current_calories
        elif current_calories >= second:
            third = second
            second = current_calories
        elif current_calories >= third:
            third = current_calories
        current_calories = 0
    else:
        current_calories = current_calories + int(line)

print(highest_calories + second + third)

file.close