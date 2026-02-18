#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar.

real = float(input('Quanto reais você tem na carteira? R$'))
dolar = real / 5.37
ienes = real / 0.03386
euro = real / 6.23
print ('Com R${} você pode comprar US${:.2f}, ¥{:.2f} e €{:.2f}'.format(real, dolar, ienes, euro))