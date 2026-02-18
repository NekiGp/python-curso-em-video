#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('digite a medida em metro'))
print('a medida de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm '.format(n, n/1000, n/100, n/10, n*10, n*100, n*1000))
