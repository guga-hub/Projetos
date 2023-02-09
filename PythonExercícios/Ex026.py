# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posição ela aparece a primeira vez.
# - Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes nessa frase.'.format(frase.count('A')))
print('A letra A aparece na posição {} pela primeira vez nessa frase.'.format(frase.find('A')+1))
print('A letra A aparece na posição {} pela última vez nessa frase.'.format(frase.rfind('A')+1))

