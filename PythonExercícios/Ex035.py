# Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.

a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

if (a < b + c) and (b < a + c) and (c < a + b):
   print("\033[32mAs retas acima PODEM formar um triângulo\033[m")
else:
   print("\033[31mAs retas acima NÃO PODEM formar um triângulo\033[m")