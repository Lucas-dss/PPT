from math import *
from random import *

sorteado = randrange(1,7)
escolhido = int(input("Digite a sorte do dado: "))
print("O número sorteado foi:", sorteado)

if escolhido == sorteado:
    print("Campeão!1!\n")
else:
    print("Fracassado\n")