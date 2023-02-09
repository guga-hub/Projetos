# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input('Digite o número do cateto oposto: '))
cateto_adjascente = float(input('Digite o número do cateto adjascente: '))

print('O número da hipotenusa desses dois catetos é {:4f}'.format(hypot(cateto_oposto, cateto_adjascente)))

