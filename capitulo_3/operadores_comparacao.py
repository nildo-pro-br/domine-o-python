#
# Operadores de Comparação
#
idade_joao = 25
idade_maria = 30
preco_cafe = 5.00
preco_cha = 5.00

# Igual a (==)
print(f"João e Maria têm a mesma idade? {idade_joao == idade_maria}") # Saída: False
print(f"Café e Chá têm o mesmo preço? {preco_cafe == preco_cha}") # Saída: True

# Diferente de (!=)
print(f"João e Maria têm idades diferentes? {idade_joao != idade_maria}") # Saída: True

# Maior que (>)
print(f"Maria é mais velha que João? {idade_maria > idade_joao}") # Saída: True

# Menor que (<)
print(f"João é mais novo que Maria? {idade_joao < idade_maria}") # Saída: True

# Maior ou igual a (>=)
print(f"João tem 25 anos ou mais? {idade_joao >= 25}") # Saída: True

# Menor ou igual a (<=)
print(f"Maria tem 30 anos ou menos? {idade_maria <= 30}") # Saída: True

# Comparando textos (strings)
nome1 = "Python"
nome2 = "python"
print(f"As palavras são iguais (com distinção de maiúsculas)? {nome1 == nome2}") # Saída: False (diferença entre 'P' maiúsculo e 'p' minúsculo)


