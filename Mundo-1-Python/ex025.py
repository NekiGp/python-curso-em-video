# ==========================================================
# Exercício 025: Procurando uma string dentro de outra
# Curso: Python 3 - Mundo 1 (Gustavo Guanabara)
# ==========================================================

# Base de raciocínio:
# 1. Lê o nome e já trata espaços e formatação (.title())
# 2. Transforma a string em lista (.split()) para buscar a palavra isolada
nome = str(input('Digite seu nome completo: ')).strip().title()

print('Analisando seu nome......')

# Lógica de busca em lista (evita falsos positivos como "Silvano")
palavra = nome.split()

# Exibição do resultado booleano
print(f'Seu nome tem Silva? {"Silva" in palavra}')