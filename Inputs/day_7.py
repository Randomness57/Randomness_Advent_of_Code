def find_no_repeats(line, num_characters):
    return 0


source_file = open('inputs\day_7.txt', 'r')
lines = source_file.readlines()

directories = [None]
directory_sizes =[0]
directory_parents = [0]
last_command = "$ cd /"
current_directory = 0

for line in lines:
    if line.rstrip() == "$ cd /":
        current_directory = 0

    elif line.rstrip() == "$ cd ..":
        current_directory = directory_parents[current_directory]

    elif line[0:4] == "$ cd":
        new_directory = line[5:-1].rstrip()
        current_directory = directories.index(new_directory + str(current_directory))

    elif line.rstrip() == "$ ls":
        last_command = "$ ls"

    elif line[0:3] == "dir":
        new_directory = line[4:-1].rstrip()
        directories.append(new_directory + str(current_directory))
        directory_sizes.append(0)
        directory_parents.append(current_directory)

    else:
        file = line.split(" ")
        size = int(file[0])
        directory_sizes[current_directory] += size
        traceback_directory = directory_parents[current_directory]
        if current_directory != 0:
            directory_sizes[traceback_directory] += size
            while traceback_directory != 0:
                traceback_directory = directory_parents[traceback_directory]
                directory_sizes[traceback_directory] += size

i = 0
total_size = 0
cutoff_size = 100000
for directory in directories:
    if directory_sizes[i] <= cutoff_size:
        total_size += directory_sizes[i]
    i += 1

print("part a: " + str(total_size))

size_to_cut = directory_sizes[0] - 40000000
smallest_yet = 40000000
directory_to_cut = directories[0]
i = 0

for size in directory_sizes:
    if size >= size_to_cut:
        if size < smallest_yet:
            smallest_yet = size
            directory_to_cut = directories[i]
    
    i += 1

print(smallest_yet)

source_file.close