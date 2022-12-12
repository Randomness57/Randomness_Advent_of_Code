def check_horizontal(trees, i, j):
    visible_left = True
    visible_right = True
    tree_height = trees[i][j]
    width = len(trees)
    x_pos = i
    while x_pos > 0:
        x_pos = x_pos - 1
        if trees[x_pos][j] >= tree_height:
            visible_left = False
            break
        
    x_pos = i
    while x_pos < width - 1:
        x_pos = x_pos + 1
        if trees[x_pos][j] >= tree_height:
            visible_right = False
            break

    return visible_left or visible_right

def check_vertical(trees, i, j): 
    visible_up = True
    visible_down = True
    tree_height = trees[i][j]
    length = len(trees[i][:])
    y_pos = j

    while y_pos > 0:
        y_pos = y_pos - 1
        if trees[i][y_pos] >= tree_height:
            visible_up = False
            break
        
    y_pos = j
    while y_pos < length - 1:
        y_pos = y_pos + 1
        if trees[i][y_pos] >= tree_height:
            visible_down = False
            break

    return visible_up or visible_down


file = open('inputs\day_8.txt', 'r')
lines = file.readlines()
width = len(lines[0]) - 1
length = len(lines)
tree_array = [[0 for i in range(width)] for j in range(length)]

for i in range(width):
    for j in range(length):
        tree_array[i][j] = int(lines[i][j])

visible_trees = 0
for i in range(width):
    for j in range(length):
        if check_horizontal(tree_array, i, j) or check_vertical(tree_array, i, j):
            visible_trees += 1

print("part a: " + str(visible_trees))

current_best_scenic = 0

for i in range(width):
    for j in range(length):
        left = 0
        right = 0
        up = 0
        down = 0
        height = tree_array[i][j]

        for k in range(i):
            left += 1
            if height <= tree_array[i - k - 1][j]:
                break

        for k in range(i, length - 1):
            right += 1
            if height <= tree_array[k + 1][j]:
                break

        for k in range(j):
            up += 1
            if height <= tree_array[i][j - k - 1]:
                break

        for k in range(j, width - 1):
            down += 1
            if height <= tree_array[i][k+1]:
                break

        scenic_score = left * right * up * down
        if scenic_score > current_best_scenic:
            current_best_scenic = scenic_score

print("part b: " + str(current_best_scenic))

file.close