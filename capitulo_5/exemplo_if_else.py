#
# Exemplo prático para a declaração if e else
#
# Exemplo 1: Verificação de idade para acesso a um evento
idade = 17

if idade >= 18:
    print("Acesso permitido ao evento. Desfrute!")
else:
    print("Acesso negado. Idade mínima não atingida.")
# Saída: Acesso negado. Idade mínima não atingida.

# Exemplo 2: Lógica de semáforo
cor_semafaro = "verde"

if cor_semafaro == "verde":
    print("Prosseguir")
else:
    print("Pare! Ou prepara-se para parar.")
# Saída: Prossiga!

# Exemplo 3: Verificação de saldo para compra
saldo = 500.00
valor_compra = 600.00

if saldo >= valor_compra:
    print("Compra aprovada!")
    saldo = saldo - valor_compra # Atualiza o saldo
    print(f"Seu novo saldo é: R${saldo:.2f}")
else:
    print("Compra negada! Saldo insuficiente.")
    print(f"Faltam R${valor_compra - saldo:.2f} para esta compra.")

# Saída:
# Compra negada! Saldo insuficiente.
# Faltam R$100.00 para essa compra.

print() # pula uma linha
