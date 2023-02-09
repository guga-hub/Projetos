# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com
# 15% de aumento.

salario = float(input('Qual é seu salário atual: R$'))
aumento = salario + (salario*(15/100))

print('O seu novo salario com aumento é: R${}.'.format(aumento))

