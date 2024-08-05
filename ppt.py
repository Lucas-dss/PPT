from math import *
from random import *

sorteado = randrange(1,4)
escolhido = int(input("Digite \n(1) - pedra\n (2) - papel\n (3) - tesoura\n"))
print("A máquina escolheu:", sorteado)

if escolhido == 1 and sorteado == 3:
    print("Pedra vence de Tesoura\nCampeão!1!\n")

if escolhido == 2 and sorteado == 1:
    print("Papel vence de Pedra\nCampeão!1!\n")

if escolhido == 3 and sorteado == 2:
    print("Tesoura vence de Papel\nCampeão!1!\n")

if escolhido == 1 and sorteado == 2:
    print("Pedra perde de Papel\nFracassado.\n")

if escolhido == 2 and sorteado == 3:
    print("Papel perde de Tesoura\nFracassado.\n")

if escolhido == 3 and sorteado == 1:
    print("Tesoura perde de Pedra\nFracassado.\n")

if escolhido == sorteado:
    print("Deu empate :/\n")

if escolhido > 3 or escolhido < 1:
    print("Isso não é válido besta\n")