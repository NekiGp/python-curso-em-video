# ==========================================================
# Exercício 022: Analisador de Textos
# Curso: Python 3 - Mundo 1 (Gustavo Guanabara)
# Objetivo: Manipular strings e extrair informações específicas.
# ==========================================================

# Entrada de dados com .strip() para remover espaços desnecessários nas extremidades
nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')

# 1. Transformação de maiúsculas e minúsculas
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')

# 2. Contagem total de letras (Nome completo menos a quantidade de espaços)
# A lógica: len(total) - count(' ') isola apenas os caracteres alfabéticos
total_letras = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {total_letras} letras')

# 3. Contagem do primeiro nome
# O .split() divide a string em uma lista; o índice [0] pega a primeira palavra
separa = nome.split()
print(f'Seu primeiro nome é {separa[0].title()} e ele tem {len(separa[0])} letras')

print('=' * 40)