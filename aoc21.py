f = open('input.txt')

def read_data():
    list = [x.strip() for x in f.readlines()]
    dict = {}
    for linie in list:
        l = linie.split('(')
        l[0] = l[0][:-1].split()
        l[1] = l[1].replace(')','').replace('contains','')[1:].split(',')
        l[1] = [s.strip() for s in l[1]]
        print(l)

        for el in l[1]:
            if el in dict:
                for food in l[0]:
                    dict[el].add(food)
            else:
                dict[el] = set()
                for food in l[0]:
                    dict[el].add(food)

    print(dict)
    f.close()


read_data()