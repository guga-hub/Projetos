# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "SANTO".

cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(cidade.upper()[0:5] ==  'SANTO')
