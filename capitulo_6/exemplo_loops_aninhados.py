#
# Exemplo 1: Geração da Tabuada
#
print("--- Tabuada de 1 a 10 ---")
for multiplicador in range(1, 11): # Laço externo: para cada número de 1 a 10
    print(f"\nTabuada do {multiplicador}: ") # Título da tabuada atual
    for i in range(1, 11):
        resultado = multiplicador * i
        print(f"{multiplicador} x {i} = {resultado}")
# Saída (parcial):
# Tabuada do 1:
# 1 x 1 = 1
# ...
# 1 x 10 = 10
#
# Tabuada do 2:
# 2 x 1 = 2
# ...
# 2 x 10 = 20
# ... e assim sucessivamente.


# Exemplo 2: Desenho de uma Grade Simples (com coordenadas)
linhas = 3
colunas = 3

print("\n--- Grade de Coordenadas ---")
for linha in range(linhas):
    for coluna in range(colunas):
        # Exibe a posição atual sem quebrar a linha
        print(f"[{linha, coluna}]", end=" ")
    print() # Quebra a linha após o término das colunas de uma linha


print() # pula uma linha
