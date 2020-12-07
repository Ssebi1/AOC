f = open('input.txt')

l = f.readlines()
finalSum = 0
colors = [("shiny gold",1)]
for color in colors:
    sum = 0
    for linie in l:
        if color[0] in linie:
            tempL = linie.split('contain')
            if tempL[0] == color[0] + " bags " and tempL[1]!=' no other bags.':
                tempColors = tempL[1].replace('bags', '').replace('bag', '').replace('.', '').replace('\n', '').split(',')
                for t in tempColors:
                    if t[1]!='n':
                        sum += int(t[1])
                        colors.append((t[3:-1],int(color[1])*int(t[1])))
                finalSum += int(color[1])*sum
print(colors)
print(finalSum)