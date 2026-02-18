#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit.

celsius = float(input('Qual a temperatura em Celsius: '))
Fh = (celsius * 1.8) + 32
print (f'A temperatura de {celsius}ºC corresponde a {Fh}ºF')
