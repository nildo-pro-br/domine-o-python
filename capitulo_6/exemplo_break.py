#
# Exemplo: Busca por um item específico em uma coleção
#
colecao_de_objetos = ["livro", "caneta", "lanche", "celular", "chave"]
item_procurado = "celular"

for item in colecao_de_objetos:
    print(f"Verificando {item}")
    if item == item_procurado:
        print(f"Item encontrado: {item_procurado}!")
        break # Interrompe o laço assim que o item é encontrado
print("Busca na coleção de objetos finalizado.")
# Saída (se 'celular' é o 4º item):
# Verificando: livro
# Verificando: caneta
# Verificando: lanche
# Verificando: celular
# Item encontrado: celular!
# Busca na coleção finalizada.
print() # pula uma linha
