import math
f = open('input.txt')

def calculateSeatId(ticket):
    left = 0
    right = 127
    for i in range(0, 7):

        if ticket[i] == 'F':
            mid = int((left + right) / 2)
            right = mid
        elif ticket[i] == 'B':
            mid = round((left + right) / 2)
            left = mid
    if ticket[6] == 'F':
        row = left
    else:
        row = right

    left = 0
    right = 7
    for i in range(6, 9):

        if ticket[i] == 'L':
            mid = int((left + right) / 2)
            right = mid
        elif ticket[i] == 'R':
            mid = round((left + right) / 2)
            left = mid

    if ticket[9] == 'L':
        column = left
    else:
        column = right
    return row*8+column;



maxi = 930
l=[]
for ticket in f:
    id = calculateSeatId(ticket)
    l.append(id)
l.sort()
lung = len(l)
for i in range(1,lung-1):
    if l[i]!=l[i+1]-1:
        print(l[i]+1)
        break

print(l)
