#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

P = float(input('Quanto custa o produto?'))
Desconto = 5/100
VF = P * Desconto
print ('O produto custava R${}, na promoção com desconto de 5% vai custar R${:.3f}'.format(P, (P-VF)))