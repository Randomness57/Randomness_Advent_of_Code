def parse_stack_line(existing_stacks, new_line, num_stacks):
    for i in range(num_stacks):
        crate_type = new_line[i * 4 + 1]
        if crate_type != ' ':
            existing_stacks[i] = crate_type + existing_stacks[i]
    
    return existing_stacks

def count_stacks(lines):
    first_line = lines[0]
    num_stacks = round(len(first_line) / 4)
    return int(num_stacks)

def parse_move(line):
    parsing = line.split(' ')
    num_crates_to_move = int(parsing[1])
    initial_stack_num = int(parsing[3])
    final_stack_num = int(parsing [5])
    return num_crates_to_move, initial_stack_num, final_stack_num

def move_crates(stacks, line):
    num_crates_to_move, initial_stack_num, final_stack_num = parse_move(line)
    initial_stack = stacks[initial_stack_num - 1]
    final_stack = stacks[final_stack_num - 1]
    
    for i in range(num_crates_to_move):
        crate = initial_stack[-1]
        initial_stack = initial_stack[:-1]
        final_stack += crate
    
    stacks[initial_stack_num - 1] = initial_stack
    stacks[final_stack_num - 1] = final_stack
    return stacks

def move_crates_part_b(stacks, line):
    num_crates_to_move, initial_stack_num, final_stack_num = parse_move(line)
    initial_stack = stacks[initial_stack_num - 1]
    final_stack = stacks[final_stack_num - 1]

    crates = initial_stack[len(initial_stack) - num_crates_to_move:]
    final_stack += crates
    initial_stack = initial_stack[:-1*num_crates_to_move]

    stacks[initial_stack_num - 1] = initial_stack
    stacks[final_stack_num - 1] = final_stack
    return stacks

    
file = open('inputs\day_5.txt', 'r')
lines = file.readlines()

stacks_parsed = False
num_stacks = count_stacks(lines)
stacks = [None] * num_stacks
stacks_part_b = stacks
for i in range(num_stacks):
    stacks[i] = ''

for line in lines:

    if stacks_parsed == False and line[1].isdigit() == False:
        stacks = parse_stack_line(stacks, line, num_stacks)

    elif stacks_parsed == False:
        stacks_part_b = stacks.copy()
        stacks_parsed = True
    
    elif len(line) > 1:
        stacks = move_crates(stacks, line)
        stacks_part_b = move_crates_part_b(stacks_part_b, line)

top_crates_a = ''
top_crates_b = ''
for stack in stacks:
    top_crates_a += stack[-1]

    
for stack in stacks_part_b:
    top_crates_b += stack[-1]

print(top_crates_a)
print(top_crates_b)

file.close