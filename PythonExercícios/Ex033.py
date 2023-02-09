# Faça um programa que leia três números e mostre qual é o maior e qual
# é o menor.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

# ESTRUTURA ANINHADA
# if num1 > num2 > num3:
#     print('O maior número dentre os três é o primeiro: {}'.format(num1))
# elif num2 > num3 > num1:
#     print('O maior número dentre os três é o segundo: {}'.format(num2))
# elif num3 > num2 > num1:
#     print('O maior número dentre os três é o terceiro: {}'.format(num3))
#
# if num1 < num2 < num3:
#     print('O menor número dentre os três é o primeiro: {}'.format(num1))
# elif num2 < num3 < num1:
#     print('O menor número dentre os três é o segundo: {}'.format(num2))
# elif num3 < num2 < num1:
#     print('O menor número dentre os três é o terceiro: {}'.format(num3))

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior= num3
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))