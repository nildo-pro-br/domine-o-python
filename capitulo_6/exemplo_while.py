#
# Exemplo 1: Processo de cozimento até o ponto ideal
#
ponto_atingido = False
iteracoes = 0

print("--- Realizando Processo ---")
while not ponto_atingido: # Enquanto a condição de 'ponto_atingido' NÃO for True
    iteracoes = iteracoes + 1 # Ou iteracoes += 1
    print(f"Executando iteração número {iteracoes}...")
    if iteracoes >= 5: # Condição para atingir o "ponto" (exemplo didático)
        ponto_atingido = True # A condição do laço torna-se True, permitindo a interrupção
print("Processo conluido após {interacoes} interações.")
# Saída (após 5 iterações):
# Executando iteração número 1...
# ...
# Executando iteração número 5...
# Processo concluído após 5 iterações!

# Exemplo 2: Solicitação de senha até acerto
senha_correta = "coelhinho123"
senha_digitada = "" # Inicialização vazia

while senha_digitada != senha_correta: # Enquanto a senha digitada for DIFERENTE da correta
        senha_digitada = input("Digite a senha: ")
        if senha_digitada != senha_correta:
            print("Senha Incorreta! Tente novamente!")
print("Senha Correta! Acesso liberado!")

print() # pula uma linha
