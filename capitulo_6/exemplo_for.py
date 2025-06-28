#
# Exemplo 1: Cumprimentando cada pessoa em uma lista
#
nomes = ["Alice", "Bob", "Carlos", "Diana"]

print("--- Comprimentos ---")
for nome in nomes: # Para CADA 'nome' na lista 'nomes'
    print(f"Olá {nome}!")

# Saída:
# Olá, Alice!
# Olá, Bob!
# Olá, Carlos!
# Olá, Diana!

# Exemplo 2: Contagem de 0 a 4 (utilizando range())
# range(5) gera uma sequência de números de 0 a 4
print("\n--- Contagem Padrão ---")
for numero in range(5):
    print(numero)
# Saída:
# 0
# 1
# 2
# 3
# 4

# Exemplo 3: Contagem de 1 a 5 (utilizando range() com início e fim)
print("\n--- Contagem de 1 a 5 ---")
for numero in range(1, 6): # Inicia em 1, vai até 5 (o 6 não é incluído)
    print(numero)
# Saída:
# 1
# 2
# 3
# 4
# 5

# Exemplo 4: Iterando sobre caracteres de uma string
frase = "Python"
print("\n--- Caracteres da Palavra ---")
for letra in frase:
    print(letra)
# Saída:
# P
# y
# t
# h
# o
# n

print() # pula uma linha
