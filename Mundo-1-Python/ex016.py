#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#modo com import
"""import math
num = float(input('digite um valor: '))
inteiro = math.trunc(num)
print(f'O valor digitado foi {num} e a sua porção inteira é {inteiro}')"""


#modo sem import
num = float(input('digite um valor: '))
print (f'o valor digitado foi {num} e a sua porção inteira é {int(num)}')