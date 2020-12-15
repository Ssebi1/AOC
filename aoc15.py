f = open('input.txt')
values = f.readline().strip().split()
list = [(int(x),-1,i) for i,x in enumerate(values)] #list = [(valoare,penultimaPoz,ultimaPoz)]
spoken = [-1]*30000000
for t in list:
    spoken[t[0]]=t[2]
while len(list)<30000000:
    if list[-1][1]==-1:
        list.append((0,spoken[0],len(list)))
        spoken[0]=len(list)-1
    else:
        list.append((list[-1][2]-list[-1][1],spoken[list[-1][2]-list[-1][1]],len(list)))
        spoken[list[-2][2]-list[-2][1]]=len(list)-1

print(list[29999999])