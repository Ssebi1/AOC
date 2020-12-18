f = open('input.txt')

def calculateParantheses(calc):
    i = 0
    while i < len(calc):
        if calc[i] == '(':
            start = i
            end = start+1
            while end < len(calc) and calc[end]!='(' and calc[end]!=')':
                end+=1
            if end < len(calc) and calc[end]==')':
                calc = calc[:start] + calculate(calc,start,end) + calc[end+1:]
        i+=1
    return calc


def calculate(calc,start,end):
        eq = calc[start+1:end]
        pos = eq.find('+')
        while pos!=-1:
            i = pos-2
            while i>0 and eq[i]>='0' and eq[i]<='9':
                i-=1
            p1 = i
            nr1 = int(eq[i:pos-1])
            i = pos + 2
            while i<len(eq) and eq[i] >= '0' and eq[i] <= '9':
                i += 1
            p2 = i
            nr2 = int(eq[pos+2:i])
            sum = nr1+nr2
            eq = eq[:p1] + ' ' + str(sum) + eq[p2:]
            pos = eq.find('+')
        p = 1
        eq = eq.split()

        for x in eq:
            if x!='*' and x!=' ':
                p*=int(x)
        return str(p)


def calculateSum():
    s = 0
    for calc in f:
        calc = calc.strip()
        while calc.find('(') != -1:
            calc = calculateParantheses(calc)
        result = calculate(calc, -1, len(calc))
        s += int(result)
        print(result)
    return s


print(calculateSum())