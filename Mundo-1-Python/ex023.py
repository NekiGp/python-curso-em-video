# ==========================================================
# Exercício 023: Separador de Dígitos de um Número
# Curso: Python 3 - Mundo 1 (Gustavo Guanabara)
# Objetivo: Decompor um número de 0 a 9999 em Unidade, Dezena, Centena e Milhar.
# ==========================================================

# Entrada de dados
# Nota: Lemos como int para aplicar operações matemáticas de decomposição.
num = int(input('Digite um número entre 0 e 9999: '))

print(f'\nAnalisando o número {num}...')
print('-' * 30)

# Lógica Matemática:
# % 10 -> Pega o resto da divisão por 10 (o último dígito)
# //   -> Divisão inteira (desloca a casa decimal para a direita)

unidade = num // 1 % 10
dezena  = num // 10 % 10
centena = num // 100 % 10
milhar  = num // 1000 % 10

# Exibição dos Resultados
print(f'Unidade: {unidade}')
print(f'Dezena:  {dezena}')
print(f'Centena: {centena}')
print(f'Milhar:  {milhar}')

print('-' * 30)

