# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

from colorama import  Fore

velocidade_carro = float(input('Digite a velocidade do seu carro: '))
multa = (velocidade_carro - 80) * 7

if velocidade_carro > 80.00:
    print(Fore.RED + 'Você está acima da velocidade e foi multado em R${:.2f}.'.format(multa))
else:
    print(Fore.GREEN + 'Você está dentro do limite de velocidade.')
