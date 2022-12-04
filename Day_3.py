file = open('inputs\day_3.txt', 'r')
lines = file.readlines()

priority_sum = 0
br = False

for line in lines:
    length = int(len(line) / 2)
    for i in range(0, length):
        for j in range(length, 2 * length):
            if line[i] == line[j]:
                if(ord(line[i]) < 96):
                    priority_sum = priority_sum + ord(line[i]) - 38

                else:
                    priority_sum = priority_sum + ord(line[i]) - 96

                br = True
                break

        if br == True:
            br = False
            break

print(priority_sum)

num_groups = int(len(lines) / 3)
print(num_groups)
priority_sum = 0

for i in range(0, num_groups):
    br = False
    first = lines[3 * i]
    second = lines[3 * i + 1]
    third = lines[3 * i + 2]
    for j in range(65, 91):
        if chr(j) in first and chr(j) in second and chr(j) in third:
            priority_sum = priority_sum + j - 38
            br = True
            break



    for j in range(97, 123):
        if br == True:
            br = False
            break
        if chr(j) in first and chr(j) in second and chr(j) in third:
            priority_sum = priority_sum + j - 96
            break

print(priority_sum)

file.close