f = open('input.txt')
c = set()

L = list(l.strip() for l in f.readlines())
for i,l in enumerate(L):
    for j,ch in enumerate(l):
        if ch=='#':
            c.add((i,j,0,0))

f.close()

for i in range(6):
    new_c = set()
    for x in range(-15,15):
        for y in range(-15,15):
            for z in range(-8,8):
                for w in range(-8,8):
                    nb = 0
                    for dx in [-1,0,1]:
                        for dy in [-1,0,1]:
                            for dz in [-1,0,1]:
                                for dw in [-1,0,1]:
                                    if dx!=0 or dy!=0 or dz!=0 or dw!=0:
                                        if (x+dx,y+dy,z+dz,w+dw) in c:
                                            nb+=1
                    if (x,y,z,w) not in c and nb == 3:
                        new_c.add((x,y,z,w))
                    if (x,y,z,w) in c and nb in [2,3]:
                        new_c.add((x,y,z,w))
    c = new_c

print(len(c))