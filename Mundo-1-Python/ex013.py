#Exercício Python 13:Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salarioatual = float(input('Qual o salario atual? R$'))
salarionovo = salarioatual + (salarioatual * 15/100)
print ('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}.'.format(salarioatual,salarionovo))