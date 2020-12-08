f = open('input.txt')

instr = [[x.split()[0],int(x.split()[1])] for x in f.readlines()]
print(instr)

def verif_loop(instr):
    visited = [0] * len(instr)
    code = 0
    i = 0
    while i < len(instr) and visited[i] != 1:
        if instr[i][0] == 'acc':
            code += instr[i][1]
            visited[i] = 1
            i += 1
        elif instr[i][0] == 'nop':
            visited[i] = 1
            i += 1
        elif instr[i][0] == 'jmp':
            visited[i] = 1
            i += instr[i][1]

    return code,i


code = 0
for i in range(len(instr)-1,0,-1):
    if instr[i][0]=='jmp':
        instr[i][0]='nop'
        code,j = verif_loop(instr)
        if j >= len(instr):
            print(code,j,len(instr))
            break
        else:
            instr[i][0] = 'jmp'

