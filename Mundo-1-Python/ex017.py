#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
#mostre o comprimento da hipotenusa.

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# A função hypot já faz a raiz quadrada da soma dos quadrados (a² + b² = c²)
hi = math.hypot(co, ca)

print(f'A hipotenusa vai medir {hi:.2f}')