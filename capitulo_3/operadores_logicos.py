#
# Operadores Lógicos
#
# Exemplo com 'and' (E)
tem_dinheiro = True
esta_aberto = True

posso_comprar = tem_dinheiro and esta_aberto
print(f"Posso comprar (dinheiro E aberto)? {posso_comprar}") # Saída: True (ambos são True)

tem_dinheiro = True
esta_aberto = False
posso_comprar = tem_dinheiro and esta_aberto
print(f"Posso comprar (dinheiro E aberto)? {posso_comprar}") # Saída: False (uma condição é False)

# Exemplo com 'or' (OU)
tem_sol = False
tem_nuvens = True
posso_ir_praia = tem_sol or tem_nuvens
print(f"Posso ir pra praia (sol OU nuvens)? {posso_ir_praia}") # Saída: True (tem nuvens, então True)

tem_sol = False
tem_nuvens = False
posso_ir_praia = tem_sol or tem_nuvens
print(f"Posso ir pra praia (sol OU nuvens)? {posso_ir_praia}") # Saída: False (ambos são False)


# Exemplo com 'not' (NÃO)
esta_chovendo = True
print(f"Não está chovendo? {not esta_chovendo}") # Saída: False (porque esta_chovendo É True)

tem_bolo = False
print(f"Não tem bolo? {not tem_bolo}") # Saída: True (porque tem_bolo É False)
