# Lista de carros da garagem
minha_garagem = ["BMW", "Mercedes", "Audi"]

# Preços dos carros da garagem
preco = [35000, 40000, 24800]

# Lista de carrros disponivel na loja
loja = ["Chevt", "Fiat", "Peugeot"]

# Preços dos carros na loja
precos_loja = [1000, 500, 1]

# Listas dos carros
carros_caros = []
carros_baratos = []

# Verifica carros da garagem
for i in range(len(minha_garagem)):
    if preco[i] > 20000:
        carros_caros.append(minha_garagem)  # caro
    else:
        carros_baratos.append(minha_garagem)  # barato

# Verifica carros da loja
for i in range(len(loja)):
    if precos_loja[i] > 20000:
        carros_caros.append(loja)  # caro
    else:
        carros_baratos.append(loja)  # barato

# Mostra resultados
print("Carros baratos:", carros_baratos)
print("Carros caros:", carros_caros)