f = open('input.txt')

s = set()
ft = []
fline = f.readline()
while fline != '\n':
    fline = fline.strip().replace('or','').split()
    fline = [*fline[-2].split('-'),*fline[-1].split('-')]
    fline = [int(fline[0]),int(fline[1]),int(fline[2]),int(fline[3])]
    ft.append((fline[0],fline[1]))
    ft.append((fline[2],fline[3]))
    for i in range(fline[0], fline[1] + 1):
        s.add(i)
    for i in range(fline[2], fline[3] + 1):
        s.add(i)
    fline = f.readline()


print(ft)
f.readline()
myTicket = f.readline().strip()

f.readline()
f.readline()
tickets = [tuple(int(k) for k in x.strip().split(',')) for x in f.readlines()]

f.close()

i=0
while i < len(tickets):
    for t in tickets[i]:
        if t not in s:
            tickets.pop(i)
            i-=1
            break
    i+=1

print(tickets)
mm = []
ok=1
vok = [0]*20
for i in range(0,len(ft),2):
    for j in range(len(tickets[0])):
        ok = 1
        for t in tickets:
            if (t[j]>=ft[i][0] and t[j]<=ft[i][1]) or (t[j]>=ft[i+1][0] and t[j]<=ft[i+1][1]):
                continue
            else:
                ok=0
        if ok==1 and int(i/2)+1 not in vok:
            vok[j]=int(i/2)+1

print(vok)