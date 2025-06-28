#
# Exemplo prático para condicional aninhada
#
idade = 15
tem_ingresso = True
altura = 1.60

if tem_ingresso: # Primeiro, verifica a posse do ingresso
    print("Ingresso verificado. Prosseguindo para a próxima etapa...")
    if idade >= 18: # Se tem ingresso, verifica a idade
        print("Você é adulto e tem acesso a todas as atrações!")
    elif altura >= 1.50: # Se não é adulto, verifica a altura para atrações específicas
        print("Você é adolescente e tem acesso às atrações de nível médio!")
    else:
        print("Você é criança e deve utilizar a área infantil!")
else: # Se NÃO possui ingresso
    print("É necessário um ingresso para entrar no parque!")

# Testando com idade 15, tem_ingresso True, altura 1.60:
# Saída:
# Ingresso verificado. Prosseguindo para a próxima etapa...
# Você é adolescente e tem acesso às atrações de nível médio!



# Exemplo 2: Sistema de Login com Usuário e Senha
usuario_correto = "admin"
senha_correta = "123mudar"

usuario_digitado = input("Digite seu usuário: ")
senha_digitada = input("Digite sua senha: ")


if usuario_digitado == usuario_correto:
    print("Usuário correto")
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso concedido ao sistema!")
    else:
        print("Senha incorreta! Acesso negado")
else:
    print(" Usuário incorreta! Acesso negado!")

# Teste com usuário "admin", senha "123mudar": Saída: Senha correta! Acesso concedido ao sistema!
# Teste com usuário "admin", senha "senhaerrada": Saída: Senha incorreta! Acesso negado.
# Teste com usuário "usuarioerrado": Saída: Usuário incorreto! Acesso negado.

print() # pula uma linha
