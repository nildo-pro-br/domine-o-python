#
# Trabalhando com F-Strings
#
nome = "Mila"
idade = 10 # Idade do personagem
altura = 1.35 # Altura em metros
saldo_conta = 1234.5678 # Valor de saldo

# Exemplo básico de f-string
print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")
# Saída: Olá, meu nome é Mila e eu tenho 10 anos.

# Formatando números decimais (float) - Limitação de casas decimais:
# O especificador ":.2f" formata o número como ponto flutuante com 2 casas decimais
print(f"Minha altura é {altura:.2f} metros.") # Saída: Minha altura é 1.35 metros.
print(f"Meu saldo na conta é R${saldo_conta:.2f}.") # Saída: Meu saldo na conta é R$1234.57.

# Alinhamento de texto (preenchimento com espaços)
# >10: alinha à direita em um campo de 10 caracteres
# <:10: alinha à esquerda em um campo de 10 caracteres
# ^10: centraliza em um campo de 10 caracteres
item = "Maçã"
preco = 3.50
print(f"Item: {item:<10} Preço: R${preco:>8.2f}") # Saída: Item: Maçã          Preço:    R$3.50
# Neste exemplo, "Maçã" ocupa 10 espaços (com 6 espaços após o texto) e "R$3.50" ocupa 8 espaços (com 3 espaços antes).
print() # pula uma linha
