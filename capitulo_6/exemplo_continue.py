#
# Exemplo: Processamento de alimentos, pulando um item específic
#
alimentos = ["arroz", "feijão", "chocolate", "salada", "frango"]

print("--- Processamento de Refeição ---")
for comida in alimentos:
    if comida == "chocolate":
        print("Chocolate: Item ignorado por restrição dietético.")
        continue # Pula as instruções restantes para 'chocolate' e vai para o próximo alimento
    print(f"Adicionado {comida} ao prato.")
print("Refeição montada!")
# Saída:
# Adicionando arroz ao prato.
# Adicionando feijão ao prato.
# Chocolate: Item ignorado por restrição dietética.
# Adicionando salada ao prato.
# Adicionando frango ao prato.
# Refeição montada!
print() # pula uma linha
