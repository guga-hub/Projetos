# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador.
# O Programa deverá escever na tela se o usuário venceu ou perdeu.
#print('Vou escolher um número de 0 à 5, se prepare...')

# from random import choice
# numeros_possiveis = [0, 1, 2, 3, 4, 5]
# aleatorio = choice(numeros_possiveis)
#
# numero_usuario = int(input('Digite o número que acha que eu escolhi: '))
#
# if numero_usuario == aleatorio:
#     print('Você acertou (Dessa vez), parabéns!')
# else:
#     print('Sinto muito, mas você errou hahaha... ')

from random import randint
from time import sleep
computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('\033[1;32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[1;31mGANHEI! Eu pensei no número '
          '\033[1;34m{}'
          '\033[m \033[1;31me nao no '
          '\033[1;36m{}!'.format(computador, jogador))
