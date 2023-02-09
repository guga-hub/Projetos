# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar. Considere U$1,00 = R$3,27.

reais = float(input('Digite quanto tem atualmente em reais: '))
quantidade_de_dolares = reais / 3.27

print('Com esse dinheiro você consegue comprar U${:.3f}'.format(quantidade_de_dolares))
