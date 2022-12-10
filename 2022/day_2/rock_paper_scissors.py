#part 1
file = open("input.txt", "r")

lines = file.readlines()
col = []

win = 6
draw = 3
lose = 0
rock = 1
paper = 2
scissors = 3

for i in lines:
    col.append(i.split())

sum_score = 0

for i in col:
    if i[1] == 'X':
        sum_score += rock
    elif i[1] == 'Y':
        sum_score += paper
    else:
        sum_score += scissors
        
    if i[0] == 'A':
        if i[1] == 'X':
            sum_score += draw
        elif i[1] == 'Y':
            sum_score += win
        else:
            sum_score += lose
    elif i[0] == 'B':
        if i[1] == 'X':
            sum_score += lose
        elif i[1] == 'Y':
            sum_score += draw
        else:
            sum_score += win
    elif i[0] == 'C':
        if i[1] == 'X':
            sum_score += win
        elif i[1] == 'Y':
            sum_score += lose
        else:
            sum_score += draw

#Answer :
#print(sum_score)


#part 2
sum_score = 0
for i in col:
    if i[0] == 'A':
        if i[1] == 'X':
            sum_score += lose
            sum_score += scissors
        elif i[1] == 'Y':
            sum_score += draw
            sum_score += rock
        else:
            sum_score += win
            sum_score += paper
    elif i[0] == 'B':
        if i[1] == 'X':
            sum_score += lose
            sum_score += rock
        elif i[1] == 'Y':
            sum_score += draw
            sum_score += paper
        else:
            sum_score += win
            sum_score += scissors
    else:
        if i[1] == 'X':
            sum_score += lose
            sum_score += paper
        elif i[1] == 'Y':
            sum_score += draw
            sum_score += scissors
        else:
            sum_score += win
            sum_score += rock

#Answer :
#print(sum_score)
