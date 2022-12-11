def find_no_repeats(line, num_characters):
    length = len(line)

    for i in range(length - num_characters + 1):
        #print(i)
        x = set(line[i:i+num_characters])
        #print(x)
        if len(x) == num_characters:
            return i + num_characters
            break
    return 0


file = open('inputs\day_6.txt', 'r')
lines = file.readlines()

for line in lines:
    num_characters = 4
    print(find_no_repeats(line, num_characters))
    num_characters = 14
    print(find_no_repeats(line, num_characters))

file.close