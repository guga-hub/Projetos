# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento.
# Para salários superiores a R$1250,00 calcule um aumento de 10%.
# Para salários inferiores ou iguais a R$1250,00 o aumento é de 15%.

salario = float(input('Digite o seu salário atual e veja quanto terá após seu aumento: R$'))

if salario >= 1250:
    salario = salario+((salario*10)/100)
    print('Seu salário terá um aumento de 10% e fserá exatamente: R${:.2f}'.format(salario))
else:
    salario = salario+((salario*15)/100)
    print('Seu salário terá um aumento de 15% e será exatamente: R${:.2f}'.format(salario))