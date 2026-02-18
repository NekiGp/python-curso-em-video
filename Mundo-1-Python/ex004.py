# Exercício Python 4: Faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('digite algo')
print ('o tipo primitivo desse valor é', (type(n)))
print ('Só tem espaços?', n.isspace())
print ('é um numero?', n.isnumeric())
print ('é alfabetico?', n.isalpha())
print ('é alfanumerico?', n.isalnum())
print ('Está em maiusculas?', n.isupper())
print ('Está em minusculuas?', n.islower())
print ('Está capitalizada?', n.istitle())