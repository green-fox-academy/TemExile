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

a = []
for i in range(len(dominoes)):
    b = []
    c = dominoes
    b.append(c[i])
    c.pop(i)
    for j in range(len(c)):
        if b[j][1] == c[]
