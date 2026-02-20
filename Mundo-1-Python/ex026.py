# ==========================================================
# Exercício 026: Analisador de Ocorrências em Strings
# Curso: Python 3 - Mundo 1 (Gustavo Guanabara)
# Objetivo: Identificar contagem e posições específicas de um caractere.
# ==========================================================

# Entrada de dados padronizada para maiúsculas para facilitar a busca
frase = str(input('Digite uma frase: ')).upper().strip()

print('Analisando sua frase..........')
print ('-'*40)

# 1. Contagem de caracteres específicos
print(f'A letra "A" aparece {frase.count("A")} vezes')

# 2. Localização da primeira ocorrência
# Somamos +1 para converter o índice de programação (0-based) para posição humana
print(f'Pela primeira vez ela aparece na posição {frase.find("A")+1}')

# 3. Localização da última ocorrência
# O rfind() começa a procurar da direita (right) para a esquerda
print(f'Pela última vez ela aparece na posição {frase.rfind("A")+1}')
print ('-'*40)