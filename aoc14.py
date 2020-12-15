f = open('input.txt')

mem = [0]*100001
mask1 = mask2 = 0
for linie in f.readlines():
    if 'mask' in linie:
        mask = linie.split()[2].strip()
        mask1 = mask.replace('X', '0')
    else:
        number = int(linie.split()[2].strip())
        position = int(linie.split()[0][4:-1])
        position = position | int(mask1,2)
        print(position)

print(sum(mem))



