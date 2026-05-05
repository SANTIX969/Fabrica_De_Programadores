lista = ["Vanessa", "Carla"]

usuario = input("Digite seu usuario: \n")

if usuario in lista:

    
    print(f"{usuario}, seja bem-vindo!!!\n")

else:
    opcao = input("Usuario não existe !!!\n\nDeseja cadratrar um novo usuario?  (sim/não)\n\n ").lower ()

    if opcao == "sim":
     
     novo_usuario = input ("\n Digite o nome do novo usuario: \n")
     lista.append(novo_usuario)
     print("usuario adicionado com sucesso!!!\n", lista)

    else:
       print("Encerrado...kitisug")