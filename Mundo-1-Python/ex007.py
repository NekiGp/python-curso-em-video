#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Qual a primeira nota?'))
n2 = float(input('Qual a segunda nota?'))
print ('A media entre {} e {} é igual a {}'.format(n1, n2, (n1+n2)/2))