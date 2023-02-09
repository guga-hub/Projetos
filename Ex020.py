# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. faça um programa que leia o nome dos quatro
# alunos e mostre a ordem sorteada.

import random

aluno1 = str(input('Digite o primeiro nome: '))
aluno2 = str(input('Digite o segundo nome: '))
aluno3 = str(input('Digite o terceiro nome: '))
aluno4 = str(input('Digite o quarto nome: '))
list = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(list)

print('A seguencia de apresentação ficou a seguinte {}'.format(list))