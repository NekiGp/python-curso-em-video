#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('digite um numero'))
print ('analisando o valor {},seu antecessor é {} e seu sucessor é {}'.format(n1, (n1-1), (n1+1)))