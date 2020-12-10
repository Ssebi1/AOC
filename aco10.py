f = open('input.txt')

v = [0]
v += [int(x) for x in f.readlines()]
v.sort()
v.append(v[-1]+3)
print(v)

f.close()

DP = {}
def dp(i):
    if i==len(v)-1:
        return 1
    if i in DP:
        return DP[i]
    rez = 0
    for j in range(i+1,len(v)):
        if v[j]-v[i]<=3:
            rez+=dp(j)
    DP[i]=rez
    return rez


print(dp(0))