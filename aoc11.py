import copy

f = open('input.txt')
list = [[c for c in x.strip()] for x in f.readlines()]
f.close()

def countOccupied(list,i,j):
    ct=0
    n = len(list)
    m = len(list[0])

    # Horizontal
    for k in range(j-1, -1,-1):
        if list[i][k] == 'L':
            break
        elif list[i][k] == '#':
            ct += 1
            break
    for k in range(j + 1, m):
        if list[i][k] == 'L':
            break
        elif list[i][k] == '#':
            ct += 1
            break

    # Vertical
    auxList = [list[k][j] for k in range(0,n)]
    for k in range(i-1,-1,-1):
        if auxList[k]=='L':
            break
        elif auxList[k]=='#':
            ct+=1
            break
    for k in range(i+1, n):
        if auxList[k] == 'L':
            break
        elif auxList[k] == '#':
            ct += 1
            break

    # Diagonal 1
    o = i-1
    p = j-1
    while o>=0 and p>=0:
        if list[o][p]=='L':
            break
        if list[o][p]=='#':
            ct+=1
            break
        o-=1
        p-=1

    o = i+1
    p = j+1
    while o < n and p < m:
        if list[o][p]=='L':
            break
        if list[o][p] == '#':
            ct += 1
            break
        o += 1
        p += 1

    # Diagonal 2
    o = i-1
    p = j+1
    while o >= 0 and p < m:
        if list[o][p]=='L':
            break
        if list[o][p] == '#':
            ct += 1
            break
        o -= 1
        p += 1

    o = i+1
    p = j-1
    while o < n and p >= 0:
        if list[o][p]=='L':
            break
        if list[o][p] == '#':
            ct += 1
            break
        o += 1
        p -= 1

    return ct


def countSeats(list):
    ct=0
    for i in range(0,len(list)):
        for j in range(0,len(list[0])):
            if list[i][j]=='#':
                ct+=1
    return ct

while True:
    copyList = copy.deepcopy(list)
    for i in range(0,len(list)):
        for j in range(0,len(list[0])):
            if list[i][j]=='L' and countOccupied(copyList,i,j) == 0:
                list[i][j]='#'
            elif list[i][j]=='#' and countOccupied(copyList,i,j) >=5:
                list[i][j]='L'
    ok = 1
    for i in range(0,len(list)):
        if list[i]!=copyList[i]:
            ok=0
    if ok == 1:
        break


print(*list,sep='\n')
print(countSeats(list))