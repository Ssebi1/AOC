f = open('input.txt')

l = f.readlines()
colors = []
finalSum = 0
for linie in l:
    if "shiny gold" in linie:
        tempL = linie.split('contain')
        if tempL[0]=="shiny gold bags ":
            tempL[1] = tempL[1].replace('bags','')
            tempL[1] = tempL[1].replace('bag','')
            tempL[1] = tempL[1].replace('.','')
            tempL[1] = tempL[1].replace('\n','')
            tempColors = tempL[1].split(',')
            for t in tempColors:
                colors.append((t[3:-1],t[1]))
                finalSum += int(t[1])
values = []
sum = 0
for color in colors:
    sum = 0
    for linie in l:
        if color[0] in linie:
            tempL = linie.split('contain')
            if tempL[0] == color[0] + " bags " and tempL[1]!=' no other bags.':
                tempL[1] = tempL[1].replace('bags', '')
                tempL[1] = tempL[1].replace('bag', '')
                tempL[1] = tempL[1].replace('.', '')
                tempL[1] = tempL[1].replace('\n', '')
                tempColors = tempL[1].split(',')
                for t in tempColors:
                    if t[1]!='n':
                        sum += int(t[1])
                        colors.append((t[3:-1],int(color[1])*int(t[1])))
                print(sum)
                finalSum += int(color[1])*sum
print(colors)
print(finalSum)