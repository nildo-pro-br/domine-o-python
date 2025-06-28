#
# Aplicação do elif para a classificação da nota de um aluno
#
nota = 75

if nota >= 90:
    print("Conceito A (Excelente)!")
elif nota >= 80: # Se não foi A, testa se é B
    print("Conceito B (Ótimo)!")
elif nota >= 70: # Se não foi A nem B, testa se é C
    print("Conceito C (Satisfatório).")
else: # Se não foi A, B, nem C...
    print("Conceito D (Insuficiente). Necessita de mais estudo.")

# Testando com a nota 75: Saída: Conceito C (Satisfatório).

# Exemplo 2: Preferência alimentar do coelho
fruta_desejada = "maçã"

if fruta_desejada == "cenoura":
    print("Cenoura! Minha preferida!")
elif fruta_desejada == "maçã":
    print("Maçã? Uma boa opção alternativa!")
elif fruta_desejada == "banana":
    print("Banana? Uma fruta prática e deliciosa!")
else:
    print("Desculpe, esta fruta não está disponível para o coelho hoje.")

print() # pula uma linha
