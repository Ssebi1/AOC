f = open('input.txt')
s = [int(x) for x in f.readlines()]
print(s)

for i in range(0,len(s)-2):
    for j in range(i+1,len(s)-1):
        for k in range(j + 1, len(s)):
            if s[i]+s[j]+s[k]==2020:
                print(s[i],s[j],s[k])
                print(s[i]*s[j]*s[k])
                break