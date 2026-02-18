#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('Quantos kms foram pecorridos?: '))
dias = int(input('Por quantos dias ele foi alugado?: '))
custo = (60*dias) + (0.15 * km)
print ('Você rodou {}km por {} dias, levando em conta os custos diario. o custo sera de {:.2f}'.format(km, dias, custo))