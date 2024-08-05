temp = int(input("Digite a temperatura atual: "))
vel = int(input("Digite a velocidade do vento (km/h): "))
# temperatura
'''
Lucas
'''
if temp <25:
  print("Frio")
elif temp >= 25 and temp < 30:
  print("Agradável")
elif temp >= 30:
  print("Calorzão Parça")

# vento
if vel < 89:
  print("Normal")
elif vel >= 89 and vel < 103:
  print("Tempestade")
elif vel >= 103 and vel < 118:
  print("Tempestade Violenta")
elif vel > 118:
  print("Furacão")