import os

opcao = input("Digite\n(1) - Paint\n(2) - Calculadora\n(3) - Bloco de Notas\n")

if opcao == "1":
    os.system("mspaint")
if opcao == "2":
    os.system("calc")
if opcao == "3":
    os.system("notepad")