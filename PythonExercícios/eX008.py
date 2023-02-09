# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros.

valor = float(input('Digite o valor que deseja converter: '))
centimetros = valor * 100
milimetro = valor * 1000

print('O valor {}m convertido para centímetros resulta em {:.2f}cm, e em milímetros resulta em {:.2f}mm.'.format(valor, centimetros, milimetro))
