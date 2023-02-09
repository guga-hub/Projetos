# Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60,00 por dia e
# R$0,15 por Km rodado.

km = float(input('A quantidade de Km percorridos: '))
dias_alugados = int(input('Quantidade de dias alugados: '))
preco = (km*0.15) + (dias_alugados*60)

print('Já que percorreu {:1f}Km e também alugou o carro por {} dias você pagará exatamente: R${:.2f}'.format(km, dias_alugados, preco))



