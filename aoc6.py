f = open('input.txt')

def clearArray(array):
    for i in range(ord('a'),ord('z')+1):
        array[i]=0
    return array


fa = [0]*130
nrLinii=0
ct=0
for linie in f:
    if linie[0]=='\n':
        print(fa[ord('a'):ord('z')+1])
        if nrLinii != 0:
            for i in range(ord('a'),ord('z')+1):
                if fa[i]==nrLinii:
                    ct+=1
        fa = clearArray(fa)
        nrLinii = 0
    else:
        nrLinii+=1
        for i in range(0,len(linie)):
            if linie[i]>='a' and linie[i]<='z':
                if linie.count(linie[i],i)==1:
                    fa[ord(linie[i])]+=1

print(ct)