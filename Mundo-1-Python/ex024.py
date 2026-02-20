# ==========================================================
# Exercício 024: Verificador de Início de Texto
# Curso: Python 3 - Mundo 1 (Gustavo Guanabara)
# Objetivo: Validar se o nome de uma cidade começa com a palavra "SANTO".
# ==========================================================

# Entrada de dados com .strip() para eliminar espaços antes/depois da string
cidade = str (input ('digite o nome da cidade ').strip())

# Exibição dos resultados
print ('Analisando o nome da cidade...')
print ('-' * 40)
print (f'A cidade se chama {cidade.title()} portanto a resposta é {cidade.title()[:5] == 'Santo'}')
print ('-' * 40)


