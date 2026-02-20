# ==========================================================
# Exercício 027: Primeiro e Último Nome de uma Pessoa
# Curso: Python 3 - Mundo 1 (Gustavo Guanabara)
# Objetivo: Isolar o primeiro e o último nome de uma string completa.
# ==========================================================

n = str(input('Digite seu nome completo: ')).strip().title()
nome = n.split()

print('-' * 40)
print('É um prazer te conhecer!')

# Exibição dos resultados
print(f'Seu primeiro nome é: {nome[0]}')

# Se usa o len(nome)-1 dentro dos colchetes para acessar a palavra
# Ou pode usar nome[-1], que também pega o último elemento
print(f'Seu último nome é:   {nome[len(nome)-1]}')
print('-' * 40)