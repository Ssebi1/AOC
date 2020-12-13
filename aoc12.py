import math

f = open('input.txt')

instructions = [(x[0],int(x[1:])) for x in f.readlines()]
f.close()

waypointX = 10
waypointY = 1

x = 0
y = 0

for instr in instructions:
    if instr[0] == 'N':
        waypointY += instr[1]
    elif instr[0] == 'S':
        waypointY -= instr[1]
    elif instr[0] == 'E':
        waypointX += instr[1]
    elif instr[0] == 'W':
        waypointX -= instr[1]
    elif instr[0] == 'L':
        n = instr[1] // 90
        for i in range(n):
            waypointX,waypointY = -waypointY,waypointX
    elif instr[0] == 'R':
        n = instr[1] // 90
        for i in range(n):
            waypointX,waypointY = waypointY,-waypointX
    elif instr[0] == 'F':
        x += instr[1]*waypointX
        y += instr[1]*waypointY

print(abs(x)+abs(y))