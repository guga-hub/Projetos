# For Loops (Looping)

# Imprimir de 1 a 5
'''
for numero in range (1, 90, 8):
    print (numero)
'''






# For Loops (Looping) - Para Strings
'''
palavra = 'Espetacular'

for letra in palavra:
    print(f'{letra} esta dentro da palavra {palavra}')
'''






# Enviar um email com os detalhes da compra online (Máximo de 3 tentativas para compras confirmadas).
'''
compra_confirmada = True
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada.'

for enviar in range (3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail.')
        break
else:
    print('Falha na compra.')
'''





# == for loop nested ===

    # Outer loop
      #Inner loop

'''
for numero1 in range(1, 6):
    print('produto' + str(numero1))
    for numero2 in range(11):
        print(numero1, numero2)
        for numero3 in range(1):
            print(numero1, numero2, numero3)
            for numero4 in range(2):
                print(numero1, numero2, numero3, numero4)
                for numero5 in range(3):
                    print(numero1, numero2, numero3, numero4, numero5)
                    for numero6 in range(4):
                        print(numero1, numero2, numero3, numero4, numero5, numero6)
                        for numero7 in range(5):
                            print(numero1, numero2, numero3, numero4, numero5, numero6, numero7)
'''                            




#For Loops 
# Modificar de FANTASTICO para F A N T A S T I C O 

'''
palavra = 'JORNAL DIÁRIO'


for spaco in palavra:
    print (f' {spaco}' , end='')
'''




#For Loops
# Fazer um retângulo no output

'''
linhas = 6
colunas = 6
simbolo='*'


for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()
'''

def FirstFactorial(num): 

    if num == 8:
      return num
    else:
      return num * (FirstFactorial(num - 1))

      print (FirstFactorial)
