 # Exercício Python 12: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.ano = int(input("Digite um ano: "))
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")
