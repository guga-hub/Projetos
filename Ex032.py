# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano_bissexto = float(input('Digite o ano que deseja descobrir se é bissexto? Coloque 0 para analisar o ano atual:  '))
if ano_bissexto == 0:
    ano_bissexto = date.today().year
if ano_bissexto % 4 == 0 and ano_bissexto % 100 != 0 or ano_bissexto % 400 == 0:
    print('O ano {} é bissexto.'.format(ano_bissexto))
else:
    print('O ano {} não é bissexto.'.format(ano_bissexto))
