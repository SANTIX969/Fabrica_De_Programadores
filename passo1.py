contador = 0 
while contador <15:
    contador = contador +1
    arquivo = open("arquivo.txt", "a", encoding="utf-8")
    nome = input("Digite seu nome:\n")
    arquivo.write(f"\n nomes: {nome}\n")

    arquivo.close()

print("Arquivo criado com sucesso (●'◡'●)")