#   ==  Equal
#   !=  Not Equal
#   >   Greater Than
#   <   Less Than
#   >=  Greater than or equal to
#   <=  Less than or equal to
'''
operadores = 10 >= 12
print(operadores)
'''

# Assignment operators (Operadores de Atribuição)

'''
x = 100

#x = x + 5
#x += 5
#x -= 5
#x *= 5
#x /= 5
#x %= 3 

print(x)
'''



# Logical operators (Operadores lógicos)
# Boolean
'''
renda_acima_5mil = False
nome_limpo = False

if renda_acima_5mil or nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento Negado')
'''





# Ternary Operator (Operador Ternário)
'''
idade = 16

resultado = 'Voto permitido' if idade >= 16 else 'Voto não permitido'

print(resultado)
'''




# Multiple Comparison Operators (Multiplos Operadores de Comparação)

valor = 41

if 20 <= valor < 40:

    print('Produto foi Aceito')
else:
    print('produto não Aceito')