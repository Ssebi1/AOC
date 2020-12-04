f = open('input.txt')

def checkFullandValid(dictionary):
    info = [0] * 7

    if 'byr' in dictionary:
        if int(dictionary['byr'])>=1920 and int(dictionary['byr'])<=2002:
            info[0]=1
    if 'iyr' in dictionary:
        if int(dictionary['iyr']) >= 2010 and int(dictionary['iyr']) <= 2020:
            info[1] = 1
    if 'eyr' in dictionary:
        if int(dictionary['eyr']) >= 2020 and int(dictionary['eyr']) <= 2030:
            info[2] = 1
    if 'hgt' in dictionary:
        ok = 1
        for char in dictionary['hgt'][:-2]:
            if char>='0' and char<='9':
                continue
            else:
                ok=0
                break;
        if ok==1 and len(dictionary['hgt'])>2:
            height = int(dictionary['hgt'][:-2])
            if dictionary['hgt'][-2]=='c' and dictionary['hgt'][-1]=='m' and height>=150 and height<=193:
                info[3] = 1
            elif dictionary['hgt'][-2]=='i' and dictionary['hgt'][-1]=='n' and height>=59 and height<=76:
                info[3] = 1
    if 'hcl' in dictionary:
        if dictionary['hcl'][0]=='#' and len(dictionary['hcl'])==7:
            ok=1
            for i in range(1,7):
                if (dictionary['hcl'][i]>='0' and dictionary['hcl'][i]<='9') or (dictionary['hcl'][i]>='a' and dictionary['hcl'][i]<='f'):
                    continue
                else:
                    ok=0
                    break
            if ok==1:
                info[4] = 1
    if 'ecl' in dictionary:
        if dictionary['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
            info[5] = 1
    if 'pid' in dictionary:
        if len(dictionary['pid'])==9:
            ok = 1
            for char in dictionary['pid']:
                if char>='0' and char<='9':
                    continue
                else:
                    ok = 0
                    break
            if ok == 1:
                info[6] = 1

    p = 1
    for i in info:
        p *= i
    if p == 1:
        return 1


ct = 0

data = []
for linie in f:
    if linie[0]=='\n':
        ddata = {data[i][0]:data[i][1] for i in range(len(data))}
        if checkFullandValid(ddata):
            ct+=1
        data = []
        ddata = {}


    else:
        linie = linie.split()
        for i in range(len(linie)):
            linie[i] = linie[i].split(':')
        data += linie

ddata = {data[i][0]:data[i][1] for i in range(len(data))}
if checkFullandValid(ddata):
    ct += 1
print(ct)