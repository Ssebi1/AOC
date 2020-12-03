f = open('input.txt')

ct=0

s = f.readlines()
for el in s:
    el.replace('\n','')
    linie = el.split()
    numbers = linie[0].split('-')
    if len(linie[2])>=int(numbers[1]):
        ap = 0
        if linie[2][int(numbers[0])-1]==linie[1][0]:
            ap+=1
        if linie[2][int(numbers[1])-1]==linie[1][0]:
            ap+=1
        if ap==1:
            ct+=1
    print(numbers[0],numbers[1],linie[1][0],linie[2])

print(ct)

