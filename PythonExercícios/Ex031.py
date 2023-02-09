# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até
# 200Km e R$0,45 para viagens mais longas.
from typing import Tuple

km_viagem = float(input('Digite a distância da sua viagem: '))

# if km_viagem <= 200:
#     preco = km_viagem * 0.50
# else:
#     preco = km_viagem * 0.45
print('O preço da sua viagem ficará em: R${:.2f}'.format(preco))