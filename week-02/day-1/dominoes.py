from domino import Domino
def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes
dominoes = initialize_dominoes()
print(dominoes)
list_1 = list(map(lambda x: x, dominoes))
print(list_1)
print(type(list_1[0]))
a = [list_1[0]]
j = 0
while j < len(list_1) - 1:
        for i in range(len(list_1)):
                cc = a[-1].values[1]
                bb = list_1[i].values[0]
                if cc == bb:
                        a.append(list_1[i])
                        j += 1
print(a)