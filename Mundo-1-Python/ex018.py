#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do angulo: '))

seno = (sin(radians(angulo)))
cosseno = (cos(radians(angulo)))
tangente = (tan(radians(angulo)))

print (f'O ângulo de {angulo} tem o valor {seno:.2f}')
print (f'O ângulo de {angulo} tem o valor {cosseno:.2f}')
print (f'O ângulo de {angulo} tem o valor {tangente:.2f}')