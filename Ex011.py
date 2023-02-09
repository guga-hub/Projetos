# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que
# 1L de tinta pinta 2m quadrados.

altura = float(input('Qual a altura da sua parede: '))
largura = float(input('Qual a largura da sua parede: '))
area = altura * largura
tinta = area/2

print('Para a área de {}m será necessário {}L de tinta.'.format(area,tinta))

