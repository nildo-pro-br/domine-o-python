#
# Precedência de Operadores
#
# Exemplo com Operadores Aritméticos
resultado1 = 10 + 5 * 2 # Primeiro 5*2 (10), depois 10+10
print(f"Resultado 1: {resultado1}") # Saída: Resultado 1: 20

resultado2 = (10 + 5) * 2 # Primeiro (10+5=15), depois 15*2
print(f"Resultado 2: {resultado2}") # Saída: Resultado 2: 30

# Exemplo com Operadores Lógicos e Comparação
idade = 18
tem_carteira = True

# Condição: (idade maior ou igual a 18 E tem carteira)
pode_dirigir = idade >= 18 and tem_carteira
print(f"Pode dirigir? {pode_dirigir}") # Saída: True

# Condição complexa: (idade maior que 20 OU tem carteira) E (não é menor de idade)
# Ordem de avaliação:
# 1. (idade > 20) -> False
# 2. (False or tem_carteira) -> (False or True) -> True
# 3. (idade < 18) -> False
# 4. (not False) -> True
# 5. (True and True) -> True
condicao_complexa = (idade > 20 or tem_carteira) and (not idade < 18)
print(f"Condição complexa: {condicao_complexa}") # Saída: True
