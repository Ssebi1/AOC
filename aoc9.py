f = open('input.txt')

def calculateSums(list,start,end):
    sum = []
    for i in range(start,end):
        for j in range(i+1,end+1):
            sum.append(list[i]+list[j])
    return sum


def calculateInvalidNumber(preamble,list):
    for i in range(preamble, len(list)):
        sum = calculateSums(list, i - preamble, i + 1)
        if list[i] not in sum:
            return list[i]


def generatePartialSums(list):
    i = 1
    pSums = [0, list[0]]
    while i < len(list):
        pSums.append(list[i] + pSums[i])
        i += 1

    return pSums


def findSumInterval(pSums):
    j = len(pSums) - 1
    i = 0
    while i < len(pSums) - 1:
        if pSums[i] - pSums[j] == c:
            return j,i
        j -= 1
        if j < 0:
            j = len(pSums) - 1
            i += 1


def findMinMax(list,start,end):
    mini = 10 ** 9
    maxi = -1
    for i in range(start, end):
        if list[i] < mini:
            mini = list[i]
        if list[i] > maxi:
            maxi = list[i]
    return mini,maxi


list = [int(x.strip()) for x in f.readlines()]
f.close()

pSums = generatePartialSums(list)

c = calculateInvalidNumber(25,list)
print(c)


start,end = findSumInterval(pSums)
mini,maxi = findMinMax(list,start,end)
print(mini+maxi)
