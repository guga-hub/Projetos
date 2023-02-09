# Crie um programa que leia um número e mostre seu dobro, seu triplo
# e sua raíz quadrada.

num = float(input('Digite um valor: '))
dobro = num * 2
triplo = num*3
raiz_quadrada = num**(1/2)

print('O dobro desse numero é {}, o triplo é {} e a raíz quadrada é {:.3f}'. format(dobro, triplo, raiz_quadrada))