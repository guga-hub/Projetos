# Faça um programa que leia o nome completo de uma pessoa, mostrando em
# seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é \033[1;34m{}.'.format(nome[0]))
print('Seu último nome é \033[1;34m{}.'.format(nome[len(nome)-1]))



