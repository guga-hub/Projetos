# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
# e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que desejar: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O angulo de {}º corresponde a: {:.4f} cos, {:.4f} sen, {:.4f} tan.'.format(angulo, seno, cosseno, tangente))
