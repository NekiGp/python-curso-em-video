#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

L = float(input("Qual a largura da parede em metros: "))
A = float(input("Qual a altura da parede em metros: "))
At = L*A
print ('Sua parede tem a dimensão de {}x{} e sua aréa é de {}m2.\nPara pintar essa parede, você precisará de {}l de tinta.'.format(L, A, At, (At/2)))