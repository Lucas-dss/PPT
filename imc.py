temp = float(input("Seu IMC é: "))
# imc
if temp < 18.5:
  print("Baixo peso")
elif temp >= 18.5 and temp < 24.99:
  print("Normal")
elif temp >= 25 and temp < 29.99:
  print("Sobrepeso")
elif temp > 30:
  print("Obesidade")