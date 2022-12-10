#part 1
f = open("input.txt", "r")
lines = f.readlines()
lines[0] = ''
lines[1] = ''
print(lines)

sum_apple_elf = []
sum_apple = 0

for i in lines:
    if i == '':
        continue
    elif i != '\n':
        sum_apple += int(i)
    else:
        sum_apple_elf.append(sum_apple)
        sum_apple = 0
#Answer :
#print(max(sum_apple_elf))



#part 2
sum_apple_elf.sort()
sum_apple_elf.reverse()

total_sum_3max_elves = sum_apple_elf[0] + sum_apple_elf[1] + sum_apple_elf[2]
#Answer :
#print(total_sum_3max_elves)
