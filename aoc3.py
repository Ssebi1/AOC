f = open('input.txt')
ct = 0
i = 2
poz = 1+1
l = f.readline()
lungimeLinie = len(l)-1
# print(lungimeLinie)
for linie in f:
    if i%2==1:
        if linie[poz-1]=='#':
            ct+=1
            # print(i,linie,poz)
        poz+=1
        if poz>lungimeLinie:
            poz = int(poz%lungimeLinie)
    i+=1
print(ct)