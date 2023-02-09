#Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço com 5% de desconto.

preco = float(input('Digite o valor para descontar 5%:' ))
desc = preco - (preco*(5/100))

print('O preço com desconto de 5% fica {}'.format(desc))